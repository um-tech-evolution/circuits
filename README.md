
# Circuits

A Python program and library that allows the simulation of technological
evolution using logic circuits as a proxy for actual technologies. Based on the
work of Arthur and Polak [1].

We expect to use the program in two ways.  First, we will replicate the results
of Arthur and Polak.  Second, this program will be a component in a larger
simulation of the role of social communication in technological innovation.

[1] W. Arthur and W. Polak, “The evolution of technology within a simple
computer model,” Complexity, vol. 11, no. 5, pp. 23–31, 2006.

## Documentation

![Docs](https://readthedocs.org/projects/evolutionary-circuits/badge/?version=latest>)

The [documentation](http://evolutionary-circuits.readthedocs.org/en/latest/) is
hosted over at Read The Docs and is automatically built on each commit.

## Tests

![Build Status](https://travis-ci.org/um-tech-evolution/circuits.svg?branch=master)

There is a suite of unit tests in the `test` directory. They use both standard
Python tests and Nose-style tests, so it is best to use Nose to run them.
Additionally, some of the simpler functions only have doc tests, these can be
run very simple with Nose, just add the `--with-doctest` flag. This can be done
with the following command (once the `nose` package is installed):

```
$ nosetests --with-doctest
```
