from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder


Builder.load_file("./uix/upload_button.kv")
class UploadButton(Button):
	pass