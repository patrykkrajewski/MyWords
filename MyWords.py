import keyboard as keyboard
from kivy import Config
from kivy.app import App
from kivy.uix.progressbar import ProgressBar

Config.read('Config.ini')
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import mysql.connector



class Aplication(Widget):
    def koniec_nauka(self):
        self.clear_widgets()
        self.szablon(self)
        self.zal = Label(text="Koniec Kolekcji!", pos=(150, 300), color="#F44424",font_size=18)
        self.add_widget(self.zal)
        self.zal = Label(text="Twój wynik to: "+ str(self.dob) +" / "+str(self.dob + self.zle), pos=(150, 270),font_size=18, color="#43CC37")
        self.add_widget(self.zal)
        progress_bar = ProgressBar(pos=(105,190),max=round(len(self.tab)/3), value=self.dob,size=(200,200))
        self.add_widget(progress_bar)
        self.cofnij(self)
        self.button = Button(pos=(77, 110), size=(250, 30), text="Pokaż błędy!", on_press=self.zle_wpisane, bold=True,
                             background_color='#FF0000', color='#FFFFFF')
        self.add_widget(self.button)
        self.dob = 0
        self.zle = 0

    def zle_wpisane(self,app):
        self.clear_widgets()
        self.szablon(self)

        self.word = Label(text="Polski", pos=(50, 380), font_size=18, bold=True, color="#F50B00")
        self.add_widget(self.word)
        self.word = Label(text="Angielski", pos=(250, 380), font_size=18, bold=True, color="#F50B00")
        self.add_widget(self.word)

        i = 1
        x = 360
        y = 370
        while i <= len(self.tab_zle):
            self.ins = Label(text=self.tab_zle[i], pos=(50, x), color="#00FFCE")
            self.add_widget(self.ins)
            self.ins_2 = Label(text=self.tab_zle[i + 1], pos=(250, x), color="#00FFCE")
            self.add_widget(self.ins_2)
            i += 3
            x -= 20
        self.tab_zle = []
        self.cofnij(self)

    def __init__(self, **kwargs):
        super(Aplication, self).__init__(**kwargs)

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="mywords"
        )
        self.dob = 0
        self.zle = 0
        self.tab = []
        self.tab_zle = []
        self.tab_dobrze = []
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM `slowa`")
        myresult = mycursor.fetchall()
        for x in myresult:
            for i in x:
                self.tab.append(i)
        mydb.close()

        self.szablon(self)
# ------------------------------Logowanie
        self.img = Image(source="img/kwadrat.png", pos=(28, 80), size=(350, 350), opacity=0.5)
        self.add_widget(self.img)
        self.pop = Label(text="Logowanie...", pos=(150, 310), font_size=30, bold=True)
        self.add_widget(self.pop)
        self.zal = Label(text="Login", pos=(150, 260), font_size=15, bold=True)
        self.add_widget(self.zal)
        self.user_log = TextInput(pos=(85, 254), size=(236, 42), font_size=18, multiline=False,background_color='#182A38', foreground_color='#FFFFFF', halign='center',padding_y=(10, 10))
        self.add_widget(self.user_log)
        self.zal = Label(text="Hasło", pos=(150, 187), font_size=15, bold=True,valign='middle',halign='center')
        self.add_widget(self.zal)
        self.user_has = TextInput(pos=(85, 184), size=(236, 42), font_size=18, multiline=False,background_color='#182A38', foreground_color='#FFFFFF', halign='center',padding_y=(10, 10))
        self.add_widget(self.user_has)
        self.img = Image(source="img/prz.png", pos=(-30, -25), size=(350, 350))
        self.add_widget(self.img)
        self.button_zaloguj = Button(pos=(85, 130),opacity=0, size=(113, 37), bold=True, on_press=self.logowanie,background_color='#00FFCE', background_normal="", color='#000000')
        self.add_widget(self.button_zaloguj)
        self.zal = Label(text="Zaloguj się!", pos=(95, 100), font_size=13, bold=True)
        self.add_widget(self.zal)
        self.img = Image(source="img/prz.png", pos=(90, -25), size=(350, 350))
        self.add_widget(self.img)
        self.button_nowe = Button(pos=(210, 130),opacity=0, size=(113, 37),bold=True,background_color='#00FFCE', background_normal="", color='#000000')
        self.add_widget(self.button_nowe)
        self.zal = Label(text="Stwórz konto!", pos=(215, 100), font_size=13, bold=True)
        self.add_widget(self.zal)
    def szablon(self,app):
#------------------------------Zdjęcie
        self.img = Image(source="img/planeta.jpg", pos=(28, 340), size=(350, 350))
        self.add_widget(self.img)
        self.zal = Label(text="Nauka słówek", pos=(150, 500), font_size=24)
        self.add_widget(self.zal)
        self.zal = Label(text="MyWords", pos=(150, 470),font_size=48, bold=True)
        self.add_widget(self.zal)
# ------------------------------Footer
        self.img = Image(source="img/footer.png", pos=(-25, -200), size=(450, 450))
        self.add_widget(self.img)
        self.zal = Label(text="MyWords.pl 2023", pos=(150, -20), font_size=15, bold=True)
        self.add_widget(self.zal)
    def logowanie(self, app):
        haslo = self.user_has.text
        login = self.user_log.text
        if "" == login and "" == haslo:
            self.clear_widgets()
            self.szablon(self)
# ------------------------------Tytuł
            self.kol = Label(text="Kolekcje", pos=(150, 360), color='#FFFFFF', font_size=40)
            self.add_widget(self.kol)
# ------------------------------Wypisanie kolekcji
            self.button = Button(pos=(77, 350), size=(250, 30), text="Moje słowka 1", bold=True, on_press=self.kolekcja_jeden, background_color='#51BBFF',color='#FFFFFF')
            self.add_widget(self.button)
            #self.button = Button(pos=(77, 390), size=(250, 50), text="Moje słowka 2", bold=True,on_press=self.kolekcja_dwa, background_color='#00FFCE', background_normal="", color='#000000')
            #self.add_widget(self.button)

            #self.button = Button(pos=(77, 70), size=(250, 50), text="Dodaj Kolekcje", bold=True, background_color='#BA0F2F', background_normal="", color='#000000')
            #self.add_widget(self.button)

        else:
            sss = "Zły login lub hasło"
            self.pop.text = "Niepoprawne logowanie!"
            self.pop.font_size=23
            self.pop.color='#FF0000'
    def kolekcja_jeden(self, app):
        self.clear_widgets()
        self.szablon(self)
        # ---------------------Nazwa
        self.kol = Label(text="Moje słowa 1", pos=(150, 360), color='#FFFFFF', font_size=40)
        self.add_widget(self.kol)
        # ---------------------Słownik
        self.button = Button(pos=(77, 350), size=(250, 30), text="Słownik:",on_press=self.slownik, bold=True, background_color='#51BBFF',
                              color='#FFFFFF')
        self.add_widget(self.button)
        # ---------------------Tryb nauki
        self.button = Button(pos=(77, 310), size=(250, 30), text="Trub Nauki!",on_press=self.nauka, bold=True,
                            background_color='#51BBFF', color='#FFFFFF')
        self.add_widget(self.button)
        # ---------------------Cofnij
        self.cofnij(self)
    def nauka(self, app):
        self.i = 1
        self.x = 0
        self.tab_zle = []
        self.tab_dobrze = []
        self.clear_widgets()
        self.szablon(self)
# -----------------------------Tytuł
        self.kol = Label(text="Trub nauki", pos=(150, 360), color='#FFFFFF', font_size=30)
        self.add_widget(self.kol)
        self.kol = Label(text="Naciśnij przycisk 'Następne pytanie' aby zacząć", pos=(150, 330), color='43CC37', font_size=15)
        self.add_widget(self.kol)

        self.footer = Label(text="", pos=(150, 400), bold=True, color="#00FFCE")
        self.add_widget(self.footer)

        self.button = Button(pos=(77, 110), size=(250, 30), text="Następne pytanie!",on_press=self.nxt ,on_release=self.sprawdz, bold=True, background_color='#BA0F2F', color='#FFFFFF')
        self.add_widget(self.button)

        self.cofnij(self)
    def cofnij(self,app):
        self.button = Button(pos=(77, 70), size=(250, 30), text="Cofnij!", on_press=self.logowanie, bold=True,
                             background_color='#FF0000', color='#FFFFFF')
        self.add_widget(self.button)
    def sprawdz(self,app):
        if len(self.tab_zle) + len(self.tab_dobrze) != len(self.tab):
            self.button_spr = Button(pos=(77, 110), size=(250, 30), text="Sprawdz!",on_press=self.spr,  bold=True, background_color='#BA0F2F', color='#FFFFFF')
            self.add_widget(self.button_spr)
        else:
            self.koniec_nauka()
    def nxt(self, app):
        self.clear_widgets()
        self.szablon(self)
        if self.i < len(self.tab):
            self.kol = Label(text="Przetłumacz słowo!", pos=(150, 360), color='#FFFFFF', font_size=20)
            self.add_widget(self.kol)
            self.word = Label(text=self.tab[self.i], pos=(150, 330),font_size=18, bold=True, color="#FFFFFF")
            self.add_widget(self.word)
            self.word_ang = TextInput(pos=(85, 324), size=(236, 42), font_size=18, multiline=False,background_color='#182A38', foreground_color='#FFFFFF', halign='center',padding_y=(10, 10))
            self.add_widget(self.word_ang)
            self.i += 3
            self.x += 3
            self.button = Button(pos=(77, 110), size=(250, 30), text="Następne pytanie!",on_press=self.nxt ,on_release=self.sprawdz, bold=True, background_color='#BA0F2F', color='#FFFFFF')
            self.add_widget(self.button)
            self.remove_widget(self.button)
            self.cofnij(self)
    def spr(self,app):

        if self.i <= len(self.tab)+1:
            if self.tab[self.i -2] == self.word_ang.text:
                self.kol = Label(text="Dobra odpowiedz!", pos=(150, 250), color='43CC37', font_size=18)
                self.add_widget(self.kol)
                self.tab_dobrze.append(self.tab[self.i - 4])
                self.tab_dobrze.append(self.tab[self.i - 3])
                self.tab_dobrze.append(self.tab[self.i - 2])
                self.dob = self.dob + 1
            if self.tab[self.i - 2] != self.word_ang.text:
                self.kol = Label(text="Źle poprawna odpowiedz to: " + self.tab[self.i -2], pos=(150, 250), color='#FF0000', font_size=18)
                self.add_widget(self.kol)
                self.tab_zle.append(self.tab[self.i - 4])
                self.tab_zle.append(self.tab[self.i - 3])
                self.tab_zle.append(self.tab[self.i - 2])
                self.zle +=1
        self.button = Button(pos=(77, 110), size=(250, 30), text="Następne pytanie!", on_press=self.nxt,
                             on_release=self.sprawdz, bold=True, background_color='#337202', color='#FFFFFF')
        self.add_widget(self.button)
        self.remove_widget(self.button_spr)
        self.cofnij(self)

    def slownik(self, app):
        self.clear_widgets()
        self.szablon(self)

        self.word = Label(text="Polski", pos=(35, 380), font_size=18, bold=True, color="#F50B00")
        self.add_widget(self.word)
        self.word = Label(text="Angielski", pos=(165, 380), font_size=18, bold=True, color="#F50B00")
        self.add_widget(self.word)

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
        i = 1
        x = 389
        self.t = 0
        while i <= len(self.tab):
            self.inside = GridLayout(cols=3, pos=(25, x), size=(350, 20))
            self.ins = Label(text=self.tab[i], color="#00FFCE")
            self.inside.add_widget(self.ins)
            self.ins_2 = Label(text=self.tab[i + 1], color="#00FFCE")
            self.inside.add_widget(self.ins_2)
            self.button_usun = Button(text="Usuń", background_color='#FF0000', color='#FFFFFF',size_hint=(0.8,1), bold=True, on_press=self.usun_ele)
            self.inside.add_widget(self.button_usun)
            self.add_widget(self.inside)
            self.t +=1
            i += 3
            x -= 20

        self.inside = GridLayout(cols=3, pos=(25, 145), size=(350, 40))
        self.textinput_pl = TextInput(text="PL", font_size=16, background_color='#182A38', foreground_color='#FFFFFF',halign='center', multiline=False, padding_y=(10, 10), size_hint=(0.5, 1))
        self.inside.add_widget(self.textinput_pl)
        self.textinput_ang = TextInput(text="ANG", font_size=16, background_color='#182A38', foreground_color='#FFFFFF', halign='center', multiline=False, padding_y=(10, 10), size_hint=(0.5, 1))
        self.inside.add_widget(self.textinput_ang)
        self.add_widget(self.inside)
        self.button = Button(text="Dodaj słowo:", background_color='#43CC37', color='#FFFFFF', pos=(25, 110), size=(350, 30),
                             on_press=self.slownik_dodaj)
        self.add_widget(self.button)

        self.cofnij(self)
    def usun_ele(self,app):
        self.indexy(self)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mywords"
        )
        mycursor = mydb.cursor()
        val = self.t
        sql = "DELETE FROM `slowa` WHERE `slowa`.`Id` = %s;"

        mycursor.execute(sql, (val,))
        mydb.commit()


    def indexy(self, app):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="mywords"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM `slowa`")
        myresult = mycursor.fetchall()
        for i, x in enumerate(myresult):
            sql = "UPDATE `slowa` SET `id` = %s WHERE `id` = %s;"
            mycursor.execute(sql, (i + 1, x[0]))
        mydb.commit()
        mydb.close()

    def slownik_dodaj(self,app):
        self.indexy(self)
        a = self.textinput_ang.text
        b = self.textinput_pl.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mywords"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO slowa (pl, ang) VALUES (%s, %s)"
        val = (str(b), str(a))
        mycursor.execute(sql, val)
        mydb.commit()

class MyWords(App):
    def build(self):
        return Aplication()

