from kivy.config import Config
# Config.set('graphics', 'fullscreen', 0)
#Config.set('graphics', 'resizable', 1)#Может быть понадобится
Config.set('graphics', 'height', 400)
Config.set('graphics', 'width', 300)
Config.write()
from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        label = Label(text='Привет мир!')
        return label


if __name__ == '__main__':
    app = MainApp()
    app.run()
