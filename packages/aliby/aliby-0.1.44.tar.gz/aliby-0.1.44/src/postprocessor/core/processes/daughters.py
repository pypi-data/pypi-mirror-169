from itertools import product
from typing import Dict, Tuple

import numpy as np
import pandas as pd

from agora.utils.lineage import mb_array_to_dict
from postprocessor.core.processes.lineageprocess import (
    LineageProcess,
    LineageProcessParameters,
)


class daughtersParameters(LineageProcessParameters):
    """
    Parameters
    """

    _defaults = {"lineage_location": "postprocessing/lineage_merged"}


class daughters(LineageProcess):
    """
    Return a DataFrame with the daughers with index indicating their mother. Unlike bud_metrics,
    this retrieves the entire time-lapse.
    """

    def __init__(self, parameters: daughtersParameters):
        super().__init__(parameters)

    def run(
        self,
        signal: pd.DataFrame,
        mother_bud_ids: Dict[pd.Index, Tuple[pd.Index]] = None,
    ):
        if mother_bud_ids is None:
            filtered_lineage = self.filter_signal_cells(signal)
            mother_bud_ids = mb_array_to_dict(filtered_lineage)

        daughter_signal = []
        for i, ((trap_id, mother_id), daughter_ids) in enumerate(mother_bud_ids.items()):
            daughter_ids = list(set(daughter_ids))
            dau_vals = signal.loc[product([trap_id], daughter_ids)]
            dau_vals["mother_label"] = mother_id
            dau_vals.set_index("mother_label", append=True, inplace=True)
            daughter_signal.append(dau_vals)

        combined = pd.concat(daughter_signal, axis=0)
        combined.swap_level(["mother_level", "cell_label"])
        return combined

    def load_lineage(self, lineage):
        """
        Reshape the lineage information if needed
        """

        self.lineage = lineage
