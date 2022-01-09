import math
import sys
import coloredlogs
from pyvox.parser import VoxParser
from pyvox.writer import VoxWriter
from pyvox.models import Vox
import copy

charModel = VoxParser(sys.argv[1]).parse()
charImg = charModel.to_dense()
headImg = copy.deepcopy(charImg)
UTorImg = copy.deepcopy(charImg)
LTorImg = copy.deepcopy(charImg)
lUArImg = copy.deepcopy(charImg)
lLArImg = copy.deepcopy(charImg)
lHanImg = copy.deepcopy(charImg)
rUArImg = copy.deepcopy(charImg)
rLArImg = copy.deepcopy(charImg)
rHanImg = copy.deepcopy(charImg)
lULeImg = copy.deepcopy(charImg)
lLLeImg = copy.deepcopy(charImg)
lFotImg = copy.deepcopy(charImg)
rULeImg = copy.deepcopy(charImg)
rLLeImg = copy.deepcopy(charImg)
rFotImg = copy.deepcopy(charImg)

print(charImg.shape)
for i in range(80):
    for j in range(80):
        for k in range(80):
            x=79-i;y=79-j;z=79-k
            if z< 50 : 
                headImg[j][k][i]=0
            if z>49  or z<36  or x<31 or x> 47 : 
                UTorImg[j][k][i]=0
            if z>35  or z<28  or x<31 or x> 47 : 
                LTorImg[j][k][i]=0
            if x< 45 or x> 54 : 
                rUArImg[j][k][i]=0 
            if x< 55 or x> 65 : 
                rLArImg[j][k][i]=0 
            if x< 66 : 
                rHanImg[j][k][i]=0
            if x< 24 or x> 33 : 
                lUArImg[j][k][i]=0 
            if x< 13 or x> 23 : 
                lLArImg[j][k][i]=0 
            if x> 12 : 
                lHanImg[j][k][i]=0
            if x< 40 or z>32 or z<17: 
                rULeImg[j][k][i]=0
            if x< 40 or z>16 or z< 3: 
                rLLeImg[j][k][i]=0  
            if x< 40 or z>2 : 
                rFotImg[j][k][i]=0  
            if x> 38 or z>32 or z<17: 
                lULeImg[j][k][i]=0 
            if x> 38 or z>16 or z< 3: 
                lLLeImg[j][k][i]=0 
            if x> 38 or z>2: 
                lFotImg[j][k][i]=0 


headModel=Vox.from_dense(headImg)
UTorModel=Vox.from_dense(UTorImg)
LTorModel=Vox.from_dense(LTorImg)
rUArModel=Vox.from_dense(rUArImg)
rLArModel=Vox.from_dense(rLArImg)
rHanModel=Vox.from_dense(rHanImg)
lUArModel=Vox.from_dense(lUArImg)
lLArModel=Vox.from_dense(lLArImg)
lHanModel=Vox.from_dense(lHanImg)
rULeModel=Vox.from_dense(rULeImg)
rLLeModel=Vox.from_dense(rLLeImg)
rFotModel=Vox.from_dense(rFotImg)
lULeModel=Vox.from_dense(lULeImg)
lLLeModel=Vox.from_dense(lLLeImg)
lFotModel=Vox.from_dense(lFotImg)


VoxWriter('explode/Head_Geo.vox',headModel).write()
VoxWriter('explode/UpperTorso_Geo.vox',UTorModel).write()
VoxWriter('explode/LowerTorso_Geo.vox',LTorModel).write()

VoxWriter('explode/RightUpperArm.vox',rUArModel).write()
VoxWriter('explode/RightLowerArm.vox',rLArModel).write()
VoxWriter('explode/RightHand.vox',rHanModel).write()

VoxWriter('explode/LeftUpperArm.vox',lUArModel).write()
VoxWriter('explode/LeftLowerArm.vox',lLArModel).write()
VoxWriter('explode/LeftHand.vox',lHanModel).write()

VoxWriter('explode/RightUpperLeg_Geo.vox',rULeModel).write()
VoxWriter('explode/RightLowerLeg_Geo.vox',rLLeModel).write()
VoxWriter('explode/RightFoot_Geo.vox',rFotModel).write()

VoxWriter('explode/LeftUpperLeg_Geo.vox',lULeModel).write()
VoxWriter('explode/LeftLowerLeg_Geo.vox',lLLeModel).write()
VoxWriter('explode/LeftFoot_Geo.vox',lFotModel).write()