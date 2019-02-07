"""
echam6 Component

A atmosphere Model, Version: 6.3.04p1

Please write some more documentation.

Written by component_cookiecutter

----
"""

import logging
import os

from pyesm.component import Component


class Echam6(Component):
    """ A docstring for your component """
    DOWNLOAD_ADDRESS = "http://some/address/of/a/project"
    NAME = "echam6"
    VERSION = "6.3.04p1"
    TYPE = "atmosphere"

    def _resolution(self, res_key=None):
        """
        Defines the resolution and generates the following attributes
        """
        Resolutions = {
                    "T31":
                        {
                            "res": "T31",
                            "levels": "L19",
                            "Timestep": 450,
                            "_nx": 96,
                            "_ny": 48,
                            "_ngridpoints": 96*48,
                            },

                    "T63":
                        {
                            "res": "T63",
                            "levels": "L47",
                            "Timestep": 450,
                            "_nx": 192,
                            "_ny": 96,
                            "_ngridpoints": 192*96,
                            },

                    "T127":
                        {
                            "res": "T127",
                            "levels": "L47",
                            "Timestep": 200,
                            "_nx": 384,
                            "_ny": 192,
                            "_ngridpoints": 384*192,
                            },
                      }
        for key, value in Resolutions[res_key].items():
            setattr(self, key, value)
