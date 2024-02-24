
import numpy as np

from qc_learn.abstract import (
    qrng,
    Qubit,
    QuantumDevice,
)

class SimulatedQubit(Qubit):
    """
    A class representing a simulated qubit.

    Attributes:
        H (np.ndarray): The Hadamard gate matrix.
        KET_0 (np.ndarray): The ket 0 state matrix.
        state (np.ndarray): The current state of the qubit.

    Methods:
        __init__(): Initializes the qubit.
        h(): Applies the Hadamard gate to the qubit.
        measure() -> bool: Measures the qubit and returns the measurement result.
        reset(): Resets the qubit to the ket 0 state.
    """

    H: np.ndarray[np.int32, np.dtype[np.int32]] = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    KET_0: np.ndarray[np.int32, np.dtype[np.int32]] = np.array([[1], [0]])

    
    state: np.ndarray[np.int32, np.dtype[np.int32]]
    def __init__(self):
        self.reset()

    def h(self):
        self.state = self.H @ self.state

    def measure(self) -> bool:
        pr0 = np.abs(self.state[0, 0]) ** 2
        sample = np.random.random() <= pr0
        return bool(0 if sample else 1)

    def reset(self):
        self.state = self.KET_0.copy()

class SingleQubitSimulator(QuantumDevice[SimulatedQubit]):
    """
    A class representing a single qubit simulator.

    Attributes:
        qubit (SimulatedQubit): The simulated qubit.

    Methods:
        __init__(): Initializes the simulator.
        allocate_qubit() -> SimulatedQubit: Allocates a qubit.
        deallocate_qubit(qubit: SimulatedQubit): Deallocates a qubit.
    """

    def __init__(self) -> None:
        self.qubit = SimulatedQubit()
    
    def allocate_qubit(self) -> SimulatedQubit:
        return self.qubit

    
    def deallocate_qubit(self, qubit: SimulatedQubit):
        qubit.reset()
        self.qubit = qubit

__all__ = [
    "SimulatedQubit",
    "SingleQubitSimulator"   
]

if __name__ == "__main__":
    # example of creating a simulator
    qsim = SingleQubitSimulator()
    for idx_sample in range(10):
        random_sample = qrng(qsim)
        print(f"Our QRNG returned {random_sample}.")
