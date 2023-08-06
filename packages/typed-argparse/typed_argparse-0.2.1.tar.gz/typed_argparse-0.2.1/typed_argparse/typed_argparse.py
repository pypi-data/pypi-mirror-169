import argparse
from typing import Dict, Generic, List, Type, TypeVar, cast

from .choices import Choices
from .dataclass_transform_backport import dataclass_transform
from .param import Param
from .runtime_generic import RuntimeGeneric
from .type_utils import (
    RawTypeAnnotation,
    TypeAnnotation,
    assert_not_none,
    collect_type_annotations,
    typename,
)

C = TypeVar("C", bound="TypedArgs")


@dataclass_transform(kw_only_default=True, field_specifiers=(Param,))
class TypedArgs:
    def __init__(self, *args: object, **kwargs: object):
        """
        Constructs an instance of the TypedArgs class from a given argparse Namespace.

        Performs various validations / sanity check to make sure the runtime values
        match the type annotations.
        """

        # Temporary backwards compatibility. To be removed in 0.3.
        if len(args) == 1 and isinstance(args[0], argparse.Namespace):
            kwargs = _argparse_namespace_to_dict(type(self), args[0], disallow_extra_args=False)

        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def from_argparse(
        cls: Type[C], args: argparse.Namespace, disallow_extra_args: bool = False
    ) -> C:
        kwargs = _argparse_namespace_to_dict(cls, args, disallow_extra_args=disallow_extra_args)
        return cls(**kwargs)

    def __repr__(self) -> str:
        key_value_pairs = [f"{k}={repr(v)}" for k, v in self.__dict__.items() if k != "_args"]
        return f"{self.__class__.__name__}({', '.join(key_value_pairs)})"

    def __str__(self) -> str:
        return repr(self)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TypedArgs):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)

    @classmethod
    def get_choices_from(cls: type, field: str) -> Choices:
        """
        Helper function to extract allowed values from class field (which is a literal/enum like).

        Use case: Forward as `choices=...` argument to argparse.
        """
        return get_choices_from_class(cls, field)


def _argparse_namespace_to_dict(
    cls: Type[C], args: argparse.Namespace, disallow_extra_args: bool
) -> Dict[str, object]:
    missing_args: List[str] = []

    annotations = collect_type_annotations(cls, include_super_types=True)

    kwargs = {}

    for arg_name, type_annotation in annotations.items():
        if arg_name in TypedArgs.__dict__:
            raise TypeError(f"A type must not have an argument called '{arg_name}'")

        if hasattr(args, arg_name):
            # Validate the value and add as attribute
            value: object = getattr(args, arg_name)
            value = type_annotation.validate_with_error(value, arg_name)
            kwargs[arg_name] = value
        else:
            missing_args.append(arg_name)

    # Report missing args if any
    if len(missing_args) > 0:
        if len(missing_args) == 1:
            raise TypeError(f"Arguments object is missing argument '{missing_args[0]}'")
        else:
            raise TypeError(f"Arguments object is missing arguments {missing_args}")

    # Report extra args if any
    if disallow_extra_args:
        extra_args = sorted(set(args.__dict__.keys()) - set(annotations.keys()))
        if len(extra_args) > 0:
            if len(extra_args) == 1:
                raise TypeError(
                    f"Arguments object has an unexpected extra argument '{extra_args[0]}'"
                )
            else:
                raise TypeError(f"Arguments object has unexpected extra arguments {extra_args}")

    return kwargs


def get_choices_from_class(cls: type, field: str) -> Choices:
    """
    Helper function to extract allowed values from class field (which is a literal/enum like).

    Use case: Forward as `choices=...` argument to argparse.
    """
    if field in cls.__annotations__:
        raw_type_annotation: RawTypeAnnotation = cls.__annotations__[field]
        try:
            return get_choices_from(raw_type_annotation)
        except TypeError as e:
            raise TypeError(
                f"Could not infer literal values of field '{field}' "
                f"of type {typename(raw_type_annotation)}"
            ) from e
    else:
        raise TypeError(f"Class {cls.__name__} doesn't have a type annotation for field '{field}'")


def get_choices_from(raw_type_annotation: RawTypeAnnotation) -> Choices:
    """
    Helper function to extract allowed values from a literal/enum like type.

    Use case: Forward as `choices=...` argument to argparse.
    """
    type_annotation = TypeAnnotation(raw_type_annotation)

    while type_annotation.get_underlying_if_list() is not None:
        type_annotation = assert_not_none(type_annotation.get_underlying_if_list())

    allowed_values = type_annotation.get_allowed_values_if_literal()
    if allowed_values is not None:
        return Choices(*allowed_values)

    allowed_values = type_annotation.get_allowed_values_if_enum()
    if allowed_values is not None:
        return Choices(*allowed_values)

    raise TypeError(f"Could not infer literal values of type {typename(raw_type_annotation)}")


T = TypeVar("T")

# It may seem natural to use a generic signature for this function to return the
# type corresponding to the specified union type like:
#
#     def validate_type_union(type_union: Type[T], args: argparse.Namespace) -> T:
#
# However, that doesn't work currently, because of limitations of Union and Type[T].
# See: https://github.com/python/mypy/issues/9003


def validate_type_union(args: argparse.Namespace, type_union: object) -> object:
    """
    Helper function to validate args against a type union (but with untyped return).
    """
    type_annotation = TypeAnnotation(type_union)

    errors = []

    for sub_type in type_annotation.get_underlyings_if_union():
        if isinstance(sub_type.raw_type, type) and issubclass(sub_type.raw_type, TypedArgs):
            try:
                typed_args_class = cast(TypedArgs, sub_type.raw_type)
                return typed_args_class.from_argparse(args)
            except Exception as e:
                errors.append(str(e))

    if len(errors) == 0:
        raise TypeError(f"Type union {type_union} did not contain any sub types of type TypedArgs.")
    else:
        errors_str = "\n".join([f" - {error}" for error in errors])
        raise TypeError(f"Validation failed against all sub types of union type:\n{errors_str}")


class WithUnionType(RuntimeGeneric, Generic[T]):
    """
    Helper class to validate args against a type union (with proper return type).
    """

    @classmethod
    def validate(cls, args: argparse.Namespace) -> T:
        generic_args = TypeAnnotation(cls).args
        # Should be impossible to violate, because the Python interpreter already checks
        # that the number of specified generics is correct.
        assert (
            len(generic_args) == 1
        ), f"Class needs exactly one generic annotation. Annotations are {generic_args}."
        return validate_type_union(args, generic_args[0])  # type: ignore
