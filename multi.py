from kivymd.app import MDApp    
from kivy.lang import Builder
from kivy.core.window import Window


LoginPage =""" 
MDFloatLayout:
     
    Image:
        source: '1.jpg' 
        allow_stretch: True
    
    MDCard :

        size_hint : .45,.8
        pos_hint : {"center_x":.5,"center_y":.5}
        Carousel: 
            MDTextField:
                hint_text:"first name"
                pos_hint:{"center_x": .5,"center_y":.48}
                size_hint_x:.8
            MDTextField:
                hint_text:"last name"
                pos_hint:{"center_x": .5,"center_y":36}
                size_hint_x:.8
        
"""




class login(MDApp):
    def build(self):
        login_page=Builder.load_string(LoginPage)
        return login_page

if __name__=="__main__":
    login().run()