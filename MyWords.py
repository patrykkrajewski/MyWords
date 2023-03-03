import keyboard as keyboard
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
import mysql.connector



class Aplication(Widget):
    def __init__(self, **kwargs):
        super(Aplication, self).__init__(**kwargs)
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="mywords"
        )
        self.tab = []
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM `slowa`")
        myresult = mycursor.fetchall()
        for x in myresult:
            for i in x:
                self.tab.append(i)
        mydb.close()
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
    def nauka(self, instrukcja):
        self.x = 420
        self.y = 385
        self.i = 1
        self.clear_widgets()
        # -----------------------------Tytuł

        self.kol = Label(text="Nauka:", pos=(150, 500), color='#00FFCE', font_size=40)
        self.add_widget(self.kol)
# -----------------------------Program
        self.inside = GridLayout(cols= 1, pos=(70, 400),size=(200,200))
        self.napis_jeden = Label(text="Przetłumacz słowo: ", bold=True, color="#BA0F2F", font_size= 24)
        self.inside.add_widget(self.napis_jeden)

        self.add_widget(self.inside)


        self.footer = Label(text="", pos=(150, 400), bold=True, color="#00FFCE")
        self.add_widget(self.footer)

        self.button = Button(pos=(77, 130), size=(250, 50), text="Następne pytanie!",on_press=self.nxt, bold=True, background_color='#BA0F2F', background_normal="", color='#000000')
        self.add_widget(self.button)
# ---------------------Wynik
        self.button = Button(pos=(77, 190), size=(250, 50), text="Sprawdz!",on_press=self.spr, bold=True,background_color='#BA0F2F', background_normal="", color='#000000')
        self.add_widget(self.button)

# -----------------------------Footer
        self.button = Button(pos=(77, 70), size=(250, 50), text="Cofnij!", on_press=self.logowanie, bold=True,background_color='#BA0F2F', background_normal="", color='#000000')
        self.add_widget(self.button)


        self.footer = Label(text="MyWords 2022", pos=(150, 0), bold=True, color="#00FFCE")
        self.add_widget(self.footer)

    def nxt(self, h5y):

        if self.i < len(self.tab):
            self.word = Label(text=self.tab[self.i], pos=(50, self.x), bold=True, color="#00FFCE")
            self.add_widget(self.word)
            self.word_ang = TextInput(text="Przetłumacz!", pos=(250, self.y), background_color='#000000',
                                      foreground_color='#00FFCE')
            self.add_widget(self.word_ang)
            self.x = self.x - 20
            self.y = self.y - 20
            self.i += 3

    def spr(self,y5b):
        print(self.tab)


        if self.tab[self.i -2] == self.word_ang.text:
            print("Dobra odp!")
        else:
            print("zla odpowiedz, poprawna to: " + self.tab[self.i -2])
    def slownik(self, tab_pl):
        self.clear_widgets()

        self.kol = Label(text="Słownik: ", pos=(150, 500), color='#00FFCE', font_size=40)
        self.add_widget(self.kol)

        self.word = Label(text="Polski", pos=(50, 460),font_size=18, bold=True, color="#F50B00")
        self.add_widget(self.word)
        self.word = Label(text="Angielski", pos=(250, 460),font_size=18, bold=True, color="#F50B00")
        self.add_widget(self.word)

        self.wyp(self.tab)

        self.inside = GridLayout(cols=3, pos=(25, 140), size=(350, 50))
        self.textinput_pl = TextInput(text="PL", font_size=16, background_color='#000000', foreground_color='#00FFCE',halign='center', multiline=False, padding_y=(10, 10), size_hint=(0.5, 0.85))
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
    def wyp(self, tab):
        i=1
        x = 430
        y = 370
        while i <= len(tab):
            self.ins = Label(text=tab[i], pos=(50, x),color="#00FFCE")
            self.add_widget(self.ins)
            self.ins_2 = Label(text=tab[i+1], pos=(250, x), color="#00FFCE")
            self.add_widget(self.ins_2)
            i +=3
            x -= 20
    def wyp_dwa(self, tab):
        i = 1
        x = 420
        y = 385
        c = 0
        while i <= len(tab):
            word_ang = c
            self.word = Label(text=tab[i], pos=(50, x), bold=True, color="#00FFCE")
            self.add_widget(self.word)
            self.word_ang = TextInput(text="Przetłumacz!",pos=(250, y), background_color='#000000', foreground_color='#00FFCE')
            self.add_widget(self.word_ang)
            x = x - 20
            y = y - 20
            i+=3
            c +=1
    def slownik_dodaj(self,ver):
        a = self.textinput_ang.text
        b = self.textinput_pl.text

class MyWords(App):

    def build(self):
        return Aplication()

