import time as t
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
physicsClient = p.connect(p.GUI) 
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

#forces 
p.setGravity(0,0,-9.8)

#floor
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

#loading the world
p.loadSDF("world.sdf")

# vectors for storing sensor data
backLegSensorValues = np.zeros(10000)
frontLegSensorValues = np.zeros(10000)

#starting simulation

#initialising the robot from the robotId
pyrosim.Prepare_To_Simulate(robotId)
for i in range(0, 1000):
    #stepping the simulation
    p.stepSimulation()
    
    #adding Touch sensor on the BackLeg link. Note: Touch sensors only work in non-root links.
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    #printing sensor values
    
    
    #delaying the execution of the loop so that we can see the simulation in action for each step
    t.sleep(0.01)
    

p.disconnect()

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)