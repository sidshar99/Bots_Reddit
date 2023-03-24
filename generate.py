import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF("world.sdf")

    #initializing box dimensions
    length = 1
    width = 1
    height = 1  

    pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5] , size=[length, width, height])

    pyrosim.End()
    
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    
    #initializing box dimensions
    length = 1
    width = 1
    height = 1
    
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length, width, height])
    
    #adding a joint between Torso and Leg links. Note: joints should always be named "Parent_Child"
    pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso", child = "BackLeg", type = "revolute", position = [1,0,1])
    
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[length, width, height])
    
    #Joints with no upstream joint have absolute positions. Every other joint has a position relative to its upstream joint.
    pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [2,0,1])
    
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[length, width, height])
    
    
    pyrosim.End()    

Create_Robot()
Create_World()