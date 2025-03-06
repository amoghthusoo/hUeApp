# SOURCE CODE

'''
PROJECT : hUeApp © 2022 Amogh Thusoo
VERSION : 0.1
COMPILED THROUGH : WINDOWS 10 > ORACLE VIRTUAL BOX > LINUX OS > UBUNTU 20.04 LTS (VIRTUAL MACHINE)

CAUTION : IF YOU ARE USING THIS APP ON WINDOWS, MACOS OR LINUX, THEN MANUALLY SET THE 'Windows_Mode' TO 'True' FOR PRESERVING THE DIMENSIONS OF THE APP WINDOW.
'''

Windows_Mode = True

# IMPORTING NECESSARY MODULES FORM KIVY, KIVYMD AND COLORSYS LIBRARIES

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.base import EventLoop
from kivy.animation import Animation
from kivy.clock import Clock
import colorsys as cs

# RESIZING KIVY WINDOW TO ANDROID DIMENSIONS

if Windows_Mode == True:
    Window.size = (380, 768)
    Window.top = 0
    Window.left = 986

# DEFINING USER-INTERFACE THROUGH MULTILINE STRING

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

MDScreenManager:

    # DEFINING PRESPLASH SCREEN 1

    MDScreen:

        name : "presplash_1"

        MDCard:
            id : eye_background
            md_bg_color : [0, 0, 0, 1]
            radius : [1, 1, 1, 1]

            MDFloatLayout:
            
                Image:
                    id : eye
                    source : "data/eye.png"
                    pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                    size_hint : (0.6, 0.6)
                
                MyWidget:
                    id : color_wheel
                    source : "data/color_wheel.png"
                    pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                    size_hint : (0.29, 0.29)
                
                Image:
                    id : eye_lid
                    source : "data/eye_lid.png"
                    pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                    size_hint : (0.7, 0.7)

    # DEFINING PRESPLASH SCREEN 2

    MDScreen:

        name : "presplash_2"

        MDFloatLayout:

            MDCard:
                id : h
                size_hint_x : None
                size_hint_y : None
                width : "35dp"
                height : "35dp"
                pos_hint : {"center_x" : 0.25, "center_y" : 0.45}
                #md_bg_color : [128/255, 1/255, 173/255]
                opacity : 0

                MDRelativeLayout:
                    MDLabel:
                        id : h_label
                        text : "h"
                        halign : "center"
                        #color : [1, 1, 1]
                        bold : True
            
            MDCard:
                id : U
                size_hint_x : None
                size_hint_y : None
                width : "35dp"
                height : "35dp"
                pos_hint : {"center_x" : 0.35, "center_y" : 0.45}
                #md_bg_color : [128/255, 1/255, 173/255]
                opacity : 0

                MDRelativeLayout:
                    MDLabel:
                        id : U_label
                        text : "U"
                        halign : "center"
                        #color : [1, 1, 1]
                        bold : True
            
            MDCard:
                id : e
                size_hint_x : None
                size_hint_y : None
                width : "35dp"
                height : "35dp"
                pos_hint : {"center_x" : 0.45, "center_y" : 0.45}
                #md_bg_color : [128/255, 1/255, 173/255]
                opacity : 0

                MDRelativeLayout:
                    MDLabel:
                        id : e_label
                        text : "e"
                        halign : "center"
                        #color : [1, 1, 1]
                        bold : True
            
            MDCard:
                id : A
                size_hint_x : None
                size_hint_y : None
                width : "35dp"
                height : "35dp"
                pos_hint : {"center_x" : 0.55, "center_y" : 0.45}
                #md_bg_color : [128/255, 1/255, 173/255]
                opacity : 0

                MDRelativeLayout:
                    MDLabel:
                        id : A_label
                        text : "A"
                        halign : "center"
                        #color : [1, 1, 1]
                        bold : True
            
            MDCard:
                id : p_1
                size_hint_x : None
                size_hint_y : None
                width : "35dp"
                height : "35dp"
                pos_hint : {"center_x" : 0.65, "center_y" : 0.45}
                #md_bg_color : [128/255, 1/255, 173/255]
                opacity : 0

                MDRelativeLayout:
                    MDLabel:
                        id : p_1_label
                        text : "p"
                        halign : "center"
                        #color : [1, 1, 1]
                        bold : True
            
            MDCard:
                id : p_2
                size_hint_x : None
                size_hint_y : None
                width : "35dp"
                height : "35dp"
                pos_hint : {"center_x" : 0.75, "center_y" : 0.45}
                #md_bg_color : [128/255, 1/255, 173/255]
                opacity : 0

                MDRelativeLayout:
                    MDLabel:
                        id : p_2_label
                        text : "p"
                        halign : "center"
                        #color : [1, 1, 1]
                        bold : True
            MDCard :
                id : Umang 
                size_hint : (0.15, 0.05)
                pos_hint : {"center_x" : 0.85, "center_y" : 0.95}
                md_bg_color : [1, 1, 1, 0]
                opacity : 0
                MDLabel:
                    text : "Umang"
                    halign : "center"
                    bold : True
            
            MDCard :
                id : Amogh 
                size_hint : (0.15, 0.05)
                pos_hint : {"center_x" : 0.85, "center_y" : 0.90}
                md_bg_color : [1, 1, 1, 0]
                opacity : 0
                MDLabel:
                    text : "Amogh"
                    halign : "center"
                    bold : True
        
        MDFloatLayout:
            
            MDProgressBar:
                id : presplash_progress_bar
                value : 0
                pos_hint : {"center_x" : 0.5, "center_y" : 0.1}
                size_hint : (0.9, 1)

    # DEFINING HOME SCREEN

    MDScreen:

        name : "home"
    
        MDBoxLayout:

            orientation : "vertical"
            spacing : "15dp"

            MDTopAppBar:

                id : home_screen_top_app_bar
                title : "hUeApp"
                right_action_items :[ ["refresh", lambda x : app.callback_reset_primary_palette_for_custom_widgets()], \
                                      ["dots-vertical", lambda x : app.callback_options(x)] \
                                    ]
                #left_action_items : [["menu", lambda x : app.temp(x)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0

            MDBoxLayout:

                orientation : "vertical"
                spacing : "20dp"
                padding : "20dp"

                MDLabel:
                    
                    text : "Select Color Scheme :"
                    font_size : "18sp"
                    size_hint_y : None
                    height : self.texture_size[1]

                    bold : True
                    

                MDRaisedButton:

                    id : color_scheme
                    text : "SELECT"
                    font_size : "18sp"
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.5}
                    on_release : app.callback_color_scheme()
                    md_bg_color : app.azure_s1_rgb
                    text_color : app.callback_contrasting_text_color(self.md_bg_color)

                    elevation : 0
                    shadow_softness : 80
                    shadow_softness_size : 2
                
                MDLabel:
                    
                    text : "Select Color :"
                    font_size : "18sp"
                    size_hint_y : None
                    height : self.texture_size[1]

                    bold : True

                MDRaisedButton:

                    id : color_selection
                    text : "SELECT"
                    font_size : "18sp"
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.5}
                    on_release : app.callback_color()
                    md_bg_color : app.azure_s1_rgb
                    text_color : app.callback_contrasting_text_color(self.md_bg_color)

                    elevation : 0
                    shadow_softness : 80
                    shadow_softness_size : 2
                
                MDLabel:
                    
                    text : "Select Tint or Shade (Optional) :"
                    font_size : "18sp"
                    size_hint_y : None
                    height : self.texture_size[1]

                    bold : True
                
                MDRaisedButton:

                    id : tint_shade
                    text : "SELECT"
                    font_size : "18sp"
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.5}
                    on_release : app.callback_tint_shade()
                    md_bg_color : app.azure_s1_rgb
                    text_color : app.callback_contrasting_text_color(self.md_bg_color)

                    elevation : 0
                    shadow_softness : 80
                    shadow_softness_size : 2

                MDFloatLayout:

                    orientation : "vertical"

                    MDRaisedButton:

                        id : get_color_harmonies
                        text : "Get Color Harmonies"
                        font_size : "18sp"
                        pos_hint : {'center_x' : 0.5, 'center_y' : 0.8}
                        on_release : app.callback_get_color_harmonies()
                        md_bg_color : app.azure_s1_rgb
                        text_color : app.callback_contrasting_text_color(self.md_bg_color)

                        elevation : 0
                        shadow_softness : 80
                        shadow_softness_size : 2
                
                    MDFloatLayout:

                        orientation : "vertical"

                        MDFloatingActionButton:

                            id : color_wheel_indicator
                            icon : ""
                            md_bg_color : app.azure_s1_rgb
                            pos_hint : {"center_x" : 1 , "center_y" : 0.12}
                            on_release : app.callback_color_wheel_indicator()

                            elevation : 0
                            shadow_softness : 80
                            shadow_softness_size : 2

                            MDRelativeLayout:

                                MDLabel:

                                    id : color_wheel_indicator_info_text
                                    text : "RGB"
                                    halign : "center"
                                    theme_text_color : "Custom"
                                    text_color : app.callback_contrasting_text_color(root.ids.color_wheel_indicator.md_bg_color)
                            
        # MDFloatLayout:

        #     orientation : "vertical"

        #     MDCard:

        #         size_hint_y : None
        #         height : root.ids.temp.texture_size[1]
        #         md_bg_color : (0, 0, 0)
        #         radius : (0, 0, 0, 0)
        #         MDLabel:

        #             id : temp
        #             text : "Warning :- For Development Purpose Only!"
        #             theme_text_color : "Custom"
        #             text_color : (1, 1, 1)
        #             halign : "center"

    # DEFINING DEVELOPER SCREEN

    MDScreen:

        name : "developer"

        MDBoxLayout:
            orientation : "vertical"
            
            MDTopAppBar:

                id : developer_screen_top_app_bar
                title : "Developer"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0
            
            MDBoxLayout:

                orientation : "vertical"
                spacing : "10dp"
                padding : "20dp"

                MDLabel:

                    text : "Ideator :- Umang Thusoo"
                    size_hint_y : None
                    height : self.texture_size[1]
                
                MDLabel:

                    text : "Developer :- Amogh Thusoo"
                    size_hint_y : None
                    height : self.texture_size[1]
                
                MDLabel:

                    size_hint_y : None
                    height : self.texture_size[1]
                
                MDLabel:

                    text : "© 2022 Amogh Thusoo"
                    size_hint_y : None
                    height : self.texture_size[1]

                MDWidget:
            
            MDWidget:

    # DEFINING ABOUT SCREEN

    MDScreen:

        name : "about"

        MDBoxLayout:
            orientation : "vertical"

            MDTopAppBar:

                id : about_screen_top_app_bar
                title : "About"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0

            MDBoxLayout:

                orientation : "vertical"
                spacing : "10dp"
                padding : "20dp"

                MDLabel:
                    text : "hUeApp is an app for Android which provides diffenent color harmonies along with various color schemes "\
                            + "including Complementary, Monochromatic, Analogous, Triadic and Tetradic." 
                    size_hint_y : None
                    height : self.texture_size[1]
                    halign : "justify"
                
                MDLabel:
                    text : "One can use this app for designing and styling purposes."    
                    size_hint_y : None
                    height : self.texture_size[1]
                    halign : "justify"

                MDWidget:

            MDWidget:

    # DEFINING HELP SCREEN

    MDScreen:

        name : "help"

        MDBoxLayout:

            orientation : "vertical"

            MDTopAppBar:

                id : help_screen_top_app_bar
                title : "Help"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0
            
            MDBoxLayout:

                orientation : "vertical"
                spacing : "10dp"
                padding : "20dp"

                MDLabel:

                    text : "1. Select a color scheme as Complementary, Monochromatic, Analogous, Triadic or Tetradic."
                    size_hint_y : None
                    height : self.texture_size[1]
                    halign : "justify"
                
                MDLabel:

                    text : "2. Select a base color from 12 given colors."
                    size_hint_y : None
                    height : self.texture_size[1]
                    halign : "justify"
                
                MDLabel:

                    text : "3. Select a Tint or Shade of that base color as per requirement. A total of 9 Tints and 9 Shades are available."
                    size_hint_y : None
                    height : self.texture_size[1]
                    halign : "justify"
                
                MDLabel:

                    text : "4. Click on 'Get Color Harmonies' to view the appropriate color combinations."
                    size_hint_y : None
                    height : self.texture_size[1]
                    halign : "justify"

                MDWidget:

            MDWidget:

    # DEFINING SETTINGS SCREEN

    MDScreen:

        name : "settings"

        MDBoxLayout:

            orientation : "vertical"

            MDTopAppBar:

                id : settings_screen_top_app_bar
                title : "Settings"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0
            
            MDScrollView:

                
                MDList:

                    OneLineListItem:

                        text : "Color Wheels"
                        ripple_scale : 0
                        theme_text_color : "Custom"
                        text_color : app.azure_s1_rgb

                    OneLineListItem:

                        text : "RGB"
                        on_release : app.callback_rgb_listitem()
                        MDSwitch:

                            id : rgb_switch
                            active : True
                            pos_hint : {"center_x" : 0.9, "center_y" : 0.5}
                            on_active : app.callback_rgb_switch()
                                 
                    OneLineListItem:

                        text : "RYB"
                        on_release : on_release : app.callback_ryb_listitem()
                        MDSwitch:

                            id : ryb_switch
                            active : False
                            pos_hint : {"center_x" : 0.9, "center_y" : 0.5}
                            on_active : app.callback_ryb_switch()

                            
                        
                    OneLineListItem:

                        text : "Theme"
                        ripple_scale : 0
                        theme_text_color : "Custom"
                        text_color : app.azure_s1_rgb
                    
                    OneLineListItem:

                        text : "Light"
                        on_release : app.callback_light_theme_listitem()
                        MDSwitch:

                            id : light_theme_switch
                            active : True
                            pos_hint : {"center_x" : 0.9, "center_y" : 0.5}
                            on_active : app.callback_light_theme_switch()
                                 
                    OneLineListItem:

                        text : "Dark"
                        on_release : on_release : app.callback_dark_theme_listitem()
                        MDSwitch:

                            id : dark_theme_switch
                            active : False
                            pos_hint : {"center_x" : 0.9, "center_y" : 0.5}
                            on_active : app.callback_dark_theme_switch()
                    
                    OneLineListItem:

                        text : "Reset"
                        ripple_scale : 0
                        theme_text_color : "Custom"
                        text_color : app.azure_s1_rgb
                    
                    OneLineListItem:

                        text : "Reset to Default Settings"
                        on_release : app.callback_dialog_reset_confirmation()

    # DEFINING COLORS SCREEN

    MDScreen:

        name : "colors"

        MDBoxLayout:
            orientation : "vertical"

            MDTopAppBar:

                id : colors_screen_top_app_bar
                title : "Colors"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0
            
            MDScrollView:

                MDList:

                    spacing : "5dp"
                    padding : "5dp"

                    OneLineListItem:

                        id : color_selection_listitem_1
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_1()
                    
                    OneLineListItem:

                        id : color_selection_listitem_2
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_2()
                    
                    OneLineListItem:

                        id : color_selection_listitem_3
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_3()
                    
                    OneLineListItem:

                        id : color_selection_listitem_4
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_4()
                    
                    OneLineListItem:

                        id : color_selection_listitem_5
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_5()
                    
                    OneLineListItem:

                        id : color_selection_listitem_6
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_6()
                    
                    OneLineListItem:

                        id : color_selection_listitem_7
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_7()

                    OneLineListItem:

                        id : color_selection_listitem_8
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_8()
                    
                    OneLineListItem:

                        id : color_selection_listitem_9
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_9()
                    
                    OneLineListItem:

                        id : color_selection_listitem_10
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_10()
                    
                    OneLineListItem:

                        id : color_selection_listitem_11
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_11()
                    
                    OneLineListItem:

                        id : color_selection_listitem_12
                        theme_text_color : "Custom"
                        on_release : app.callback_color_selection_listitem_12()
                    
                    OneLineListItem:

                        id : reset
                        text : "Reset"
                        on_release : app.callback_reset_color_selection()                

    # DEFINING TINT SCREEN

    MDScreen:

        name : "tint"

        MDBoxLayout:
            orientation : "vertical"

            MDTopAppBar:

                id : tint_screen_top_app_bar
                title : "Tint"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0
            
            MDScrollView:

                MDList:

                    spacing : "5dp"
                    padding : "5dp"

                    OneLineListItem:

                        id : t1
                        text : "Tint 1"
                        theme_text_color : "Custom"
                        text_color : "black"
                        on_release : app.callback_t1()
                    
                    OneLineListItem:

                        id : t2
                        text : "Tint 2"
                        theme_text_color : "Custom"
                        text_color : "black"
                        on_release : app.callback_t2()
                    
                    OneLineListItem:

                        id : t3
                        text : "Tint 3"
                        theme_text_color : "Custom"
                        text_color : "black"
                        on_release : app.callback_t3()
                    
                    OneLineListItem:

                        id : t4
                        text : "Tint 4"
                        theme_text_color : "Custom"
                        text_color : "black"
                        on_release : app.callback_t4()
                    
                    OneLineListItem:

                        id : t5
                        text : "Tint 5"
                        theme_text_color : "Custom"
                        text_color : "black"
                        on_release : app.callback_t5()
                    
                    OneLineListItem:

                        id : t6
                        text : "Tint 6"
                        theme_text_color : "Custom"
                        text_color : "black"
                        on_release : app.callback_t6()
                    
                    OneLineListItem:

                        id : t7
                        text : "Tint 7"
                        theme_text_color : "Custom"
                        text_color : "black"
                        on_release : app.callback_t7()

                    OneLineListItem:

                        id : t8
                        text : "Tint 8"
                        theme_text_color : "Custom"
                        text_color : "black"
                        on_release : app.callback_t8()
                    
                    OneLineListItem:

                        id : t9
                        text : "Tint 9"
                        theme_text_color : "Custom"
                        text_color : "black"
                        on_release : app.callback_t9()

    # DEFINING SHADE SCREEN

    MDScreen:

        name : "shade"

        MDBoxLayout:
            orientation : "vertical"

            MDTopAppBar:

                id : shade_screen_top_app_bar
                title : "Shade"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0
            
            MDScrollView:

                MDList:

                    spacing : "5dp"
                    padding : "5dp"

                    OneLineListItem:

                        id : s1
                        text : "Shade 1"
                        theme_text_color : "Custom"
                        text_color : "white"
                        on_release : app.callback_s1()
                    
                    OneLineListItem:

                        id : s2
                        text : "Shade 2"
                        theme_text_color : "Custom"
                        text_color : "white"
                        on_release : app.callback_s2()
                    
                    OneLineListItem:

                        id : s3
                        text : "Shade 3"
                        theme_text_color : "Custom"
                        text_color : "white"
                        on_release : app.callback_s3()
                    
                    OneLineListItem:

                        id : s4
                        text : "Shade 4"
                        theme_text_color : "Custom"
                        text_color : "white"
                        on_release : app.callback_s4()
                    
                    OneLineListItem:

                        id : s5
                        text : "Shade 5"
                        theme_text_color : "Custom"
                        text_color : "white"
                        on_release : app.callback_s5()
                    
                    OneLineListItem:

                        id : s6
                        text : "Shade 6"
                        theme_text_color : "Custom"
                        text_color : "white"
                        on_release : app.callback_s6()
                    
                    OneLineListItem:

                        id : s7
                        text : "Shade 7"
                        theme_text_color : "Custom"
                        text_color : "white"
                        on_release : app.callback_s7()

                    OneLineListItem:

                        id : s8
                        text : "Shade 8"
                        theme_text_color : "Custom"
                        text_color : "white"
                        on_release : app.callback_s8()
                    
                    OneLineListItem:

                        id : s9
                        text : "Shade 9"
                        theme_text_color : "Custom"
                        text_color : "white"
                        on_release : app.callback_s9()

    # DEFINING COMPLEMENTARY SCREEN

    MDScreen:

        name : "complementary"

        MDBoxLayout:
            orientation : "vertical"

            MDTopAppBar:
            
                id : complementary_screen_top_app_bar
                title : "Complementary"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)
                
                elevation : 0

            MDFloatLayout:

                MDCard:

                    id : complementary_master_color_card
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.35} 
                    size_hint : (0.5, 0.5)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.complementary_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                text : root.ids.color_selection.text
                                color : app.callback_contrasting_text_color(root.ids.complementary_master_color_card.md_bg_color)
                                halign : "center"
                                
                        
                        MDCard:

                            md_bg_color : root.ids.complementary_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : complementary_master_color_card_info_tint_shade
                                color : app.callback_contrasting_text_color(root.ids.complementary_master_color_card.md_bg_color)
                                halign : "center"
                                
                        
                        MDCard:

                            md_bg_color : root.ids.complementary_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : complementary_master_color_card_info_hex
                                color : app.callback_contrasting_text_color(root.ids.complementary_master_color_card.md_bg_color)
                                halign : "center"
                                
                                
            MDFloatLayout:
    
                MDCard:

                    id : complementary_color_card
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.65} 
                    size_hint : (0.5, 0.5)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.complementary_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : complementary_color_card_info_text
                                color : app.callback_contrasting_text_color(root.ids.complementary_color_card.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.complementary_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                text : root.ids.complementary_master_color_card_info_tint_shade.text
                                color : app.callback_contrasting_text_color(root.ids.complementary_color_card.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.complementary_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : complementary_color_card_info_hex
                                color : app.callback_contrasting_text_color(root.ids.complementary_color_card.md_bg_color)
                                halign : "center"

    # DEFINING MONOCHROMATIC SCREEN

    MDScreen:

        name : "monochromatic"

        MDBoxLayout:
            orientation : "vertical"

            MDTopAppBar:

                id : monochromatic_screen_top_app_bar
                title : "Monochromatic"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0
            
            MDFloatLayout:

                MDCard:

                    id : monochromatic_master_color_card
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.4} 
                    size_hint : (0.5, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.monochromatic_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                text : root.ids.color_selection.text
                                color : app.callback_contrasting_text_color(root.ids.monochromatic_master_color_card.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.monochromatic_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : monochromatic_master_color_card_info_tint_shade
                                color : app.callback_contrasting_text_color(root.ids.monochromatic_master_color_card.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.monochromatic_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : monochromatic_master_color_card_info_hex
                                color : app.callback_contrasting_text_color(root.ids.monochromatic_master_color_card.md_bg_color)
                                halign : "center"
                
            MDFloatLayout:

                MDCard:

                    id : monochromatic_color_card_1
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.5} 
                    size_hint : (0.5, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.monochromatic_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                text : root.ids.color_selection.text
                                color : app.callback_contrasting_text_color(root.ids.monochromatic_color_card_1.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.monochromatic_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : monochromatic_color_card_1_info_tint_shade
                                color : app.callback_contrasting_text_color(root.ids.monochromatic_color_card_1.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.monochromatic_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : monochromatic_color_card_1_info_hex
                                color : app.callback_contrasting_text_color(root.ids.monochromatic_color_card_1.md_bg_color)
                                halign : "center"
                    

            MDFloatLayout:

                MDCard:

                    id : monochromatic_color_card_2
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.6} 
                    size_hint : (0.5, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.monochromatic_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                text : root.ids.color_selection.text
                                color : app.callback_contrasting_text_color(root.ids.monochromatic_color_card_2.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.monochromatic_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : monochromatic_color_card_2_info_tint_shade
                                color : app.callback_contrasting_text_color(root.ids.monochromatic_color_card_2.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.monochromatic_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : monochromatic_color_card_2_info_hex
                                color : app.callback_contrasting_text_color(root.ids.monochromatic_color_card_2.md_bg_color)
                                halign : "center"
                 
    # DEFINING ANALOGOUS SCREEN        

    MDScreen:

        name : "analogous"

        MDBoxLayout:
            orientation : "vertical"

            MDTopAppBar:

                id : analogous_screen_top_app_bar
                title : "Analogous"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0
            
            MDFloatLayout:

                MDCard:

                    id : analogous_master_color_card
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.4} 
                    size_hint : (0.5, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.analogous_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                text : root.ids.color_selection.text
                                color : app.callback_contrasting_text_color(root.ids.analogous_master_color_card.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.analogous_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : analogous_master_color_card_info_tint_shade
                                color : app.callback_contrasting_text_color(root.ids.analogous_master_color_card.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.analogous_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : analogous_master_color_card_info_hex
                                color : app.callback_contrasting_text_color(root.ids.analogous_master_color_card.md_bg_color)
                                halign : "center"
                    

            MDFloatLayout:

                MDCard:

                    id : analogous_color_card_1
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.5} 
                    size_hint : (0.5, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.analogous_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : analogous_color_card_1_info_text
                                color : app.callback_contrasting_text_color(root.ids.analogous_color_card_1.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.analogous_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                text : root.ids.analogous_master_color_card_info_tint_shade.text
                                color : app.callback_contrasting_text_color(root.ids.analogous_color_card_1.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.analogous_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : analogous_color_card_1_info_hex
                                color : app.callback_contrasting_text_color(root.ids.analogous_color_card_1.md_bg_color)
                                halign : "center"
                    

            MDFloatLayout:

                MDCard:

                    id : analogous_color_card_2
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.6} 
                    size_hint : (0.5, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                
                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.analogous_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : analogous_color_card_2_info_text
                                color : app.callback_contrasting_text_color(root.ids.analogous_color_card_2.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.analogous_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                text : root.ids.analogous_master_color_card_info_tint_shade.text
                                color : app.callback_contrasting_text_color(root.ids.analogous_color_card_2.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.analogous_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : analogous_color_card_2_info_hex
                                color : app.callback_contrasting_text_color(root.ids.analogous_color_card_2.md_bg_color)
                                halign : "center"

    # DEFINING TRIADIC SCREEN

    MDScreen:

        name : "triadic"

        MDBoxLayout:
            orientation : "vertical"

            MDTopAppBar:

                id : triadic_screen_top_app_bar
                title : "Triadic"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0
            
            MDFloatLayout:

                MDCard:

                    id : triadic_master_color_card
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.4} 
                    size_hint : (0.5, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.triadic_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                text : root.ids.color_selection.text
                                color : app.callback_contrasting_text_color(root.ids.triadic_master_color_card.md_bg_color)
                                halign : "center"
                        
                        MDCard:
                        
                            md_bg_color : root.ids.triadic_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : triadic_master_color_card_info_tint_shade
                                color : app.callback_contrasting_text_color(root.ids.triadic_master_color_card.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.triadic_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : triadic_master_color_card_info_hex
                                color : app.callback_contrasting_text_color(root.ids.triadic_master_color_card.md_bg_color)
                                halign : "center"
                    

            MDFloatLayout:

                MDCard:

                    id : triadic_color_card_1
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.5} 
                    size_hint : (0.5, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.triadic_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : triadic_color_card_1_info_text
                                color : app.callback_contrasting_text_color(root.ids.triadic_color_card_1.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.triadic_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                text : root.ids.triadic_master_color_card_info_tint_shade.text
                                color : app.callback_contrasting_text_color(root.ids.triadic_color_card_1.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.triadic_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                id : triadic_color_card_1_info_hex
                                color : app.callback_contrasting_text_color(root.ids.triadic_color_card_1.md_bg_color)
                                halign : "center"


              
            MDFloatLayout:

                MDCard:

                    id : triadic_color_card_2
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.6} 
                    size_hint : (0.5, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.triadic_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : triadic_color_card_2_info_text
                                color : app.callback_contrasting_text_color(root.ids.triadic_color_card_2.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.triadic_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                text : root.ids.triadic_master_color_card_info_tint_shade.text
                                color : app.callback_contrasting_text_color(root.ids.triadic_color_card_2.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.triadic_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : triadic_color_card_2_info_hex
                                color : app.callback_contrasting_text_color(root.ids.triadic_color_card_2.md_bg_color)
                                halign : "center"
                    
    # DEFINING TETRADIC SCREEN

    MDScreen:

        name : "tetradic"

        MDBoxLayout:
            orientation : "vertical"

            MDTopAppBar:

                id : tetradic_screen_top_app_bar
                title : "Tetradic"
                left_action_items : [["arrow-left", lambda x : app.callback_return_home(self.title)]]
                md_bg_color : app.azure_s1_rgb
                specific_text_color : app.callback_contrasting_text_color(self.md_bg_color)

                elevation : 0
            
            MDFloatLayout:

                MDCard:

                    id : tetradic_master_color_card
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.35} 
                    size_hint : (0.4, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.tetradic_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                                text : root.ids.color_selection.text
                                color : app.callback_contrasting_text_color(root.ids.tetradic_master_color_card.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.tetradic_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : tetradic_master_color_card_info_tint_shade
                                color : app.callback_contrasting_text_color(root.ids.tetradic_master_color_card.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.tetradic_master_color_card.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : tetradic_master_color_card_info_hex
                                color : app.callback_contrasting_text_color(root.ids.tetradic_master_color_card.md_bg_color)
                                halign : "center"
    
            MDFloatLayout:

                MDCard:

                    id : tetradic_color_card_1
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.45} 
                    size_hint : (0.4, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.tetradic_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : tetradic_color_card_1_info_text
                                color : app.callback_contrasting_text_color(root.ids.tetradic_color_card_1.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.tetradic_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                text : root.ids.tetradic_master_color_card_info_tint_shade.text
                                color : app.callback_contrasting_text_color(root.ids.tetradic_color_card_1.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.tetradic_color_card_1.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : tetradic_color_card_1_info_hex
                                color : app.callback_contrasting_text_color(root.ids.tetradic_color_card_1.md_bg_color)
                                halign : "center"
                    

            MDFloatLayout:

                MDCard:

                    id : tetradic_color_card_2
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.55} 
                    size_hint : (0.4, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.tetradic_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : tetradic_color_card_2_info_text
                                color : app.callback_contrasting_text_color(root.ids.tetradic_color_card_2.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.tetradic_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                text : root.ids.tetradic_master_color_card_info_tint_shade.text
                                color : app.callback_contrasting_text_color(root.ids.tetradic_color_card_2.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.tetradic_color_card_2.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : tetradic_color_card_2_info_hex
                                color : app.callback_contrasting_text_color(root.ids.tetradic_color_card_2.md_bg_color)
                                halign : "center"
                    
            
            MDFloatLayout:

                MDCard:

                    id : tetradic_color_card_3
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.65} 
                    size_hint : (0.4, 0.8)
                    on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)

                    MDRelativeLayout:

                        MDCard:

                            md_bg_color : root.ids.tetradic_color_card_3.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.65}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                id : tetradic_color_card_3_info_text
                                color : app.callback_contrasting_text_color(root.ids.tetradic_color_card_3.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.tetradic_color_card_3.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:

                                text : root.ids.tetradic_master_color_card_info_tint_shade.text
                                color : app.callback_contrasting_text_color(root.ids.tetradic_color_card_3.md_bg_color)
                                halign : "center"
                        
                        MDCard:

                            md_bg_color : root.ids.tetradic_color_card_3.md_bg_color
                            size_hint : (1, 0.2)
                            pos_hint : {"center_x" : 0.5, "center_y" : 0.35}
                            on_release : app.callback_primary_palette_for_custom_widgets(self.md_bg_color)
                            MDLabel:
                            
                                id : tetradic_color_card_3_info_hex
                                color : app.callback_contrasting_text_color(root.ids.tetradic_color_card_3.md_bg_color)
                                halign : "center"
                   
'''

# DEFINING MAIN APP CLASS

class hUeApp(MDApp):

    # DEFINING CONSTRUCTOR

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # DEFINING OPTIONS MENU

        self.option_items = [
            {
                "viewclass" : "OneLineListItem",
                "text" : "Developer",
                "on_release" : lambda : self.callback_developer()
            },
            {
                "viewclass" : "OneLineListItem",
                "text" : "About",
                "on_release" : lambda : self.callback_about()
            },
            {
                "viewclass" : "OneLineListItem",
                "text" : "Help",
                "on_release" : lambda : self.callback_help()
            },
            {
                "viewclass" : "OneLineListItem",
                "text" : "Settings",
                "on_release" : lambda : self.callback_settings()
            }
            ]

        self.options = MDDropdownMenu(
            items = self.option_items,
            width_mult = 3,
            max_height = "200dp",
            opening_time = 0
        )

        # DEFINING COLOR SCHEMES MENU

        self.color_scheme_items = [
        {
            "viewclass" : "OneLineListItem",
            "text" : "Complementary",
            "on_release" : lambda : self.callback_complementary()
        },
        {
            "viewclass" : "OneLineListItem",
            "text" : "Monochromatic",
            "on_release" : lambda : self.callback_monochromatic()
        },
        {
            "viewclass" : "OneLineListItem",
            "text" : "Analogous",
            "on_release" : lambda : self.callback_analogous()
        },
        {
            "viewclass" : "OneLineListItem",
            "text" : "Triadic",
            "on_release" : lambda : self.callback_triadic()
        },
        {
            "viewclass" : "OneLineListItem",
            "text" : "Tetradic",
            "on_release" : lambda : self.callback_tetradic()
        },
        {
            "viewclass" : "OneLineListItem",
            "text" : "Reset",
            "on_release" : lambda : self.callback_reset_color_scheme()
        }
        ]

        self.color_schemes = MDDropdownMenu(    
        items = self.color_scheme_items,
        width_mult = 3,
        max_height = "300dp",
        opening_time = 0
        )

        # DEFINING TINT/SHADE MENU

        self.tint_shade = MDDropdownMenu(
        items = [
        {
            "viewclass" : "OneLineListItem",
            "text" : "Tint",
            "on_release" : lambda : self.callback_tint()
        },
        {
            "viewclass" : "OneLineListItem",
            "text" : "Shade",
            "on_release" : lambda : self.callback_shade()
        },
        {
            "viewclass" : "OneLineListItem",
            "text" : "Reset",
            "on_release" : lambda : self.callback_reset_tint_shade()
        }
        ],
        width_mult = 3,
        max_height = "150dp",
        opening_time = 0
        )

        self.dialog_reset_confirmation = MDDialog(
        title = "Reset settings?",
        text = "This will reset the app to its default settings?",
        buttons =   [
            MDFlatButton(text = "CANCEL", on_release = lambda x : self.callback_dialog_reset_confirmation_close()),
            MDRaisedButton(text = "ACCEPT", on_release = lambda x : self.callback_dialog_reset_confirmation_accept())
                    ],
        size_hint = (0.9, 0.2)
        )

        # DEFINING RGB COLORS

        self.red_rgb = cs.hsv_to_rgb(0, 1, 1)
        self.red_t1_rgb = cs.hsv_to_rgb(0, 0.9, 1)
        self.red_t2_rgb = cs.hsv_to_rgb(0, 0.8, 1)
        self.red_t3_rgb = cs.hsv_to_rgb(0, 0.7, 1)
        self.red_t4_rgb = cs.hsv_to_rgb(0, 0.6, 1)
        self.red_t5_rgb = cs.hsv_to_rgb(0, 0.5, 1)
        self.red_t6_rgb = cs.hsv_to_rgb(0, 0.4, 1)
        self.red_t7_rgb = cs.hsv_to_rgb(0, 0.3, 1)
        self.red_t8_rgb = cs.hsv_to_rgb(0, 0.2, 1)
        self.red_t9_rgb = cs.hsv_to_rgb(0, 0.1, 1)
        self.red_s1_rgb = cs.hsv_to_rgb(0, 1, 0.9)
        self.red_s2_rgb = cs.hsv_to_rgb(0, 1, 0.8)
        self.red_s3_rgb = cs.hsv_to_rgb(0, 1, 0.7)
        self.red_s4_rgb = cs.hsv_to_rgb(0, 1, 0.6)
        self.red_s5_rgb = cs.hsv_to_rgb(0, 1, 0.5)
        self.red_s6_rgb = cs.hsv_to_rgb(0, 1, 0.4)
        self.red_s7_rgb = cs.hsv_to_rgb(0, 1, 0.3)
        self.red_s8_rgb = cs.hsv_to_rgb(0, 1, 0.2)
        self.red_s9_rgb = cs.hsv_to_rgb(0, 1, 0.1)
        self.orange_rgb = cs.hsv_to_rgb(0.08, 1, 1)
        self.orange_t1_rgb = cs.hsv_to_rgb(0.08, 0.9, 1)
        self.orange_t2_rgb = cs.hsv_to_rgb(0.08, 0.8, 1)
        self.orange_t3_rgb = cs.hsv_to_rgb(0.08, 0.7, 1)
        self.orange_t4_rgb = cs.hsv_to_rgb(0.08, 0.6, 1)
        self.orange_t5_rgb = cs.hsv_to_rgb(0.08, 0.5, 1)
        self.orange_t6_rgb = cs.hsv_to_rgb(0.08, 0.4, 1)
        self.orange_t7_rgb = cs.hsv_to_rgb(0.08, 0.3, 1)
        self.orange_t8_rgb = cs.hsv_to_rgb(0.08, 0.2, 1)
        self.orange_t9_rgb = cs.hsv_to_rgb(0.08, 0.1, 1)
        self.orange_s1_rgb = cs.hsv_to_rgb(0.08, 1, 0.9)
        self.orange_s2_rgb = cs.hsv_to_rgb(0.08, 1, 0.8)
        self.orange_s3_rgb = cs.hsv_to_rgb(0.08, 1, 0.7)
        self.orange_s4_rgb = cs.hsv_to_rgb(0.08, 1, 0.6)
        self.orange_s5_rgb = cs.hsv_to_rgb(0.08, 1, 0.5)
        self.orange_s6_rgb = cs.hsv_to_rgb(0.08, 1, 0.4)
        self.orange_s7_rgb = cs.hsv_to_rgb(0.08, 1, 0.3)
        self.orange_s8_rgb = cs.hsv_to_rgb(0.08, 1, 0.2)
        self.orange_s9_rgb = cs.hsv_to_rgb(0.08, 1, 0.1)
        self.yellow_rgb = cs.hsv_to_rgb(0.16, 1, 1)
        self.yellow_t1_rgb = cs.hsv_to_rgb(0.16, 0.9, 1)
        self.yellow_t2_rgb = cs.hsv_to_rgb(0.16, 0.8, 1)
        self.yellow_t3_rgb = cs.hsv_to_rgb(0.16, 0.7, 1)
        self.yellow_t4_rgb = cs.hsv_to_rgb(0.16, 0.6, 1)
        self.yellow_t5_rgb = cs.hsv_to_rgb(0.16, 0.5, 1)
        self.yellow_t6_rgb = cs.hsv_to_rgb(0.16, 0.4, 1)
        self.yellow_t7_rgb = cs.hsv_to_rgb(0.16, 0.3, 1)
        self.yellow_t8_rgb = cs.hsv_to_rgb(0.16, 0.2, 1)
        self.yellow_t9_rgb = cs.hsv_to_rgb(0.16, 0.1, 1)
        self.yellow_s1_rgb = cs.hsv_to_rgb(0.16, 1, 0.9)
        self.yellow_s2_rgb = cs.hsv_to_rgb(0.16, 1, 0.8)
        self.yellow_s3_rgb = cs.hsv_to_rgb(0.16, 1, 0.7)
        self.yellow_s4_rgb = cs.hsv_to_rgb(0.16, 1, 0.6)
        self.yellow_s5_rgb = cs.hsv_to_rgb(0.16, 1, 0.5)
        self.yellow_s6_rgb = cs.hsv_to_rgb(0.16, 1, 0.4)
        self.yellow_s7_rgb = cs.hsv_to_rgb(0.16, 1, 0.3)
        self.yellow_s8_rgb = cs.hsv_to_rgb(0.16, 1, 0.2)
        self.yellow_s9_rgb = cs.hsv_to_rgb(0.16, 1, 0.1)
        self.chartreuse_green_rgb = cs.hsv_to_rgb(0.24, 1, 1)
        self.chartreuse_green_t1_rgb = cs.hsv_to_rgb(0.24, 0.9, 1)
        self.chartreuse_green_t2_rgb = cs.hsv_to_rgb(0.24, 0.8, 1)
        self.chartreuse_green_t3_rgb = cs.hsv_to_rgb(0.24, 0.7, 1)
        self.chartreuse_green_t4_rgb = cs.hsv_to_rgb(0.24, 0.6, 1)
        self.chartreuse_green_t5_rgb = cs.hsv_to_rgb(0.24, 0.5, 1)
        self.chartreuse_green_t6_rgb = cs.hsv_to_rgb(0.24, 0.4, 1)
        self.chartreuse_green_t7_rgb = cs.hsv_to_rgb(0.24, 0.3, 1)
        self.chartreuse_green_t8_rgb = cs.hsv_to_rgb(0.24, 0.2, 1)
        self.chartreuse_green_t9_rgb = cs.hsv_to_rgb(0.24, 0.1, 1)
        self.chartreuse_green_s1_rgb = cs.hsv_to_rgb(0.24, 1, 0.9)
        self.chartreuse_green_s2_rgb = cs.hsv_to_rgb(0.24, 1, 0.8)
        self.chartreuse_green_s3_rgb = cs.hsv_to_rgb(0.24, 1, 0.7)
        self.chartreuse_green_s4_rgb = cs.hsv_to_rgb(0.24, 1, 0.6)
        self.chartreuse_green_s5_rgb = cs.hsv_to_rgb(0.24, 1, 0.5)
        self.chartreuse_green_s6_rgb = cs.hsv_to_rgb(0.24, 1, 0.4)
        self.chartreuse_green_s7_rgb = cs.hsv_to_rgb(0.24, 1, 0.3)
        self.chartreuse_green_s8_rgb = cs.hsv_to_rgb(0.24, 1, 0.2)
        self.chartreuse_green_s9_rgb = cs.hsv_to_rgb(0.24, 1, 0.1)
        self.green_rgb = cs.hsv_to_rgb(0.33, 1, 1)
        self.green_t1_rgb = cs.hsv_to_rgb(0.33, 0.9, 1)
        self.green_t2_rgb = cs.hsv_to_rgb(0.33, 0.8, 1)
        self.green_t3_rgb = cs.hsv_to_rgb(0.33, 0.7, 1)
        self.green_t4_rgb = cs.hsv_to_rgb(0.33, 0.6, 1)
        self.green_t5_rgb = cs.hsv_to_rgb(0.33, 0.5, 1)
        self.green_t6_rgb = cs.hsv_to_rgb(0.33, 0.4, 1)
        self.green_t7_rgb = cs.hsv_to_rgb(0.33, 0.3, 1)
        self.green_t8_rgb = cs.hsv_to_rgb(0.33, 0.2, 1)
        self.green_t9_rgb = cs.hsv_to_rgb(0.33, 0.1, 1)
        self.green_s1_rgb = cs.hsv_to_rgb(0.33, 1, 0.9)
        self.green_s2_rgb = cs.hsv_to_rgb(0.33, 1, 0.8)
        self.green_s3_rgb = cs.hsv_to_rgb(0.33, 1, 0.7)
        self.green_s4_rgb = cs.hsv_to_rgb(0.33, 1, 0.6)
        self.green_s5_rgb = cs.hsv_to_rgb(0.33, 1, 0.5)
        self.green_s6_rgb = cs.hsv_to_rgb(0.33, 1, 0.4)
        self.green_s7_rgb = cs.hsv_to_rgb(0.33, 1, 0.3)
        self.green_s8_rgb = cs.hsv_to_rgb(0.33, 1, 0.2)
        self.green_s9_rgb = cs.hsv_to_rgb(0.33, 1, 0.1)
        self.spring_green_rgb = cs.hsv_to_rgb(0.41, 1, 1)
        self.spring_green_t1_rgb = cs.hsv_to_rgb(0.41, 0.9, 1)
        self.spring_green_t2_rgb = cs.hsv_to_rgb(0.41, 0.8, 1)
        self.spring_green_t3_rgb = cs.hsv_to_rgb(0.41, 0.7, 1)
        self.spring_green_t4_rgb = cs.hsv_to_rgb(0.41, 0.6, 1)
        self.spring_green_t5_rgb = cs.hsv_to_rgb(0.41, 0.5, 1)
        self.spring_green_t6_rgb = cs.hsv_to_rgb(0.41, 0.4, 1)
        self.spring_green_t7_rgb = cs.hsv_to_rgb(0.41, 0.3, 1)
        self.spring_green_t8_rgb = cs.hsv_to_rgb(0.41, 0.2, 1)
        self.spring_green_t9_rgb = cs.hsv_to_rgb(0.41, 0.1, 1)
        self.spring_green_s1_rgb = cs.hsv_to_rgb(0.41, 1, 0.9)
        self.spring_green_s2_rgb = cs.hsv_to_rgb(0.41, 1, 0.8)
        self.spring_green_s3_rgb = cs.hsv_to_rgb(0.41, 1, 0.7)
        self.spring_green_s4_rgb = cs.hsv_to_rgb(0.41, 1, 0.6)
        self.spring_green_s5_rgb = cs.hsv_to_rgb(0.41, 1, 0.5)
        self.spring_green_s6_rgb = cs.hsv_to_rgb(0.41, 1, 0.4)
        self.spring_green_s7_rgb = cs.hsv_to_rgb(0.41, 1, 0.3)
        self.spring_green_s8_rgb = cs.hsv_to_rgb(0.41, 1, 0.2)
        self.spring_green_s9_rgb = cs.hsv_to_rgb(0.41, 1, 0.1)
        self.cyan_rgb = cs.hsv_to_rgb(0.5, 1, 1)
        self.cyan_t1_rgb = cs.hsv_to_rgb(0.5, 0.9, 1)
        self.cyan_t2_rgb = cs.hsv_to_rgb(0.5, 0.8, 1)
        self.cyan_t3_rgb = cs.hsv_to_rgb(0.5, 0.7, 1)
        self.cyan_t4_rgb = cs.hsv_to_rgb(0.5, 0.6, 1)
        self.cyan_t5_rgb = cs.hsv_to_rgb(0.5, 0.5, 1)
        self.cyan_t6_rgb = cs.hsv_to_rgb(0.5, 0.4, 1)
        self.cyan_t7_rgb = cs.hsv_to_rgb(0.5, 0.3, 1)
        self.cyan_t8_rgb = cs.hsv_to_rgb(0.5, 0.2, 1)
        self.cyan_t9_rgb = cs.hsv_to_rgb(0.5, 0.1, 1)
        self.cyan_s1_rgb = cs.hsv_to_rgb(0.5, 1, 0.9)
        self.cyan_s2_rgb = cs.hsv_to_rgb(0.5, 1, 0.8)
        self.cyan_s3_rgb = cs.hsv_to_rgb(0.5, 1, 0.7)
        self.cyan_s4_rgb = cs.hsv_to_rgb(0.5, 1, 0.6)
        self.cyan_s5_rgb = cs.hsv_to_rgb(0.5, 1, 0.5)
        self.cyan_s6_rgb = cs.hsv_to_rgb(0.5, 1, 0.4)
        self.cyan_s7_rgb = cs.hsv_to_rgb(0.5, 1, 0.3)
        self.cyan_s8_rgb = cs.hsv_to_rgb(0.5, 1, 0.2)
        self.cyan_s9_rgb = cs.hsv_to_rgb(0.5, 1, 0.1)
        self.azure_rgb = cs.hsv_to_rgb(0.58, 1, 1)
        self.azure_t1_rgb = cs.hsv_to_rgb(0.58, 0.9, 1)
        self.azure_t2_rgb = cs.hsv_to_rgb(0.58, 0.8, 1)
        self.azure_t3_rgb = cs.hsv_to_rgb(0.58, 0.7, 1)
        self.azure_t4_rgb = cs.hsv_to_rgb(0.58, 0.6, 1)
        self.azure_t5_rgb = cs.hsv_to_rgb(0.58, 0.5, 1)
        self.azure_t6_rgb = cs.hsv_to_rgb(0.58, 0.4, 1)
        self.azure_t7_rgb = cs.hsv_to_rgb(0.58, 0.3, 1)
        self.azure_t8_rgb = cs.hsv_to_rgb(0.58, 0.2, 1)
        self.azure_t9_rgb = cs.hsv_to_rgb(0.58, 0.1, 1)
        self.azure_s1_rgb = cs.hsv_to_rgb(0.58, 1, 0.9)
        self.azure_s2_rgb = cs.hsv_to_rgb(0.58, 1, 0.8)
        self.azure_s3_rgb = cs.hsv_to_rgb(0.58, 1, 0.7)
        self.azure_s4_rgb = cs.hsv_to_rgb(0.58, 1, 0.6)
        self.azure_s5_rgb = cs.hsv_to_rgb(0.58, 1, 0.5)
        self.azure_s6_rgb = cs.hsv_to_rgb(0.58, 1, 0.4)
        self.azure_s7_rgb = cs.hsv_to_rgb(0.58, 1, 0.3)
        self.azure_s8_rgb = cs.hsv_to_rgb(0.58, 1, 0.2)
        self.azure_s9_rgb = cs.hsv_to_rgb(0.58, 1, 0.1)
        self.blue_rgb = cs.hsv_to_rgb(0.66, 1, 1)
        self.blue_t1_rgb = cs.hsv_to_rgb(0.66, 0.9, 1)
        self.blue_t2_rgb = cs.hsv_to_rgb(0.66, 0.8, 1)
        self.blue_t3_rgb = cs.hsv_to_rgb(0.66, 0.7, 1)
        self.blue_t4_rgb = cs.hsv_to_rgb(0.66, 0.6, 1)
        self.blue_t5_rgb = cs.hsv_to_rgb(0.66, 0.5, 1)
        self.blue_t6_rgb = cs.hsv_to_rgb(0.66, 0.4, 1)
        self.blue_t7_rgb = cs.hsv_to_rgb(0.66, 0.3, 1)
        self.blue_t8_rgb = cs.hsv_to_rgb(0.66, 0.2, 1)
        self.blue_t9_rgb = cs.hsv_to_rgb(0.66, 0.1, 1)
        self.blue_s1_rgb = cs.hsv_to_rgb(0.66, 1, 0.9)
        self.blue_s2_rgb = cs.hsv_to_rgb(0.66, 1, 0.8)
        self.blue_s3_rgb = cs.hsv_to_rgb(0.66, 1, 0.7)
        self.blue_s4_rgb = cs.hsv_to_rgb(0.66, 1, 0.6)
        self.blue_s5_rgb = cs.hsv_to_rgb(0.66, 1, 0.5)
        self.blue_s6_rgb = cs.hsv_to_rgb(0.66, 1, 0.4)
        self.blue_s7_rgb = cs.hsv_to_rgb(0.66, 1, 0.3)
        self.blue_s8_rgb = cs.hsv_to_rgb(0.66, 1, 0.2)
        self.blue_s9_rgb = cs.hsv_to_rgb(0.66, 1, 0.1)
        self.violet_rgb = cs.hsv_to_rgb(0.75, 1, 1)
        self.violet_t1_rgb = cs.hsv_to_rgb(0.75, 0.9, 1)
        self.violet_t2_rgb = cs.hsv_to_rgb(0.75, 0.8, 1)
        self.violet_t3_rgb = cs.hsv_to_rgb(0.75, 0.7, 1)
        self.violet_t4_rgb = cs.hsv_to_rgb(0.75, 0.6, 1)
        self.violet_t5_rgb = cs.hsv_to_rgb(0.75, 0.5, 1)
        self.violet_t6_rgb = cs.hsv_to_rgb(0.75, 0.4, 1)
        self.violet_t7_rgb = cs.hsv_to_rgb(0.75, 0.3, 1)
        self.violet_t8_rgb = cs.hsv_to_rgb(0.75, 0.2, 1)
        self.violet_t9_rgb = cs.hsv_to_rgb(0.75, 0.1, 1)
        self.violet_s1_rgb = cs.hsv_to_rgb(0.75, 1, 0.9)
        self.violet_s2_rgb = cs.hsv_to_rgb(0.75, 1, 0.8)
        self.violet_s3_rgb = cs.hsv_to_rgb(0.75, 1, 0.7)
        self.violet_s4_rgb = cs.hsv_to_rgb(0.75, 1, 0.6)
        self.violet_s5_rgb = cs.hsv_to_rgb(0.75, 1, 0.5)
        self.violet_s6_rgb = cs.hsv_to_rgb(0.75, 1, 0.4)
        self.violet_s7_rgb = cs.hsv_to_rgb(0.75, 1, 0.3)
        self.violet_s8_rgb = cs.hsv_to_rgb(0.75, 1, 0.2)
        self.violet_s9_rgb = cs.hsv_to_rgb(0.75, 1, 0.1)
        self.magenta_rgb = cs.hsv_to_rgb(0.83, 1, 1)
        self.magenta_t1_rgb = cs.hsv_to_rgb(0.83, 0.9, 1)
        self.magenta_t2_rgb = cs.hsv_to_rgb(0.83, 0.8, 1)
        self.magenta_t3_rgb = cs.hsv_to_rgb(0.83, 0.7, 1)
        self.magenta_t4_rgb = cs.hsv_to_rgb(0.83, 0.6, 1)
        self.magenta_t5_rgb = cs.hsv_to_rgb(0.83, 0.5, 1)
        self.magenta_t6_rgb = cs.hsv_to_rgb(0.83, 0.4, 1)
        self.magenta_t7_rgb = cs.hsv_to_rgb(0.83, 0.3, 1)
        self.magenta_t8_rgb = cs.hsv_to_rgb(0.83, 0.2, 1)
        self.magenta_t9_rgb = cs.hsv_to_rgb(0.83, 0.1, 1)
        self.magenta_s1_rgb = cs.hsv_to_rgb(0.83, 1, 0.9)
        self.magenta_s2_rgb = cs.hsv_to_rgb(0.83, 1, 0.8)
        self.magenta_s3_rgb = cs.hsv_to_rgb(0.83, 1, 0.7)
        self.magenta_s4_rgb = cs.hsv_to_rgb(0.83, 1, 0.6)
        self.magenta_s5_rgb = cs.hsv_to_rgb(0.83, 1, 0.5)
        self.magenta_s6_rgb = cs.hsv_to_rgb(0.83, 1, 0.4)
        self.magenta_s7_rgb = cs.hsv_to_rgb(0.83, 1, 0.3)
        self.magenta_s8_rgb = cs.hsv_to_rgb(0.83, 1, 0.2)
        self.magenta_s9_rgb = cs.hsv_to_rgb(0.83, 1, 0.1)
        self.rose_rgb = cs.hsv_to_rgb(0.91, 1, 1)
        self.rose_t1_rgb = cs.hsv_to_rgb(0.91, 0.9, 1)
        self.rose_t2_rgb = cs.hsv_to_rgb(0.91, 0.8, 1)
        self.rose_t3_rgb = cs.hsv_to_rgb(0.91, 0.7, 1)
        self.rose_t4_rgb = cs.hsv_to_rgb(0.91, 0.6, 1)
        self.rose_t5_rgb = cs.hsv_to_rgb(0.91, 0.5, 1)
        self.rose_t6_rgb = cs.hsv_to_rgb(0.91, 0.4, 1)
        self.rose_t7_rgb = cs.hsv_to_rgb(0.91, 0.3, 1)
        self.rose_t8_rgb = cs.hsv_to_rgb(0.91, 0.2, 1)
        self.rose_t9_rgb = cs.hsv_to_rgb(0.91, 0.1, 1)
        self.rose_s1_rgb = cs.hsv_to_rgb(0.91, 1, 0.9)
        self.rose_s2_rgb = cs.hsv_to_rgb(0.91, 1, 0.8)
        self.rose_s3_rgb = cs.hsv_to_rgb(0.91, 1, 0.7)
        self.rose_s4_rgb = cs.hsv_to_rgb(0.91, 1, 0.6)
        self.rose_s5_rgb = cs.hsv_to_rgb(0.91, 1, 0.5)
        self.rose_s6_rgb = cs.hsv_to_rgb(0.91, 1, 0.4)
        self.rose_s7_rgb = cs.hsv_to_rgb(0.91, 1, 0.3)
        self.rose_s8_rgb = cs.hsv_to_rgb(0.91, 1, 0.2)
        self.rose_s9_rgb = cs.hsv_to_rgb(0.91, 1, 0.1)

        # DEFINING RYB COLORS

        self.red_ryb = cs.hsv_to_rgb(0.01, 0.92, 0.99)
        self.red_t1_ryb = cs.hsv_to_rgb(0.01, 0.83, 0.99)
        self.red_t2_ryb = cs.hsv_to_rgb(0.01, 0.74, 0.99)
        self.red_t3_ryb = cs.hsv_to_rgb(0.01, 0.65, 0.99)
        self.red_t4_ryb = cs.hsv_to_rgb(0.01, 0.56, 0.99)
        self.red_t5_ryb = cs.hsv_to_rgb(0.01, 0.47, 0.99)
        self.red_t6_ryb = cs.hsv_to_rgb(0.01, 0.38, 0.99)
        self.red_t7_ryb = cs.hsv_to_rgb(0.01, 0.29, 0.99)
        self.red_t8_ryb = cs.hsv_to_rgb(0.01, 0.20, 0.99)
        self.red_t9_ryb = cs.hsv_to_rgb(0.01, 0.11, 0.99)
        self.red_s1_ryb = cs.hsv_to_rgb(0.01, 0.92, 0.89)
        self.red_s2_ryb = cs.hsv_to_rgb(0.01, 0.92, 0.79)
        self.red_s3_ryb = cs.hsv_to_rgb(0.01, 0.92, 0.69)
        self.red_s4_ryb = cs.hsv_to_rgb(0.01, 0.92, 0.59)
        self.red_s5_ryb = cs.hsv_to_rgb(0.01, 0.92, 0.49)
        self.red_s6_ryb = cs.hsv_to_rgb(0.01, 0.92, 0.39)
        self.red_s7_ryb = cs.hsv_to_rgb(0.01, 0.92, 0.29)
        self.red_s8_ryb = cs.hsv_to_rgb(0.01, 0.92, 0.19)
        self.red_s9_ryb = cs.hsv_to_rgb(0.01, 0.92, 0.09)
        self.red_orange_ryb = cs.hsv_to_rgb(0.05, 0.96, 0.98)
        self.red_orange_t1_ryb = cs.hsv_to_rgb(0.05, 0.87, 0.98)
        self.red_orange_t2_ryb = cs.hsv_to_rgb(0.05, 0.78, 0.98)
        self.red_orange_t3_ryb = cs.hsv_to_rgb(0.05, 0.69, 0.98)
        self.red_orange_t4_ryb = cs.hsv_to_rgb(0.05, 0.60, 0.98)
        self.red_orange_t5_ryb = cs.hsv_to_rgb(0.05, 0.51, 0.98)
        self.red_orange_t6_ryb = cs.hsv_to_rgb(0.05, 0.42, 0.98)
        self.red_orange_t7_ryb = cs.hsv_to_rgb(0.05, 0.33, 0.98)
        self.red_orange_t8_ryb = cs.hsv_to_rgb(0.05, 0.24, 0.98)
        self.red_orange_t9_ryb = cs.hsv_to_rgb(0.05, 0.15, 0.98)
        self.red_orange_s1_ryb = cs.hsv_to_rgb(0.05, 0.96, 0.89)
        self.red_orange_s2_ryb = cs.hsv_to_rgb(0.05, 0.96, 0.80)
        self.red_orange_s3_ryb = cs.hsv_to_rgb(0.05, 0.96, 0.71)
        self.red_orange_s4_ryb = cs.hsv_to_rgb(0.05, 0.96, 0.62)
        self.red_orange_s5_ryb = cs.hsv_to_rgb(0.05, 0.96, 0.53)
        self.red_orange_s6_ryb = cs.hsv_to_rgb(0.05, 0.96, 0.44)
        self.red_orange_s7_ryb = cs.hsv_to_rgb(0.05, 0.96, 0.35)
        self.red_orange_s8_ryb = cs.hsv_to_rgb(0.05, 0.96, 0.26)
        self.red_orange_s9_ryb = cs.hsv_to_rgb(0.05, 0.96, 0.17)
        self.orange_ryb = cs.hsv_to_rgb(0.10, 0.99, 0.98)
        self.orange_t1_ryb = cs.hsv_to_rgb(0.10, 0.89, 0.98)
        self.orange_t2_ryb = cs.hsv_to_rgb(0.10, 0.79, 0.98)
        self.orange_t3_ryb = cs.hsv_to_rgb(0.10, 0.69, 0.98)
        self.orange_t4_ryb = cs.hsv_to_rgb(0.10, 0.59, 0.98)
        self.orange_t5_ryb = cs.hsv_to_rgb(0.10, 0.49, 0.98)
        self.orange_t6_ryb = cs.hsv_to_rgb(0.10, 0.39, 0.98)
        self.orange_t7_ryb = cs.hsv_to_rgb(0.10, 0.29, 0.98)
        self.orange_t8_ryb = cs.hsv_to_rgb(0.10, 0.19, 0.98)
        self.orange_t9_ryb = cs.hsv_to_rgb(0.10, 0.09, 0.98)
        self.orange_s1_ryb = cs.hsv_to_rgb(0.10, 0.99, 0.89)
        self.orange_s2_ryb = cs.hsv_to_rgb(0.10, 0.99, 0.80)
        self.orange_s3_ryb = cs.hsv_to_rgb(0.10, 0.99, 0.71)
        self.orange_s4_ryb = cs.hsv_to_rgb(0.10, 0.99, 0.62)
        self.orange_s5_ryb = cs.hsv_to_rgb(0.10, 0.99, 0.53)
        self.orange_s6_ryb = cs.hsv_to_rgb(0.10, 0.99, 0.44)
        self.orange_s7_ryb = cs.hsv_to_rgb(0.10, 0.99, 0.35)
        self.orange_s8_ryb = cs.hsv_to_rgb(0.10, 0.99, 0.26)
        self.orange_s9_ryb = cs.hsv_to_rgb(0.10, 0.99, 0.17)
        self.yellow_orange_ryb = cs.hsv_to_rgb(0.13, 0.89, 0.98)
        self.yellow_orange_t1_ryb = cs.hsv_to_rgb(0.13, 0.81, 0.98)
        self.yellow_orange_t2_ryb = cs.hsv_to_rgb(0.13, 0.73, 0.98)
        self.yellow_orange_t3_ryb = cs.hsv_to_rgb(0.13, 0.65, 0.98)
        self.yellow_orange_t4_ryb = cs.hsv_to_rgb(0.13, 0.57, 0.98)
        self.yellow_orange_t5_ryb = cs.hsv_to_rgb(0.13, 0.49, 0.98)
        self.yellow_orange_t6_ryb = cs.hsv_to_rgb(0.13, 0.41, 0.98)
        self.yellow_orange_t7_ryb = cs.hsv_to_rgb(0.13, 0.33, 0.98)
        self.yellow_orange_t8_ryb = cs.hsv_to_rgb(0.13, 0.25, 0.98)
        self.yellow_orange_t9_ryb = cs.hsv_to_rgb(0.13, 0.17, 0.98)
        self.yellow_orange_s1_ryb = cs.hsv_to_rgb(0.13, 0.89, 0.89)
        self.yellow_orange_s2_ryb = cs.hsv_to_rgb(0.13, 0.89, 0.80)
        self.yellow_orange_s3_ryb = cs.hsv_to_rgb(0.13, 0.89, 0.71)
        self.yellow_orange_s4_ryb = cs.hsv_to_rgb(0.13, 0.89, 0.62)
        self.yellow_orange_s5_ryb = cs.hsv_to_rgb(0.13, 0.89, 0.53)
        self.yellow_orange_s6_ryb = cs.hsv_to_rgb(0.13, 0.89, 0.44)
        self.yellow_orange_s7_ryb = cs.hsv_to_rgb(0.13, 0.89, 0.35)
        self.yellow_orange_s8_ryb = cs.hsv_to_rgb(0.13, 0.89, 0.26)
        self.yellow_orange_s9_ryb = cs.hsv_to_rgb(0.13, 0.89, 0.17)
        self.yellow_ryb = cs.hsv_to_rgb(0.16, 0.79, 0.99)
        self.yellow_t1_ryb = cs.hsv_to_rgb(0.16, 0.72, 0.99)
        self.yellow_t2_ryb = cs.hsv_to_rgb(0.16, 0.65, 0.99)
        self.yellow_t3_ryb = cs.hsv_to_rgb(0.16, 0.58, 0.99)
        self.yellow_t4_ryb = cs.hsv_to_rgb(0.16, 0.51, 0.99)
        self.yellow_t5_ryb = cs.hsv_to_rgb(0.16, 0.44, 0.99)
        self.yellow_t6_ryb = cs.hsv_to_rgb(0.16, 0.37, 0.99)
        self.yellow_t7_ryb = cs.hsv_to_rgb(0.16, 0.30, 0.99)
        self.yellow_t8_ryb = cs.hsv_to_rgb(0.16, 0.23, 0.99)
        self.yellow_t9_ryb = cs.hsv_to_rgb(0.16, 0.16, 0.99)
        self.yellow_s1_ryb = cs.hsv_to_rgb(0.16, 0.79, 0.89)
        self.yellow_s2_ryb = cs.hsv_to_rgb(0.16, 0.79, 0.79)
        self.yellow_s3_ryb = cs.hsv_to_rgb(0.16, 0.79, 0.69)
        self.yellow_s4_ryb = cs.hsv_to_rgb(0.16, 0.79, 0.59)
        self.yellow_s5_ryb = cs.hsv_to_rgb(0.16, 0.79, 0.49)
        self.yellow_s6_ryb = cs.hsv_to_rgb(0.16, 0.79, 0.39)
        self.yellow_s7_ryb = cs.hsv_to_rgb(0.16, 0.79, 0.29)
        self.yellow_s8_ryb = cs.hsv_to_rgb(0.16, 0.79, 0.19)
        self.yellow_s9_ryb = cs.hsv_to_rgb(0.16, 0.79, 0.09)
        self.yellow_green_ryb = cs.hsv_to_rgb(0.20, 0.76, 0.84)
        self.yellow_green_t1_ryb = cs.hsv_to_rgb(0.20, 0.69, 0.84)
        self.yellow_green_t2_ryb = cs.hsv_to_rgb(0.20, 0.62, 0.84)
        self.yellow_green_t3_ryb = cs.hsv_to_rgb(0.20, 0.55, 0.84)
        self.yellow_green_t4_ryb = cs.hsv_to_rgb(0.20, 0.48, 0.84)
        self.yellow_green_t5_ryb = cs.hsv_to_rgb(0.20, 0.41, 0.84)
        self.yellow_green_t6_ryb = cs.hsv_to_rgb(0.20, 0.34, 0.84)
        self.yellow_green_t7_ryb = cs.hsv_to_rgb(0.20, 0.27, 0.84)
        self.yellow_green_t8_ryb = cs.hsv_to_rgb(0.20, 0.20, 0.84)
        self.yellow_green_t9_ryb = cs.hsv_to_rgb(0.20, 0.13, 0.84)
        self.yellow_green_s1_ryb = cs.hsv_to_rgb(0.20, 0.76, 0.76)
        self.yellow_green_s2_ryb = cs.hsv_to_rgb(0.20, 0.76, 0.68)
        self.yellow_green_s3_ryb = cs.hsv_to_rgb(0.20, 0.76, 0.60)
        self.yellow_green_s4_ryb = cs.hsv_to_rgb(0.20, 0.76, 0.52)
        self.yellow_green_s5_ryb = cs.hsv_to_rgb(0.20, 0.76, 0.44)
        self.yellow_green_s6_ryb = cs.hsv_to_rgb(0.20, 0.76, 0.36)
        self.yellow_green_s7_ryb = cs.hsv_to_rgb(0.20, 0.76, 0.28)
        self.yellow_green_s8_ryb = cs.hsv_to_rgb(0.20, 0.76, 0.20)
        self.yellow_green_s9_ryb = cs.hsv_to_rgb(0.20, 0.76, 0.12)
        self.green_ryb = cs.hsv_to_rgb(0.26, 0.71, 0.69)
        self.green_t1_ryb = cs.hsv_to_rgb(0.26, 0.65, 0.69)
        self.green_t2_ryb = cs.hsv_to_rgb(0.26, 0.59, 0.69)
        self.green_t3_ryb = cs.hsv_to_rgb(0.26, 0.53, 0.69)
        self.green_t4_ryb = cs.hsv_to_rgb(0.26, 0.47, 0.69)
        self.green_t5_ryb = cs.hsv_to_rgb(0.26, 0.41, 0.69)
        self.green_t6_ryb = cs.hsv_to_rgb(0.26, 0.35, 0.69)
        self.green_t7_ryb = cs.hsv_to_rgb(0.26, 0.29, 0.69)
        self.green_t8_ryb = cs.hsv_to_rgb(0.26, 0.23, 0.69)
        self.green_t9_ryb = cs.hsv_to_rgb(0.26, 0.17, 0.69)
        self.green_s1_ryb = cs.hsv_to_rgb(0.26, 0.71, 0.63)
        self.green_s2_ryb = cs.hsv_to_rgb(0.26, 0.71, 0.57)
        self.green_s3_ryb = cs.hsv_to_rgb(0.26, 0.71, 0.51)
        self.green_s4_ryb = cs.hsv_to_rgb(0.26, 0.71, 0.45)
        self.green_s5_ryb = cs.hsv_to_rgb(0.26, 0.71, 0.39)
        self.green_s6_ryb = cs.hsv_to_rgb(0.26, 0.71, 0.33)
        self.green_s7_ryb = cs.hsv_to_rgb(0.26, 0.71, 0.27)
        self.green_s8_ryb = cs.hsv_to_rgb(0.26, 0.71, 0.21)
        self.green_s9_ryb = cs.hsv_to_rgb(0.26, 0.71, 0.15)
        self.blue_green_ryb = cs.hsv_to_rgb(0.54, 0.65, 0.59)
        self.blue_green_t1_ryb = cs.hsv_to_rgb(0.54, 0.59, 0.59)
        self.blue_green_t2_ryb = cs.hsv_to_rgb(0.54, 0.53, 0.59)
        self.blue_green_t3_ryb = cs.hsv_to_rgb(0.54, 0.47, 0.59)
        self.blue_green_t4_ryb = cs.hsv_to_rgb(0.54, 0.41, 0.59)
        self.blue_green_t5_ryb = cs.hsv_to_rgb(0.54, 0.35, 0.59)
        self.blue_green_t6_ryb = cs.hsv_to_rgb(0.54, 0.29, 0.59)
        self.blue_green_t7_ryb = cs.hsv_to_rgb(0.54, 0.23, 0.59)
        self.blue_green_t8_ryb = cs.hsv_to_rgb(0.54, 0.17, 0.59)
        self.blue_green_t9_ryb = cs.hsv_to_rgb(0.54, 0.11, 0.59)
        self.blue_green_s1_ryb = cs.hsv_to_rgb(0.54, 0.65, 0.54)
        self.blue_green_s2_ryb = cs.hsv_to_rgb(0.54, 0.65, 0.49)
        self.blue_green_s3_ryb = cs.hsv_to_rgb(0.54, 0.65, 0.44)
        self.blue_green_s4_ryb = cs.hsv_to_rgb(0.54, 0.65, 0.39)
        self.blue_green_s5_ryb = cs.hsv_to_rgb(0.54, 0.65, 0.34)
        self.blue_green_s6_ryb = cs.hsv_to_rgb(0.54, 0.65, 0.29)
        self.blue_green_s7_ryb = cs.hsv_to_rgb(0.54, 0.65, 0.24)
        self.blue_green_s8_ryb = cs.hsv_to_rgb(0.54, 0.65, 0.19)
        self.blue_green_s9_ryb = cs.hsv_to_rgb(0.54, 0.65, 0.14)
        self.blue_ryb = cs.hsv_to_rgb(0.62, 0.99, 0.99)
        self.blue_t1_ryb = cs.hsv_to_rgb(0.62, 0.89, 0.99)
        self.blue_t2_ryb = cs.hsv_to_rgb(0.62, 0.79, 0.99)
        self.blue_t3_ryb = cs.hsv_to_rgb(0.62, 0.69, 0.99)
        self.blue_t4_ryb = cs.hsv_to_rgb(0.62, 0.59, 0.99)
        self.blue_t5_ryb = cs.hsv_to_rgb(0.62, 0.49, 0.99)
        self.blue_t6_ryb = cs.hsv_to_rgb(0.62, 0.39, 0.99)
        self.blue_t7_ryb = cs.hsv_to_rgb(0.62, 0.29, 0.99)
        self.blue_t8_ryb = cs.hsv_to_rgb(0.62, 0.19, 0.99)
        self.blue_t9_ryb = cs.hsv_to_rgb(0.62, 0.09, 0.99)
        self.blue_s1_ryb = cs.hsv_to_rgb(0.62, 0.99, 0.89)
        self.blue_s2_ryb = cs.hsv_to_rgb(0.62, 0.99, 0.79)
        self.blue_s3_ryb = cs.hsv_to_rgb(0.62, 0.99, 0.69)
        self.blue_s4_ryb = cs.hsv_to_rgb(0.62, 0.99, 0.59)
        self.blue_s5_ryb = cs.hsv_to_rgb(0.62, 0.99, 0.49)
        self.blue_s6_ryb = cs.hsv_to_rgb(0.62, 0.99, 0.39)
        self.blue_s7_ryb = cs.hsv_to_rgb(0.62, 0.99, 0.29)
        self.blue_s8_ryb = cs.hsv_to_rgb(0.62, 0.99, 0.19)
        self.blue_s9_ryb = cs.hsv_to_rgb(0.62, 0.99, 0.09)
        self.blue_purple_ryb = cs.hsv_to_rgb(0.69, 0.83, 0.83)
        self.blue_purple_t1_ryb = cs.hsv_to_rgb(0.69, 0.75, 0.83)
        self.blue_purple_t2_ryb = cs.hsv_to_rgb(0.69, 0.67, 0.83)
        self.blue_purple_t3_ryb = cs.hsv_to_rgb(0.69, 0.59, 0.83)
        self.blue_purple_t4_ryb = cs.hsv_to_rgb(0.69, 0.51, 0.83)
        self.blue_purple_t5_ryb = cs.hsv_to_rgb(0.69, 0.43, 0.83)
        self.blue_purple_t6_ryb = cs.hsv_to_rgb(0.69, 0.35, 0.83)
        self.blue_purple_t7_ryb = cs.hsv_to_rgb(0.69, 0.27, 0.83)
        self.blue_purple_t8_ryb = cs.hsv_to_rgb(0.69, 0.19, 0.83)
        self.blue_purple_t9_ryb = cs.hsv_to_rgb(0.69, 0.11, 0.83)
        self.blue_purple_s1_ryb = cs.hsv_to_rgb(0.69, 0.83, 0.75)
        self.blue_purple_s2_ryb = cs.hsv_to_rgb(0.69, 0.83, 0.67)
        self.blue_purple_s3_ryb = cs.hsv_to_rgb(0.69, 0.83, 0.59)
        self.blue_purple_s4_ryb = cs.hsv_to_rgb(0.69, 0.83, 0.51)
        self.blue_purple_s5_ryb = cs.hsv_to_rgb(0.69, 0.83, 0.43)
        self.blue_purple_s6_ryb = cs.hsv_to_rgb(0.69, 0.83, 0.35)
        self.blue_purple_s7_ryb = cs.hsv_to_rgb(0.69, 0.83, 0.27)
        self.blue_purple_s8_ryb = cs.hsv_to_rgb(0.69, 0.83, 0.19)
        self.blue_purple_s9_ryb = cs.hsv_to_rgb(0.69, 0.83, 0.11)
        self.purple_ryb = cs.hsv_to_rgb(0.79, 0.99, 0.68)
        self.purple_t1_ryb = cs.hsv_to_rgb(0.79, 0.89, 0.68)
        self.purple_t2_ryb = cs.hsv_to_rgb(0.79, 0.79, 0.68)
        self.purple_t3_ryb = cs.hsv_to_rgb(0.79, 0.69, 0.68)
        self.purple_t4_ryb = cs.hsv_to_rgb(0.79, 0.59, 0.68)
        self.purple_t5_ryb = cs.hsv_to_rgb(0.79, 0.49, 0.68)
        self.purple_t6_ryb = cs.hsv_to_rgb(0.79, 0.39, 0.68)
        self.purple_t7_ryb = cs.hsv_to_rgb(0.79, 0.29, 0.68)
        self.purple_t8_ryb = cs.hsv_to_rgb(0.79, 0.19, 0.68)
        self.purple_t9_ryb = cs.hsv_to_rgb(0.79, 0.09, 0.68)
        self.purple_s1_ryb = cs.hsv_to_rgb(0.79, 0.99, 0.62)
        self.purple_s2_ryb = cs.hsv_to_rgb(0.79, 0.99, 0.56)
        self.purple_s3_ryb = cs.hsv_to_rgb(0.79, 0.99, 0.50)
        self.purple_s4_ryb = cs.hsv_to_rgb(0.79, 0.99, 0.44)
        self.purple_s5_ryb = cs.hsv_to_rgb(0.79, 0.99, 0.38)
        self.purple_s6_ryb = cs.hsv_to_rgb(0.79, 0.99, 0.32)
        self.purple_s7_ryb = cs.hsv_to_rgb(0.79, 0.99, 0.26)
        self.purple_s8_ryb = cs.hsv_to_rgb(0.79, 0.99, 0.20)
        self.purple_s9_ryb = cs.hsv_to_rgb(0.79, 0.99, 0.14)
        self.red_purple_ryb = cs.hsv_to_rgb(0.92, 0.89, 0.76)
        self.red_purple_t1_ryb = cs.hsv_to_rgb(0.92, 0.81, 0.76)
        self.red_purple_t2_ryb = cs.hsv_to_rgb(0.92, 0.73, 0.76)
        self.red_purple_t3_ryb = cs.hsv_to_rgb(0.92, 0.65, 0.76)
        self.red_purple_t4_ryb = cs.hsv_to_rgb(0.92, 0.57, 0.76)
        self.red_purple_t5_ryb = cs.hsv_to_rgb(0.92, 0.49, 0.76)
        self.red_purple_t6_ryb = cs.hsv_to_rgb(0.92, 0.41, 0.76)
        self.red_purple_t7_ryb = cs.hsv_to_rgb(0.92, 0.33, 0.76)
        self.red_purple_t8_ryb = cs.hsv_to_rgb(0.92, 0.25, 0.76)
        self.red_purple_t9_ryb = cs.hsv_to_rgb(0.92, 0.17, 0.76)
        self.red_purple_s1_ryb = cs.hsv_to_rgb(0.92, 0.89, 0.69)
        self.red_purple_s2_ryb = cs.hsv_to_rgb(0.92, 0.89, 0.62)
        self.red_purple_s3_ryb = cs.hsv_to_rgb(0.92, 0.89, 0.55)
        self.red_purple_s4_ryb = cs.hsv_to_rgb(0.92, 0.89, 0.48)
        self.red_purple_s5_ryb = cs.hsv_to_rgb(0.92, 0.89, 0.41)
        self.red_purple_s6_ryb = cs.hsv_to_rgb(0.92, 0.89, 0.34)
        self.red_purple_s7_ryb = cs.hsv_to_rgb(0.92, 0.89, 0.27)
        self.red_purple_s8_ryb = cs.hsv_to_rgb(0.92, 0.89, 0.20)
        self.red_purple_s9_ryb = cs.hsv_to_rgb(0.92, 0.89, 0.13)

        # DEFINING REPRESENTATION FOR BASE COLOR NAMES

        self.base_colors_representation = {
            
            (1, 1) : "Red",
            (2, 1) : "Orange",
            (3, 1) : "Yellow",
            (4, 1) : "Chartreuse Green",
            (5, 1) : "Green",
            (6, 1) : "Spring Green",
            (7, 1) : "Cyan",
            (8, 1) : "Azure",
            (9, 1) : "Blue",
            (10, 1) : "Violet",
            (11, 1) : "Magenta",
            (12, 1) : "Rose",
            (1, 2) : "Red",
            (2, 2) : "Red-Orange",
            (3, 2) : "Orange",
            (4, 2) : "Yellow-Orange",
            (5, 2) : "Yellow",
            (6, 2) : "Yellow-Green",
            (7, 2) : "Green",
            (8, 2) : "Blue-Green",
            (9, 2) : "Blue",
            (10, 2) : "Blue-Purple",
            (11, 2) : "Purple",
            (12, 2) : "Red-Purple"
        }

        # DEFINING REPRESENTATION FOR TINT/SHADE NUMBER

        self.tint_shade_representation = {

            (0, 0) : "Base Color",
            (1, 1) : "Tint 1",
            (1, 2) : "Tint 2",
            (1, 3) : "Tint 3",
            (1, 4) : "Tint 4",
            (1, 5) : "Tint 5",
            (1, 6) : "Tint 6",
            (1, 7) : "Tint 7",
            (1, 8) : "Tint 8",
            (1, 9) : "Tint 9",
            (2, 1) : "Shade 1",
            (2, 2) : "Shade 2",
            (2, 3) : "Shade 3",
            (2, 4) : "Shade 4",
            (2, 5) : "Shade 5",
            (2, 6) : "Shade 6",
            (2, 7) : "Shade 7",
            (2, 8) : "Shade 8",
            (2, 9) : "Shade 9",

        }

        # DEFINING REPRESENTATION FOR RGB COLORS

        self.color_ids = {

        (1, 0, 0, 1) : self.red_rgb,
        (1, 1, 1, 1) : self.red_t1_rgb,
        (1, 1, 2, 1) : self.red_t2_rgb,
        (1, 1, 3, 1) : self.red_t3_rgb,
        (1, 1, 4, 1) : self.red_t4_rgb,
        (1, 1, 5, 1) : self.red_t5_rgb,
        (1, 1, 6, 1) : self.red_t6_rgb,
        (1, 1, 7, 1) : self.red_t7_rgb,
        (1, 1, 8, 1) : self.red_t8_rgb,
        (1, 1, 9, 1) : self.red_t9_rgb,
        (1, 2, 1, 1) : self.red_s1_rgb,
        (1, 2, 2, 1) : self.red_s2_rgb,
        (1, 2, 3, 1) : self.red_s3_rgb,
        (1, 2, 4, 1) : self.red_s4_rgb,
        (1, 2, 5, 1) : self.red_s5_rgb,
        (1, 2, 6, 1) : self.red_s6_rgb,
        (1, 2, 7, 1) : self.red_s7_rgb,
        (1, 2, 8, 1) : self.red_s8_rgb,
        (1, 2, 9, 1) : self.red_s9_rgb,
        (2, 0, 0, 1) : self.orange_rgb,
        (2, 1, 1, 1) : self.orange_t1_rgb,
        (2, 1, 2, 1) : self.orange_t2_rgb,
        (2, 1, 3, 1) : self.orange_t3_rgb,
        (2, 1, 4, 1) : self.orange_t4_rgb,
        (2, 1, 5, 1) : self.orange_t5_rgb,
        (2, 1, 6, 1) : self.orange_t6_rgb,
        (2, 1, 7, 1) : self.orange_t7_rgb,
        (2, 1, 8, 1) : self.orange_t8_rgb,
        (2, 1, 9, 1) : self.orange_t9_rgb,
        (2, 2, 1, 1) : self.orange_s1_rgb,
        (2, 2, 2, 1) : self.orange_s2_rgb,
        (2, 2, 3, 1) : self.orange_s3_rgb,
        (2, 2, 4, 1) : self.orange_s4_rgb,
        (2, 2, 5, 1) : self.orange_s5_rgb,
        (2, 2, 6, 1) : self.orange_s6_rgb,
        (2, 2, 7, 1) : self.orange_s7_rgb,
        (2, 2, 8, 1) : self.orange_s8_rgb,
        (2, 2, 9, 1) : self.orange_s9_rgb,
        (3, 0, 0, 1) : self.yellow_rgb,
        (3, 1, 1, 1) : self.yellow_t1_rgb,
        (3, 1, 2, 1) : self.yellow_t2_rgb,
        (3, 1, 3, 1) : self.yellow_t3_rgb,
        (3, 1, 4, 1) : self.yellow_t4_rgb,
        (3, 1, 5, 1) : self.yellow_t5_rgb,
        (3, 1, 6, 1) : self.yellow_t6_rgb,
        (3, 1, 7, 1) : self.yellow_t7_rgb,
        (3, 1, 8, 1) : self.yellow_t8_rgb,
        (3, 1, 9, 1) : self.yellow_t9_rgb,
        (3, 2, 1, 1) : self.yellow_s1_rgb,
        (3, 2, 2, 1) : self.yellow_s2_rgb,
        (3, 2, 3, 1) : self.yellow_s3_rgb,
        (3, 2, 4, 1) : self.yellow_s4_rgb,
        (3, 2, 5, 1) : self.yellow_s5_rgb,
        (3, 2, 6, 1) : self.yellow_s6_rgb,
        (3, 2, 7, 1) : self.yellow_s7_rgb,
        (3, 2, 8, 1) : self.yellow_s8_rgb,
        (3, 2, 9, 1) : self.yellow_s9_rgb,
        (4, 0, 0, 1) : self.chartreuse_green_rgb,
        (4, 1, 1, 1) : self.chartreuse_green_t1_rgb,
        (4, 1, 2, 1) : self.chartreuse_green_t2_rgb,
        (4, 1, 3, 1) : self.chartreuse_green_t3_rgb,
        (4, 1, 4, 1) : self.chartreuse_green_t4_rgb,
        (4, 1, 5, 1) : self.chartreuse_green_t5_rgb,
        (4, 1, 6, 1) : self.chartreuse_green_t6_rgb,
        (4, 1, 7, 1) : self.chartreuse_green_t7_rgb,
        (4, 1, 8, 1) : self.chartreuse_green_t8_rgb,
        (4, 1, 9, 1) : self.chartreuse_green_t9_rgb,
        (4, 2, 1, 1) : self.chartreuse_green_s1_rgb,
        (4, 2, 2, 1) : self.chartreuse_green_s2_rgb,
        (4, 2, 3, 1) : self.chartreuse_green_s3_rgb,
        (4, 2, 4, 1) : self.chartreuse_green_s4_rgb,
        (4, 2, 5, 1) : self.chartreuse_green_s5_rgb,
        (4, 2, 6, 1) : self.chartreuse_green_s6_rgb,
        (4, 2, 7, 1) : self.chartreuse_green_s7_rgb,
        (4, 2, 8, 1) : self.chartreuse_green_s8_rgb,
        (4, 2, 9, 1) : self.chartreuse_green_s9_rgb,
        (5, 0, 0, 1) : self.green_rgb,
        (5, 1, 1, 1) : self.green_t1_rgb,
        (5, 1, 2, 1) : self.green_t2_rgb,
        (5, 1, 3, 1) : self.green_t3_rgb,
        (5, 1, 4, 1) : self.green_t4_rgb,
        (5, 1, 5, 1) : self.green_t5_rgb,
        (5, 1, 6, 1) : self.green_t6_rgb,
        (5, 1, 7, 1) : self.green_t7_rgb,
        (5, 1, 8, 1) : self.green_t8_rgb,
        (5, 1, 9, 1) : self.green_t9_rgb,
        (5, 2, 1, 1) : self.green_s1_rgb,
        (5, 2, 2, 1) : self.green_s2_rgb,
        (5, 2, 3, 1) : self.green_s3_rgb,
        (5, 2, 4, 1) : self.green_s4_rgb,
        (5, 2, 5, 1) : self.green_s5_rgb,
        (5, 2, 6, 1) : self.green_s6_rgb,
        (5, 2, 7, 1) : self.green_s7_rgb,
        (5, 2, 8, 1) : self.green_s8_rgb,
        (5, 2, 9, 1) : self.green_s9_rgb,
        (6, 0, 0, 1) : self.spring_green_rgb,
        (6, 1, 1, 1) : self.spring_green_t1_rgb,
        (6, 1, 2, 1) : self.spring_green_t2_rgb,
        (6, 1, 3, 1) : self.spring_green_t3_rgb,
        (6, 1, 4, 1) : self.spring_green_t4_rgb,
        (6, 1, 5, 1) : self.spring_green_t5_rgb,
        (6, 1, 6, 1) : self.spring_green_t6_rgb,
        (6, 1, 7, 1) : self.spring_green_t7_rgb,
        (6, 1, 8, 1) : self.spring_green_t8_rgb,
        (6, 1, 9, 1) : self.spring_green_t9_rgb,
        (6, 2, 1, 1) : self.spring_green_s1_rgb,
        (6, 2, 2, 1) : self.spring_green_s2_rgb,
        (6, 2, 3, 1) : self.spring_green_s3_rgb,
        (6, 2, 4, 1) : self.spring_green_s4_rgb,
        (6, 2, 5, 1) : self.spring_green_s5_rgb,
        (6, 2, 6, 1) : self.spring_green_s6_rgb,
        (6, 2, 7, 1) : self.spring_green_s7_rgb,
        (6, 2, 8, 1) : self.spring_green_s8_rgb,
        (6, 2, 9, 1) : self.spring_green_s9_rgb,
        (7, 0, 0, 1) : self.cyan_rgb,
        (7, 1, 1, 1) : self.cyan_t1_rgb,
        (7, 1, 2, 1) : self.cyan_t2_rgb,
        (7, 1, 3, 1) : self.cyan_t3_rgb,
        (7, 1, 4, 1) : self.cyan_t4_rgb,
        (7, 1, 5, 1) : self.cyan_t5_rgb,
        (7, 1, 6, 1) : self.cyan_t6_rgb,
        (7, 1, 7, 1) : self.cyan_t7_rgb,
        (7, 1, 8, 1) : self.cyan_t8_rgb,
        (7, 1, 9, 1) : self.cyan_t9_rgb,
        (7, 2, 1, 1) : self.cyan_s1_rgb,
        (7, 2, 2, 1) : self.cyan_s2_rgb,
        (7, 2, 3, 1) : self.cyan_s3_rgb,
        (7, 2, 4, 1) : self.cyan_s4_rgb,
        (7, 2, 5, 1) : self.cyan_s5_rgb,
        (7, 2, 6, 1) : self.cyan_s6_rgb,
        (7, 2, 7, 1) : self.cyan_s7_rgb,
        (7, 2, 8, 1) : self.cyan_s8_rgb,
        (7, 2, 9, 1) : self.cyan_s9_rgb,
        (8, 0, 0, 1) : self.azure_rgb,
        (8, 1, 1, 1) : self.azure_t1_rgb,
        (8, 1, 2, 1) : self.azure_t2_rgb,
        (8, 1, 3, 1) : self.azure_t3_rgb,
        (8, 1, 4, 1) : self.azure_t4_rgb,
        (8, 1, 5, 1) : self.azure_t5_rgb,
        (8, 1, 6, 1) : self.azure_t6_rgb,
        (8, 1, 7, 1) : self.azure_t7_rgb,
        (8, 1, 8, 1) : self.azure_t8_rgb,
        (8, 1, 9, 1) : self.azure_t9_rgb,
        (8, 2, 1, 1) : self.azure_s1_rgb,
        (8, 2, 2, 1) : self.azure_s2_rgb,
        (8, 2, 3, 1) : self.azure_s3_rgb,
        (8, 2, 4, 1) : self.azure_s4_rgb,
        (8, 2, 5, 1) : self.azure_s5_rgb,
        (8, 2, 6, 1) : self.azure_s6_rgb,
        (8, 2, 7, 1) : self.azure_s7_rgb,
        (8, 2, 8, 1) : self.azure_s8_rgb,
        (8, 2, 9, 1) : self.azure_s9_rgb,
        (9, 0, 0, 1) : self.blue_rgb,
        (9, 1, 1, 1) : self.blue_t1_rgb,
        (9, 1, 2, 1) : self.blue_t2_rgb,
        (9, 1, 3, 1) : self.blue_t3_rgb,
        (9, 1, 4, 1) : self.blue_t4_rgb,
        (9, 1, 5, 1) : self.blue_t5_rgb,
        (9, 1, 6, 1) : self.blue_t6_rgb,
        (9, 1, 7, 1) : self.blue_t7_rgb,
        (9, 1, 8, 1) : self.blue_t8_rgb,
        (9, 1, 9, 1) : self.blue_t9_rgb,
        (9, 2, 1, 1) : self.blue_s1_rgb,
        (9, 2, 2, 1) : self.blue_s2_rgb,
        (9, 2, 3, 1) : self.blue_s3_rgb,
        (9, 2, 4, 1) : self.blue_s4_rgb,
        (9, 2, 5, 1) : self.blue_s5_rgb,
        (9, 2, 6, 1) : self.blue_s6_rgb,
        (9, 2, 7, 1) : self.blue_s7_rgb,
        (9, 2, 8, 1) : self.blue_s8_rgb,
        (9, 2, 9, 1) : self.blue_s9_rgb,
        (10, 0, 0, 1) : self.violet_rgb,
        (10, 1, 1, 1) : self.violet_t1_rgb,
        (10, 1, 2, 1) : self.violet_t2_rgb,
        (10, 1, 3, 1) : self.violet_t3_rgb,
        (10, 1, 4, 1) : self.violet_t4_rgb,
        (10, 1, 5, 1) : self.violet_t5_rgb,
        (10, 1, 6, 1) : self.violet_t6_rgb,
        (10, 1, 7, 1) : self.violet_t7_rgb,
        (10, 1, 8, 1) : self.violet_t8_rgb,
        (10, 1, 9, 1) : self.violet_t9_rgb,
        (10, 2, 1, 1) : self.violet_s1_rgb,
        (10, 2, 2, 1) : self.violet_s2_rgb,
        (10, 2, 3, 1) : self.violet_s3_rgb,
        (10, 2, 4, 1) : self.violet_s4_rgb,
        (10, 2, 5, 1) : self.violet_s5_rgb,
        (10, 2, 6, 1) : self.violet_s6_rgb,
        (10, 2, 7, 1) : self.violet_s7_rgb,
        (10, 2, 8, 1) : self.violet_s8_rgb,
        (10, 2, 9, 1) : self.violet_s9_rgb,
        (11, 0, 0, 1) : self.magenta_rgb,
        (11, 1, 1, 1) : self.magenta_t1_rgb,
        (11, 1, 2, 1) : self.magenta_t2_rgb,
        (11, 1, 3, 1) : self.magenta_t3_rgb,
        (11, 1, 4, 1) : self.magenta_t4_rgb,
        (11, 1, 5, 1) : self.magenta_t5_rgb,
        (11, 1, 6, 1) : self.magenta_t6_rgb,
        (11, 1, 7, 1) : self.magenta_t7_rgb,
        (11, 1, 8, 1) : self.magenta_t8_rgb,
        (11, 1, 9, 1) : self.magenta_t9_rgb,
        (11, 2, 1, 1) : self.magenta_s1_rgb,
        (11, 2, 2, 1) : self.magenta_s2_rgb,
        (11, 2, 3, 1) : self.magenta_s3_rgb,
        (11, 2, 4, 1) : self.magenta_s4_rgb,
        (11, 2, 5, 1) : self.magenta_s5_rgb,
        (11, 2, 6, 1) : self.magenta_s6_rgb,
        (11, 2, 7, 1) : self.magenta_s7_rgb,
        (11, 2, 8, 1) : self.magenta_s8_rgb,
        (11, 2, 9, 1) : self.magenta_s9_rgb,
        (12, 0, 0, 1) : self.rose_rgb,
        (12, 1, 1, 1) : self.rose_t1_rgb,
        (12, 1, 2, 1) : self.rose_t2_rgb,
        (12, 1, 3, 1) : self.rose_t3_rgb,
        (12, 1, 4, 1) : self.rose_t4_rgb,
        (12, 1, 5, 1) : self.rose_t5_rgb,
        (12, 1, 6, 1) : self.rose_t6_rgb,
        (12, 1, 7, 1) : self.rose_t7_rgb,
        (12, 1, 8, 1) : self.rose_t8_rgb,
        (12, 1, 9, 1) : self.rose_t9_rgb,
        (12, 2, 1, 1) : self.rose_s1_rgb,
        (12, 2, 2, 1) : self.rose_s2_rgb,
        (12, 2, 3, 1) : self.rose_s3_rgb,
        (12, 2, 4, 1) : self.rose_s4_rgb,
        (12, 2, 5, 1) : self.rose_s5_rgb,
        (12, 2, 6, 1) : self.rose_s6_rgb,
        (12, 2, 7, 1) : self.rose_s7_rgb,
        (12, 2, 8, 1) : self.rose_s8_rgb,
        (12, 2, 9, 1) : self.rose_s9_rgb,

        # DEFINING REPRESENTATION FOR RYB COLORS

        (1, 0, 0, 2) : self.red_ryb,
        (1, 1, 1, 2) : self.red_t1_ryb,
        (1, 1, 2, 2) : self.red_t2_ryb,
        (1, 1, 3, 2) : self.red_t3_ryb,
        (1, 1, 4, 2) : self.red_t4_ryb,
        (1, 1, 5, 2) : self.red_t5_ryb,
        (1, 1, 6, 2) : self.red_t6_ryb,
        (1, 1, 7, 2) : self.red_t7_ryb,
        (1, 1, 8, 2) : self.red_t8_ryb,
        (1, 1, 9, 2) : self.red_t9_ryb,
        (1, 2, 1, 2) : self.red_s1_ryb,
        (1, 2, 2, 2) : self.red_s2_ryb,
        (1, 2, 3, 2) : self.red_s3_ryb,
        (1, 2, 4, 2) : self.red_s4_ryb,
        (1, 2, 5, 2) : self.red_s5_ryb,
        (1, 2, 6, 2) : self.red_s6_ryb,
        (1, 2, 7, 2) : self.red_s7_ryb,
        (1, 2, 8, 2) : self.red_s8_ryb,
        (1, 2, 9, 2) : self.red_s9_ryb,
        (2, 0, 0, 2) : self.red_orange_ryb,
        (2, 1, 1, 2) : self.red_orange_t1_ryb,
        (2, 1, 2, 2) : self.red_orange_t2_ryb,
        (2, 1, 3, 2) : self.red_orange_t3_ryb,
        (2, 1, 4, 2) : self.red_orange_t4_ryb,
        (2, 1, 5, 2) : self.red_orange_t5_ryb,
        (2, 1, 6, 2) : self.red_orange_t6_ryb,
        (2, 1, 7, 2) : self.red_orange_t7_ryb,
        (2, 1, 8, 2) : self.red_orange_t8_ryb,
        (2, 1, 9, 2) : self.red_orange_t9_ryb,
        (2, 2, 1, 2) : self.red_orange_s1_ryb,
        (2, 2, 2, 2) : self.red_orange_s2_ryb,
        (2, 2, 3, 2) : self.red_orange_s3_ryb,
        (2, 2, 4, 2) : self.red_orange_s4_ryb,
        (2, 2, 5, 2) : self.red_orange_s5_ryb,
        (2, 2, 6, 2) : self.red_orange_s6_ryb,
        (2, 2, 7, 2) : self.red_orange_s7_ryb,
        (2, 2, 8, 2) : self.red_orange_s8_ryb,
        (2, 2, 9, 2) : self.red_orange_s9_ryb,
        (3, 0, 0, 2) : self.orange_ryb,
        (3, 1, 1, 2) : self.orange_t1_ryb,
        (3, 1, 2, 2) : self.orange_t2_ryb,
        (3, 1, 3, 2) : self.orange_t3_ryb,
        (3, 1, 4, 2) : self.orange_t4_ryb,
        (3, 1, 5, 2) : self.orange_t5_ryb,
        (3, 1, 6, 2) : self.orange_t6_ryb,
        (3, 1, 7, 2) : self.orange_t7_ryb,
        (3, 1, 8, 2) : self.orange_t8_ryb,
        (3, 1, 9, 2) : self.orange_t9_ryb,
        (3, 2, 1, 2) : self.orange_s1_ryb,
        (3, 2, 2, 2) : self.orange_s2_ryb,
        (3, 2, 3, 2) : self.orange_s3_ryb,
        (3, 2, 4, 2) : self.orange_s4_ryb,
        (3, 2, 5, 2) : self.orange_s5_ryb,
        (3, 2, 6, 2) : self.orange_s6_ryb,
        (3, 2, 7, 2) : self.orange_s7_ryb,
        (3, 2, 8, 2) : self.orange_s8_ryb,
        (3, 2, 9, 2) : self.orange_s9_ryb,
        (4, 0, 0, 2) : self.yellow_orange_ryb,
        (4, 1, 1, 2) : self.yellow_orange_t1_ryb,
        (4, 1, 2, 2) : self.yellow_orange_t2_ryb,
        (4, 1, 3, 2) : self.yellow_orange_t3_ryb,
        (4, 1, 4, 2) : self.yellow_orange_t4_ryb,
        (4, 1, 5, 2) : self.yellow_orange_t5_ryb,
        (4, 1, 6, 2) : self.yellow_orange_t6_ryb,
        (4, 1, 7, 2) : self.yellow_orange_t7_ryb,
        (4, 1, 8, 2) : self.yellow_orange_t8_ryb,
        (4, 1, 9, 2) : self.yellow_orange_t9_ryb,
        (4, 2, 1, 2) : self.yellow_orange_s1_ryb,
        (4, 2, 2, 2) : self.yellow_orange_s2_ryb,
        (4, 2, 3, 2) : self.yellow_orange_s3_ryb,
        (4, 2, 4, 2) : self.yellow_orange_s4_ryb,
        (4, 2, 5, 2) : self.yellow_orange_s5_ryb,
        (4, 2, 6, 2) : self.yellow_orange_s6_ryb,
        (4, 2, 7, 2) : self.yellow_orange_s7_ryb,
        (4, 2, 8, 2) : self.yellow_orange_s8_ryb,
        (4, 2, 9, 2) : self.yellow_orange_s9_ryb,
        (5, 0, 0, 2) : self.yellow_ryb,
        (5, 1, 1, 2) : self.yellow_t1_ryb,
        (5, 1, 2, 2) : self.yellow_t2_ryb,
        (5, 1, 3, 2) : self.yellow_t3_ryb,
        (5, 1, 4, 2) : self.yellow_t4_ryb,
        (5, 1, 5, 2) : self.yellow_t5_ryb,
        (5, 1, 6, 2) : self.yellow_t6_ryb,
        (5, 1, 7, 2) : self.yellow_t7_ryb,
        (5, 1, 8, 2) : self.yellow_t8_ryb,
        (5, 1, 9, 2) : self.yellow_t9_ryb,
        (5, 2, 1, 2) : self.yellow_s1_ryb,
        (5, 2, 2, 2) : self.yellow_s2_ryb,
        (5, 2, 3, 2) : self.yellow_s3_ryb,
        (5, 2, 4, 2) : self.yellow_s4_ryb,
        (5, 2, 5, 2) : self.yellow_s5_ryb,
        (5, 2, 6, 2) : self.yellow_s6_ryb,
        (5, 2, 7, 2) : self.yellow_s7_ryb,
        (5, 2, 8, 2) : self.yellow_s8_ryb,
        (5, 2, 9, 2) : self.yellow_s9_ryb,
        (6, 0, 0, 2) : self.yellow_green_ryb,
        (6, 1, 1, 2) : self.yellow_green_t1_ryb,
        (6, 1, 2, 2) : self.yellow_green_t2_ryb,
        (6, 1, 3, 2) : self.yellow_green_t3_ryb,
        (6, 1, 4, 2) : self.yellow_green_t4_ryb,
        (6, 1, 5, 2) : self.yellow_green_t5_ryb,
        (6, 1, 6, 2) : self.yellow_green_t6_ryb,
        (6, 1, 7, 2) : self.yellow_green_t7_ryb,
        (6, 1, 8, 2) : self.yellow_green_t8_ryb,
        (6, 1, 9, 2) : self.yellow_green_t9_ryb,
        (6, 2, 1, 2) : self.yellow_green_s1_ryb,
        (6, 2, 2, 2) : self.yellow_green_s2_ryb,
        (6, 2, 3, 2) : self.yellow_green_s3_ryb,
        (6, 2, 4, 2) : self.yellow_green_s4_ryb,
        (6, 2, 5, 2) : self.yellow_green_s5_ryb,
        (6, 2, 6, 2) : self.yellow_green_s6_ryb,
        (6, 2, 7, 2) : self.yellow_green_s7_ryb,
        (6, 2, 8, 2) : self.yellow_green_s8_ryb,
        (6, 2, 9, 2) : self.yellow_green_s9_ryb,
        (7, 0, 0, 2) : self.green_ryb,
        (7, 1, 1, 2) : self.green_t1_ryb,
        (7, 1, 2, 2) : self.green_t2_ryb,
        (7, 1, 3, 2) : self.green_t3_ryb,
        (7, 1, 4, 2) : self.green_t4_ryb,
        (7, 1, 5, 2) : self.green_t5_ryb,
        (7, 1, 6, 2) : self.green_t6_ryb,
        (7, 1, 7, 2) : self.green_t7_ryb,
        (7, 1, 8, 2) : self.green_t8_ryb,
        (7, 1, 9, 2) : self.green_t9_ryb,
        (7, 2, 1, 2) : self.green_s1_ryb,
        (7, 2, 2, 2) : self.green_s2_ryb,
        (7, 2, 3, 2) : self.green_s3_ryb,
        (7, 2, 4, 2) : self.green_s4_ryb,
        (7, 2, 5, 2) : self.green_s5_ryb,
        (7, 2, 6, 2) : self.green_s6_ryb,
        (7, 2, 7, 2) : self.green_s7_ryb,
        (7, 2, 8, 2) : self.green_s8_ryb,
        (7, 2, 9, 2) : self.green_s9_ryb,
        (8, 0, 0, 2) : self.blue_green_ryb,
        (8, 1, 1, 2) : self.blue_green_t1_ryb,
        (8, 1, 2, 2) : self.blue_green_t2_ryb,
        (8, 1, 3, 2) : self.blue_green_t3_ryb,
        (8, 1, 4, 2) : self.blue_green_t4_ryb,
        (8, 1, 5, 2) : self.blue_green_t5_ryb,
        (8, 1, 6, 2) : self.blue_green_t6_ryb,
        (8, 1, 7, 2) : self.blue_green_t7_ryb,
        (8, 1, 8, 2) : self.blue_green_t8_ryb,
        (8, 1, 9, 2) : self.blue_green_t9_ryb,
        (8, 2, 1, 2) : self.blue_green_s1_ryb,
        (8, 2, 2, 2) : self.blue_green_s2_ryb,
        (8, 2, 3, 2) : self.blue_green_s3_ryb,
        (8, 2, 4, 2) : self.blue_green_s4_ryb,
        (8, 2, 5, 2) : self.blue_green_s5_ryb,
        (8, 2, 6, 2) : self.blue_green_s6_ryb,
        (8, 2, 7, 2) : self.blue_green_s7_ryb,
        (8, 2, 8, 2) : self.blue_green_s8_ryb,
        (8, 2, 9, 2) : self.blue_green_s9_ryb,
        (9, 0, 0, 2) : self.blue_ryb,
        (9, 1, 1, 2) : self.blue_t1_ryb,
        (9, 1, 2, 2) : self.blue_t2_ryb,
        (9, 1, 3, 2) : self.blue_t3_ryb,
        (9, 1, 4, 2) : self.blue_t4_ryb,
        (9, 1, 5, 2) : self.blue_t5_ryb,
        (9, 1, 6, 2) : self.blue_t6_ryb,
        (9, 1, 7, 2) : self.blue_t7_ryb,
        (9, 1, 8, 2) : self.blue_t8_ryb,
        (9, 1, 9, 2) : self.blue_t9_ryb,
        (9, 2, 1, 2) : self.blue_s1_ryb,
        (9, 2, 2, 2) : self.blue_s2_ryb,
        (9, 2, 3, 2) : self.blue_s3_ryb,
        (9, 2, 4, 2) : self.blue_s4_ryb,
        (9, 2, 5, 2) : self.blue_s5_ryb,
        (9, 2, 6, 2) : self.blue_s6_ryb,
        (9, 2, 7, 2) : self.blue_s7_ryb,
        (9, 2, 8, 2) : self.blue_s8_ryb,
        (9, 2, 9, 2) : self.blue_s9_ryb,
        (10, 0, 0, 2) : self.blue_purple_ryb,
        (10, 1, 1, 2) : self.blue_purple_t1_ryb,
        (10, 1, 2, 2) : self.blue_purple_t2_ryb,
        (10, 1, 3, 2) : self.blue_purple_t3_ryb,
        (10, 1, 4, 2) : self.blue_purple_t4_ryb,
        (10, 1, 5, 2) : self.blue_purple_t5_ryb,
        (10, 1, 6, 2) : self.blue_purple_t6_ryb,
        (10, 1, 7, 2) : self.blue_purple_t7_ryb,
        (10, 1, 8, 2) : self.blue_purple_t8_ryb,
        (10, 1, 9, 2) : self.blue_purple_t9_ryb,
        (10, 2, 1, 2) : self.blue_purple_s1_ryb,
        (10, 2, 2, 2) : self.blue_purple_s2_ryb,
        (10, 2, 3, 2) : self.blue_purple_s3_ryb,
        (10, 2, 4, 2) : self.blue_purple_s4_ryb,
        (10, 2, 5, 2) : self.blue_purple_s5_ryb,
        (10, 2, 6, 2) : self.blue_purple_s6_ryb,
        (10, 2, 7, 2) : self.blue_purple_s7_ryb,
        (10, 2, 8, 2) : self.blue_purple_s8_ryb,
        (10, 2, 9, 2) : self.blue_purple_s9_ryb,
        (11, 0, 0, 2) : self.purple_ryb,
        (11, 1, 1, 2) : self.purple_t1_ryb,
        (11, 1, 2, 2) : self.purple_t2_ryb,
        (11, 1, 3, 2) : self.purple_t3_ryb,
        (11, 1, 4, 2) : self.purple_t4_ryb,
        (11, 1, 5, 2) : self.purple_t5_ryb,
        (11, 1, 6, 2) : self.purple_t6_ryb,
        (11, 1, 7, 2) : self.purple_t7_ryb,
        (11, 1, 8, 2) : self.purple_t8_ryb,
        (11, 1, 9, 2) : self.purple_t9_ryb,
        (11, 2, 1, 2) : self.purple_s1_ryb,
        (11, 2, 2, 2) : self.purple_s2_ryb,
        (11, 2, 3, 2) : self.purple_s3_ryb,
        (11, 2, 4, 2) : self.purple_s4_ryb,
        (11, 2, 5, 2) : self.purple_s5_ryb,
        (11, 2, 6, 2) : self.purple_s6_ryb,
        (11, 2, 7, 2) : self.purple_s7_ryb,
        (11, 2, 8, 2) : self.purple_s8_ryb,
        (11, 2, 9, 2) : self.purple_s9_ryb,
        (12, 0, 0, 2) : self.red_purple_ryb,
        (12, 1, 1, 2) : self.red_purple_t1_ryb,
        (12, 1, 2, 2) : self.red_purple_t2_ryb,
        (12, 1, 3, 2) : self.red_purple_t3_ryb,
        (12, 1, 4, 2) : self.red_purple_t4_ryb,
        (12, 1, 5, 2) : self.red_purple_t5_ryb,
        (12, 1, 6, 2) : self.red_purple_t6_ryb,
        (12, 1, 7, 2) : self.red_purple_t7_ryb,
        (12, 1, 8, 2) : self.red_purple_t8_ryb,
        (12, 1, 9, 2) : self.red_purple_t9_ryb,
        (12, 2, 1, 2) : self.red_purple_s1_ryb,
        (12, 2, 2, 2) : self.red_purple_s2_ryb,
        (12, 2, 3, 2) : self.red_purple_s3_ryb,
        (12, 2, 4, 2) : self.red_purple_s4_ryb,
        (12, 2, 5, 2) : self.red_purple_s5_ryb,
        (12, 2, 6, 2) : self.red_purple_s6_ryb,
        (12, 2, 7, 2) : self.red_purple_s7_ryb,
        (12, 2, 8, 2) : self.red_purple_s8_ryb,
        (12, 2, 9, 2) : self.red_purple_s9_ryb,

        }
        
        # ANIMATION WHILE SWITCHING THEMES >> NOT IN CURRENT KIVYMD VERSION I.E. 1.0.2

        #self.theme_cls.theme_style_switch_animation = True
        
        # STORING NECESSARY CONFIGURATION TAKEN FROM USER
        # FORMAT >> [COLOR_SCHEME, [BASE_COLOR_NUMBER, TINT/SHADE_NUMBER, TINT/SHADE_INTENSITY_NUMBER], COLOR_WHEEL_NUMBER]

        self.master_selection = [None, [None, None, None], 1]

        # DEFINING ANIMATION DURATION FOR DIFFERENT ANIMATIONS OF PRESPLASH SCREEN
        
        self.appear_animation_duration = 0.4
        self.change_color_animation_duration = 0.3
        self.vanish_animation_duration = 0.3
        self.move_animation_duration = 0.3
        self.appear_name_animation_duration = 1

    # DEFININING FUNCTION FOR SELECTING APPROPRIATE TEXT COLOR

    def callback_contrasting_text_color(self, rgb):

        if (rgb[0] * 255 * 0.299 + rgb[1] * 255 * 0.587 + rgb[2] * 255 * 0.114) > 150:
            return (0, 0, 0)
        else:
            return (1, 1, 1)
    
    # DEFINING FUNCTION FOR CONVERSION OF RGB TO HEX CODE
    
    def callback_rgb_to_hex(self, color):

        raw_hex_val =  "{:02x}{:02x}{:02x}".format(round(color[0] * 255), round(color[1] * 255), round(color[2] * 255))
    
        if raw_hex_val.isdigit():
            return "#" + raw_hex_val

        else:
            hex_val = ""

            for char in raw_hex_val:

                if char.isalpha():
                    hex_val += char.capitalize()
                else:
                    hex_val += char
            return "#" + hex_val
        
    # DEFINING CALLBACK FUNCTION FOR OPTIONS BUTTON

    def callback_options(self, button):

        self.options.caller = button
        self.options.open()

    # DEFINING CALLBACK FUNCTIONS FOR DIFFERENT OPTIONS

    def callback_developer(self):
        self.options.dismiss()
        self.root.transition.direction = "left"
        self.root.current = 'developer'

    def callback_about(self):
        self.options.dismiss()
        self.root.transition.direction = "left"
        self.root.current = 'about'

    def callback_help(self):
        self.options.dismiss()
        self.root.transition.direction = "left"
        self.root.current = "help"

    def callback_settings(self):
        self.options.dismiss()
        self.root.transition.direction = "left"
        self.root.current = "settings"

    # DEFINING CALLBACK FUNCTION FOR RETURNING TO HOME SCREEN
        
    def callback_return_home(self, screen_name):
        if screen_name in ["Colors", "Tint", "Shade"]:
            self.root.transition.direction = "down"
        else:
            self.root.transition.direction = "right" 
        self.root.current = "home"

    # DEFINING FUNCTION FOR COLOR SCHEME BUTTON

    def callback_color_scheme(self):
        self.color_schemes.caller = self.root.ids.color_scheme
        self.color_schemes.open()

    # DEFINING FUNCTIONS FOR DIFFERNET COLOR SCHEMES SELECTION

    def callback_complementary(self):
        self.color_schemes.dismiss()
        self.root.ids.color_scheme.text = "Complementary"
        self.master_selection[0] = 1

    def callback_monochromatic(self):
        self.color_schemes.dismiss()
        self.root.ids.color_scheme.text = "Monochromatic"
        self.master_selection[0] = 2

    def callback_analogous(self):
        self.color_schemes.dismiss()
        self.root.ids.color_scheme.text = "Analogous"
        self.master_selection[0] = 3
        
    def callback_triadic(self):
        self.color_schemes.dismiss()
        self.root.ids.color_scheme.text = "Triadic"
        self.master_selection[0] = 4

    def callback_tetradic(self):
        self.color_schemes.dismiss()
        self.root.ids.color_scheme.text = "Tetradic"
        self.master_selection[0] = 5

    # DEFINING FUNCTION TO RESET THE COLOR SCHEME SELECTION

    def callback_reset_color_scheme(self):
        self.color_schemes.dismiss()
        self.root.ids.color_scheme.text = "SELECT"
        self.root.ids.color_scheme.md_bg_color = self.azure_s1_rgb
        self.root.ids.color_scheme.text_color = self.callback_contrasting_text_color(self.root.ids.color_scheme.md_bg_color)
        self.master_selection[0] = None

    # INITIALISING ALL THE BASE COLORS FOR COLORS SCREEN

    def callback_initialize_colors(self):
        
        self.callback_initialize_listitem_1()
        self.callback_initialize_listitem_2()
        self.callback_initialize_listitem_3()
        self.callback_initialize_listitem_4()
        self.callback_initialize_listitem_5()
        self.callback_initialize_listitem_6()
        self.callback_initialize_listitem_7()
        self.callback_initialize_listitem_8()
        self.callback_initialize_listitem_9()
        self.callback_initialize_listitem_10()
        self.callback_initialize_listitem_11()
        self.callback_initialize_listitem_12()

    def callback_initialize_listitem_1(self):
        
        self.root.ids.color_selection_listitem_1.text = "1. " + self.base_colors_representation[(1, self.master_selection[2])]
        self.root.ids.color_selection_listitem_1.bg_color = self.color_ids[(1, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_1.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_1.bg_color)
    
    def callback_initialize_listitem_2(self):
        
        self.root.ids.color_selection_listitem_2.text = "2. " + self.base_colors_representation[(2, self.master_selection[2])]
        self.root.ids.color_selection_listitem_2.bg_color = self.color_ids[(2, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_2.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_2.bg_color)
    
    def callback_initialize_listitem_3(self):
        
        self.root.ids.color_selection_listitem_3.text = "3. " + self.base_colors_representation[(3, self.master_selection[2])]
        self.root.ids.color_selection_listitem_3.bg_color = self.color_ids[(3, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_3.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_3.bg_color)
    
    def callback_initialize_listitem_4(self):
        
        self.root.ids.color_selection_listitem_4.text = "4. " + self.base_colors_representation[(4, self.master_selection[2])]
        self.root.ids.color_selection_listitem_4.bg_color = self.color_ids[(4, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_4.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_4.bg_color)
    
    def callback_initialize_listitem_5(self):
        
        self.root.ids.color_selection_listitem_5.text = "5. " + self.base_colors_representation[(5, self.master_selection[2])]
        self.root.ids.color_selection_listitem_5.bg_color = self.color_ids[(5, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_5.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_5.bg_color)
    
    def callback_initialize_listitem_6(self):
        
        self.root.ids.color_selection_listitem_6.text = "6. " + self.base_colors_representation[(6, self.master_selection[2])]
        self.root.ids.color_selection_listitem_6.bg_color = self.color_ids[(6, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_6.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_6.bg_color)
    
    def callback_initialize_listitem_7(self):
        
        self.root.ids.color_selection_listitem_7.text = "7. " + self.base_colors_representation[(7, self.master_selection[2])]
        self.root.ids.color_selection_listitem_7.bg_color = self.color_ids[(7, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_7.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_7.bg_color)
    
    def callback_initialize_listitem_8(self):
        
        self.root.ids.color_selection_listitem_8.text = "8. " + self.base_colors_representation[(8, self.master_selection[2])]
        self.root.ids.color_selection_listitem_8.bg_color = self.color_ids[(8, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_8.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_8.bg_color)

    def callback_initialize_listitem_9(self):
        
        self.root.ids.color_selection_listitem_9.text = "9. " + self.base_colors_representation[(9, self.master_selection[2])]
        self.root.ids.color_selection_listitem_9.bg_color = self.color_ids[(9, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_9.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_9.bg_color)

    def callback_initialize_listitem_10(self):
        
        self.root.ids.color_selection_listitem_10.text = "10. " + self.base_colors_representation[(10, self.master_selection[2])]
        self.root.ids.color_selection_listitem_10.bg_color = self.color_ids[(10, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_10.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_10.bg_color)
    
    def callback_initialize_listitem_11(self):
        
        self.root.ids.color_selection_listitem_11.text = "11. " + self.base_colors_representation[(11, self.master_selection[2])]
        self.root.ids.color_selection_listitem_11.bg_color = self.color_ids[(11, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_11.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_11.bg_color)
    
    def callback_initialize_listitem_12(self):
        
        self.root.ids.color_selection_listitem_12.text = "12. " + self.base_colors_representation[(12, self.master_selection[2])]
        self.root.ids.color_selection_listitem_12.bg_color = self.color_ids[(12, 0, 0, self.master_selection[2])]
        self.root.ids.color_selection_listitem_12.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection_listitem_12.bg_color)
   
    # DEFINING CALLBACK FUNCTION FOR COLOR SELECTION BUTTON

    def callback_color(self):

            self.root.transition.direction = "up"
            self.root.current = "colors"
            self.callback_initialize_colors()
    
    # DEFINING CALLBACK FUNTIONS FOR DIFFERENT BASE COLOR BUTTONS IN COLORS SCREEN

    def callback_color_selection_listitem_1(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_1.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(1, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_1.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 1
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0

    def callback_color_selection_listitem_2(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_2.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(2, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_2.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 2
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0

    def callback_color_selection_listitem_3(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_3.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(3, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_3.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 3
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0

    def callback_color_selection_listitem_4(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_4.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(4, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_4.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 4
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0
    
    def callback_color_selection_listitem_5(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_5.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(5, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_5.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 5
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0
    
    def callback_color_selection_listitem_6(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_6.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(6, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_6.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 6
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0
    
    def callback_color_selection_listitem_7(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_7.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(7, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_7.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 7
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0
    
    def callback_color_selection_listitem_8(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_8.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(8, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_8.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 8
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0
    
    def callback_color_selection_listitem_9(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_9.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(9, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_9.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 9
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0
    
    def callback_color_selection_listitem_10(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_10.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(10, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_10.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 10
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0
    
    def callback_color_selection_listitem_11(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_11.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(11, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_11.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 11
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0
    
    def callback_color_selection_listitem_12(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.md_bg_color = self.root.ids.color_selection_listitem_12.bg_color
        self.root.ids.color_selection.text = self.base_colors_representation[(12, self.master_selection[2])]
        self.root.ids.color_selection.text_color = self.root.ids.color_selection_listitem_12.text_color
        self.callback_reset_tint_shade()
        self.master_selection[1][0] = 12
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0
    
    # DEFINING FUNCTION TO RESET COLOR SELECTION

    def callback_reset_color_selection(self):
        self.callback_return_home("Colors")
        self.root.ids.color_selection.text = "SELECT"
        self.root.ids.color_selection.md_bg_color = self.azure_s1_rgb
        self.root.ids.color_selection.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection.md_bg_color)
        self.callback_reset_tint_shade()
        self.master_selection[1] = [None, None, None]
    
    # INITIALISING ALL THE TINTS/SHADES FOR TINT/SHADE SCREEN 

    def tint_shade_initilize(self):

        self.root.ids.t1.bg_color = self.color_ids[(self.master_selection[1][0], 1, 1, self.master_selection[2])]
        self.root.ids.t2.bg_color = self.color_ids[(self.master_selection[1][0], 1, 2, self.master_selection[2])]
        self.root.ids.t3.bg_color = self.color_ids[(self.master_selection[1][0], 1, 3, self.master_selection[2])]
        self.root.ids.t4.bg_color = self.color_ids[(self.master_selection[1][0], 1, 4, self.master_selection[2])]
        self.root.ids.t5.bg_color = self.color_ids[(self.master_selection[1][0], 1, 5, self.master_selection[2])]
        self.root.ids.t6.bg_color = self.color_ids[(self.master_selection[1][0], 1, 6, self.master_selection[2])]
        self.root.ids.t7.bg_color = self.color_ids[(self.master_selection[1][0], 1, 7, self.master_selection[2])]
        self.root.ids.t8.bg_color = self.color_ids[(self.master_selection[1][0], 1, 8, self.master_selection[2])]
        self.root.ids.t9.bg_color = self.color_ids[(self.master_selection[1][0], 1, 9, self.master_selection[2])]
        
        self.root.ids.s1.bg_color = self.color_ids[(self.master_selection[1][0], 2, 1, self.master_selection[2])]
        self.root.ids.s2.bg_color = self.color_ids[(self.master_selection[1][0], 2, 2, self.master_selection[2])]
        self.root.ids.s3.bg_color = self.color_ids[(self.master_selection[1][0], 2, 3, self.master_selection[2])]
        self.root.ids.s4.bg_color = self.color_ids[(self.master_selection[1][0], 2, 4, self.master_selection[2])]
        self.root.ids.s5.bg_color = self.color_ids[(self.master_selection[1][0], 2, 5, self.master_selection[2])]
        self.root.ids.s6.bg_color = self.color_ids[(self.master_selection[1][0], 2, 6, self.master_selection[2])]
        self.root.ids.s7.bg_color = self.color_ids[(self.master_selection[1][0], 2, 7, self.master_selection[2])]
        self.root.ids.s8.bg_color = self.color_ids[(self.master_selection[1][0], 2, 8, self.master_selection[2])]
        self.root.ids.s9.bg_color = self.color_ids[(self.master_selection[1][0], 2, 9, self.master_selection[2])]

        self.root.ids.t1.text_color = self.callback_contrasting_text_color(self.root.ids.t1.bg_color)
        self.root.ids.t2.text_color = self.callback_contrasting_text_color(self.root.ids.t2.bg_color)
        self.root.ids.t3.text_color = self.callback_contrasting_text_color(self.root.ids.t3.bg_color)
        self.root.ids.t4.text_color = self.callback_contrasting_text_color(self.root.ids.t4.bg_color)
        self.root.ids.t5.text_color = self.callback_contrasting_text_color(self.root.ids.t5.bg_color)
        self.root.ids.t6.text_color = self.callback_contrasting_text_color(self.root.ids.t6.bg_color)
        self.root.ids.t7.text_color = self.callback_contrasting_text_color(self.root.ids.t7.bg_color)
        self.root.ids.t8.text_color = self.callback_contrasting_text_color(self.root.ids.t8.bg_color)
        self.root.ids.t9.text_color = self.callback_contrasting_text_color(self.root.ids.t9.bg_color)

        self.root.ids.s1.text_color = self.callback_contrasting_text_color(self.root.ids.s1.bg_color)
        self.root.ids.s2.text_color = self.callback_contrasting_text_color(self.root.ids.s2.bg_color)
        self.root.ids.s3.text_color = self.callback_contrasting_text_color(self.root.ids.s3.bg_color)
        self.root.ids.s4.text_color = self.callback_contrasting_text_color(self.root.ids.s4.bg_color)
        self.root.ids.s5.text_color = self.callback_contrasting_text_color(self.root.ids.s5.bg_color)
        self.root.ids.s6.text_color = self.callback_contrasting_text_color(self.root.ids.s6.bg_color)
        self.root.ids.s7.text_color = self.callback_contrasting_text_color(self.root.ids.s7.bg_color)
        self.root.ids.s8.text_color = self.callback_contrasting_text_color(self.root.ids.s8.bg_color)
        self.root.ids.s9.text_color = self.callback_contrasting_text_color(self.root.ids.s9.bg_color)

    # DEFINING CALLBACK FUNCTION FOR TINT/SHADE BUTTON
    
    def callback_tint_shade(self):
        if self.root.ids.color_selection.text == "SELECT":
            Snackbar(
                text = 'Please select a color first !',
                snackbar_x = "9dp",
                snackbar_y = "9dp",
                size_hint_x = 0.95,
                duration = 1.5
                ).open()
        else:
            self.tint_shade.caller = self.root.ids.tint_shade
            self.tint_shade.open()
            self.tint_shade_initilize()
    
    # DEFINING CALLBACK FUNCTION FOR TINT BUTTON

    def callback_tint(self):
        self.tint_shade.dismiss()
        self.root.transition.direction = "up"
        self.root.current = "tint"
        
    # DEFINING CALLBACK FUNCTION FOR SHADE BUTTON        

    def callback_shade(self):
        self.tint_shade.dismiss()
        self.root.transition.direction = "up"
        self.root.current = "shade"
        
    # DEFINING FUNCTION TO RESET TINT/SHADE SELECTION

    def callback_reset_tint_shade(self):
        self.tint_shade.dismiss()
        self.root.ids.tint_shade.text = "SELECT"
        self.root.ids.tint_shade.md_bg_color = self.azure_s1_rgb
        self.root.ids.tint_shade.text_color = self.callback_contrasting_text_color(self.root.ids.tint_shade.md_bg_color)
        self.master_selection[1][1] = 0
        self.master_selection[1][2] = 0
    
    # DEFINING CALLBACK FUNCTIONS FOR ALL THE TINT BUTTONS IN TINT SCREEN

    def callback_t1(self):
        self.callback_return_home("Tint")
        self.master_selection[1][1] = 1
        self.master_selection[1][2] = 1
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.t1.text 
        self.root.ids.tint_shade.text_color = self.root.ids.t1.text_color

    def callback_t2(self):
        self.callback_return_home("Tint")
        self.master_selection[1][1] = 1
        self.master_selection[1][2] = 2
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.t2.text
        self.root.ids.tint_shade.text_color = self.root.ids.t2.text_color
    
    def callback_t3(self):
        self.callback_return_home("Tint")
        self.master_selection[1][1] = 1
        self.master_selection[1][2] = 3
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.t3.text
        self.root.ids.tint_shade.text_color = self.root.ids.t3.text_color
    
    def callback_t4(self):
        self.callback_return_home("Tint")
        self.master_selection[1][1] = 1
        self.master_selection[1][2] = 4
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.t4.text
        self.root.ids.tint_shade.text_color = self.root.ids.t4.text_color
    
    def callback_t5(self):
        self.callback_return_home("Tint")
        self.master_selection[1][1] = 1
        self.master_selection[1][2] = 5
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.t5.text
        self.root.ids.tint_shade.text_color = self.root.ids.t5.text_color
    
    def callback_t6(self):
        self.callback_return_home("Tint")
        self.master_selection[1][1] = 1
        self.master_selection[1][2] = 6
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.t6.text
        self.root.ids.tint_shade.text_color = self.root.ids.t6.text_color
    
    def callback_t7(self):
        self.callback_return_home("Tint")
        self.master_selection[1][1] = 1
        self.master_selection[1][2] = 7
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.t7.text
        self.root.ids.tint_shade.text_color = self.root.ids.t7.text_color
    
    def callback_t8(self):
        self.callback_return_home("Tint")
        self.master_selection[1][1] = 1
        self.master_selection[1][2] = 8
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.t8.text
        self.root.ids.tint_shade.text_color = self.root.ids.t8.text_color
    
    def callback_t9(self):
        self.callback_return_home("Tint")
        self.master_selection[1][1] = 1
        self.master_selection[1][2] = 9
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.t9.text
        self.root.ids.tint_shade.text_color = self.root.ids.t9.text_color

    # DEFINING CALLBACK FUNCTIONS FOR ALL THE SHADE BUTTONS IN SHADE SCREEN

    def callback_s1(self):
        self.callback_return_home("Shade")
        self.master_selection[1][1] = 2
        self.master_selection[1][2] = 1
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.s1.text
        self.root.ids.tint_shade.text_color = self.root.ids.s1.text_color
    
    def callback_s2(self):
        self.callback_return_home("Shade")
        self.master_selection[1][1] = 2
        self.master_selection[1][2] = 2
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.s2.text
        self.root.ids.tint_shade.text_color = self.root.ids.s2.text_color
    
    def callback_s3(self):
        self.callback_return_home("Shade")
        self.master_selection[1][1] = 2
        self.master_selection[1][2] = 3
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.s3.text
        self.root.ids.tint_shade.text_color = self.root.ids.s3.text_color
    
    def callback_s4(self):
        self.callback_return_home("Shade")
        self.master_selection[1][1] = 2
        self.master_selection[1][2] = 4
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.s4.text
        self.root.ids.tint_shade.text_color = self.root.ids.s4.text_color
    
    def callback_s5(self):
        self.callback_return_home("Shade")
        self.master_selection[1][1] = 2
        self.master_selection[1][2] = 5
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.s5.text
        self.root.ids.tint_shade.text_color = self.root.ids.s5.text_color
    
    def callback_s6(self):
        self.callback_return_home("Shade")
        self.master_selection[1][1] = 2
        self.master_selection[1][2] = 6
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.s6.text
        self.root.ids.tint_shade.text_color = self.root.ids.s6.text_color
    
    def callback_s7(self):
        self.callback_return_home("Shade")
        self.master_selection[1][1] = 2
        self.master_selection[1][2] = 7
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.s7.text
        self.root.ids.tint_shade.text_color = self.root.ids.s7.text_color
    
    def callback_s8(self):
        self.callback_return_home("Shade")
        self.master_selection[1][1] = 2
        self.master_selection[1][2] = 8
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.s8.text
        self.root.ids.tint_shade.text_color = self.root.ids.s8.text_color
    
    def callback_s9(self):
        self.callback_return_home("Shade")
        self.master_selection[1][1] = 2
        self.master_selection[1][2] = 9
        self.root.ids.tint_shade.md_bg_color = self.color_ids[tuple(self.master_selection[1]) + (self.master_selection[2],)]
        self.root.ids.tint_shade.text = self.root.ids.s9.text
        self.root.ids.tint_shade.text_color = self.root.ids.s9.text_color

    # WRITING LOGIC FOR COMPLEMENTARY COLORS
     
    def callback_complementary_result(self, master_color, master_tint_shade, master_level, color_wheel):
        
        complementary_key = {
            1 : 7,
            2 : 8,
            3 : 9,
            4 : 10,
            5 : 11,
            6 : 12, 
            7 : 1,
            8 : 2,
            9 : 3,
            10 : 4,
            11 : 5,
            12 : 6
        }

        complementary_color = (complementary_key[master_color], master_tint_shade, master_level, color_wheel)
        self.root.ids.complementary_master_color_card.md_bg_color = self.color_ids[(master_color, master_tint_shade, master_level, color_wheel)]
        self.root.ids.complementary_color_card.md_bg_color = self.color_ids[complementary_color]
        
        self.callback_complementary_info_tint_shade()
        self.callback_complementary_info_hex(   self.root.ids.complementary_master_color_card.md_bg_color, 
                                                self.root.ids.complementary_color_card.md_bg_color
                                            )
        self.root.ids.complementary_color_card_info_text.text = self.base_colors_representation[(complementary_color[0], complementary_color[3])]
        
    # WRITING LOGIC FOR MONOCHROMATIC COLORS

    def callback_monochromatic_result(self, master_color, master_tint_shade, master_level, color_wheel):
        
        monochromatic_key = {
            (master_color, 2, 9, color_wheel) : ((master_color, 2, 6, color_wheel), (master_color, 2, 3, color_wheel)),
            (master_color, 2, 8, color_wheel) : ((master_color, 2, 5, color_wheel), (master_color, 2, 2, color_wheel)),
            (master_color, 2, 7, color_wheel) : ((master_color, 2, 4, color_wheel), (master_color, 2, 1, color_wheel)),
            (master_color, 2, 6, color_wheel) : ((master_color, 2, 3, color_wheel), (master_color, 0, 0, color_wheel)),
            (master_color, 2, 5, color_wheel) : ((master_color, 2, 2, color_wheel), (master_color, 1, 1, color_wheel)),
            (master_color, 2, 4, color_wheel) : ((master_color, 2, 1, color_wheel), (master_color, 1, 2, color_wheel)),            
            (master_color, 2, 3, color_wheel) : ((master_color, 0, 0, color_wheel), (master_color, 1, 3, color_wheel)),
            (master_color, 2, 2, color_wheel) : ((master_color, 1, 1, color_wheel), (master_color, 1, 4, color_wheel)),
            (master_color, 2, 1, color_wheel) : ((master_color, 1, 2, color_wheel), (master_color, 1, 5, color_wheel)),            
            (master_color, 0, 0, color_wheel) : ((master_color, 1, 3, color_wheel), (master_color, 1, 6, color_wheel)),            
            (master_color, 1, 1, color_wheel) : ((master_color, 1, 4, color_wheel), (master_color, 1, 7, color_wheel)),
            (master_color, 1, 2, color_wheel) : ((master_color, 1, 5, color_wheel), (master_color, 1, 8, color_wheel)),
            (master_color, 1, 3, color_wheel) : ((master_color, 1, 6, color_wheel), (master_color, 1, 9, color_wheel)),
            (master_color, 1, 4, color_wheel) : ((master_color, 1, 1, color_wheel), (master_color, 2, 2, color_wheel)),
            (master_color, 1, 5, color_wheel) : ((master_color, 1, 2, color_wheel), (master_color, 2, 1, color_wheel)),
            (master_color, 1, 6, color_wheel) : ((master_color, 1, 3, color_wheel), (master_color, 0, 0, color_wheel)),
            (master_color, 1, 7, color_wheel) : ((master_color, 1, 4, color_wheel), (master_color, 1, 1, color_wheel)),
            (master_color, 1, 8, color_wheel) : ((master_color, 1, 5, color_wheel), (master_color, 1, 2, color_wheel)),
            (master_color, 1, 9, color_wheel) : ((master_color, 1, 6, color_wheel), (master_color, 1, 3, color_wheel))            
        }

        monochromatic_color_1 = monochromatic_key[(master_color, master_tint_shade, master_level, color_wheel)][0]
        monochromatic_color_2 = monochromatic_key[(master_color, master_tint_shade, master_level, color_wheel)][1]
        self.root.ids.monochromatic_master_color_card.md_bg_color = self.color_ids[(master_color, master_tint_shade, master_level, color_wheel)]
        self.root.ids.monochromatic_color_card_1.md_bg_color = self.color_ids[monochromatic_color_1]
        self.root.ids.monochromatic_color_card_2.md_bg_color = self.color_ids[monochromatic_color_2]

        self.callback_monochromatic_info_tint_shade()
        self.callback_monochromatic_info_hex(   self.root.ids.monochromatic_master_color_card.md_bg_color, 
                                                self.root.ids.monochromatic_color_card_1.md_bg_color,
                                                self.root.ids.monochromatic_color_card_2.md_bg_color 
                                            )
        self.root.ids.monochromatic_color_card_1_info_tint_shade.text = self.tint_shade_representation[(monochromatic_color_1[1], monochromatic_color_1[2])]
        self.root.ids.monochromatic_color_card_2_info_tint_shade.text = self.tint_shade_representation[(monochromatic_color_2[1], monochromatic_color_2[2])]

    # WRITING LOGIC FOR ANALOGOUS COLORS

    def callback_analogous_result(self, master_color, master_tint_shade, master_level, color_wheel):
        
        analogous_key = {
            1 : (12, 2),
            2 : (1, 3),
            3 : (2, 4),
            4 : (3, 5),
            5 : (4, 6),
            6 : (5, 7),
            7 : (6, 8),
            8 : (7, 9),
            9 : (8, 10),
            10 : (9, 11),
            11 : (10, 12),
            12 : (11, 1)
        }

        analogous_color_1 = (analogous_key[master_color][0], master_tint_shade, master_level, color_wheel)
        analogous_color_2 = (analogous_key[master_color][1], master_tint_shade, master_level, color_wheel)
        self.root.ids.analogous_master_color_card.md_bg_color = self.color_ids[(master_color, master_tint_shade, master_level, color_wheel)]
        self.root.ids.analogous_color_card_1.md_bg_color = self.color_ids[analogous_color_1]
        self.root.ids.analogous_color_card_2.md_bg_color = self.color_ids[analogous_color_2]

        self.callback_analogous_info_tint_shade()
        self.callback_analogous_info_hex(   self.root.ids.analogous_master_color_card.md_bg_color,
                                            self.root.ids.analogous_color_card_1.md_bg_color,
                                            self.root.ids.analogous_color_card_2.md_bg_color    
                                        )
        self.root.ids.analogous_color_card_1_info_text.text = self.base_colors_representation[(analogous_color_1[0], analogous_color_1[3])]
        self.root.ids.analogous_color_card_2_info_text.text = self.base_colors_representation[(analogous_color_2[0], analogous_color_2[3])]

    # WRITING LOGIC FOR TRIADIC COLORS

    def callback_triadic_result(self, master_color, master_tint_shade, master_level, color_wheel):
        triadic_key = {
            1 : (5, 9),
            2 : (6, 10),
            3 : (7, 11),
            4 : (8, 12),
            5 : (9, 1),
            6 : (10, 2),
            7 : (11, 3),
            8 : (12, 4),
            9 : (1, 5),
            10 : (2, 6),
            11 : (3, 7),
            12 : (4, 8)
        }

        triadic_color_1 = (triadic_key[master_color][0], master_tint_shade, master_level, color_wheel)
        triadic_color_2 = (triadic_key[master_color][1], master_tint_shade, master_level, color_wheel)
        self.root.ids.triadic_master_color_card.md_bg_color = self.color_ids[(master_color, master_tint_shade, master_level, color_wheel)]
        self.root.ids.triadic_color_card_1.md_bg_color = self.color_ids[triadic_color_1]
        self.root.ids.triadic_color_card_2.md_bg_color = self.color_ids[triadic_color_2]

        self.callback_triadic_info_tint_shade()
        self.callback_triadic_info_hex(   self.root.ids.triadic_master_color_card.md_bg_color,
                                            self.root.ids.triadic_color_card_1.md_bg_color,
                                            self.root.ids.triadic_color_card_2.md_bg_color    
                                        )
        self.root.ids.triadic_color_card_1_info_text.text = self.base_colors_representation[(triadic_color_1[0], triadic_color_1[3])]
        self.root.ids.triadic_color_card_2_info_text.text = self.base_colors_representation[(triadic_color_2[0], triadic_color_2[3])]

    # WRITING LOGIC FOR TETRADIC COLORS

    def callback_tetradic_result(self, master_color, master_tint_shade, master_level, color_wheel):
        
        tetradic_key = {
            1 : (4, 7, 10),
            2 : (5, 8, 11),
            3 : (6, 9, 12),
            4 : (7, 10, 1),
            5 : (8, 11, 2),
            6 : (9, 12, 3),
            7 : (10, 1, 4),
            8 : (11, 2, 5),
            9 : (12, 3, 6),
            10 : (1, 4, 7),
            11 : (2, 5, 8),
            12 : (3, 6, 9)
        }

        tetradic_color_1 = (tetradic_key[master_color][0], master_tint_shade, master_level, color_wheel)
        tetradic_color_2 = (tetradic_key[master_color][1], master_tint_shade, master_level, color_wheel)
        tetradic_color_3 = (tetradic_key[master_color][2], master_tint_shade, master_level, color_wheel)
        self.root.ids.tetradic_master_color_card.md_bg_color = self.color_ids[(master_color, master_tint_shade, master_level, color_wheel)]
        self.root.ids.tetradic_color_card_1.md_bg_color = self.color_ids[tetradic_color_1]
        self.root.ids.tetradic_color_card_2.md_bg_color = self.color_ids[tetradic_color_2]
        self.root.ids.tetradic_color_card_3.md_bg_color = self.color_ids[tetradic_color_3]

        self.callback_tetradic_info_tint_shade()
        self.callback_tetradic_info_hex(    self.root.ids.tetradic_master_color_card.md_bg_color,
                                            self.root.ids.tetradic_color_card_1.md_bg_color,
                                            self.root.ids.tetradic_color_card_2.md_bg_color,
                                            self.root.ids.tetradic_color_card_3.md_bg_color        
                                        )
        self.root.ids.tetradic_color_card_1_info_text.text = self.base_colors_representation[(tetradic_color_1[0], tetradic_color_1[3])]
        self.root.ids.tetradic_color_card_2_info_text.text = self.base_colors_representation[(tetradic_color_2[0], tetradic_color_2[3])]
        self.root.ids.tetradic_color_card_3_info_text.text = self.base_colors_representation[(tetradic_color_3[0], tetradic_color_3[3])]
        
    # DEFINING CALLBACK FUNCTION FOR GET COLOR HARMONIES BUTTON

    def callback_get_color_harmonies(self):
        
        if self.master_selection[0] == None:
            Snackbar(
                text = 'Please select a color scheme !',
                snackbar_x = "9dp",
                snackbar_y = "9dp",
                size_hint_x = 0.95,
                duration = 1.5
                ).open()
        elif self.master_selection[1][0] == None:
            Snackbar(
                text = 'Please select a color !',
                snackbar_x = "9dp",
                snackbar_y = "9dp",
                size_hint_x = 0.95,
                duration = 1.5
                ).open()

        else:

            if self.master_selection[0] == 1:
                self.root.transition.direction = "left"
                self.root.current = "complementary"
                self.callback_complementary_result( self.master_selection[1][0], 
                                                    self.master_selection[1][1], 
                                                    self.master_selection[1][2], 
                                                    self.master_selection[2]
                                                    )

            elif self.master_selection[0] == 2:
                self.root.transition.direction = "left"
                self.root.current = "monochromatic"
                self.callback_monochromatic_result( self.master_selection[1][0], 
                                                    self.master_selection[1][1], 
                                                    self.master_selection[1][2],
                                                    self.master_selection[2]
                                                    )

            elif self.master_selection[0] == 3:
                self.root.transition.direction = "left"
                self.root.current = "analogous"
                self.callback_analogous_result( self.master_selection[1][0], 
                                                self.master_selection[1][1], 
                                                self.master_selection[1][2],
                                                self.master_selection[2]
                                                )

            elif self.master_selection[0] == 4:
                self.root.transition.direction = "left"
                self.root.current = "triadic"
                self.callback_triadic_result(   self.master_selection[1][0], 
                                                self.master_selection[1][1], 
                                                self.master_selection[1][2],
                                                self.master_selection[2]
                                                )

            elif self.master_selection[0] == 5:
                self.root.transition.direction = "left"
                self.root.current = "tetradic"
                self.callback_tetradic_result( self.master_selection[1][0], 
                                                self.master_selection[1][1], 
                                                self.master_selection[1][2],
                                                self.master_selection[2]
                                                )
    
    # DEFINING CALLBACK FUNCTIONS FOR ADDED COLOR SUPPORT FUNCTIONALITIES IN THE SETTINGS SCREEN

    def callback_master_color_wheel(self):
        
        if self.root.ids.rgb_switch.active:
            self.master_selection[2] = 1
        else:
            self.master_selection[2] = 2

    def callback_rgb_listitem(self):
        if self.root.ids.rgb_switch.active == True:
            self.root.ids.rgb_switch.active = False
        else:
            self.root.ids.rgb_switch.active = True

    def callback_ryb_listitem(self):
        if self.root.ids.ryb_switch.active == True:
            self.root.ids.ryb_switch.active = False
        else:
            self.root.ids.ryb_switch.active = True
    
    def callback_rgb_switch(self):
        
        if self.root.ids.rgb_switch.active:
            self.root.ids.ryb_switch.active = False
            self.root.ids.color_wheel_indicator_info_text.text = "RGB"

        else:
            self.root.ids.ryb_switch.active = True
            self.root.ids.color_wheel_indicator_info_text.text = "RYB"

        self.root.ids.color_selection.text = "SELECT"
        self.root.ids.color_selection.md_bg_color = self.azure_s1_rgb
        self.root.ids.color_selection.text_color = self.callback_contrasting_text_color(self.root.ids.color_selection.md_bg_color)
        self.callback_reset_tint_shade()
        self.master_selection[1] = [None, None, None]
        self.callback_master_color_wheel()
        

    def callback_ryb_switch(self):
        
        if self.root.ids.ryb_switch.active:
            self.root.ids.rgb_switch.active = False
        else:
            self.root.ids.rgb_switch.active = True
    
    # DEFINING FUNCTIONS FOR DISPLAYING COLOR NAME, TINT/SHADE VALUE AND HEX CODES IN VARIOUS CARDS IN DIFFERENT COLOR SCHEME SCREENS

    def callback_complementary_info_tint_shade(self):
        
        if self.root.ids.tint_shade.text == "SELECT":
            self.root.ids.complementary_master_color_card_info_tint_shade.text = "Base Color"
        else:
            self.root.ids.complementary_master_color_card_info_tint_shade.text = self.root.ids.tint_shade.text
    
    def callback_monochromatic_info_tint_shade(self):
        
        if self.root.ids.tint_shade.text == "SELECT":
            self.root.ids.monochromatic_master_color_card_info_tint_shade.text = "Base Color"
        else:
            self.root.ids.monochromatic_master_color_card_info_tint_shade.text = self.root.ids.tint_shade.text

    def callback_analogous_info_tint_shade(self):
        
        if self.root.ids.tint_shade.text == "SELECT":
            self.root.ids.analogous_master_color_card_info_tint_shade.text = "Base Color"
        else:
            self.root.ids.analogous_master_color_card_info_tint_shade.text = self.root.ids.tint_shade.text
    
    def callback_triadic_info_tint_shade(self):
        
        if self.root.ids.tint_shade.text == "SELECT":
            self.root.ids.triadic_master_color_card_info_tint_shade.text = "Base Color"
        else:
            self.root.ids.triadic_master_color_card_info_tint_shade.text = self.root.ids.tint_shade.text
    
    def callback_tetradic_info_tint_shade(self):
        
        if self.root.ids.tint_shade.text == "SELECT":
            self.root.ids.tetradic_master_color_card_info_tint_shade.text = "Base Color"
        else:
            self.root.ids.tetradic_master_color_card_info_tint_shade.text = self.root.ids.tint_shade.text

    def callback_complementary_info_hex(self, master_color, complementary_color):
        self.root.ids.complementary_master_color_card_info_hex.text = self.callback_rgb_to_hex(master_color)
        self.root.ids.complementary_color_card_info_hex.text = self.callback_rgb_to_hex(complementary_color)
    
    def callback_monochromatic_info_hex(self, master_color, monochromatic_color_1, monochromatic_color_2):
        self.root.ids.monochromatic_master_color_card_info_hex.text = self.callback_rgb_to_hex(master_color)
        self.root.ids.monochromatic_color_card_1_info_hex.text = self.callback_rgb_to_hex(monochromatic_color_1)
        self.root.ids.monochromatic_color_card_2_info_hex.text = self.callback_rgb_to_hex(monochromatic_color_2)
    
    def callback_analogous_info_hex(self, master_color, analogous_color_1, analogous_color_2):
        self.root.ids.analogous_master_color_card_info_hex.text = self.callback_rgb_to_hex(master_color)
        self.root.ids.analogous_color_card_1_info_hex.text = self.callback_rgb_to_hex(analogous_color_1)
        self.root.ids.analogous_color_card_2_info_hex.text = self.callback_rgb_to_hex(analogous_color_2)
    
    def callback_triadic_info_hex(self, master_color, triadic_color_1, triadic_color_2):
        self.root.ids.triadic_master_color_card_info_hex.text = self.callback_rgb_to_hex(master_color)
        self.root.ids.triadic_color_card_1_info_hex.text = self.callback_rgb_to_hex(triadic_color_1)
        self.root.ids.triadic_color_card_2_info_hex.text = self.callback_rgb_to_hex(triadic_color_2)
    
    def callback_tetradic_info_hex(self, master_color, tetradic_color_1, tetradic_color_2, tetradic_color_3):
        self.root.ids.tetradic_master_color_card_info_hex.text = self.callback_rgb_to_hex(master_color)
        self.root.ids.tetradic_color_card_1_info_hex.text = self.callback_rgb_to_hex(tetradic_color_1)
        self.root.ids.tetradic_color_card_2_info_hex.text = self.callback_rgb_to_hex(tetradic_color_2)
        self.root.ids.tetradic_color_card_3_info_hex.text = self.callback_rgb_to_hex(tetradic_color_3)

    # DEFINING FUNCTIONS FOR SWITCHING BETWEEN DARK AND LIGHT THEMES 

    def callback_light_theme_listitem(self):
        if self.root.ids.light_theme_switch.active == True:
            self.root.ids.light_theme_switch.active = False
        else:
            self.root.ids.light_theme_switch.active = True
    
    def callback_dark_theme_listitem(self):
        if self.root.ids.dark_theme_switch.active == True:
            self.root.ids.dark_theme_switch.active = False
        else:
            self.root.ids.dark_theme_switch.active = True

    def callback_light_theme_switch(self):
        if self.root.ids.light_theme_switch.active:
            self.root.ids.dark_theme_switch.active = False
            self.theme_cls.theme_style = "Light"

        else:
            self.root.ids.dark_theme_switch.active = True
            self.theme_cls.theme_style = "Dark"
        
    def callback_dark_theme_switch(self):
        if self.root.ids.dark_theme_switch.active:
            self.root.ids.light_theme_switch.active = False
        else:
            self.root.ids.light_theme_switch.active = True

    # DEFINING CALLBACK FUNCTION FOR COLOR WHEEL INDICATOR BUTTON

    def callback_color_wheel_indicator(self):
         Snackbar(
                text = 'Color Wheels can be changed in Settings.',
                snackbar_x = "9dp",
                snackbar_y = "9dp",
                size_hint_x = 0.95,
                duration = 1.5
                ).open()
    
    # DEFINING CALLBACK FUNCTIONS FOR CHANGING THEME COLORS ON CLICKING CARDS IN DIFFERENT COLOR SCHEME SCREENS
    
    def callback_primary_palette_for_custom_widgets(self, master_color):
        
        self.callback_primary_pallete_for_home_screen(master_color)
        self.callback_primary_pallete_for_developer_screen(master_color)
        self.callback_primary_pallete_for_about_screen(master_color)
        self.callback_primary_pallete_for_help_screen(master_color)
        self.callback_primary_pallete_for_settings_screen(master_color)
        self.callback_primary_pallete_for_colors_screen(master_color)
        self.callback_primary_pallete_for_tint_screen(master_color)
        self.callback_primary_pallete_for_shade_screen(master_color)
        self.callback_primary_pallete_for_complementary_screen(master_color)
        self.callback_primary_pallete_for_monochromatic_screen(master_color)
        self.callback_primary_pallete_for_analogous_screen(master_color)
        self.callback_primary_pallete_for_triadic_screen(master_color)
        self.callback_primary_pallete_for_tetradic_screen(master_color)

    def callback_primary_pallete_for_home_screen(self, master_color):
        self.root.ids.home_screen_top_app_bar.md_bg_color = master_color
        self.root.ids.color_scheme.md_bg_color = master_color
        self.root.ids.get_color_harmonies.md_bg_color = master_color
        self.root.ids.color_wheel_indicator.md_bg_color = master_color
    
    def callback_primary_pallete_for_developer_screen(self, master_color):
        self.root.ids.developer_screen_top_app_bar.md_bg_color = master_color

    def callback_primary_pallete_for_about_screen(self, master_color):
        self.root.ids.about_screen_top_app_bar.md_bg_color = master_color

    def callback_primary_pallete_for_help_screen(self, master_color):
        self.root.ids.help_screen_top_app_bar.md_bg_color = master_color

    def callback_primary_pallete_for_settings_screen(self, master_color):
        self.root.ids.settings_screen_top_app_bar.md_bg_color = master_color
    
    def callback_primary_pallete_for_colors_screen(self, master_color):
        self.root.ids.colors_screen_top_app_bar.md_bg_color = master_color
    
    def callback_primary_pallete_for_tint_screen(self, master_color):
        self.root.ids.tint_screen_top_app_bar.md_bg_color = master_color

    def callback_primary_pallete_for_shade_screen(self, master_color):
        self.root.ids.shade_screen_top_app_bar.md_bg_color = master_color
    
    def callback_primary_pallete_for_complementary_screen(self, master_color):
        self.root.ids.complementary_screen_top_app_bar.md_bg_color = master_color

    def callback_primary_pallete_for_monochromatic_screen(self, master_color):
        self.root.ids.monochromatic_screen_top_app_bar.md_bg_color = master_color

    def callback_primary_pallete_for_analogous_screen(self, master_color):
        self.root.ids.analogous_screen_top_app_bar.md_bg_color = master_color
    
    def callback_primary_pallete_for_triadic_screen(self, master_color):
        self.root.ids.triadic_screen_top_app_bar.md_bg_color = master_color
    
    def callback_primary_pallete_for_tetradic_screen(self, master_color):
        self.root.ids.tetradic_screen_top_app_bar.md_bg_color = master_color
    
    # DEFINING CALLBACK FUNCTIONS FOR CHANGING THEME COLORS ON CLICKING CARDS IN DIFFERENT COLOR SCHEME SCREENS

    def callback_reset_primary_palette_for_custom_widgets(self):
        
        self.callback_reset_primary_pallete_for_home_screen()
        self.callback_reset_primary_pallete_for_developer_screen()
        self.callback_reset_primary_pallete_for_about_screen()
        self.callback_reset_primary_pallete_for_help_screen()
        self.callback_reset_primary_pallete_for_settings_screen()
        self.callback_reset_primary_pallete_for_colors_screen()
        self.callback_reset_primary_pallete_for_tint_screen()
        self.callback_reset_primary_pallete_for_shade_screen()
        self.callback_reset_primary_pallete_for_complementary_screen()
        self.callback_reset_primary_pallete_for_monochromatic_screen()
        self.callback_reset_primary_pallete_for_analogous_screen()
        self.callback_reset_primary_pallete_for_triadic_screen()
        self.callback_reset_primary_pallete_for_tetradic_screen()

        self.callback_reset_color_scheme()
        self.callback_reset_color_selection()

        self.callback_snackbar_reset_primary_pallete()

    def callback_reset_primary_pallete_for_home_screen(self):
        self.root.ids.home_screen_top_app_bar.md_bg_color = self.azure_s1_rgb
        self.root.ids.color_scheme.md_bg_color = self.azure_s1_rgb
        self.root.ids.get_color_harmonies.md_bg_color = self.azure_s1_rgb
        self.root.ids.color_wheel_indicator.md_bg_color = self.azure_s1_rgb
    
    def callback_reset_primary_pallete_for_developer_screen(self):
        self.root.ids.developer_screen_top_app_bar.md_bg_color = self.azure_s1_rgb

    def callback_reset_primary_pallete_for_about_screen(self):
        self.root.ids.about_screen_top_app_bar.md_bg_color = self.azure_s1_rgb

    def callback_reset_primary_pallete_for_help_screen(self):
        self.root.ids.help_screen_top_app_bar.md_bg_color = self.azure_s1_rgb

    def callback_reset_primary_pallete_for_settings_screen(self):
        self.root.ids.settings_screen_top_app_bar.md_bg_color = self.azure_s1_rgb
    
    def callback_reset_primary_pallete_for_colors_screen(self):
        self.root.ids.colors_screen_top_app_bar.md_bg_color = self.azure_s1_rgb
    
    def callback_reset_primary_pallete_for_tint_screen(self):
        self.root.ids.tint_screen_top_app_bar.md_bg_color = self.azure_s1_rgb

    def callback_reset_primary_pallete_for_shade_screen(self):
        self.root.ids.shade_screen_top_app_bar.md_bg_color = self.azure_s1_rgb
    
    def callback_reset_primary_pallete_for_complementary_screen(self):
        self.root.ids.complementary_screen_top_app_bar.md_bg_color = self.azure_s1_rgb

    def callback_reset_primary_pallete_for_monochromatic_screen(self):
        self.root.ids.monochromatic_screen_top_app_bar.md_bg_color = self.azure_s1_rgb

    def callback_reset_primary_pallete_for_analogous_screen(self):
        self.root.ids.analogous_screen_top_app_bar.md_bg_color = self.azure_s1_rgb
    
    def callback_reset_primary_pallete_for_triadic_screen(self):
        self.root.ids.triadic_screen_top_app_bar.md_bg_color = self.azure_s1_rgb
    
    def callback_reset_primary_pallete_for_tetradic_screen(self):
        self.root.ids.tetradic_screen_top_app_bar.md_bg_color = self.azure_s1_rgb

    def callback_snackbar_reset_primary_pallete(self):
        Snackbar(
                text = 'Configuration has been set to default.',
                snackbar_x = "9dp",
                snackbar_y = "9dp",
                size_hint_x = 0.95,
                duration = 1.5
                ).open()
    
    # DEFINING FUNCTIONS FOR ADDING RESET SETTINGS FUNCTIONALITY IN SETTINGS SCREEN

    def callback_dialog_reset_confirmation(self):
        self.dialog_reset_confirmation.open()

    def callback_dialog_reset_confirmation_accept(self):
        
        self.callback_reset_settings()
        self.callback_dialog_reset_confirmation_close()

    def callback_dialog_reset_confirmation_close(self):
        self.dialog_reset_confirmation.dismiss()

    def callback_reset_settings(self):
        
        self.root.ids.rgb_switch.active = True
        self.root.ids.light_theme_switch.active = True
    
    # DEFINING FUNCTION TO BE CALLED ON START UP

    def on_start(self):
        #self.fps_monitor_start()
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

        Clock.schedule_once(self.callback_initialize_presplash_animation_1, 6)
        self.change_animation_event = Clock.schedule_interval(self.callback_check_for_screen_change_to_animation_2, 1/5)
        # Clock.schedule_once(self.callback_initialize_presplash_animation_2, 15)
        # Clock.schedule_once(self.callback_initialize_progress_bar, 15)

    # HANDLING BACK BUTTON FUNCTIONALITY IN ANDROID

    def hook_keyboard(self, window, key, *largs):
        
        if key == 27:
            
            if self.root.current in ["home", "presplash"]:
                self.stop()
            
            elif self.root.current == "developer":
                self.callback_return_home("Developer")
            
            elif self.root.current == "about":
                self.callback_return_home("About")
            
            elif self.root.current == "help":
                self.callback_return_home("Help")
            
            elif self.root.current == "settings":
                self.callback_return_home("Settings")
            
            elif self.root.current == "colors":
                self.callback_return_home("Colors")
            
            elif self.root.current == "tint":
                self.callback_return_home("Tint")
            
            elif self.root.current == "shade":
                self.callback_return_home("Shade")
            
            elif self.root.current == "complementary":    
                self.callback_return_home("Complementary")
            
            elif self.root.current == "monochromatic":
                self.callback_return_home("Monochromatic")
            
            elif self.root.current == "analogous":
                self.callback_return_home("Analogous")
            
            elif self.root.current == "triadic":
                self.callback_return_home("Triadic")
            
            elif self.root.current == "Triadic":
                self.callback_return_home("Monochromatic")
            
            elif self.root.current == "tetradic":
                self.callback_return_home("Tetradic")
        
        return True
    
    # DEFINING FUNCTIONS FOR ANIMATING WIDGETS OF PRESPLASH SCREENS

    def callback_initialize_presplash_animation_1(self, *args):
        
        Clock.schedule_once(self.callback_animate_eye_lid)
        Clock.schedule_once(self.callback_animate_eye_background, 2)
        Clock.schedule_once(self.callback_animate_vanish_eye, 2)
        Clock.schedule_once(self.callback_vanish_eye_lid, 2)
        Clock.schedule_once(self.callback_animate_enlarge_color_wheel, 2)
        Clock.schedule_once(self.callback_animate_rotate_color_wheel, 2)
    
    def callback_check_for_screen_change_to_animation_2(self, *args):
        
        if self.root.ids.color_wheel.angle == 360:
            self.root.transition.direction = "up"
            self.root.current = "presplash_2"
            self.callback_initialize_presplash_animation_2()
            self.callback_initialize_progress_bar()
            Clock.unschedule(self.change_animation_event)

    def callback_initialize_presplash_animation_2(self, *args):

        Clock.schedule_once(self.callback_animate_h_appear, 0.0)
        Clock.schedule_once(self.callback_animate_U_appear, 0.4)
        Clock.schedule_once(self.callback_animate_e_appear, 0.8)
        Clock.schedule_once(self.callback_animate_A_appear, 1.2)
        Clock.schedule_once(self.callback_animate_p_1_appear, 1.6)
        Clock.schedule_once(self.callback_animate_p_2_appear, 2.0)
        
        Clock.schedule_once(self.callback_animate_h_change_color, 2.3)
        Clock.schedule_once(self.callback_animate_U_change_color, 2.6)
        Clock.schedule_once(self.callback_animate_e_change_color, 2.9)
        Clock.schedule_once(self.callback_animate_A_change_color, 3.2)
        Clock.schedule_once(self.callback_animate_p_1_change_color, 3.5)
        Clock.schedule_once(self.callback_animate_p_2_change_color, 3.8)

        Clock.schedule_once(self.callback_animate_h_vanish, 5)
        Clock.schedule_once(self.callback_animate_e_vanish, 5.4)
        Clock.schedule_once(self.callback_animate_p_1_vanish, 5.8)
        Clock.schedule_once(self.callback_animate_p_2_vanish, 6.2)

        Clock.schedule_once(self.callback_animate_U_move, 7)
        Clock.schedule_once(self.callback_animate_A_move, 7)
    
        Clock.schedule_once(self.callback_animate_Umang_appear, 8)
        Clock.schedule_once(self.callback_animate_Amogh_appear, 9)


    def callback_animate_h_appear(self, *args):

        animation = Animation(  pos_hint = {"center_y" : 0.5},
                                opacity = 1,
                                duration = self.appear_animation_duration)
        widget = self.root.ids.h
        animation.start(widget)
    
    def callback_animate_U_appear(self, *args):

        animation = Animation(  pos_hint = {"center_y" : 0.5},
                                opacity = 1,
                                duration = self.appear_animation_duration)
        widget = self.root.ids.U
        animation.start(widget)
    
    def callback_animate_e_appear(self, *args):

        animation = Animation(  pos_hint = {"center_y" : 0.5},
                                opacity = 1,
                                duration = self.appear_animation_duration)
        widget = self.root.ids.e
        animation.start(widget)
    
    def callback_animate_A_appear(self, *args):

        animation = Animation(  pos_hint = {"center_y" : 0.5},
                                opacity = 1,
                                duration = self.appear_animation_duration)
        widget = self.root.ids.A
        animation.start(widget)
    
    def callback_animate_p_1_appear(self, *args):

        animation = Animation(  pos_hint = {"center_y" : 0.5},
                                opacity = 1,
                                duration = self.appear_animation_duration)
        widget = self.root.ids.p_1
        animation.start(widget)
    
    def callback_animate_p_2_appear(self, *args):

        animation = Animation(  pos_hint = {"center_y" : 0.5},
                                opacity = 1,
                                duration = self.appear_animation_duration)
        widget = self.root.ids.p_2
        animation.start(widget)
    
    def callback_animate_h_change_color(self, *args):

        animation = Animation(  md_bg_color = [128/255, 1/255, 173/255, 1],
                                duration = self.change_color_animation_duration
                                )
        animation_ = Animation( color = [1, 1, 1, 1],
                                duration = self.change_color_animation_duration)
        widget = self.root.ids.h
        widget_ = self.root.ids.h_label
        animation.start(widget)
        animation_.start(widget_)
    
    def callback_animate_U_change_color(self, *args):

        animation = Animation(  md_bg_color = [128/255, 1/255, 173/255, 1],
                                duration = self.change_color_animation_duration
                                )
        animation_ = Animation( color = [1, 1, 1, 1],
                                duration = self.change_color_animation_duration)
        widget = self.root.ids.U
        widget_ = self.root.ids.U_label
        animation.start(widget)
        animation_.start(widget_)
    
    def callback_animate_e_change_color(self, *args):

        animation = Animation(  md_bg_color = [128/255, 1/255, 173/255, 1],
                                duration = self.change_color_animation_duration
                                )
        animation_ = Animation( color = [1, 1, 1, 1],
                                duration = self.change_color_animation_duration)
        widget = self.root.ids.e
        widget_ = self.root.ids.e_label
        animation.start(widget)
        animation_.start(widget_)
    
    def callback_animate_A_change_color(self, *args):

        animation = Animation(  md_bg_color = [128/255, 1/255, 173/255, 1],
                                duration = self.change_color_animation_duration
                                )
        animation_ = Animation( color = [1, 1, 1, 1],
                                duration = self.change_color_animation_duration)
        widget = self.root.ids.A
        widget_ = self.root.ids.A_label
        animation.start(widget)
        animation_.start(widget_)
    
    def callback_animate_p_1_change_color(self, *args):

        animation = Animation(  md_bg_color = [128/255, 1/255, 173/255, 1],
                                duration = self.change_color_animation_duration
                                )
        animation_ = Animation( color = [1, 1, 1, 1],
                                duration = self.change_color_animation_duration)
        widget = self.root.ids.p_1
        widget_ = self.root.ids.p_1_label
        animation.start(widget)
        animation_.start(widget_)
    
    def callback_animate_p_2_change_color(self, *args):

        animation = Animation(  md_bg_color = [128/255, 1/255, 173/255, 1],
                                duration = self.change_color_animation_duration
                                )
        animation_ = Animation( color = [1, 1, 1, 1],
                                duration = self.change_color_animation_duration)
        widget = self.root.ids.p_2
        widget_ = self.root.ids.p_2_label
        animation.start(widget)
        animation_.start(widget_)

    def callback_animate_h_vanish(self, *args):

        animation = Animation(  opacity = 0,
                                duration = self.vanish_animation_duration)
        widget = self.root.ids.h
        animation.start(widget)
    
    def callback_animate_e_vanish(self, *args):

        animation = Animation(  opacity = 0,
                                duration = self.vanish_animation_duration)
        widget = self.root.ids.e
        animation.start(widget)
    
    def callback_animate_p_1_vanish(self, *args):

        animation = Animation(  opacity = 0,
                                duration = self.vanish_animation_duration)
        widget = self.root.ids.p_1
        animation.start(widget)
    
    def callback_animate_p_2_vanish(self, *args):

        animation = Animation(  opacity = 0,
                                duration = self.vanish_animation_duration)
        widget = self.root.ids.p_2
        animation.start(widget)
    
    def callback_animate_U_move(self, *args):

        animation = Animation(   pos_hint = {"center_x" : 0.7, "center_y" : 0.95},
                                duration = self.move_animation_duration)
        widget = self.root.ids.U
        animation.start(widget)
    
    def callback_animate_A_move(self, *args):

        animation = Animation(  pos_hint = {"center_x" : 0.7, "center_y" : 0.90},
                                duration = self.move_animation_duration)
        widget = self.root.ids.A
        animation.start(widget)

    def callback_animate_Umang_appear(self, *args):

        animation = Animation(  opacity = 1,
                                duration = self.appear_name_animation_duration)
        widget = self.root.ids.Umang
        animation.start(widget)
    
    def callback_animate_Amogh_appear(self, *args):

        animation = Animation(  opacity = 1,
                                duration = self.appear_name_animation_duration)
        widget = self.root.ids.Amogh
        animation.start(widget)

    def callback_presplash_progress_bar(self, dt):
        self.root.ids.presplash_progress_bar.value += 1 * 1

        if self.root.ids.presplash_progress_bar.value == 100:
            self.presplash_progress_bar_event.cancel()
            self.root.transition.direction = "left"
            self.root.current = "home"
    
    def callback_initialize_progress_bar(self, *args):
        self.presplash_progress_bar_event = Clock.schedule_interval(self.callback_presplash_progress_bar, 1/ (10 / 1))
    
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
    
    # DEFINING BUILD METHOD FOR APP

    def build(self):
        self.app = Builder.load_string(UI)
        return self.app

    # DEFINING TEMPORARY FUNCTION FOR TESTING AND DEBUGGING

    def temp(self, x):
        print(self.master_selection)
        
    
# ASSIGNING HUEAPP CLASS TO "ROOT" VARIABLE

root = hUeApp()

# EXECUTING CODE 

if __name__ == '__main__':
    root.run() 
