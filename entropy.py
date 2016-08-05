# -*- coding: utf-8 -*-

import numpy as np


def entropy(data):
    """
    エントロピーを求める関数
    """

    all_packets = sum(data)
    p_distribution = [float(x) / all_packets for x in data]
    result = [-(p * np.log2(p)) for p in p_distribution]
    return sum(result)
