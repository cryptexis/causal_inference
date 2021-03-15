from typing import Dict

from .variable import Variable


class SCM:
    def __init__(self, name: str):
        self.name = name
        self.equations = []
        self.variable_registry = []
        self.output_nodes = set()
        self.input_nodes = set()

    def add_equation(
        self, outcome_variable: Variable, input_variables: Dict[Variable, float]
    ):
        """
        Adds equation of the SCM according to the relation of outcome variable and input variables
        :param outcome_variable: instance of Variable class
        :param input_variables: Dict of Variables as keys and coefficients as values
        :return:
        """

        if outcome_variable.name not in self.variable_registry:
            self.variable_registry.append(outcome_variable.name)
            self.output_nodes.add(outcome_variable)

        for input_variable, _ in input_variables.items():
            if input_variable.name not in self.variable_registry:
                raise AttributeError(
                    "Independent variables should be added to SCM before Dependent variable"
                )

            self.input_nodes.add(outcome_variable)

        self.equations.append(
            {"input_variables": input_variables, "output_variable": outcome_variable}
        )
