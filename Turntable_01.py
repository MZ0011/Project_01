import bpy
from bpy.types import Panel, Operator

bl_info = {  
 "name": "Turntable",  
 "author": "M.Z",  
 "version": (1, 0),  
 "blender": (2, 7, 9),  
 "location": "Properties > Scene > Turntable",  
 "description": "User can select to rotate either the mesh or the camera",  
 "warning": "",  
 "wiki_url": "",  
 "tracker_url": "",  
 "category": "Animation"}  


    
class rotateMesh(Operator):
    bl_label = "RotateMesh"
    bl_idname = 'rotate.mesh'
    

    def execute(self, context):
        
        scene = bpy.context.scene
        camera = bpy.context.scene.camera
        
        fstart = bpy.context.scene.frame_start 
        fend = bpy.context.scene.frame_end 

        for obj in scene.objects:
            if obj.type == 'MESH':
                obj.select = True
                group = bpy.ops.group.create()
                
                obj.rotation_euler = (0, 0, 0)
                obj.keyframe_insert(data_path="rotation_euler", frame = fstart)
                
                obj.rotation_euler = (0, 0, 6.28319) #360
                obj.keyframe_insert(data_path="rotation_euler", frame = fend)
       
            else: 
                obj.select = False
        
        bpy.ops.view3d.camera_to_view_selected()    
      
 
     
        return{'FINISHED'}   
    
    
class cameraRotate(Operator):
    bl_label = "Turntable"
    bl_idname = 'rotate.cam'
     
        
    def execute(self, context):
            
        scene = bpy.context.scene
        
         
        fstart = bpy.context.scene.frame_start 
        fend = bpy.context.scene.frame_end 
          
        for obj in scene.objects:
            if obj.type == 'MESH':
                obj.select = True
                area = bpy.context.area
                old_type = area.type
                area.type = 'VIEW_3D'
                group = bpy.ops.group.create()
                bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')
                bpy.ops.view3d.snap_cursor_to_selected()
                area.type = old_type
               
                 
            else: 
                obj.select = False
         
        empty = bpy.ops.object.empty_add(type='PLAIN_AXES',view_align=False)
        
       
        for camera in scene.objects:
          
           if camera.type == 'CAMERA':
                camera.select = True
               
                bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
                
           else:
              camera.select = False
          

        for empty in scene.objects:
            if empty.type == 'EMPTY':
                empty.select = True

                empty.rotation_euler = (0, 0, 0)
                empty.keyframe_insert(data_path="rotation_euler", frame = fstart)

                empty.rotation_euler = (0, 0, 6.28319) #360
                empty.keyframe_insert(data_path="rotation_euler", frame = fend)   


            else:
                empty.select = False
                
                

        camera.select = True   
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.view3d.camera_to_view_selected()  
        
        return{'FINISHED'}


class newScenePanel(Panel):
    bl_label = "Turntable"
    bl_idname = "SCENE_PT_turtable"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = 'scene'

    def draw(self, context):
        layout = self.layout
        obj = context.object
        scene = context.scene

       
        layout.label(text="Animation:")

        row = layout.row()
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")
        
        row = layout.row()
        row.operator("rotate.cam", text="Rotate Camera", icon="CAMERA_DATA")
        
        row = layout.row()
        row.operator("rotate.mesh", text="Rotate Mesh", icon="MESH_CUBE")




def register():
    
    bpy.utils.register_class(newScenePanel)
    bpy.utils.register_class(cameraRotate)
    bpy.utils.register_class(rotateMesh)



def unregister():
   
    bpy.utils.unregister_class(newScenePanel)
    bpy.utils.unregister_class(cameraRotate)
    bpy.utils.unregister_class(rotateMesh)


if __name__ == "__main__":
    register()
