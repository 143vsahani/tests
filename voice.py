from kivymd.app import MDApp    
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(412, 732)

voicePage =""" 
MDFloatLayout:
    MDLabel:
        text:"Welcom to I-secure"
        pos_hint:{"center_y": .95}
        font_style:"H4"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1

    MDLabel:
        text:"voice module"
        pos_hint:{"center_y": .85}
        font_style:"H5"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1  

    MDTextField:
       
        hint_text:"enter your key1"
        pos_hint:{"center_x": .3,"center_y":.6}
        current_hint_text_color:0,0,0,1
        size_hint_x:.4
    MDTextField:
        
        hint_text:"enter your key2"
        pos_hint:{"center_x": .3,"center_y":.5}
        current_hint_text_color:0,0,0,1
        size_hint_x:.4
    MDTextField:
        
        hint_text:"enter yor phon1"
        pos_hint:{"center_x": .8,"center_y":.6}
        current_hint_text_color:0,0,0,1
        size_hint_x:.4
    MDTextField:
        
        hint_text:"enter yor phon2"
        pos_hint:{"center_x": .8,"center_y":.5}
        current_hint_text_color:0,0,0,1
        size_hint_x:.4            
    
    MDRaisedButton:
        text: "save"
        pos_hint:{"center_x": .5,"center_y":.3}
        size_hint_x:.5
        theme_text_color:"Custom"
        
"""




class voice(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        voice_page=Builder.load_string(voicePage)


        return voice_page


if __name__=="__main__":
    voice().run()
