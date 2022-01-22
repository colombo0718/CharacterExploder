import bpy,math,os
directory="C:/Users/user/Desktop/examples/explode/"


rightJointPosition=(-0.6, 0.0, 4.8)#(-0.5, 0.0, 3.8)
leftJointPosition=(0.7, 0.0, 4.8)#(0.6, 0.0, 3.8)


HandPartNames=[
'LeftUpperArm','LeftLowerArm','LeftHand',
'RightUpperArm','RightLowerArm','RightHand'
]

for hand in HandPartNames :
    for file in os.listdir("./explode/") :
        if hand+".ply" in file:
            print(file)
            if "Right" in file: 
                bpy.ops.import_mesh.ply(filepath="./explode/"+file)
                bpy.context.scene.cursor.location = rightJointPosition
                bpy.context.scene.objects[file.split('.')[0]] 
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR',center='MEDIAN')
#                bpy.ops.transform.rotate(value=-math.pi/2,orient_axis='X')# @@@@@
                bpy.ops.transform.rotate(value=math.pi/2,orient_axis='Y')
                bpy.ops.export_mesh.ply(filepath="./explode/"+file)
                bpy.ops.object.delete()
            if "Left" in file: 
                bpy.ops.import_mesh.ply(filepath="./explode/"+file)
                bpy.context.scene.cursor.location = leftJointPosition
                bpy.context.scene.objects[file.split('.')[0]] 
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR',center='MEDIAN')
#                bpy.ops.transform.rotate(value=-math.pi/2,orient_axis='X')# @@@@@
                bpy.ops.transform.rotate(value=-math.pi/2,orient_axis='Y')
                bpy.ops.export_mesh.ply(filepath="./explode/"+file)
                bpy.ops.object.delete()


partNames=[
'Head','UpperTorso','LowerTorso',
'LeftUpperArm','LeftLowerArm','LeftHand',
'RightUpperArm','RightLowerArm','RightHand',
'LeftUpperLeg','LeftLowerLeg','LeftFoot',
'RightUpperLeg','RightLowerLeg','RightFoot'
]

for pname in partNames:
    for file in os.listdir("./explode/") :
        if pname+".ply" in file :
            print(file)
    
            bpy.ops.import_mesh.ply(filepath="./explode/"+file)
            part=bpy.data.objects[file.split('.')[0]]
            part.name=pname+"_Geo"
            arma=bpy.data.objects['Armature']
            bone=arma.data.bones.get(pname)

            part.parent = arma
            part.parent_bone = bone.name
            part.parent_type = 'BONE'

            matx = part.matrix_world.copy()
            part.matrix_local @= matx

            print(part.parent,part.parent_bone)
