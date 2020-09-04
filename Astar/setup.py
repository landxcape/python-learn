from setuptools import setup
from Cython.Build import cythonize

setup(name='Astar',
      ext_modules=(cythonize("astar.pyx")),
      zip_safe=False
      )
