from kivy import Config
from kivy.app import App
Config.read('Config.ini')
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

tab_pl = []
class Aplication(Widget):
    def __init__(self, **kwargs):
        super(Aplication, self).__init__(**kwargs)
#------------------------------Zdjęcie
        self.img = Image(source="img/logo.jpg", pos=(-40, 180), size=(500, 500))
        self.add_widget(self.img)
# ------------------------------Czy logowanie się powiodło
        self.zal = Label(text="", pos=(150, 350), color="#F44424")
        self.add_widget(self.zal)
# ------------------------------Logowanie
        self.inside = GridLayout(cols=1, pos=(100, 150), size=(200, 200))
        self.user_log = TextInput(text="Podaj login:", font_size=18,background_color='#000000' ,foreground_color='#00FFCE',halign='center', multiline=False, padding_y=(10, 10), size_hint=(0.5, 0.85))
        self.inside.add_widget(self.user_log)
        self.inside.cols = 1
        self.user_has = TextInput(text="Podaj login:", font_size=18,background_color='#000000' ,foreground_color='#00FFCE',halign='center', multiline=False, padding_y=(10, 10), size_hint=(0.5, 0.85))
        self.inside.add_widget(self.user_has)
        self.button = Button(text="Zaloguj się!", bold=True, background_color='#00FFCE', background_normal = "", on_press=self.logowanie, color='#000000')
        self.inside.add_widget(self.button)
        self.add_widget(self.inside)
# ------------------------------Footer
        self.footer = Label(text="MyWords 2022", pos=(150, 0), bold=True, color="#00FFCE")
        self.add_widget(self.footer)

    def logowanie(self, instrukcja):
        haslo = self.user_has.text
        login = self.user_log.text
        if "Podaj login:" == login and "Podaj login:" == haslo:
            self.clear_widgets()
# ------------------------------Tytuł
            self.kol = Label(text="Kolekcje", pos=(150, 500), color='#00FFCE', font_size=40)
            self.add_widget(self.kol)
# ------------------------------Wypisanie kolekcji
            self.button = Button(pos=(77, 450), size=(250, 50), text="Moje słowka 1", bold=True, on_press=self.kolekcja_jeden, background_color='#00FFCE', background_normal="", color='#000000')
            self.add_widget(self.button)
            self.button = Button(pos=(77, 390), size=(250, 50), text="Moje słowka 2", bold=True,on_press=self.kolekcja_dwa, background_color='#00FFCE', background_normal="", color='#000000')
            self.add_widget(self.button)

            self.button = Button(pos=(77, 70), size=(250, 50), text="Dodaj Kolekcje", bold=True, background_color='#BA0F2F', background_normal="", color='#000000')
            self.add_widget(self.button)

# ------------------------------Footer
            self.footer = Label(text="MyWords 2022", pos=(150, 0), bold=True, color="#00FFCE")
            self.add_widget(self.footer)
        else:
            sss = "Zły login lub hasło"
            self.zal.text = sss
    def kolekcja_jeden(self, instreea):
        self.clear_widgets()
        # ---------------------Nazwa
        self.kol = Label(text="Kolekcje 1", pos=(150, 500), color='#00FFCE', font_size=40)
        self.add_widget(self.kol)
        # ---------------------Słownik
        self.button = Button(pos=(77, 400), size=(250, 50), text="Słownik:",on_press=self.slownik, bold=True, background_color='#00FFCE',
                             background_normal="", color='#000000')
        self.add_widget(self.button)
        # ---------------------Dodawanie słowa


        # ---------------------Tryb nauki
        self.button = Button(pos=(77, 340), size=(250, 50), text="Trub Nauki!",on_press=self.nauka, bold=True,
                             background_color='#00FFCE', background_normal="", color='#000000')
        self.add_widget(self.button)
        # ---------------------Cofnij
        self.button = Button(pos=(77, 70), size=(250, 50), text="Cofnij!", on_press=self.logowanie, bold=True,
                             background_color='#BA0F2F', background_normal="", color='#000000')
        self.add_widget(self.button)
        # --------------------Footer
        self.footer = Label(text="MyWords 2022", pos=(150, 0), bold=True, color="#00FFCE")
        self.add_widget(self.footer)
    def kolekcja_dwa(self, instrukcja):
        self.clear_widgets()
#---------------------Nazwa
        self.kol = Label(text="Kolekcje 1", pos=(150, 500), color='#00FFCE', font_size=40)
        self.add_widget(self.kol)
#---------------------Słownik
        self.button = Button(pos=(77, 400), size=(250, 50),on_press=self.slownik, text="Słownik:", bold=True, background_color='#00FFCE',background_normal="", color='#000000')
        self.add_widget(self.button)

#---------------------Tryb nauki
        self.button = Button(pos=(77, 340), size=(250, 50), text="Trub Nauki!",on_press=self.nauka, bold=True, background_color='#00FFCE',background_normal="", color='#000000')
        self.add_widget(self.button)
#---------------------Cofnij
        self.button = Button(pos=(77, 70), size=(250, 50), text="Cofnij!",on_press=self.logowanie, bold=True, background_color='#BA0F2F',background_normal="", color='#000000')
        self.add_widget(self.button)
# --------------------Footer
        self.footer = Label(text="MyWords 2022", pos=(150, 0), bold=True, color="#00FFCE")
        self.add_widget(self.footer)
    def slowo(self,vrtbe):
        tab_pl = []
        tab_ang = []
        tab_pl.append("siema")
        tab_ang.append("hello")
        tab_pl.append("siema")
        tab_ang.append("hello")



    def nauka(self, instrukcja):
        tab_pl = ["jeden", "dwa", "trzy"]
        tab_ang = ["one", "two", "three"]
        self.clear_widgets()
        # -----------------------------Tytuł
        self.kol = Label(text="Nauka:", pos=(150, 500), color='#00FFCE', font_size=40)
        self.add_widget(self.kol)
# -----------------------------Program
        self.inside = GridLayout(cols= 2, pos=(70, 350),size=(300,300))
        self.napis_jeden = Label(text="Przetłumacz słowo: ", bold=True, color="#BA0F2F", font_size= 24)
        self.inside.add_widget(self.napis_jeden)
        self.napis_dwa = Label(text=tab_pl[0], bold=True, color="#00FFCE")
        self.inside.add_widget(self.napis_dwa)
        self.add_widget(self.inside)

        self.odp = TextInput(text="Przetłumacz:", font_size=18,background_color='#000000' ,foreground_color='#00FFCE',halign='center', multiline=False, padding_y=(10, 10), size_hint=(0.5, 0.85),pos=(120, 280),size=(150,150))
        self.add_widget(self.odp)

        self.footer = Label(text="", pos=(150, 400), bold=True, color="#00FFCE")
        self.add_widget(self.footer)

        self.button = Button(pos=(77, 320), size=(250, 50), text="Sprawdz!",on_press=self.spr, bold=True, background_color='#BA0F2F', background_normal="", color='#000000')
        self.add_widget(self.button)

        self.but_next = Button(pos=(77, 260), size=(250, 50), text="Następne!",on_press=self.but_next, bold=True, background_color='#BA0F2F', background_normal="", color='#000000')
        self.add_widget(self.but_next)
# -----------------------------Footer
        self.button = Button(pos=(77, 70), size=(250, 50), text="Cofnij!", on_press=self.logowanie, bold=True,background_color='#BA0F2F', background_normal="", color='#000000')
        self.add_widget(self.button)


        self.footer = Label(text="MyWords 2022", pos=(150, 0), bold=True, color="#00FFCE")
        self.add_widget(self.footer)
    def but_next(self,rev):
        pass
    def spr(self,ger):
        tab_pl = ["jeden", "dwa", "trzy"]
        tab_ang = ["one", "two", "three"]

    def slownik(self, tab_pl):
        self.clear_widgets()

        self.kol = Label(text="Słownik: ", pos=(150, 500), color='#00FFCE', font_size=40)
        self.add_widget(self.kol)

        self.word = Label(text="Polski", pos=(50, 460),font_size=18, bold=True, color="#F50B00")
        self.add_widget(self.word)
        self.word = Label(text="Angielski", pos=(250, 460),font_size=18, bold=True, color="#F50B00")
        self.add_widget(self.word)
        tab_pl = []
        tab_ang = []
        tab_pl.append("siema")
        tab_ang.append("hello")
        tab_pl.append("siema")
        tab_ang.append("hello")

        self.wyp(tab_pl, tab_ang)


        self.inside = GridLayout(cols=3, pos=(25, 140), size=(350, 50))
        self.textinput_pl = TextInput(text="PL", font_size=16, background_color='#000000', foreground_color='#00FFCE',halign='center', multiline=False, padding_y=(10, 10), size_hint=(0.5, 0.85))
        b = self.textinput_pl.text
        self.inside.add_widget(self.textinput_pl)
        self.textinput_ang = TextInput(text="ANG", font_size=16, background_color='#000000', foreground_color='#00FFCE',halign='center', multiline=False, padding_y=(10, 10), size_hint=(0.5, 0.85))
        self.inside.add_widget(self.textinput_ang)
        self.button = Button(text="Dodaj słowo:", bold=True, background_color='#00FFCE', background_normal="",color='#000000',on_press=self.slownik_dodaj)
        self.inside.add_widget(self.button)
        self.add_widget(self.inside)


        self.button = Button(pos=(77, 70), size=(250, 50), text="Cofnij!", on_press=self.logowanie, bold=True,
                             background_color='#BA0F2F', background_normal="", color='#000000')
        self.add_widget(self.button)

        self.footer = Label(text="MyWords 2022", pos=(150, 0), bold=True, color="#00FFCE")
        self.add_widget(self.footer)
    def wyp(self, tab_pl, tab_ang):
        x = 430
        y = 430
        for i in tab_pl:
            self.word = Label(text=i, pos=(50, x), bold=True, color="#00FFCE")
            self.add_widget(self.word)
            x = x - 20
        for i in tab_ang:
            self.word = Label(text=i, pos=(250, y), bold=True, color="#00FFCE")
            self.add_widget(self.word)
            y = y - 20
    def slownik_dodaj(self,ver):
        a = self.textinput_ang.text
        b = self.textinput_pl.text
        print(a, " ", b)

class MyWords(App):

    def build(self):
        return Aplication()

