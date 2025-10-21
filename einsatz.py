import tkinter as tk
import os 
import json
import datetime
from params import Params

class Einsatz:

    def __init__(self, root, par):
        self.name = ""
        self.location = ""
        self.description = ""
        self.start_time = "0:00"
        self.filename = ""

        self.par = par

        self.input_window_einsatz(root)

        
    def input_window_einsatz(self,root):
        """ Creates a toplevel frame to input information about the einsatz that should be created.
        """
        self.top = tk.Toplevel(root)
        self.top.config(bg=self.par.colorTheme)
        #self.top.geometry("500x400")
        self.top.title("Neuen Einsatz anlegen")
        self.top.lift(root)

        tk.Label(self.top, text="Name des Einsatzes:", font=("Arial", 9), bg=self.par.colorTheme).grid(row=0, column=0, sticky="W", padx=5, pady=5)
        self.tname = tk.Entry(self.top, font=("Arial", 9), bg=self.par.colorTheme)
        self.tname.grid(row=0, column=1, padx=5, pady=5, sticky="W")


        tk.Label(self.top, text="Einsatzort:", font=("Arial", 9), bg=self.par.colorTheme).grid(row=1, column=0, sticky="W", padx=5, pady=5)
        self.tlocation = tk.Entry(self.top, font=("Arial", 9), bg=self.par.colorTheme)
        self.tlocation.grid(row=1, column=1, padx=5, pady=5, sticky="W")

        tk.Label(self.top, text="Beschreibung:", font=("Arial", 9), bg=self.par.colorTheme).grid(row=2, column=0, sticky="W", padx=5, pady=5)
        self.tdescription = tk.Text(self.top, font=("Arial", 9), bg=self.par.colorTheme, wrap="word", padx=5, pady=5, undo=True)
        self.tdescription.grid(row=2, column=1, padx=5, pady=5, sticky="W")

        tk.Label(self.top, text="Startzeit:", font=("Arial", 9), bg=self.par.colorTheme).grid(row=3, column=0, sticky="W", padx=5, pady=5)
        self.tstart_time = tk.Entry(self.top, font=("Arial", 9), bg=self.par.colorTheme)
        self.tstart_time.grid(row=3, column=1, padx=5, pady=5, sticky="W")

        self.new_einsatz = tk.Button(self.top, text="Neuen Einsatz erstellen", font=("Arial", 9), background="YELLOW",
                                     command= lambda: self.create_new_einsatz(self.top))
        self.new_einsatz.grid(row=4, column=0, padx=5, pady=10, sticky="W")

        root.wait_window(self.top)

    def create_new_einsatz(self, toplevel):
        """Execution function when button is pressed in the toplevel input frame for creating an einsatz.
        Creates a json file where information about the einsatz and later the fahrzeuge are stored. 
        """
        self.name = self.tname.get()
        self.name = self.name.replace(" ", "")
        self.location = self.tlocation.get()
        self.description = self.tdescription.get("1.0", tk.END)
        self.start_time = self.tstart_time.get()

        if Params.is_valid(self.name) and Params.is_valid(self.location):
            if self.name != "" and self.location != "":

                data = {
                    "einsatz_name": self.name,
                    "location": self.location,
                    "description": self.description,
                    "start_time": self.start_time,
                    "fahrzeuge": []
                }
                
                time = datetime.datetime.now().isoformat()[:16]
                self.filename = f"{self.name}_{time[:10]}_{time[11:13]}{time[14:16]}.json"

                file_path = os.path.join("data", self.filename)
                os.makedirs("data", exist_ok=True)

                if not os.path.exists(file_path):
                    # execution only if path does not exist already
                    with open(file_path, 'w') as f:
                        json.dump(data, f)
                    
                    self.top.destroy()
                else:
                    tk.Label(toplevel, text="Einsatznamen ändern!", font=("Arial", 9), bg=self.par.colorTheme).grid(row=4, column=1, padx=5, pady=10, sticky="W")
            else:
                tk.Label(toplevel, text="Einsatzdaten ergänzen!", font=("Arial", 9), bg=self.par.colorTheme).grid(row=4, column=1, padx=5, pady=10, sticky="W")
        else:
            tk.Label(toplevel, text="Keine Sonderzeichen oder Umlaute!", font=("Arial", 9), bg=self.par.colorTheme).grid(row=4, column=1, padx=5, pady=10, sticky="W")