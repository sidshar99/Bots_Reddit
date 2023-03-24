import time as t
import pybullet as p
import pybullet_data
physicsClient = p.connect(p.GUI) 
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

#forces 
p.setGravity(0,0,-9.8)

#floor
planeId = p.loadURDF("plane.urdf")

#loading the world
p.loadSDF("boxes.sdf")

for i in range(0, 1000):
    p.stepSimulation()
    t.sleep(0.01)
    print(i)

p.disconnect()