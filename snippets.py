self.options.update_options(**options)
    shots = self.options.get("shots")
    meas_level = self.options.get("meas_level")

    result = {
        "backend_name": f"{self.__class__.__name__}",
        "backend_version": self.backend_version,
        "qobj_id": 0,
        "job_id": 0,
        "success": True,
        "results": [],
        }

memory = self._state_vector_to_result(psi/np.linalg.norm(psi), **options)
    counts = dict(zip(*np.unique(memory, return_counts=True)))
    run_result = {
        "shots": shots,
        "success": True,
        "header": {"metadata": circuit.metadata},
        "meas_level": meas_level,
        "data": {
            "counts": counts,
            "memory": memory,
        },
    }

    if meas_level == MeasLevel.CLASSIFIED:
        counts = {}
        results = self._rng.multinomial(shots, prob_arr, size=1)[0]
        for result, num_occurrences in enumerate(results):
            result_in_str = str(format(result, "b").zfill(output_length))
            counts[result_in_str] = num_occurrences
        run_result["counts"] = counts
    else:
        # Phase has meaning only for IQ shot, so we calculate it here
        phase = self.experiment_helper.iq_phase([circuit])[0]
        iq_cluster_centers, iq_cluster_width = self.experiment_helper.iq_clusters([circuit])[0]

        # 'circ_qubits' get a list of all the qubits
        memory = self._draw_iq_shots(
            prob_arr,
            shots,
            list(range(output_length)),
            iq_cluster_centers,
            iq_cluster_width,
            phase,
        )
        if meas_return == "avg":
            memory = np.average(np.array(memory), axis=0).tolist()
        run_result["memory"] = memory

    result["results"].append(run_result)
return FakeJob(self, Result.from_dict(result))