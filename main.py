from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
from components.main_form import MainForm



class ImageResizerRoot(FloatLayout):
	background_color = [200/255, 230/255, 201/255, 1]


class ImageResizerApp(App):
	def build(self):
		return ImageResizerRoot() 

if __name__ == '__main__':
	Window.clearcolor = get_color_from_hex("#03a199")
	LabelBase.register(name = "Roboto", fn_regular = "assets/fonts/Roboto/Roboto-Light.ttf", fn_bold = "assets/fonts/Roboto/Roboto-Medium.ttf")
	ImageResizerApp().run()