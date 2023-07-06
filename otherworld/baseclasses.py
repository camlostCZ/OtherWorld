from abc import abstractclassmethod
from typing import TextIO


class YAMLSourced:
    @abstractclassmethod
    def load_yaml_file(self, fd: TextIO) -> None:
        """
        Load data from a YAML file.

        Args:
            fd (TextIO): File descriptor of the source YAML file
        """
