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
        self.executeable = "echam6"
        self.command = None
        # Number of nodes is depndent on the cores per compute node. Here, we
        # use a dictionary of dictionaries. The dictionary of the **outer**
        # dictionary is the resolution, the dictionary key of the **inter**
        # dictionary is the number of nodes needed. The hostname decides how
        # many cores per compute node exit.
        self.__nnodes = {"T63": {36: 12, 24: 18}}[self.LateralResolution]
        self.__nproca = {"T63": {36: 24, 24: 24}}[self.LateralResolution]
        self.__nprocb = {"T63": {36: 18, 24: 18}}[self.LateralResolution]
        self.__num_tasks = None
        self.__num_threads = None
