from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.input1 = TextInput(hint_text='Inserisci dati 1')
        self.input2 = TextInput(hint_text='Inserisci dati 2')
        self.button = Button(text='Invia Notifica')
        self.button.bind(on_press=self.show_notification)

        layout.add_widget(self.input1)
        layout.add_widget(self.input2)
        layout.add_widget(self.button)

        return layout

    def show_notification(self, instance):
        data1 = self.input1.text
        data2 = self.input2.text

        notification_content = f'Dati inseriti:\nDato 1: {data1}\nDato 2: {data2}'

        popup = Popup(title='Notifica Push', content=Label(text=notification_content), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    MyApp().run()