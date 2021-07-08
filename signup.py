from kivymd.app import MDApp    
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(412, 732)

SignupPage =""" 
MDFloatLayout:
    Image:
        source: '1.jpg'
  
            # Giving the size of image
        
  
            # allow sterching of image 
        allow_stretch: True
    MDLabel:
        text:"Welcom to I-secure"
        pos_hint:{"center_y": .85}
        font_style:"H4"
        halign:"center"
        theme_text_color:"Custom"
        text_color:255, 255, 255,1

    MDLabel:
        text:"Signup"
        pos_hint:{"center_y": .75}
        font_style:"H5"
        halign:"center"
        theme_text_color:"Custom"
        text_color:255, 255, 255,1  

    MDTextField:
        id:user
        hint_text:"Enter your Name"
        pos_hint:{"center_x": .5,"center_y":.6}
        current_hint_text_color:0, 0, 0, 1
        size_hint_x:.8
    
    
    MDTextField:
        id:email
        hint_text:"Email-eg:abc@.abc.com"
        pos_hint:{"center_x": .5,"center_y":.5}
        current_hint_text_color:0, 0, 0, 1
        size_hint_x:.8
    MDTextField:
        id:phone
        hint_text:"Enter your phone number"
        pos_hint:{"center_x": .5,"center_y":.4}
        current_hint_text_color:0, 0, 0, 1
        size_hint_x:.8
    MDTextField:
        id:password:add
        hint_text:"Address"
        pos_hint:{"center_x": .5,"center_y":.3}
        current_hint_text_color:0, 0, 0, 1
        size_hint_x:.8        
    MDTextField:
        id:proffesion
        hint_text:"Proffesion"
        pos_hint:{"center_x": .5,"center_y":.2}
        current_hint_text_color:0, 0, 0, 1
        size_hint_x:.8


    MDRaisedButton:
        text: "Signup"
        pos_hint:{"center_x": .5,"center_y":.1}
        size_hint_x:.5
        on_release:app.verify(user.text,password.text)
        theme_text_color:"Custom"
        
"""




class signup(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Red"
        login_page=Builder.load_string(SignupPage)


        return login_page

    def verify(self,user,password):
        if user == "pradeep" and password =="123":
            print("you have beean logged")


if __name__=="__main__":
    signup().run()