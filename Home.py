from kivymd.app import MDApp    
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(412, 732)

LoginPage =""" 
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
        text:"voice-moedel"
        pos_hint:{"center_x": .5,"center_y":.5}
        size_hint_x:.8
        theme_text_color:"Custom"    
    
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
        on_release:app.AboutPage()
        
"""



class login(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Red"
        login_page=Builder.load_string(LoginPage)
        return login_page

    def AboutPage(self):
                
        return 
           
    

if __name__=="__main__":
    login().run()