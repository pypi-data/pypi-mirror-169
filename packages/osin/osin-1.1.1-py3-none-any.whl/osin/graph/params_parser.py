from abc import ABC, abstractmethod
import argparse
from dataclasses import MISSING, Field, fields, is_dataclass, dataclass
import sys
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Mapping,
    NewType,
    Optional,
    Sequence,
    Type,
    Union,
    get_args,
    get_origin,
    get_type_hints,
    Generic,
    TypeVar,
)
from enum import Enum

ParamType = TypeVar("ParamType")


class ParamsParser(Generic[ParamType]):
    """Parsing parameters defined by one or multiple dataclass.

    Some important behaviors:

    - Parameter declared as union:
        * only support mixed of primitive types, or one optional complex type.
        * this should not be confused with default value, because an optional parameter can have a default value different than None.
        * when we have one optional complex type, to specify that complex type is None, we introduce a new
            cmd argument `--<param_name> none` to specify when it is None. Then, all other fields of this complex
            type must be optional
    - Complex parameter can have a default value:
        * when a nested parameter such as MethodArgs have a default value, a default value can be different
            from the MethodArgs field's default value, so the generated cmd argument need to set the default value
            correctly.
        * when a user override some default value by providing it, it should not affect how the default value we
            set previously using the rule above.
    - Parameter declared as list or set:
        * because we are using nargs to parse, we cannot generate nested argument for complex type, therefore, if
            a parameter is a complex type, it must be able to be parsed from a string. Use `type_constructors` or
            `field_constructors` to provide a custom constructor in this case.
    - Parameter declared as a dictionary:
        * passing a dictionary is not cmd friendly, since we do not know the key, we cannot generate nested arguments
            to parse the type correctly. Therefore, the dictionary must be able to reconstructored from a string. Use
            `type_constructors` or `field_constructors` to provide a custom constructor in this case.

    Args:
        param_types: one or more classes holding parameters. Properties of each class will be converted to arguments.
            When params is a sequence of classes, the properties of all classes will be in the same namespace.
            When params is a mapping of key and classes, the key will act as the namespace and the arguments will
            be prefixed with the key and the dot character.

        underscore_to_dash: whether to convert underscore to dash in the argument name.

        type_constructors: a mapping of type to a function that takes a string and return an instance of that type.
            This is useful when the type's constructor cannot be constructed from a string, for example, a dataclass of
            more than one field

        field_constructors: a mapping of a nested field (separated by dot) to a function that takes a string and
            return an instance of the field's type.
    """

    def __init__(
        self,
        param_types: Type[ParamType],
        underscore_to_dash: bool = True,
        type_constructors: Optional[Dict[Type, Callable[[str], Type]]] = None,
        field_constructors: Optional[Dict[str, Callable[[str], Type]]] = None,
    ):
        self.parser = argparse.ArgumentParser()
        self.underscore_to_dash = underscore_to_dash
        self.param_types = param_types
        self.type_constructors = type_constructors or {}
        self.field_constructors = field_constructors or {}

        if underscore_to_dash:
            self.field_constructors = {
                k.replace("_", "-"): v for k, v in self.field_constructors.items()
            }

        if is_dataclass(param_types):
            self.deser = self._add_dataclass_arguments(param_types)
        elif isinstance(param_types, (list, tuple)):
            self.deser = []
            for dtype in param_types:  # type: ignore
                self.deser.append(self._add_dataclass_arguments(dtype))
        elif isinstance(param_types, Mapping):
            self.deser = {}
            for namespace, dtype in param_types.items():
                self.deser[namespace] = self._add_dataclass_arguments(dtype, namespace)

    def parse_args(
        self, args: Optional[Sequence[str]] = None, known_only: bool = False
    ) -> ParamType:
        if known_only:
            ns = self.parser.parse_known_args(args)
        else:
            ns = self.parser.parse_args(args)

        if isinstance(self.deser, dict):
            return {k: v.deserialize(ns) for k, v in self.deser.items()}  # type: ignore
        elif isinstance(self.deser, list):
            return [v.deserialize(ns) for v in self.deser]  # type: ignore
        else:
            return self.deser.deserialize(ns)  # type: ignore

    def _add_dataclass_arguments(
        self,
        dtype: Any,
        namespace: str = "",
        default: Any = MISSING,
        default_factory: Union[Any, Callable[[], Any]] = MISSING,
        is_nullable: bool = False,
    ):
        """Generate arguments from a dataclass

        Args:
            dtype: the dataclass type
            namespace: the namespace of the arguments
            default: the default value of the dataclass
            default_factory: the default factory of the dataclass
            is_nullable: whether the dataclass is nullable
        """
        type_hints: Dict[str, type] = get_type_hints(dtype)

        deser = DeserMultiFields(
            cls=dtype, field_names=[], is_nullable=is_nullable, null_argname=namespace
        )

        if default is not MISSING:
            default_instance = default
        elif default_factory is not MISSING:
            default_instance = default_factory()
        else:
            default_instance = None

        if is_nullable:
            assert namespace != ""
            self.parser.add_argument(
                f"--{namespace}", type=empty_or_none, default="", required=False
            )

        for field in fields(dtype):
            assert (
                field.init
            ), "Only fields with init=True are supported (included in the generated __init__ method)"
            argname = field.name if namespace == "" else f"{namespace}.{field.name}"
            if self.underscore_to_dash:
                argname = argname.replace("_", "-")

            field_doc = ""
            field_type = type_hints[field.name]

            field_default = field.default
            if default_instance is not None:
                # we have the default value
                field_default = getattr(default_instance, field.name)
            field_required = field_default is MISSING and not is_nullable

            deser.field_names.append(
                self._add_argument_from_type(
                    argname,
                    field_type,
                    field_doc,
                    field_required=field_required,
                    field_default=field_default,
                )
            )

        return deser

    def _field_type_to_parse_args(
        self, argname: str, field_type: Any, is_nullable: bool
    ):
        if is_nullable:
            wrapper = optional_wrapper
        else:
            wrapper = lambda x: x

        if field_type is bool:
            return {"type": wrapper(string_to_bool)}

        if field_type in self.type_constructors:
            return {"type": wrapper(self.type_constructors.get(field_type, field_type))}

        if argname in self.field_constructors:
            return {"type": wrapper(self.field_constructors.get(argname, field_type))}

        origin = get_origin(field_type)
        if origin is Literal:
            args = get_args(field_type)
            # Note: inclusion in the choices container is checked after any type conversions have been performed
            # https://docs.python.org/3/library/argparse.html#choices
            arg_types = list({type(arg) for arg in args})
            if len(arg_types) == 1:
                field_type_parser = arg_types[0]
            else:
                field_type_parser = get_literal_string_parser
            return {"choices": args, "type": wrapper(field_type_parser)}

        return {"type": wrapper(field_type)}

    def _add_argument_from_type(
        self,
        argname: str,
        field_type: Any,
        annotated_desc: str,
        field_required: bool,
        field_default: Any,
    ):
        origin = get_origin(field_type)
        if origin is None or origin is Union or origin is Literal:
            if origin is Union:
                non_null_args = [
                    arg for arg in get_args(field_type) if arg is not type(None)
                ]
                if len(non_null_args) != 1:
                    raise NoDerivedArgParser().add_trace(
                        argname,
                        field_type,
                        ": only `Union[X, NoneType]` (i.e., `Optional[X]`) is allowed for `Union` because"
                        " the argument parser only supports one type per argument.",
                    )
                is_nullable = True
                field_type = non_null_args[0]
            else:
                is_nullable = False

            # not generic types
            if is_dataclass(field_type):
                return self._add_dataclass_arguments(
                    field_type,
                    namespace=argname,
                    default=field_default,
                    is_nullable=is_nullable,
                )

            # we assume it can be reconstructed from string
            # some classes support this is enum.Enum, pathlib.Path
            self.parser.add_argument(
                f"--{argname}",
                default=field_default,
                required=field_required,
                help=annotated_desc,
                **self._field_type_to_parse_args(argname, field_type, is_nullable),
            )
            return DeserSingleField(argname)

        args = get_args(field_type)
        if origin is list or origin is set:
            assert len(args) == 1
            self.parser.add_argument(
                f"--{argname}",
                nargs="*",
                default=field_default,
                required=field_required,
                help=annotated_desc,
                **self._field_type_to_parse_args(argname, args[0], is_nullable=False),
            )
            if origin is set:
                return DeserSingleField(argname, postprocess=set)
            return DeserSingleField(argname)

        if origin is dict:
            self.parser.add_argument(
                f"--{argname}",
                nargs="*",
                default=field_default,
                required=field_required,
                help=annotated_desc,
                **self._field_type_to_parse_args(argname, args[0], is_nullable=False),
            )
            return DeserSingleField(argname)

        raise NoDerivedArgParser().add_trace(argname, field_type)


# From https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
def string_to_bool(v: str):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError(
            f"Truthy value expected: got {v} but expected one of yes/no, true/false, t/f, y/n, 1/0 (case insensitive)."
        )


def empty_or_none(v: str):
    if v in ("None", "none"):
        return None
    if v == "":
        return ""

    raise argparse.ArgumentTypeError(
        f"Empty or None value expected: got {v} but expected one of None/none."
    )


def get_literal_string_parser(s: str):
    if s in ("None", "none"):
        return None
    if s.isdigit():
        return int(s)
    if s.lower() in ("yes", "true", "t", "y", "1"):
        return True
    if s.lower() in ("no", "false", "f", "n", "0"):
        return False
    # don't check for float as it doesn't make lots of sense to store it
    # in a list of literal. how to distinguish between 1.2 and 1.2000001?
    return s


def optional_wrapper(fn):
    def wrapper(s):
        if s in ("None", "none"):
            return None
        return fn(s)

    return wrapper


class NoDerivedArgParser(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_trace = []

    def get_root_field(self):
        return self.error_trace[-1]

    def add_trace(self, *parents: str):
        self.error_trace.extend(reversed(parents))
        return self

    def __str__(self) -> str:
        return f"cannot derive argument parser for: {list(reversed(self.error_trace))}"


class NSDeser(ABC):
    @abstractmethod
    def deserialize(self, ns: argparse.Namespace):
        pass


@dataclass
class DeserSingleField(NSDeser):
    field_name: str
    postprocess: Callable[[Any], Any] = lambda x: x

    def deserialize(self, ns: argparse.Namespace):
        return self.postprocess(getattr(ns, self.field_name.replace("-", "_")))


@dataclass
class DeserMultiFields(NSDeser):
    cls: Type
    field_names: List[NSDeser]
    required: bool = True
    default: Optional[Any] = None
    is_nullable: bool = False
    null_argname: str = ""

    def deserialize(self, ns: argparse.Namespace):
        if (
            self.is_nullable
            and getattr(ns, self.null_argname.replace("-", "_")) is None
        ):
            return None

        values = []
        for f in self.field_names:
            value = f.deserialize(ns)
            if value is MISSING:
                assert isinstance(f, DeserSingleField)
                raise argparse.ArgumentTypeError(
                    f"Missing value for argument {f.field_name}"
                )
            values.append(value)
        return self.cls(*values)
