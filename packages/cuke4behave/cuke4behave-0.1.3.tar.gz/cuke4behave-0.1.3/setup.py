# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cuke4behave']

package_data = \
{'': ['*']}

install_requires = \
['behave==1.2.6', 'cucumber-expressions==16.0.0']

setup_kwargs = {
    'name': 'cuke4behave',
    'version': '0.1.3',
    'description': 'Give Behave the power of Cucumber Expressions',
    'long_description': 'cuke4behave\n-----------\n\n# What is this. \nThere is a popular bdd library in python, Behave. \nCucumber Expressions are areplacement for regexs in Gherkin codebases. in large swaths of Behave implementations.\nCucumber also has a good language server and vscode extension.\nTo support both, this library allows you to inject a new step matcher into Behave, for use with more modern Gherkin paradigms.\n\n\n# Installation\nPip:\n\n`pip install cuke4behave`\n\nPoetry:\n\n`poetry install cuke4behave`\n\n\n# Usage\n\n``` python\nfrom cuke4behave import build_step_matcher\n\n\nfrom behave import given, then, when\nfrom behave.matchers import matcher_mapping, use_step_matcher\n\nfrom cucumber_expressions.parameter_type import ParameterType\nfrom cucumber_expressions.parameter_type_registry import ParameterTypeRegistry\n\nfrom cuke4behave.step_matcher import build_step_matcher\nfrom features.steps.helpers import Color, full_add\n\n# Build a ParameterType and ParameterTypeRegistry\ncolor_ptr = ParameterType(\n    "color",\n    "red|blue|orange|purple|brown",\n    Color,\n    lambda s: Color(s),\n    use_for_snippets="",\n    prefer_for_regexp_match=False,\n)\nptr = ParameterTypeRegistry()\n# do this as many times as necessary\nptr.define_parameter_type(color_ptr)\n\n# step matcher to pass to behave\nstep_matcher = build_step_matcher(ptr)\n\n# THIS IS IMPORTANT. Patch in the step matcher to behave\nmatcher_mapping["cucumber_expressions"] = step_matcher\n\nuse_step_matcher("cucumber_expressions")\n```\n`\n\n',
    'author': 'Dev Kumar Gupta',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
