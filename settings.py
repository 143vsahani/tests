from kivymd.app import MDApp    
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(412, 732)

SettingPage =""" 
MDFloatLayout:
    Image:
        source: '1.jpg'
  
            # Giving the size of image
        
  
            # allow sterching of image 
        allow_stretch: True

    MDSwitch:
        pos_hint: {'center_x': .9, 'center_y': .85}
    
    MDSwitch:
        pos_hint: {'center_x': .9, 'center_y': .75}
    
    MDLabel:
        text:"desable power off button"
        pos_hint:{"center_y": .85}
        font_style:"Body1"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1
  
    MDLabel:
        text:"desable aroplan on button"
        pos_hint:{"center_y": .75}
        font_style:"Body1"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1  

    

    MDRaisedButton:
        text: "save"
        pos_hint:{"center_x": .5,"center_y":.5}
        size_hint_x:.5
        theme_text_color:"Custom"
        
"""




class Setting(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Red"
        setting_page=Builder.load_string(SettingPage)


        return setting_page

    

if __name__=="__main__":
    Setting().run()