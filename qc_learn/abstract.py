
from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from typing import Generic, TypeVar


class Qubit(metaclass=ABCMeta):
    """
    Abstract base class for representing a qubit in quantum computing.
    """

    @abstractmethod
    def h(self):
        """
        Apply the Hadamard gate to the qubit.
        """

    @abstractmethod
    def measure(self) -> bool:
        """
        Measure the qubit and return the measurement result as a boolean value.
        """

    @abstractmethod
    def reset(self):
        """
        Reset the qubit to its initial state.
        """


QubitType = TypeVar("QubitType", bound=Qubit)


class QuantumDevice(
    Generic[QubitType],
    metaclass=ABCMeta,
):
    """
    Abstract base class for representing a quantum device that can allocate and deallocate qubits.
    """

    @abstractmethod
    def allocate_qubit(self) -> QubitType:
        """
        Allocate a qubit from the quantum device and return it.
        """

    @abstractmethod
    def deallocate_qubit(self, qubit: QubitType):
        """
        Deallocate a qubit and return it to the quantum device.
        """

    @contextmanager
    def using_qubit(self):
        """
        Context manager for using a qubit from the quantum device.
        The qubit is automatically reset and deallocated after use.
        """
        qubit = self.allocate_qubit()
        try:
            yield qubit
        finally:
            qubit.reset()
            self.deallocate_qubit(qubit)


def qrng(device: QuantumDevice[QubitType]) -> bool:
    """
    Generate a random bit using a quantum device.

    Args:
        device: The quantum device to use for generating the random bit.

    Returns:
        The generated random bit as a boolean value.
    """
    with device.using_qubit() as q:
        q.h()
        return q.measure()


__all__ = [
    "qrng",
    "QuantumDevice",
    "Qubit",
    "QubitType"
]
