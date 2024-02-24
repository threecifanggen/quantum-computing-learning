import numpy as np

from qc_learn.abstract import (
    qrng,
    Qubit,
    QuantumDevice,
)

class SimulatedQubit(Qubit):
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
    qsim = SingleQubitSimulator()
    for idx_sample in range(10):
        random_sample = qrng(qsim)
        print(f"Our QRNG returned {random_sample}.")
