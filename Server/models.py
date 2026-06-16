from dataclasses import dataclass

@dataclass
class Finding:
    severity: str
    type: str
    value: str
    reason: str
