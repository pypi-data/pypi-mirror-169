#!/usr/bin/env jupyter

import typing as t

import pandas as pd

from copy import copy
from agora.io.signal import Signal, validate_merges
from postprocessor.core.abc import get_parameters, get_process
from postprocessor.core.processes.lineageprocess import (
    LineageProcessParameters,
)


class Chainer(Signal):
    """
    Class that extends signal by applying postprocesess.
    Instead of reading processes previously applied, it executes
    them when called.
    """

    process_types = ("multisignal", "processes", "reshapers")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(
        self,
        dataset: str,
        chain: t.Collection[str] = ("merger", "picker", "savgol"),
        in_minutes: bool = True,
        **kwargs,
    ):
        data = self.get_raw(dataset, in_minutes=in_minutes)
        if chain:
            data = self.apply_chain(data, **kwargs)
        return data

    def apply_chain(self, input_data: pd.DataFrame, chain, **kwargs):
        data = copy(input_data)
        for process in chain:
            params = kwargs.get(process, {})
            result = get_process(process).as_function(data, **params)
            process_type = process.__module__.split(".")[-2]
            if process_type == "reshapers":
                if process_type == "merger":
                    merges = process.as_function(data, **params)
                    valid_merges = validate_merges(
                        np.array(merges), np.array(list(df.index))
                    )
                    results = self.apply_prepost(
                        result, valid_merges, skip_pick=True
                    )
            data = results
        return data
