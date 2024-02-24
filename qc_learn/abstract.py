from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from typing import Generic, TypeVar


class Qubit(metaclass=ABCMeta):
    @abstractmethod
    def h(self):
        pass

    @abstractmethod
    def measure(self) -> bool:
        pass

    @abstractmethod
    def reset(self):
        pass


QubitType = TypeVar("QubitType", bound=Qubit)


class QuantumDevice(
    Generic[QubitType],
    metaclass=ABCMeta,
):
    @abstractmethod
    def allocate_qubit(self) -> QubitType:
        pass

    @abstractmethod
    def deallocate_qubit(self, qubit: QubitType):
        pass

    @contextmanager
    def using_qubit(self):
        qubit = self.allocate_qubit()
        try:
            yield qubit
        finally:
            qubit.reset()
            self.deallocate_qubit(qubit)


def qrng(device: QuantumDevice[QubitType]) -> bool:
    with device.using_qubit() as q:
        q.h()
        return q.measure()


__all__ = [
    "qrng",
    "QuantumDevice",
    "Qubit",
    "QubitType"
]
