import time as t
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
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

#Open-Loop Control Movement
#BackLeg movement parameters
BackLeg_amplitude = np.pi/4
BackLeg_frequency = 10
BackLeg_phaseOffset = 0

x = np.linspace(0, 2 * np.pi, 1000)
BackLeg_targetAngles = np.zeros(1000)
for i in range(0, 1000):
    BackLeg_targetAngles[i] = BackLeg_amplitude * np.sin(BackLeg_frequency * x[i] + BackLeg_phaseOffset)

np.save("data/BackLeg_targetAngles.npy", BackLeg_targetAngles)

#FrontLeg movement parameters
FrontLeg_amplitude = np.pi/4
FrontLeg_frequency = 10
FrontLeg_phaseOffset = 0

FrontLeg_targetAngles = np.zeros(1000)
for i in range(0, 1000):
    FrontLeg_targetAngles[i] = FrontLeg_amplitude * np.sin(FrontLeg_frequency * x[i] + FrontLeg_phaseOffset)

np.save("data/FrontLeg_targetAngles.npy", FrontLeg_targetAngles)
#starting simulation

#initialising the robot from the robotId
pyrosim.Prepare_To_Simulate(robotId)
for i in range(0, 1000):
    #stepping the simulation
    p.stepSimulation()
    
    #adding Touch sensor on the BackLeg link. Note: Touch sensors only work in non-root links.
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  
    # adding motors to joints. Motors are always attached to joints, rather than links.
    #The motor is going to apply rotational forces at the point where two links meet---their 
    #joint---to rotate those objects toward one another (like when you flex biped to rotate your 
    #lower arm toward your upper arm) or away from one another (like when you flex your tricep to rotate your lower arm away from your upper arm.
    pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = BackLeg_targetAngles[i],
    maxForce = 20)
    
    pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = FrontLeg_targetAngles[i],
    maxForce = 20)
    
    #delaying the execution of the loop so that we can see the simulation in action for each step
    t.sleep(0.01)
    

p.disconnect()


np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
