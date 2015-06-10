"""
Add new scalers to this file both as imports and in the dictionary!
"""

from scaler_absolute import Absolute
from scaler_relative import Relative

scalers_dict = {
    "Absolute":Absolute,
    "Relative":Relative
}

def ScalerFactory(params):
    return scalers_dict[params["type"]](params)