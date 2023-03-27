import numpy as np
import matplotlib.pyplot as plt

#printing sensor values
BackLeg_targetAngles = np.load('data/BackLeg_targetAngles.npy')
FrontLeg_targetAngles = np.load('data/FrontLeg_targetAngles.npy')

plt.plot(BackLeg_targetAngles, label = "BackLeg_targetAngles")
plt.plot(FrontLeg_targetAngles, label = "FrontLeg_targetAngles")

plt.legend()

plt.show()
