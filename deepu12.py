from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
import random

class GuessingGame(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        Window.clearcolor = (173/255, 216/255, 230/255, 1)  # Light Blue background

        layout = MDBoxLayout(orientation='vertical')

        toolbar = MDLabel(
            text="Welcome to Jaydeep Sharma's Guessing Game",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            halign="center",
            size_hint_y=None,
            height=40,
        )
        layout.add_widget(toolbar)

        screen = Screen()

        label = MDLabel(
            text="Guess a number between 1 and 10",
            halign='center'
        )
        screen.add_widget(label)

        guess_input = MDTextField(
            hint_text="Enter your guess",
            input_filter="int"
        )
        screen.add_widget(guess_input)

        guess_button = MDRaisedButton(
            text="Guess",
            on_release=self.check_guess
        )
        screen.add_widget(guess_button)

        new_game_button = MDRaisedButton(
            text="Start New Game",
            on_release=self.start_new_game
        )
        screen.add_widget(new_game_button)

        result_label = MDLabel(
            text="",
            halign='center'
        )
        screen.add_widget(result_label)

        layout.add_widget(screen)
        return layout

    def on_start(self):
        self.start_new_game()

    def start_new_game(self, instance=None):
        self.secret_number = random.randint(1, 10)
        self.root.ids.guess_input.text = ""
        self.root.ids.result_label.text = "New game started. Guess a number between 1 and 10."

    def check_guess(self, instance=None):
        try:
            user_guess = int(self.root.ids.guess_input.text)
        except ValueError:
            self.root.ids.result_label.text = "Please enter a valid number."
            return

        if user_guess == self.secret_number:
            self.root.ids.result_label.text = "Congratulations! You guessed the correct number."
        else:
            self.root.ids.result_label.text = "Try again. Wrong guess!"

if __name__ == "__main__":
    GuessingGame().run()
