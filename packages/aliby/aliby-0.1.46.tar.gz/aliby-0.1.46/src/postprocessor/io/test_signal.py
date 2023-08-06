#!/usr/bin/env jupyter

import numpy as np
from agora.io.signal import Signal, validate_merges
from postprocessor.grouper import NameGrouper

fpath = "/home/alan/Documents/dev/skeletons/scripts/data/19203_2020_09_30_downUpshift_twice_2_0_2_glu_ura8_ura8h360a_ura8h360r_00"
grouper = NameGrouper(fpath)
s = Signal(grouper.fsignal.filename)
tmp = s.retained("/extraction/general/None/area")
valid_merges = validate_merges(s.get_merges(), np.array(list(tmp.index)))
