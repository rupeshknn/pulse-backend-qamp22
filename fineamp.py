# %%
# %load_ext autoreload
# %autoreload 2
# %%
# import datetime
# from enum import Flag
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["font.size"] = 16

# from qiskit import QuantumCircuit, IBMQ, schedule
# import qiskit.pulse as pulse
# from qiskit.quantum_info.states import Statevector, DensityMatrix
# from qiskit_dynamics import Solver, Signal
# from qiskit_dynamics.pulse import InstructionToSignals
# from qiskit.providers import BackendV2, QubitProperties
# from qiskit.providers.options import Options
# from qiskit.transpiler import Target


# from qiskit.providers.models import PulseDefaults
# from qiskit.qobj.pulse_qobj import PulseLibraryItem, PulseQobjInstruction
# from qiskit.providers.models.pulsedefaults import Command

# from qiskit_experiments.exceptions import QiskitError
# %%
# IBMQ.load_account()
# provider = IBMQ.get_provider(hub="ibm-q", group="open", project="main")
# h_backend = provider.get_backend("ibmq_lima")
# %%

from qiskit_experiments.test.iq_pulse_backend import SingleTransmonTestBackend
pulse_backend = SingleTransmonTestBackend(noise=False)
# %%
from qiskit_experiments.calibration_management.calibrations import Calibrations
from qiskit_experiments.calibration_management.basis_gate_library import (
    FixedFrequencyTransmon,
)

qubit = 0
library = FixedFrequencyTransmon()
cals = Calibrations.from_backend(pulse_backend)# libraries=[library])
cals.parameters_table()
# %%

from qiskit_experiments.library.calibration.fine_amplitude import FineXAmplitudeCal
from qiskit_experiments.library.characterization import FineXAmplitude

# amp_x_cal = FineXAmplitudeCal(qubit, cals, backend=pulse_backend, schedule_name="x")
amp_x_cal = FineXAmplitude(qubit, backend=pulse_backend)


# %%
amp_x_cal._transpiled_circuits()[3].calibrations

# print(amp_x_cal.backend)
# %%

data_fine = amp_x_cal.run().block_for_results()

# %%

# list(pulse_backend._schedule_cache.keys())
data_fine.figure(0)
# %%

cals.parameters_table()['data']


# %%
data_fine.figure(0)
# %%
print(data_fine.analysis_results("d_theta"))

# %%
dtheta = data_fine.analysis_results("d_theta").value.nominal_value
target_angle = np.pi
scale = target_angle / (target_angle + dtheta)
pulse_amp = cals.get_parameter_value("amp", qubit, "x")
print(f"The ideal angle is {target_angle:.2f} rad. We measured a deviation of {dtheta:.3f} rad.")
print(f"Thus, scale the {pulse_amp:.4f} pulse amplitude by {scale:.3f} to obtain {pulse_amp*scale:.5f}.")
# %%
pd.DataFrame(**cals.parameters_table(qubit_list=[qubit, ()], parameters="amp"))

# %%
data_fine2 = amp_x_cal.run().block_for_results()
data_fine2.figure(0)
# %%
amp_x_cal.circuits()[3].data
# %%
cals.get_inst_map()._map['x']
# %%
amp_x_cal.calibrations.default_inst_map._map #_transpiled_circuits()[3].data

# %%
amp_x_cal._transpiled_circuits()[3].data[0].operation
# %%
pulse_backend