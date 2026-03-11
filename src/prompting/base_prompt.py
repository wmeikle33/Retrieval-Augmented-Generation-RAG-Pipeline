from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class BasePrompt:
    name: str
    template: str
    input_variables: List[str] = field(default_factory=list)

    def validate(self, variables: Dict[str, str]):
        missing = [v for v in self.input_variables if v not in variables]
        if missing:
            raise ValueError(
                f"Missing variables for prompt '{self.name}': {missing}"
            )

    def render(self, variables: Dict[str, str]) -> str:
        self.validate(variables)
        return self.template.format(**variables)

@dataclass
class ChatPrompt(BasePrompt):
    system_template: str = ""

    def build_messages(self, variables: Dict[str, str]):
        self.validate(variables)

        system = self.system_template.format(**variables)
        user = self.template.format(**variables)

        return [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]

@dataclass
class PromptMetadata:
    description: str
    version: str
    author: str

@dataclass
class BasePrompt:
    name: str
    template: str
    input_variables: List[str]
    metadata: PromptMetadata | None = None
