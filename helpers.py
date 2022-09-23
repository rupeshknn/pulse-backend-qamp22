from qiskit_experiments.framework.base_analysis import BaseAnalysis
from qiskit_experiments.framework import ExperimentData

def retrive_exp(exp_obj, job_id, backend = None, analysis = "default", timeout = None, **run_options):
    """Run an experiment and perform analysis.

    Args:
        backend: Optional, the backend to run the experiment on. This
                    will override any currently set backends for the single
                    execution.
        analysis: Optional, a custom analysis instance to use for performing
                    analysis. If None analysis will not be run. If ``"default"``
                    the experiments :meth:`analysis` instance will be used if
                    it contains one.
        timeout: Time to wait for experiment jobs to finish running before
                    cancelling.
        run_options: backend runtime options used for circuit execution.

    Returns:
        The experiment data object.

    Raises:
        QiskitError: if experiment is run with an incompatible existing
                        ExperimentData container.
    """

    if backend is not None or analysis != "default" or run_options:
        # Make a copy to update analysis or backend if one is provided at runtime
        experiment = exp_obj.copy()
        if backend:
            experiment._set_backend(backend)
        if isinstance(analysis, BaseAnalysis):
            experiment.analysis = analysis
        if run_options:
            experiment.set_run_options(**run_options)
    else:
        experiment = exp_obj

    # if experiment.backend is None:
    #     raise QiskitError("Cannot run experiment, no backend has been set.")

    # Finalize experiment before executions
    experiment._finalize()

    # Generate and transpile circuits
    transpiled_circuits = experiment._transpiled_circuits()

    # Initialize result container
    experiment_data = experiment._initialize_experiment_data()

    # Run options
    run_opts = experiment.run_options.__dict__

    # Run jobs
    jobs = backend.retrieve_job(job_id) #experiment._run_jobs(transpiled_circuits, **run_opts)
    experiment_data.add_jobs(jobs, timeout=timeout)

    # Optionally run analysis
    if analysis and experiment.analysis:
        experiment_data =  experiment.analysis.run(experiment_data)
    
    if exp_obj.auto_update and analysis:
            experiment_data.add_analysis_callback(exp_obj.update_calibrations)

    return experiment_data