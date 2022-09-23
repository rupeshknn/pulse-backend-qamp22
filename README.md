# pulse-backend-qamp22
Developing a backend-sim in Qiskit Experiments (QE) capable of simulating pulse schedules using the Qiskit Dynamics time evolution package. 
A Hamiltonian simulation backend would enable better tutorials and a revamped test suite for the package.


## Description
Qiskit Experiments (QE) is a framework that allows users to easily run experiments to, for example, calibrate or characterize the pulses that implement a quantum gate. QE provides a library of experiments to perform these tasks (fine amplitude calibration, drag, etc...). Currently, each experiment is tested using a fake backend that hard-codes the experimental response of a real backend. This (a) limits our testing abilities and (b) limits the tutorials that we can write. In the meantime, Qiskit Dynamics has emerged as a viable Qiskit pulse-level simulator that allows users to simulate pulse schedules.

The aim of this project is to develop a backend capable of simulating pulse schedules with Qiskit Dynamics to enable tutorials and tests in QE.

## Deliverables
The project has the following deliverables:
1. Create a backend for single-qubit characterization and calibration experiments that is capable of simulating the pulse schedules embedded in the circuit.
2. Update the existing calibration tutorial to use this backend.
3. Write new tutorials on qubit calibration and characterization.

Stretch objectives might include
1. Writing backends for readout experiments and two-qubit experiments.
2. Writing tutorials for readout and two-qubit experiments.
