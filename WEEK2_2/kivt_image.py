from kivy.app import App
from kivy.uix.image import Image

class ImageViewer(App):

    def build(self):
        return iamge(source="hummigbird.jpg")

ImageViewer().run()