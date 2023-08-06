from laboneq.dsl.enums import ModulationType
from laboneq.dsl.calibration import Oscillator, SignalCalibration, MixerCalibration


def calibrate_devices(device_setup, signal_group):

    signals = device_setup.logical_signal_groups[signal_group].logical_signals
    signals["drive_line"].calibration = SignalCalibration(
        oscillator=Oscillator(
            f"drive_osc_{signal_group}", frequency=100e6, modulation_type=ModulationType.HARDWARE
        ),
        mixer_calibration=MixerCalibration(
            voltage_offsets=[0.0, 0.0], correction_matrix=[[1.0, 0.0], [0.0, 1.0],],
        ),
    )
    qa_osc = Oscillator(f"qa_osc_{signal_group}", frequency=100e6, modulation_type=ModulationType.HARDWARE)
    signals["measure_line"].oscillator = qa_osc
    signals["acquire_line"].oscillator = qa_osc
