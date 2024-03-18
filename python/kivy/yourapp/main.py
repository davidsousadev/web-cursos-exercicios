#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.button import Button

class SimpleApp(App):
    def build(self):
        return Button(text="Hello, Kivy!")

if __name__ == "__main__":
    SimpleApp().run()
