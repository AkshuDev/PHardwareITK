from setuptools import setup, Extension
from Cython.Build import cythonize
import os

extensions = [
    Extension(name="phardwareitk.GUI.renderGUI", sources=["phardwareitk/GUI/renderGUI.pyx"]),
]

setup=(
    name="phardwareitk",
    extensions=cythonize(extensions)
)
