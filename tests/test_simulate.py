import pytest
import numpy as np

from qc_learn.simulator import SimulatedQubit, SingleQubitSimulator


def test_SimulatedQubit():
    # Test case 1: Check if the SimulatedQubit class initializes correctly
    qubit = SimulatedQubit()
    assert np.array_equiv(qubit.state, np.array([[1], [0]]))

def test_SingleQubitSimulator():
    # Test case 1: Check if the SingleQubitSimulator class initializes correctly
    simulator = SingleQubitSimulator()
    assert np.array_equiv(simulator.qubit.state, np.array([[1], [0]]))

