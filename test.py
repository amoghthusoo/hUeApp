from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (380, 768)
Window.top = 0
Window.left = 986

UI = '''
# <MyWidget@Image>:

#     angle : 0
#     canvas.before:
#         PushMatrix
#         Rotate:
#             angle:root.angle
#             axis : 0, 0, 1
#             origin : root.center
#     canvas.after:
#         PopMatrix

Image:
    id : color_wheel
    source : "data/color_wheel.png"
    pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
    #size_hint : (0.29, 0.29)
'''

class MyApp(MDApp):


    def build(self):

        app = Builder.load_string(UI)
        return app

root = MyApp()

if __name__ == "__main__":
    root.run()