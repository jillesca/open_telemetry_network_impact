from abc import ABC, abstractclassmethod
from netconf_session import connect


class Filter_call(ABC):
    @abstractclassmethod
    def parse(self, filter: str) -> str:
        raise NotImplementedError
