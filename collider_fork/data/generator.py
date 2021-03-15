import numpy as np
import pandas as pd
from .scm import SCM


class DataGenerator:

    def generate(self, scm: SCM, n_samples: int, seed: int):
        pass


class SimpleDataGenerator(DataGenerator):

    def generate(self, scm: SCM, n_samples: int, seed: int):

        np.random.seed(seed)
        data = {}

        for equation in scm.equations:

            data[equation['output_variable'].name] = np.zeros(n_samples)

            for input_variable, coeff in equation['input_variables'].items():
                if input_variable.name not in data:
                    raise AttributeError(f"No data generated for dependent variable {input_variable.name}")
                data[equation['output_variable'].name] += data[input_variable.name]*coeff

            mean = 0
            std = 1.0
            if isinstance(equation['output_variable'].config, dict):
                mean = equation['output_variable'].config.get("mean", 0)
                std = equation['output_variable'].config.get("std", 1.0)

            data[equation['output_variable'].name] += np.random.normal(loc=mean, scale=std, size=n_samples)

            if isinstance(equation['output_variable'].config, dict) and 'mask' in equation['output_variable'].config:
                out_val = data[equation['output_variable'].name]
                out_val[out_val < equation['output_variable'].config['mask']] = 0
                out_val[out_val > 0] = 1
                data[equation['output_variable'].name] = out_val

        return pd.DataFrame.from_dict(data)
