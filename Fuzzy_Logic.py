import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperature = ctrl.Antecedent(np.arange(0,101,1), 'Temperature')
humidity = ctrl.Antecedent()


temperature['cold'] = fuzz.trimf()