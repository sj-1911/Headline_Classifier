from abc import ABC, abstractmethod
from datetime import datetime

class HeadlineComponent(ABC):
    @abstractmethod
    def get_text(self) -> str:
        pass

class BaseHeadline(HeadlineComponent):
    def __init__(self, text: str):
        self._text = text

    def get_text(self) -> str:
        return self._text
    
class HeadlineDecorator(HeadlineComponent):
    def __init__ (self, component: HeadlineComponent):
        self._component = component
    
    @abstractmethod
    def get_text(self) -> str:
        pass

class TimestampDecorator(HeadlineDecorator):
    def get_text(self) -> str:
        now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        return f"{self._component.get_text()} {now}"


class KeywordDecorator(HeadlineDecorator):
    def __init__(self, component: HeadlineComponent, keyword: str):
        super().__init__(component)
        self.keyword = keyword.lower()

    def get_text(self) -> str:
        text = self._component.get_text()
        return text if self.keyword in text.lower() else ""
    

class TruncateDecorator(HeadlineDecorator):
    def __init__(self, component: HeadlineComponent, max_length: int):
        super().__init__(component)
        self.max_length = max_length

    def get_text(self) -> str:
        text = self._component.get_text()
        return text if len(text) <= self.max_length else text[:self.max_length] + "..."
