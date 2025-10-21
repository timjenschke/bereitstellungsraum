import tkinter as tk
from tkinter import filedialog as fd
from scrollableFrameContainer import ScrollableFrameContainer
from dashboard import Dashboard
from params import Params
import re
import json

class Start:

    def __init__(self):
        """Creates program start screen where user can decide between creating new einsatz and loading old one. 
        """
        self.startscreen = tk.Tk()
        screenheight=700
        screenwidth=350
        #self.startscreen.geometry(f"{screenheight}x{screenwidth}")
        self.startscreen.title("Programmstart")

        self.back_color = "#e6fbf9"

        self.newEinsatz = tk.Frame(self.startscreen, height=screenheight//2, width=screenwidth//2)
        self.newEinsatz.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.oldEinsatz = tk.Frame(self.startscreen, background=self.back_color, height=screenheight//2, width=screenwidth//2)
        self.oldEinsatz.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # NEW EINSATZ Framework

        tk.Label(self.newEinsatz, text="Neuen Einsatz anlegen: Parameter", font=("Arial", 16, "bold")
                 ).grid(row=0, column=0, padx=5, pady=5, sticky="W", columnspan=2)
        tk.Label(self.oldEinsatz, text="Alten Einsatz laden", font=("Arial", 16, "bold"), bg=self.back_color
                 ).grid(row=0, column=0, padx=5, pady=5, sticky="W", columnspan=2)
        
        tk.Label(self.newEinsatz, text="Sie können hier Parameter ändern, die Nutzeroberfläche und Einsatzmöglichkeiten beeinflussen.",
                 font=("Arial", 10)).grid(row=1, padx=5, pady=5, sticky="W", columnspan=5)
        tk.Label(self.oldEinsatz, text="Sie haben einen alten Einsatz den Sie sich noch einmal anschauen wollen?",
                 font=("Arial", 10), bg=self.back_color).grid(row=1, column=0, padx=5, pady=5, sticky="W", columnspan=5)
        
        tk.Label(self.newEinsatz, text="Hintergrundfarbe", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=5, pady=10, sticky="W")
        self.color = tk.Entry(self.newEinsatz) # self because used for loading old einsatz
        self.color.insert(0, "#fefefb")
        self.color.grid(row=2, column=1, padx=5, pady=5, sticky="W")

        tk.Label(self.newEinsatz, text="Fahrzeugtypen", font=("Arial", 10, "bold")).grid(row=3, column=0, padx=5, pady=10, sticky="W")
        fahrzeug_typs = tk.Entry(self.newEinsatz, width=70)
        fahrzeug_typs.insert(0, "KTW,MTW,RTW,GW-San,ELW,BTW,PKW,LKW")
        fahrzeug_typs.grid(row=3, column=1, padx=5, pady=10, sticky="W")
        tk.Label(self.newEinsatz, text="Diese Fahrzeugtypen sind am Einsatz beteiligt. Erster Typ gnaz links ist der default.", 
                 font=("Arial", 8)).grid(row=4, padx=5, pady=5, sticky="W", columnspan=5)
        
        tk.Label(self.newEinsatz, text="Sichtbare Fahrzeuginformationen", font=("Arial", 10, "bold")).grid(row=5, column=0, padx=5, pady=10, sticky="W")
        shown_features = tk.Entry(self.newEinsatz, width=70)
        shown_features.insert(0, "kennzeichen,funkruf,hiorg,typ,trsp_liegend,trsp_sitzend")
        shown_features.grid(row=5, column=1, padx=5, pady=10, sticky="W")
        tk.Label(self.newEinsatz, text="Diese Fahrzeugeigenschaften werden in der Tabelle sichtbar sein. Zur Auswahl stehen: ", 
                 font=("Arial", 8)).grid(row=6, padx=5, pady=0, sticky="W", columnspan=5)
        tk.Label(self.newEinsatz, text="kennzeichen, funkruf, hiorg, contact_name, contact_phone, typ, trsp_liegend, trsp_sitzend, start_time", 
                 font=("Arial", 8)).grid(row=7, padx=5, pady=0, sticky="W", columnspan=5)

        tk.Label(self.newEinsatz, text="Bezeichnung", font=("Arial", 10, "bold")).grid(row=8, column=0, padx=5, pady=10, sticky="W")
        shown_features_name = tk.Entry(self.newEinsatz, width=70)
        shown_features_name.insert(0, "Kennzeichen,Funk,Hiorg,Typ,Trsp Liegend,Trsp Sitzend")
        shown_features_name.grid(row=8, column=1, padx=5, pady=10, sticky="W")
        tk.Label(self.newEinsatz, text="So werden obige Eigenschaften mit Namen genannt. Frei wählbar in chronologischer Reihenfolge", 
                 font=("Arial", 8)).grid(row=9, padx=5, pady=0, sticky="W", columnspan=5)
        
        tk.Label(self.newEinsatz, text="Status", font=("Arial", 10, "bold")).grid(row=10, column=0, padx=5, pady=10, sticky="W")
        status_system = tk.Entry(self.newEinsatz, width=70)
        status_system.insert(0, "0,1,2,3,4,5,6,7,8,9")
        status_system.grid(row=10, column=1, padx=5, pady=10, sticky="W")
        tk.Label(self.newEinsatz, text="Wählen Sie ein Status-System für die Fahrzeuge. Frei wählbar", 
                 font=("Arial", 8)).grid(row=11, padx=5, pady=0, sticky="W", columnspan=5)
        
        tk.Label(self.newEinsatz, text="Status-Farben", font=("Arial", 10, "bold")).grid(row=12, column=0, padx=5, pady=10, sticky="W")
        status_colour = tk.Entry(self.newEinsatz, width=70)
        status_colour.insert(0, "#FFFFFF,#8FFA3D,#8FFA3D,#FF8F8F,#FF8F8F,#FFFFFF,#FFFFFF,#FF8F8F,#F3E883,#FFFFFF")
        status_colour.grid(row=12, column=1, padx=5, pady=10, sticky="W")
        tk.Label(self.newEinsatz, text="Jedem Status muss eine Farbe zugeordnet werden, welche in der Tabelle sichtbar ist.", 
                 font=("Arial", 8)).grid(row=13, padx=5, pady=0, sticky="W", columnspan=5)
        
        tk.Label(self.newEinsatz, text="Bitte beachten Sie unbedingt das gegebene Format!", 
                 font=("Arial", 10)).grid(row=14, padx=5, pady=20, sticky="W", columnspan=5)
        tk.Label(self.newEinsatz, text="Wenn Sie zufrieden mit den Voreinstellungen sind, können Sie auch direkt weitermachen.", 
                 font=("Arial", 10)).grid(row=15, padx=5, pady=0, sticky="W", columnspan=5)
        tk.Label(self.newEinsatz, text="Änderungen sind im Nachhinein nur noch bedingt möglich.", 
                 font=("Arial", 10)).grid(row=16, padx=5, pady=0, sticky="W", columnspan=5)

        tk.Button(self.newEinsatz, text="Weiter zu Einsatzinformationen", font= ("Arial", 10, "bold"), bg="yellow",
                  command= lambda: self.new_einsatz(self.color.get(), fahrzeug_typs.get(), shown_features.get(), shown_features_name.get(), status_system.get(), status_colour.get())
                  ).grid(row=19, padx=5, pady=10, sticky="W", columnspan=5)

        tk.Label(self.startscreen, text="\u00A9 Tim Jenschke Version 1.0", font=("Arial", 9)).grid(row=1, column=1, padx=5, pady=5, sticky="E")

        # OLD EINSATZ Framework

        tk.Label(self.oldEinsatz, text="Wählen Sie eine Datei zur Ansicht aus:", bg= self.back_color,
                 font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=0, sticky="W", columnspan=3)
        tk.Button(self.oldEinsatz, text= "Datei öffnen", font=("Arial", 10), bg="gray",
                 command=self.select_and_show_document).grid(row=3, column=0,padx=5, pady=0, sticky="NSEW")

        tk.Label(self.oldEinsatz, text="Bitte beachten Sie, dass nur Dateien mit der Endung .json zulässig sind. \n Alte Einsätze können nicht mehr bearbeitet werden.", bg= self.back_color,
                 font=("Arial", 10)).grid(row=5, column= 0, padx=5, pady=10, sticky="NW", rowspan=3)                                                  

        self.startscreen.mainloop()


    def check_valid_input(self, color, fahrzeug_typs, shown_features, shown_features_name, status_system, status_colour):
        """ Check if given user input to create meta parameters is valid for continuing. 
        """
        valid = True

        # check if colour is given in hexadecimal code
        if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color):
            self.error = tk.Label(self.newEinsatz, text="Überprüfen Sie ob die Hintergrundfarbe in Hexadecimal (z.B. #33ff22 / #3f2) gegeben ist.", fg="red",
                 font=("Arial", 10, "bold")).grid(row=18, padx=5, pady=10, sticky="W", columnspan=5)
            return False
        
        try:
            #check possibility to transfer to a list 
            list(fahrzeug_typs.split(","))
            shown_features = list(shown_features.split(","))
            shown_features_name = list(shown_features_name.split(","))
            status_system = list(status_system.split(","))
            status_colour = list(status_colour.split(","))
        except:
            self.error = tk.Label(self.newEinsatz, text="Überprüfen Sie, ob alle Wörter mit Komma getrennt sind. Nutzen Sie keine Leerzeichen.", fg="red",
                 font=("Arial", 10, "bold")).grid(row=18, padx=5, pady=0, sticky="W", columnspan=5)
            return False
        
        if valid:

            if len(shown_features) != len(shown_features_name):
                self.error = tk.Label(self.newEinsatz, text="Die Anzahl der sichtbaren Eigenschaften und deren Bezeichnungen muss übereinstimmen.", fg="red",
                 font=("Arial", 10, "bold")).grid(row=18, padx=5, pady=0, sticky="W", columnspan=5)
                return False
            
            if len(status_system) != len(status_colour):
                self.error = tk.Label(self.newEinsatz, text="Für jeden möglichen Status muss eine Farbe zugeordnet werden. Auch weiß muss angegeben werden.", fg="red",
                 font=("Arial", 10, "bold")).grid(row=18, padx=5, pady=0, sticky="W", columnspan=5)
                return False
            
            for c in status_colour:
                if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', c):
                    self.error = tk.Label(self.newEinsatz, text="Überprüfen Sie ob die Status-Farben in Hexadecimal (z.B. #33ff22 / #3f2) gegeben sind.", fg="red",
                     font=("Arial", 10, "bold")).grid(row=18, padx=5, pady=0, sticky="W", columnspan=5)
                    return False
        
            for typ in shown_features: 
                if typ not in ["kennzeichen", "funkruf", "hiorg", "contact_name", "contact_phone", "typ", "trsp_liegend", "trsp_sitzend", "start_time"]:
                    self.error = tk.Label(self.newEinsatz, text="Mindestens eine gewählte Fahrzeugeigenschaft existiert nicht. Rechtschreibung überprüfen.", fg="red",
                     font=("Arial", 10, "bold")).grid(row=18, padx=5, pady=0, sticky="W", columnspan=5)
                    return False 

        return True


    def new_einsatz(self, color, fahrzeug_typs, shown_features, shown_features_name, status_system, status_colour):
        "Runs a new einsatz. Loads dashboard with the given parameters."

        valid = self.check_valid_input(color, fahrzeug_typs, shown_features, shown_features_name, status_system, status_colour)

        if valid:

            fahrzeug_typs = list(fahrzeug_typs.split(","))
            shown_features = list(shown_features.split(","))
            shown_features_name = list(shown_features_name.split(","))
            status_system = list(status_system.split(","))
            status_colour = list(status_colour.split(","))

            par = Params(color, fahrzeug_typs, shown_features, shown_features_name, status_system, status_colour)

            dashboard = Dashboard(par, self.startscreen)
        
        else:
            tk.Label(self.newEinsatz, text="Eingaben sind fehlerhaft. Bitte überprüfen Sie ihre Angaben!", fg="red",
                 font=("Arial", 10, "bold")).grid(row=17, padx=5, pady=10, sticky="W", columnspan=5)


    def select_and_show_document(self):
        """ Enables user to select a json file from their disk containing an einsatz and load it. 
        """
        try:
            filename = fd.askopenfilename(
                title='Datei öffnen',
                initialdir='/Documents/',
                filetypes=[("JSON files", "*.json")])

            with open(filename, 'r') as f:
                loaded_data = json.load(f)

            #"einsatz_name": "2", "location": "osna", "description": "\n", "start_time": "", "fahrzeuge": []}
            einsatz_name = loaded_data["einsatz_name"]
            einsatz_location = loaded_data["location"]
            einsatz_description = loaded_data["description"]
            einsatz_start = loaded_data["start_time"] 
            fahrzeuge = loaded_data["fahrzeuge"]

            self.show_old_einsatz = tk.Toplevel(self.startscreen)
            self.show_old_einsatz.config(bg=self.color.get())
            size = f"{self.show_old_einsatz.winfo_screenwidth()}x{self.show_old_einsatz.winfo_screenheight()}"
            self.show_old_einsatz.geometry(size)
            self.show_old_einsatz.title(f"Alter Einsatz: {filename}")

            einsatz_infos= tk.Frame(self.show_old_einsatz, bg=self.color.get())
            einsatz_infos.pack(side="top", padx=5, pady=5, anchor="nw")
            tk.Label(einsatz_infos, text=f"Einsatzname: {einsatz_name} begonnen um {einsatz_start} Uhr.",font=("Arial",10), bg=self.color.get()
                    ).pack(side="top", padx=5, pady=5, anchor="nw")
            tk.Label(einsatz_infos, text= f"Einsatzort: {einsatz_location}", font=("Arial", 10), bg=self.color.get()
                    ).pack(side="top", padx=5, pady=5, anchor="nw")
            
            if einsatz_description != "\n":
                self.show_old_einsatz.update()
                description_frame = ScrollableFrameContainer(self.show_old_einsatz, self.color.get())
                description_frame.pack(side="top", padx=5, pady=5, anchor="nw")
                description = description_frame.scrollable_content_frame
                txt = tk.Text(description, wrap="word", font=("Arial", 10), bg=self.color.get(), height=8, borderwidth=0)
                txt.insert("1.0", einsatz_description)
                txt.config(state="disabled", bg=self.color.get())   # read-only
                txt.pack(side="top", padx=5, pady=5, anchor="nw", fill="both", expand=True)

            # crucial line: geometry() takes some while to adapt size, therefore when calling ScrollableFrameContainer()
            # the height of show_old_einsatz() is not properly apated, therefore default height=1 is taken! --> force update()
            self.show_old_einsatz.update()

            table_scroll_frame = ScrollableFrameContainer(self.show_old_einsatz, self.color.get()) # könnte zu Problemen führen, falls self.color bullshit
            table_scroll_frame.pack(side="top", padx=5, pady=5, anchor="nw")
            table = table_scroll_frame.scrollable_content_frame

            if len(fahrzeuge) > 0: 
            
                columns = len(fahrzeuge[0])
                keys = list(fahrzeuge[0].keys())
                labels = ["Kennzeichen", "Funk", "Hiorg","Kontakt Name", "Kontakt Tel", "Typ", "Trsp Liegend", "Trsp Sitzend", "Startzeit", "Endzeit"]

                for j, label in enumerate(labels):
                    
                    e = tk.Label(table, text=str(label),
                            font=("Arial", 12), background="GRAY",
                            borderwidth=1, relief="solid",
                            width=15)
                    e.grid(row=0, column=j, sticky="nsew")
            
                for i, fahrzeug in enumerate(fahrzeuge): 
                    for j in range(columns):
                            
                        e = tk.Label(table, text=str(fahrzeug[keys[j]]),
                                font=("Arial", 12), bg = "white",
                                borderwidth=1, relief="solid",
                                width=15)
                        e.grid(row=i+1, column=j, sticky="nsew")
        except:
            if hasattr(self, "show_old_einsatz"):
                self.show_old_einsatz.destroy()
            self.error = tk.Label(self.oldEinsatz, text="Datei kann nicht geladen werden, weil sie fehlerhaft ist.", bg= self.back_color, fg="red",
                 font=("Arial", 10)).grid(row=4, padx=5, pady=5, sticky="NW", columnspan=5)
            

    @staticmethod
    def is_valid(s, modus="all"):
        s = s.lower()

        for ch in s:
            code = ord(ch)

            if modus == "number":
                if not (48 <= code <= 57):  # only 0-9
                    return False

            elif modus == "letter":
                if not (97 <= code <= 122 or code == 95):  # only a-z or _
                    return False

            elif modus == "all":
                if not ((48 <= code <= 57) or (97 <= code <= 122) or code == 95):
                    return False

            else:
                raise ValueError("Invalid modus. Use 'number', 'letter', or 'all'.")

        return True


new = Start()
    