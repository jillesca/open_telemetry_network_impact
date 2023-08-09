from abc import ABC, abstractclassmethod


class Parser(ABC):
    @abstractclassmethod
    def parse(self, data_to_parse: str) -> list:
        # TODO see how to enforce that parse method must return a list
        raise NotImplementedError
