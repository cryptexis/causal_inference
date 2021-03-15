ENDOGENOUS_TYPE = "endogenous"
EXOGENOUS_TYPE = "exogenous"

from typing import Dict


class Variable:
    def __init__(self, name: str, type: str, config: Dict[str, float] = None):
        self.type = type
        self.name = name
        self.config = config
