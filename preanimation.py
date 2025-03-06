from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation

Window.size = (380, 768)
Window.top = 0
Window.left = 986

UI = '''

<MyWidget@Image>:

    angle : 0
    canvas.before:
        PushMatrix
        Rotate:
            angle:root.angle
            axis : 0, 0, 1
            origin : root.center
    canvas.after:
        PopMatrix

MDScreen:

    MDCard:
        id : eye_background
        md_bg_color : [0, 0, 0, 1]
        radius : [1, 1, 1, 1]

        MDFloatLayout:
        
            Image:
                id : eye
                source : "icon/eye.png"
                pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                size_hint : (0.6, 0.6)
            
            MyWidget:
                id : color_wheel
                source : "icon/color_wheel.png"
                pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                size_hint : (0.29, 0.29)
            
            Image:
                id : eye_lid
                source : "icon/eye_lid.png"
                pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                size_hint : (0.7, 0.7)
             
'''

class MyApp(MDApp):

    def callback_animate_eye_lid(self, *args):
        
        animation = Animation(  pos_hint = {"center_x" : 0.5, "center_y" : 0.75},
                                duration = 1)
        widget = self.root.ids.eye_lid
        animation.start(widget)
    
    def callback_animate_eye_background(self, *args):

        animation = Animation(md_bg_color = [1, 1, 1, 1])
        widget = self.root.ids.eye_background
        animation.start(widget)

    def callback_animate_vanish_eye(self, *args):

        animation = Animation(  opacity = 0,
                                duration = 1)
        widget = self.root.ids.eye
        animation.start(widget)
    
    def callback_vanish_eye_lid(self, *args):

        self.root.ids.eye_lid.opacity = 0
        
    def callback_animate_enlarge_color_wheel(self, *args):
        
        animation = Animation(size_hint = (0.9, 0.9),
                                duration = 1)
        widget = self.root.ids.color_wheel
        animation.start(widget)
    
    def callback_animate_rotate_color_wheel(self, *args):

        anim = Animation(angle = 360, duration = 1)
        widget = self.root.ids.color_wheel
        anim.start(widget)
    
    def callback_check_for_screen_change_to_animation_2(self, *args):
        
        if self.root.ids.color_wheel.angle == 360:
            print("working!!!") 
            Clock.unschedule(self.change_animation_event)

    def on_start(self):
        Clock.schedule_once(self.callback_animate_eye_lid)
        Clock.schedule_once(self.callback_animate_eye_background, 3)
        Clock.schedule_once(self.callback_animate_vanish_eye, 3)
        Clock.schedule_once(self.callback_vanish_eye_lid, 3)
        Clock.schedule_once(self.callback_animate_enlarge_color_wheel, 4)
        Clock.schedule_once(self.callback_animate_rotate_color_wheel, 4)
        self.change_animation_event = Clock.schedule_interval(self.callback_check_for_screen_change_to_animation_2, 1/5)

    def build(self):

        app = Builder.load_string(UI)
        return app

root = MyApp()

if __name__ == "__main__":
    root.run()
