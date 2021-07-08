from kivymd.app import MDApp    
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(412, 732)

AboutPage =""" 
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
            text:"we are a group of highly motivated computer science students and our goal to make this world more intersting then it is by develpment."
            pos_hint:{"center_y": .6}
            font_style:"H4"
            halign:"center"
            theme_text_color:"Custom"
            text_color:0,0,0,1
       
"""




class login(MDApp):
    def build(self):
        self.theme_cls.primary_palette="LightBlue"
        login_page=Builder.load_string(AboutPage)


        return login_page


if __name__=="__main__":
    login().run()