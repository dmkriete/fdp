# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:35:36 2015

@author: ktritz
"""

from .machine import Machine
from .parse import parse_method
from .globals import VERBOSE, FdpError
from .datasources import machineAlias, MACHINES


class Fdp(object):
    """
    The primary data object in FDP and the top-level container for machines.
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __getattr__(self, attribute):
        if VERBOSE:
            print('{}.__getattr__({})'.
                  format(self.__class__, attribute))
        machine_name = machineAlias(attribute)
        if machine_name not in MACHINES:
            raise FdpError('Invalid machine name')
        # subclass machine.Machine() for <machine_name>
        MachineClassName = 'Machine' + machine_name.capitalize()
        MachineClass = type(MachineClassName, (Machine, ), {})
        MachineClass._name = machine_name
        # parse fdp/methods and fdp/methods/<machine_name>
        parse_method(MachineClass, level='top')
        parse_method(MachineClass, level=machine_name)
        return MachineClass(machine_name, *self.args, **self.kwargs)

    def __dir__(self):
        return MACHINES
