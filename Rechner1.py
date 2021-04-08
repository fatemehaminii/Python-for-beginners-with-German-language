# Bibliothek importieren 
from tkinter import *
from tkinter import messagebox
import tkinter


# ========================== Einstellungen ========================

# Ein Fenster bauen
Fenster = Tk()
# die Länge und Breite des Fensters festsetzen
Fenster.geometry('330x170')
# Titel zum Fenster hinzufügen
Fenster.title('Rechner')
# Fenstergrösse beschränken 
Fenster.resizable(width=False, height=False)
# Hintergrundfarbe des Fensters wählen
Farbe = 'gray'
Fenster.configure(bg=Farbe)

# ========================== Variablen ==========================

# String fassen
Nummer1 = StringVar()
Nummer2 = StringVar()
Ergebnis = StringVar()

# ========================== Rahmens ==========================


Der_erste_Frame = Frame(Fenster, width=300, height=50, bg=Farbe)
Der_erste_Frame.pack(side=TOP)


Der_zweite_Frame = Frame(Fenster, width=300, height=50, bg=Farbe)
Der_zweite_Frame.pack(side=TOP)


Der_dritte_Frame = Frame(Fenster, width=300, height=50, bg=Farbe)
Der_dritte_Frame.pack(side=TOP)


Der_vierte_Frame = Frame(Fenster, width=300, height=50, bg=Farbe)
Der_vierte_Frame.pack(side=TOP)


# ========================== Funktionen ==========================


# Funktion zur Anzeige von Fehlern
def errorMsg(ms):
    if ms == 'Error':
        tkinter.messagebox.showerror('Error', 'Irgenwas stimmt nicht')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror(
            'Division Error', 'Kann nicht durch Null geteilt werden')



# Funktion zum addieren
def addieren():
    try:
        value = float(Nummer1.get()) + float(Nummer2.get())
        Ergebnis.set(value)
    except:
        errorMsg('Error')



# Funktion zum subtrahieren
def subtrahieren():
    try:
        value = float(Nummer1.get()) - float(Nummer2.get())
        Ergebnis.set(value)
    except:
        errorMsg('Error')



# Funktion zum multiplizieren
def multiplizieren():
    try:
        value = float(Nummer1.get()) * float(Nummer2.get())
        Ergebnis.set(value)
    except:
        errorMsg('Error')



# Funktion zum dividieren
def dividieren():
    if Nummer2.get() == '0':
        errorMsg('division zero error')
    elif Nummer2.get() != '0':
        try:
            value = float(Nummer1.get()) / float(Nummer2.get())
            Ergebnis.set(value)
        except:
            errorMsg('Error')


# ========================== Knöpfe ==========================

# Ein Knopf zum addieren
Knopf_plus = Button(Der_dritte_Frame, text="+", width=6,
                    highlightbackground=Farbe, command=lambda: addieren())
Knopf_plus.pack(side=LEFT, padx=5, pady=10)

# Ein Knopf zum subtrahieren
Knopf_minus = Button(Der_dritte_Frame, text="-", width=6,
                     highlightbackground=Farbe, command=lambda: subtrahieren())
Knopf_minus.pack(side=LEFT, padx=5, pady=10)

# Ein Knopf zum multiplizieren
Knopf_mul = Button(Der_dritte_Frame, text="*", width=6,
                   highlightbackground=Farbe, command=lambda: multiplizieren())
Knopf_mul.pack(side=LEFT, padx=5, pady=10)

# Ein Knopf zum dividieren
Knopf_div = Button(Der_dritte_Frame, text="/", width=6,
                   highlightbackground=Farbe, command=lambda: dividieren())
Knopf_div.pack(side=LEFT, padx=5, pady=10)


# ========================== Einträge und Labels ==========================

# Das Label für den ersten Eintrag
Label_Nummer_1 = Label(
    Der_erste_Frame, text='Bitte geben Sie die erste Zahl: ', bg=Farbe)
Label_Nummer_1.pack(side=LEFT, pady=5, padx=5)

# Erster Eintrag für die erste Zahl
Eintrag_1 = Entry(Der_erste_Frame, width=15,
                  highlightbackground=Farbe, textvariable=Nummer1)
Eintrag_1.pack(side=LEFT)

# Das Label für den zweiten Eintrag
Label_Nummer_2 = Label(
    Der_zweite_Frame, text='Bitte geben Sie die zweite Zahl: ', bg=Farbe)
Label_Nummer_2.pack(side=LEFT, pady=5, padx=5)

# Zweiter Eintrag für die zweite Zahl
Eintrag_2 = Entry(Der_zweite_Frame, width=15,
                  highlightbackground=Farbe, textvariable=Nummer2)
Eintrag_2.pack(side=LEFT, padx=10, pady=10)

# Das Label für das Ergebnis
Erg = Label(Der_vierte_Frame, text='Result: ', bg=Farbe)
Erg.pack(side=LEFT, pady=10, padx=10)

# Dritter Eintrag für das Ergebnis
Eintrag_Ergebnis = Entry(
    Der_vierte_Frame, width=20, highlightbackground=Farbe, textvariable=Ergebnis)
Eintrag_Ergebnis.pack(side=LEFT, padx=10, pady=10)



# ein Loop für das Programm erstellen
Fenster.mainloop()
