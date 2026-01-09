from dataclasses import dataclass

@dataclass(frozen=True)
class AppSettings:
    environment: str = "development"
    debug: bool = True