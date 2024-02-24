from qc_learn.abstract import Qubit, QuantumDevice, qrng
import pytest


class TestQubit:
    def test_h(self):
        
        with pytest.raises(TypeError):
            qubit = Qubit() # type: ignore
            qubit.h()

    def test_measure(self):
        
        with pytest.raises(TypeError):
            qubit = Qubit() # type: ignore
            qubit.measure()

    def test_reset(self):
        
        with pytest.raises(TypeError):
            qubit = Qubit() # type: ignore
            qubit.reset()


class TestQuantumDevice:
    def test_allocate_qubit(self):
        
        with pytest.raises(TypeError):
            device = QuantumDevice() # type: ignore
            device.allocate_qubit()

    def test_deallocate_qubit(self):
        
        with pytest.raises(TypeError):
            device = QuantumDevice() # type: ignore
            qubit = Qubit() # type: ignore
            device.deallocate_qubit(qubit)  # type: ignore

    def test_using_qubit(self):
        
        with pytest.raises(TypeError):
            device = QuantumDevice() # type: ignore
            with device.using_qubit():
                pass


def test_qrng():
    
    with pytest.raises(TypeError):
        device = QuantumDevice()  # type: ignore
        qrng(device)  # type: ignore


if __name__ == "__main__":
    pytest.main()
