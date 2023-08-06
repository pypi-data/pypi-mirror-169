"""
Nicely typed env mgmt.
"""
from dotenv import dotenv_values

from dataclasses import dataclass
from pydantic import BaseSettings

config = dotenv_values(".env")

__all__ = ["environment"]


class Common(BaseSettings):
    test: str = config["TEST"]


class Servers(BaseSettings):
    pass


class Databases(BaseSettings):
    pass


class Environment(Common, Servers, Databases):
    pass


environment = Environment()
