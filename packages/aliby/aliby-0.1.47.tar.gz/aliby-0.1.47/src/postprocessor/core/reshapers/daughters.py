from itertools import product
from typing import Dict, Tuple
import typing as t

import numpy as np
import pandas as pd

from agora.utils.lineage import mb_array_to_dict
from postprocessor.core.lineageprocess import (
    LineageProcess,
    LineageProcessParameters,
)


class daughtersParameters(LineageProcessParameters):
    """
    Parameters
    ----------
    lineage_location: str
        url within data file with image
    """

    _defaults = {"lineage_location": "postprocessing/lineage_merged"}


class daughters(LineageProcess):
    """
    Return a DataFrame with the daughers with index indicating their mother.
    Unlike bud_metrics, which prioritises the most recent bud,
    this retrieves the entire time-lapse.
    """

    def __init__(self, parameters: daughtersParameters):
        super().__init__(parameters)

    def run(
        self,
        signal: pd.DataFrame,
        lineage: t.Optional[np.ndarray] = None,
    ):
        if lineage is None:
            lineage = self.lineage

        filtered_lineage = self.filter_signal_cells(signal, lineage)

        daughter_signal = []
        for (trap_id, mother_id), daughter_ids in filtered_lineage.items():
            daughter_ids = list(set(daughter_ids))
            dau_vals = signal.loc[daughter_ids]
            dau_vals["mother_label"] = mother_id
            dau_vals.set_index("mother_label", append=True, inplace=True)
            daughter_signal.append(dau_vals)

        combined = pd.concat(daughter_signal, axis=0)
        return combined.sort_index()
