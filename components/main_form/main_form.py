from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, ListProperty
from kivy.lang import Builder
from plyer import filechooser
from uix.upload_button import UploadButton
from uix.dimension_text_inputs import DimensionTextInputs

Builder.load_file("./components/main_form/main_form.kv")
class MainForm(Widget):

	background_color = [200/255, 230/255, 201/255, 1]
	selection = ListProperty()
	form = ObjectProperty()
	dimension_text_inputs = ObjectProperty()
	title_label = ObjectProperty()
	picture_image = ObjectProperty()

	def get_dimensions(self):
		print(self.size)

	def open_file(self):
		filechooser.open_file(on_selection=self.store_photo_destination)

	def store_photo_destination(self, selection):
		self.selection = selection

	def add_dimension_text_inputs(self):
		self.dimension_text_inputs.opacity = 1
		print(self.dimension_text_inputs.width, self.dimension_text_inputs.height)
		

