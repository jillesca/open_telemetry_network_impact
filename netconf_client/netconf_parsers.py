from abc import ABC, abstractclassmethod


class Parser(ABC):
    @abstractclassmethod
    def parse(self, data_to_parse: str) -> str:
        raise NotImplementedError
