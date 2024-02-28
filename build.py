""" Modulo pybuilder"""
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


NAME = "G801.2024.T06.EG2"
DEFAULT_TASK = "publish"


@init

def SetProperties(project):
    """este es el init"""
