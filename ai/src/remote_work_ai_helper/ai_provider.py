from abc import ABC, abstractmethod

class AIProvider(ABC):
    @abstractmethod
    def complete(self, prompt: str) -> str:
        pass
    
    @abstractmethod
    def chat(self, message: str) -> str:
        pass

class NoopAIProvider(AIProvider):
    def complete(self, prompt: str) -> str:
        return "[AI Stub] Generated content based on prompt."

    def chat(self, message: str) -> str:
        return "[AI Stub] Chat response."
