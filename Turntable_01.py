import bpy
from bpy.types import Panel

class newScenePanel(Panel):
    bl_label = "Turntable"
    bl_idname = "SCENE_PT_turtable"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="New", icon='SCRIPTWIN')

       
       

def register():
    bpy.utils.register_class(newScenePanel)


def unregister():
    bpy.utils.unregister_class(newScenePanel)


if __name__ == "__main__":
    register()
