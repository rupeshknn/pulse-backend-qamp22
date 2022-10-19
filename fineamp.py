# %%
# %load_ext autoreload
# %autoreload 2
# %%
import datetime
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["font.size"] = 16

from qiskit import QuantumCircuit, IBMQ, schedule
import qiskit.pulse as pulse
from qiskit.quantum_info.states import Statevector, DensityMatrix
from qiskit_dynamics import Solver, Signal
from qiskit_dynamics.pulse import InstructionToSignals
from qiskit.providers import BackendV2, QubitProperties
from qiskit.providers.options import Options
from qiskit.transpiler import Target


from qiskit.providers.models import PulseDefaults
from qiskit.qobj.pulse_qobj import PulseLibraryItem, PulseQobjInstruction
from qiskit.providers.models.pulsedefaults import Command

from qiskit_experiments.exceptions import QiskitError
# %%
IBMQ.load_account()
provider = IBMQ.get_provider(hub="ibm-q", group="open", project="main")
backend = provider.get_backend("ibmq_lima")
# %%
from qiskit_experiments.calibration_management.calibrations import Calibrations
from qiskit_experiments.calibration_management.basis_gate_library import (
    FixedFrequencyTransmon,
)

qubit = 0
library = FixedFrequencyTransmon()
cals = Calibrations.from_backend(backend, libraries=[library])
# %%

from qiskit_experiments.test.iq_pulse_backend import SingleTransmonTestBackend
pulse_backend = SingleTransmonTestBackend()
# %%

from qiskit_experiments.library.calibration.fine_amplitude import FineXAmplitudeCal
amp_x_cal = FineXAmplitudeCal(qubit, cals, backend=backend, schedule_name="x")
# %%
amp_x_cal.circuits()[3].draw()
# %%
