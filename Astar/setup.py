from distutils.core import setup
import py2exe

setup(
    name='Astar',
    version='0.1dev',
    packages=['astar', ],
    license='TechWithTim',
    long_description=open('README.txt').read(),
)
