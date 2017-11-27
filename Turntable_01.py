import bpy
from bpy.types import Panel, Operator


class cameraRotate(Operator):
    bl_label = "Turntable"
    bl_idname = 'rotate.cam'
    
    def execute(self, context):
        camera = bpy.context.scene.camera
        camera.select = True
        
        obj = bpy.context.object
        
        bpy.ops.transform.rotate(value=1, axis=(0, 0, 1), constraint_axis=(False, False, True), 
        constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
        return{'FINISHED'}


class newScenePanel(Panel):
    bl_label = "Turntable"
    bl_idname = "SCENE_PT_turtable"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        scene = context.scene

       
        layout.label(text="Animation:")

        row = layout.row()
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")
        
        row = layout.row()
        row.operator("rotate.cam", text="Rotate", icon="QUESTION")




def register():
    
    bpy.utils.register_class(newScenePanel)
    bpy.utils.register_class(cameraRotate)


def unregister():
   
    bpy.utils.unregister_class(newScenePanel)
    bpy.utils.unregister_class(cameraRotate)


if __name__ == "__main__":
    register()
