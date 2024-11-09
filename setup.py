from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("phardwareitk.GUI.renderGUI", ["phardwareitk/GUI/renderGUI.pyx"]),
]

setup(
    name="phardwareitk",
    version="0.1.1",
    packages=["phardwareitk", "phardwareitk.CLI", ...],  # List all your packages here
    ext_modules=cythonize(extensions),
)
