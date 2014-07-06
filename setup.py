from distutils.core import setup
import os

DIRNAME = os.path.dirname(os.path.realpath(__file__))
VERSION = open(os.path.join(DIRNAME, 'VERSION'), 'r').read().strip()

setup(
    name='circuits',
    packages=['circuits'],
    scripts=['scripts'],
    version=VERSION,
    author='George Lesica',
    author_email='george@lesica.com',
    url='https://github.com/um-tech-evolution/circuits',
    description='A package for simulating technological evolution using logic circuits.',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Life',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Development Status :: 2 - Pre-Alpha'
    ]
)
