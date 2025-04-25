# strategies.py
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, headlines: list) -> list:
        pass

class AlphabeticalSort(SortStrategy):
    def sort(self, headlines: list) -> list:
        return sorted(headlines)

class LengthSort(SortStrategy):           # fixed spelling
    def sort(self, headlines: list) -> list:
        return sorted(headlines, key=len, reverse=True)

class ReverseSort(SortStrategy):
    def sort(self, headlines: list) -> list:
        return sorted(headlines, reverse=True)
