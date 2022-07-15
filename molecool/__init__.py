"""A Python package for analyzing and visualizing xyz files."""

# Add imports here
import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from .atom_data import atom_colors


from .functions import *
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
