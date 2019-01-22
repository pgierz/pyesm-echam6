"""
Compute and Post-Processing Jobs for echam6

Written by component_cookiecutter

----
"""

from component.component_simulation import ComponentCompute
from echam6 import Echam6

class Echam6Compute(Echam6, ComponentCompute):
    """ A docstring. Please fill this out at least a little bit """

    def _compute_requirements(self):
        """ Compute requirements for echam6 """
        self.executeable = None
        self.command = None
        self.num_tasks = None
        self.num_threads = None

