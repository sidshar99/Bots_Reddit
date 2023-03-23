import time as t
import pybullet as p
physicsClient = p.connect(p.GUI)
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

for i in range(0, 1000):
    p.stepSimulation()
    t.sleep(0.01)
    print(i)

p.disconnect()