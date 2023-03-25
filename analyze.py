import numpy as np
import matplotlib.pyplot as plt

#printing sensor values
backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')

plt.plot(backLegSensorValues, label = "BackLeg", linewidth=2)
plt.plot(frontLegSensorValues, label = "FrontLeg")
plt.legend()

plt.show()
