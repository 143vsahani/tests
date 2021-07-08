from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window

Window.size=(412, 732)

screen_helper ="""
ScreenManager:
    MenuScreen:
    VoiceScreen:
    AboutScreen:
<MenuScreen>:
    name:"menu"
    MDFloatLayout:
    Image:
        source: '1.jpg'
  
            # Giving the size of image
        
  
            # allow sterching of image 
        allow_stretch: True
    MDLabel:
        text:"Welcom to I-secure"
        pos_hint:{"center_y": .95}
        font_style:"H4"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1


    MDRaisedButton:
        id:userdtl
        text:"user details"
        pos_hint:{"center_x": .5,"center_y":.6}
        size_hint_x:.8
        theme_text_color:"Custom"
   
    MDRaisedButton:
        id:voice-model
        text:"voice-model"
        pos_hint:{"center_x": .5,"center_y":.5}
        size_hint_x:.8
        theme_text_color:"Custom"
        on_press:
            root.manager.current="voice"
            root.manager.transition.direction = 'left'    
                 
    
    MDRaisedButton:
        id:keypattern
        text:"Key-Pattern"
        pos_hint:{"center_x": .5,"center_y":.4}
        size_hint_x:.8
        theme_text_color:"Custom"

    MDRaisedButton:
        text: "about us"
        pos_hint:{"center_x": .5,"center_y":.3}
        size_hint_x:.8
        theme_text_color:"Custom"
        on_press:
            root.manager.current="about"
            root.manager.transition.direction = 'up'



   
<VoiceScreen>:
    name:"voice"
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
    MDRaisedButton:
        text: "back"
        pos_hint:{"center_x": .5,"center_y":.1}
        size_hint_x:.5
        on_press:
            root.manager.current="menu" 
            root.manager.transition.direction = 'right'
<AboutScreen>:
    name:"about"
    MDFloatLayout:
    Image:
        source: '1.jpg'
  
            # Giving the size of image
        
  
            # allow sterching of image 
        allow_stretch: True
    MDLabel:
        text:"About-Us"
        pos_hint:{"center_y": .95}
        font_style:"H4"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1
    MDCard :

        size_hint : None,None
        size : 320,400
        pos_hint : {"center_x":.5,"center_y":.5}
        elevation : 15
        md_bg_color : app.theme_cls.primary_color
        padding : 20
        spacing : 30
        orientation : "vertical"
    
        MDLabel:
            text:"we are a group of highly motivated computer science students and our goal to make this world more intersting then it is by our develpment."
            pos_hint:{"center_y": .6}
            font_style:"H4"
            halign:"center"
            theme_text_color:"Custom"
            text_color:0,0,0,1
    MDRaisedButton:
        text: "back"
        pos_hint:{"center_x": .5,"center_y":.1}
        size_hint_x:.5
        on_press:
            root.manager.current="menu"
            root.manager.transition.direction = 'down'

         

"""

class MenuScreen(Screen):
    pass

class VoiceScreen(Screen):
    pass

class AboutScreen(Screen):
    pass


sm=ScreenManager()
sm.add_widget(MenuScreen(name='menu')) 
sm.add_widget(VoiceScreen(name='Voice')) 
sm.add_widget(AboutScreen(name='about')) 

class mainapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Red"
        login_page=Builder.load_string(screen_helper)


        return login_page


mainapp().run()