from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

screen_helper ="""
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name:"menu"
    MDRaisedButton:
        text: "Profile"
        pos_hint:{"center_x": .5,"center_y":.6}
        size_hint_x:.5
        on_press:root.manager.current="profile"
    MDRaisedButton:
        text: "Upload"
        pos_hint:{"center_x": .5,"center_y":.5}
        size_hint_x:.5
        on_press:root.manager.current="upload"   
<ProfileScreen>:
    name:"profile"
    MDLabel:
        text:"Welcom to I-secure"
        pos_hint:{"center_y": .85}
        font_style:"H4"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1
    MDRaisedButton:
        text: "back"
        pos_hint:{"center_x": .5,"center_y":.1}
        size_hint_x:.5
        on_press:root.manager.current="menu" 
<UploadScreen>:
    name:"upload"
    MDLabel:
        text:"Welcom to I-secure upload"
        pos_hint:{"center_y": .85}
        font_style:"H4"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1
    MDRaisedButton:
        text: "back"
        pos_hint:{"center_x": .5,"center_y":.1}
        size_hint_x:.5
        on_press:root.manager.current="menu"         

"""

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass


sm=ScreenManager()
sm.add_widget(MenuScreen(name='menu')) 
sm.add_widget(ProfileScreen(name='profile')) 
sm.add_widget(UploadScreen(name='upload')) 

class mainapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Red"
        login_page=Builder.load_string(screen_helper)


        return login_page


mainapp().run()