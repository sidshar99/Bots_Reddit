import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

#initializing box dimensions
length = 1
width = 1
height = 1  

tower_height = 0
for i in range(0,10):
    pyrosim.Send_Cube(name="Box", pos=[0,0,tower_height+(height/2)] , size=[length, width, height])
    tower_height += height
    length *= 0.9
    width *= 0.9
    height *= 0.9

pyrosim.End()