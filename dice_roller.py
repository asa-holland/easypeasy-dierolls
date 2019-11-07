
import logging

logging.basicConfig(level=logging.DEBUG)




from kivy.app import App, runTouchApp
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import random
from kivy.core.clipboard import Clipboard


def generator(instance):
	value = ''
	for item in range(0, 120):
		value += str(random.randint(0, 17))
	return value


class ColoredRectangle(Label):
	def on_size(self, *args):
		self.canvas.before.clear()
		with self.canvas.before:
			Color(1, 1, .86, 0.8)
			Rectangle(pos=self.pos, size=self.size, size_hint_y=None)






class GeneratorScreen(BoxLayout):
	def __init__(self, **kwargs):
		def send(instance):
			self.die_result.text = str(random.randint(1, int(self.mainbutton.text.split('D')[1])))
			self.mid.text = ' '

		# initial set up of vertical screen setup
		super(GeneratorScreen, self).__init__(**kwargs)
		self.orientation = 'vertical'

		# create title label at top of screen
		self.main_label = Label(text='\n[b]Easy Peasy Die Roller[/b]\n', markup=True)
		self.main_label.font_size = 30
		self.main_label.size_hint_y = None
		self.main_label.bind(texture_size=self.main_label.setter('size'))
		self.add_widget(self.main_label)

		# create main display for generated backstories
		self.die_result = ColoredRectangle()
		self.die_result.text = 'Let\'s Roll!'
		self.die_result.color = (0, 0, 0, 1)
		self.die_result.font_size = 60
		self.add_widget(self.die_result)

		# create buffer area using label
		self.mid = Label(text=' ', size_hint_y=None)
		self.add_widget(self.mid)
		self.mid.bind(texture_size=self.mid.setter('size'))

		# create horizontal box for two side by side buttons
		self.horizontalBox = BoxLayout(orientation='horizontal', size_hint_y=None)
		self.add_widget(self.horizontalBox)

		# add button to copy existing text from die_result field
		# self.copy = Button(text='\nCopy die_result\n', disabled=True)
		# self.horizontalBox.add_widget(self.copy)
		# self.copy.bind(on_press=copy_text)
		# self.copy.bind(texture_size=self.horizontalBox.setter('size'))

		# create a dropdown with 10 buttons
		self.dropdown = DropDown()
		for index in [2, 4, 6, 8, 10, 12, 20, 100]:
			# When adding widgets, we need to specify the height manually
			# (disabling the size_hint_y) so the dropdown can calculate
			# the area it needs.

			btn = Button(text='D%d' % index, size_hint_y=None, height=44)

			# for each button, attach a callback that will call the select() method
			# on the dropdown. We'll pass the text of the button as the data of the
			# selection.
			btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

			# then add the button inside the dropdown
			self.dropdown.add_widget(btn)

		# create a big main button
		self.mainbutton = Button(text='Die Options', size_hint=(None, None))
		self.horizontalBox.add_widget(self.mainbutton)
		self.mainbutton.bind(on_release=self.dropdown.open)

		# show the dropdown menu when the main button is released
		# note: all the bind() calls pass the instance of the caller (here, the
		# mainbutton instance) as the first argument of the callback (here,
		# dropdown.open.).


		# one last thing, listen for the selection in the dropdown list and
		# assign the data to the button text.
		self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
		self.dropdown.bind(on_select=lambda instance, x: setattr(self.generate, 'disabled', False))
		self.dropdown.bind(on_select=lambda instance, x: setattr(self.generate, 'text', 'Roll!'))

		# add buttom to generate new die_result in field
		self.generate = Button(text='\nPick a die to begin.\n', disabled=True, font_size=30)
		self.horizontalBox.add_widget(self.generate)
		self.generate.bind(on_press=send)

		# add bottom black buffer zone
		self.bottom = Label(text=' ', size_hint_y=None)
		self.add_widget(self.bottom)
		self.bottom.bind(texture_size=self.bottom.setter('size'))


class MyApp(App):
	def build(self):
		return GeneratorScreen()


if __name__ == '__main__':
	MyApp().run()