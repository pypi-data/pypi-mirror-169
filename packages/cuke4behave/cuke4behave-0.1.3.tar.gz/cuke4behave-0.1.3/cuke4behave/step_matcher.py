"""Step Matcher for Cucumber Expressions in Behave.

Add Cucumber Expression support into Behave
"""


from typing import List, Optional, Callable

from behave.matchers import Matcher
from behave.model_core import Argument
from cucumber_expressions.expression import CucumberExpression
from cucumber_expressions.parameter_type_registry import ParameterTypeRegistry


class CucumberExpressionMatcher(Matcher):
    """Matcher for official Cucumber Expressions.

    With Parameter Type support
    """

    def __init__(
        self,
        func: Callable,
        pattern: str,
        step_type: Optional[str] = None,
        # TODO add a none type constructor for testing in basic_tests.py
        parameter_type_registry: Optional[ParameterTypeRegistry] = None,
    ):
        """Is the Constructor.

        :args
        """
        super(CucumberExpressionMatcher, self).__init__(func, pattern, step_type)
        self.func = func
        self.pattern = pattern
        self.parameter_type_registry = parameter_type_registry
        self.__cucumber_expresion_ = CucumberExpression(
            pattern, self.parameter_type_registry
        )

    def check_match(self, step: str) -> Optional[List[Argument]]:
        """Check step matches this step."""
        maybe_match = self.__cucumber_expresion_.match(step)
        if maybe_match:
            return [
                Argument(x.group.start, x.group.end, str(x.value), x.value)
                for x in maybe_match
            ]
        elif self.pattern == step:
            return []
        else:
            return None

    @property
    def regex_pattern(self):
        """Return the regex of the pattern from the Cucumber Expression."""
        self.__cucumber_expresion_.regexp


def build_step_matcher(parameter_type_registry: ParameterTypeRegistry) -> Callable:  # noqa: E501
    """Build a step matcher to use with behave.

    This builds a function that can use as a step matcher.
    It matches the internal behavior of Behave.
    It partially builds a CucumberExpressionMatcher.
    That function takes a generic and blank function, as a method to build
    the given step definition.

    The pattern is the kwarg passed to the step definition.
    These are mostly internal behaviors.
    """
    def step_matcher(func: Callable, pattern: str):
        return CucumberExpressionMatcher(func, pattern,
                                         parameter_type_registry=parameter_type_registry)  # noqa: E501
    return step_matcher
