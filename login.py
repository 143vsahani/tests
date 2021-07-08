from kivymd.app import MDApp    
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(412, 732)

LoginPage =""" 
MDFloatLayout:
    Image:
        source: '1.jpg'
        allow_stretch: True
    MDLabel:
        text:"Welcom to I-secure"
        pos_hint:{"center_y": .85}
        font_style:"H4"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1

    MDLabel:
        text:"Login"
        pos_hint:{"center_y": .75}
        font_style:"H5"
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1  

    MDTextField:
        id:user
        hint_text:"enter yor username"
        pos_hint:{"center_x": .5,"center_y":.6}
        current_hint_text_color:0,0,0,1
        size_hint_x:.8
    
    MDTextField:
        id:password
        hint_text:"password"
        pos_hint:{"center_x": .5,"center_y":.45}
        current_hint_text_color:0,0,0,1
        size_hint_x:.8
        password:True

    MDRaisedButton:
        text: "login"
        pos_hint:{"center_x": .5,"center_y":.3}
        size_hint_x:.5
        on_release:app.verify(user.text,password.text)
        theme_text_color:"Custom"
        
"""




class login(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Red"
        login_page=Builder.load_string(LoginPage)


        return login_page

    def verify(self,user,password):
        if user == "pradeep" and password =="123":
            print("you have beean logged")


if __name__=="__main__":
    login().run()