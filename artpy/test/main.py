from pytest import fixture
import numpy as np
import pandas as pd
from artpy import art

@fixture
def data():
    return pd.read_csv("data.csv").columns

@fixture
def answer():
    return pd.read_csv("result.csv")

# def test_art(data, answer):
    # result = art('Temperature', 'MaterialType', data)
    # assert(np.array_equal(result[0]['MaterialType'], answer[0]['MT']))
    # assert(np.array_equal(result[0]['Temperature'], answer[0]['TEMP']))
    # assert(np.array_equal(result[0]['Te*Ma'], answer[0]['MT*TEMP']))
