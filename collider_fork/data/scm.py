from typing import Dict
from .variable import Variable


class SCM:

    def __init__(self):
        self.equations = []
        self.variable_registry = []

    def add_equation(self, outcome_variable: Variable, input_variables: Dict[Variable, float]):

        if outcome_variable.name not in self.variable_registry:
            self.variable_registry.append(outcome_variable.name)

        for input_variable, _ in input_variables.items():
            if input_variable.name not in self.variable_registry:
                raise AttributeError('Independent variables should be added to SCM before Dependent variable')

        self.equations.append({
            'input_variables': input_variables,
            'output_variable': outcome_variable
        })
