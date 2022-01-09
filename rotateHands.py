import bpy,math
print('aaaa')

bpy.ops.import_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/RightUpperArm.ply")
bpy.context.scene.cursor.location = (-0.5, 0.0, 3.8)
bpy.context.scene.objects["RightUpperArm"] 
bpy.ops.object.origin_set(type='ORIGIN_CURSOR',center='MEDIAN')
bpy.ops.transform.rotate(value=math.pi/2,orient_axis='Y')
bpy.ops.export_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/RightUpperArm_new.ply")
bpy.ops.object.delete()

bpy.ops.import_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/RightLowerArm.ply")
bpy.context.scene.cursor.location = (-0.5, 0.0, 3.8)
bpy.context.scene.objects["RightLowerArm"] 
bpy.ops.object.origin_set(type='ORIGIN_CURSOR',center='MEDIAN')
bpy.ops.transform.rotate(value=math.pi/2,orient_axis='Y')
bpy.ops.export_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/RightLowerArm_new.ply")
bpy.ops.object.delete()

bpy.ops.import_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/RightHand.ply")
bpy.context.scene.cursor.location = (-0.5, 0.0, 3.8)
bpy.context.scene.objects["RightHand"] 
bpy.ops.object.origin_set(type='ORIGIN_CURSOR',center='MEDIAN')
bpy.ops.transform.rotate(value=math.pi/2,orient_axis='Y')
bpy.ops.export_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/RightHand_new.ply")
bpy.ops.object.delete()

bpy.ops.import_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/LeftUpperArm.ply")
bpy.context.scene.cursor.location = (0.6, 0.0, 3.8)
bpy.context.scene.objects["LeftUpperArm"] 
bpy.ops.object.origin_set(type='ORIGIN_CURSOR',center='MEDIAN')
bpy.ops.transform.rotate(value=-math.pi/2,orient_axis='Y')
bpy.ops.export_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/LeftUpperArm_new.ply")
bpy.ops.object.delete()

bpy.ops.import_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/LeftLowerArm.ply")
bpy.context.scene.cursor.location = (0.6, 0.0, 3.8)
bpy.context.scene.objects["LeftLowerArm"] 
bpy.ops.object.origin_set(type='ORIGIN_CURSOR',center='MEDIAN')
bpy.ops.transform.rotate(value=-math.pi/2,orient_axis='Y')
bpy.ops.export_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/LeftLowerArm_new.ply")
bpy.ops.object.delete()

bpy.ops.import_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/LeftHand.ply")
bpy.context.scene.cursor.location = (0.6, 0.0, 3.8)
bpy.context.scene.objects["LeftHand"] 
bpy.ops.object.origin_set(type='ORIGIN_CURSOR',center='MEDIAN')
bpy.ops.transform.rotate(value=-math.pi/2,orient_axis='Y')
bpy.ops.export_mesh.ply(filepath="C:/Users/user/Desktop/py-vox-io/examples/explode/LeftHand_new.ply")
bpy.ops.object.delete()