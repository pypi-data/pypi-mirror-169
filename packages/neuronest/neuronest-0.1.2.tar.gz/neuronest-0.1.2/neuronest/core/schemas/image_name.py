from __future__ import annotations

import re
from abc import ABC, abstractmethod
from typing import Tuple

from neuronest.core.schemas.environment import Environment


class StringWithValidation(ABC, str):
    @classmethod
    @abstractmethod
    def is_valid(cls, name: str) -> bool:
        raise NotImplementedError

    def __new__(cls, name, *args, **kwargs):
        if not cls.is_valid(name):
            raise ValueError(f"Incorrect given name: '{name}'")

        return str.__new__(cls, name, *args, **kwargs)


class PartImageName(StringWithValidation):
    @classmethod
    def is_valid(cls, name: str) -> bool:
        return len(name) > 0 and all(sep not in name for sep in (":", "/"))


class BaseImageName(PartImageName):
    """
    Example: 'ia-analysis'
    """


class Tag(PartImageName):
    """
    Example: '565726992'
    """

    @classmethod
    def is_valid(cls, name: str) -> bool:
        regex = r"(^latest$|^\d+$)"

        return super().is_valid(name) and bool(re.fullmatch(regex, name))


class GenericImageName(StringWithValidation):
    REGISTRY_DOMAIN = "eu.gcr.io"

    @classmethod
    def _split(cls, image_name: str) -> Tuple[str, str, BaseImageName, str]:
        split_image_name = image_name.split("/")

        if len(split_image_name) != 4:
            raise ValueError(f"Wrong image name: {image_name}")

        (
            registry_domain,
            project_id,
            base_image_name,
            suffix,
        ) = split_image_name

        if registry_domain != cls.REGISTRY_DOMAIN:
            raise ValueError(f"Wrong inferred registry domain: {registry_domain}")

        return (
            registry_domain,
            project_id,
            BaseImageName(base_image_name),
            suffix,
        )

    @classmethod
    def is_valid(cls, name: str) -> bool:
        try:
            cls._split(name)
        except ValueError:
            return False

        return True

    @classmethod
    def build(
        cls,
        project_id: str,
        base_image_name: BaseImageName,
        environment: Environment,
        **kwargs,
    ) -> ImageName:
        raise NotImplementedError


class ImageName(GenericImageName):
    """
    Example: 'eu.gcr.io/arctic-victor-272109/ia-analysis/test'
    """

    TEMPLATE = "{registry_domain}/{project_id}/{base_image_name}/{environment}"

    @classmethod
    def _split(cls, image_name: str) -> Tuple[str, str, BaseImageName, Environment]:
        registry_domain, project_id, base_image_name, suffix = super()._split(
            image_name
        )

        environment = Environment(suffix)

        return registry_domain, project_id, base_image_name, environment

    @classmethod
    def build(
        cls,
        project_id: str,
        base_image_name: BaseImageName,
        environment: Environment,
        **kwargs,
    ) -> ImageName:
        return cls(
            cls.TEMPLATE.format(
                registry_domain=cls.REGISTRY_DOMAIN,
                project_id=project_id,
                base_image_name=BaseImageName(base_image_name),
                environment=Environment(environment),
            )
        )

    def split_base_image_environment(
        self,
    ) -> Tuple[BaseImageName, Environment]:
        _, _, base_image_name, environment = self._split(self)

        return base_image_name, environment


class ImageNameWithTag(GenericImageName):
    """
    Example: 'eu.gcr.io/arctic-victor-272109/ia-analysis/test:565726992'
    """

    TEMPLATE = "{registry_domain}/{project_id}/{base_image_name}/{environment}:{tag}"

    @classmethod
    def _split(
        cls, image_name: str
    ) -> Tuple[str, str, BaseImageName, Environment, Tag]:
        registry_domain, project_id, base_image_name, suffix = super()._split(
            image_name
        )

        environment, tag = suffix.split(":")
        environment, tag = Environment(environment), Tag(tag)

        return registry_domain, project_id, base_image_name, environment, tag

    @classmethod
    def build(
        cls,
        project_id: str,
        base_image_name: BaseImageName,
        environment: Environment,
        **kwargs,
    ) -> ImageNameWithTag:
        return cls(
            cls.TEMPLATE.format(
                registry_domain=cls.REGISTRY_DOMAIN,
                project_id=project_id,
                base_image_name=BaseImageName(base_image_name),
                environment=Environment(environment),
                tag=Tag(kwargs["tag"]),
            )
        )

    def split_base_image_environment_and_tag(
        self,
    ) -> Tuple[BaseImageName, Environment, Tag]:
        _, _, base_image_name, environment, tag = self._split(self)

        return base_image_name, environment, tag
