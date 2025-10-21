import tkinter as tk
import os 
import json
import datetime

class Fahrzeug:

    def __init__(self, root, par, einsatz_name, einsatz_filename):

        self.start_time = datetime.datetime.now().isoformat()[:16]
        self.end_time = ""

        self.status = tk.StringVar()

        self.filename = einsatz_filename

        self.par = par

        self.input_window_fahrzeug(root)
        

    def input_window_fahrzeug(self, root, modify_fahrzeug=False):
        """Creates toplevel input window to create a new fahrzeug.
        If modify_fahrzeug == True method is used to display already existing fahrzeug.
        """
        top2 = tk.Toplevel(root)
        top2.geometry("350x400")
        top2.config(bg = self.par.colorTheme)
        if modify_fahrzeug == False:
            top2.title("Neues Fahrzeug hinzufügen")
        else:
            top2.title("Fahrzeug bearbeiten")
        top2.lift(root)

        tk.Label(top2, text="Kennzeichen:", background=self.par.colorTheme).grid(row=0, column=0, sticky="W", padx=5, pady=5)
        tkennzeichen = tk.Entry(top2)
        tkennzeichen.config(background=self.par.colorTheme)
        tkennzeichen.grid(row=0, column=1, padx=5, pady=5, sticky="W")

        tk.Label(top2, text="BOS-Funk:", background=self.par.colorTheme).grid(row=1, column=0, sticky="W", padx=5, pady=5)
        tfunkruf = tk.Entry(top2)
        tfunkruf.config(background=self.par.colorTheme)
        tfunkruf.grid(row=1, column=1, padx=5, pady=5, sticky="W")

        tk.Label(top2, text="HIORG:", background=self.par.colorTheme).grid(row=2, column=0, sticky="W", padx=5, pady=5)
        thiorg = tk.Entry(top2)
        thiorg.config(background=self.par.colorTheme)
        thiorg.grid(row=2, column=1, padx=5, pady=5, sticky="W")

        tk.Label(top2, text="Kontaktperson Name:", background=self.par.colorTheme).grid(row=3, column=0, sticky="W", padx=5, pady=5)
        tcontact_name = tk.Entry(top2)
        tcontact_name.config(background=self.par.colorTheme)
        tcontact_name.grid(row=3, column=1, padx=5, pady=5, sticky="W")

        tk.Label(top2, text="Kontaktperson Telefon:", background=self.par.colorTheme).grid(row=4, column=0, sticky="W", padx=5, pady=5)
        tcontact_phone = tk.Entry(top2)
        tcontact_phone.config(background=self.par.colorTheme)
        tcontact_phone.grid(row=4, column=1, padx=5, pady=5, sticky="W")

        tk.Label(top2,text="Transportkapazität", background=self.par.colorTheme).grid(row=5, column=0, sticky="W", padx=5, pady=20)

        fahrzeug_types = self.par.fahrzeugTypen
        selected_ttyp = tk.StringVar(value=fahrzeug_types[0]) # default
        tk.Label(top2, text="Fahrzeugtyp", background=self.par.colorTheme).grid(row=6, column=0, sticky="W", padx=5, pady=5)
        m = tk.OptionMenu(top2, selected_ttyp, *fahrzeug_types) #* selectes all elements of it --> each element has to be a parameter
        m.grid(row=6, column=1, padx=5, pady=5, sticky="W")

        tk.Label(top2, text="liegend:", background=self.par.colorTheme).grid(row=7, column=0, sticky="W", padx=5, pady=5)
        ttrsp_liegend = tk.Entry(top2)
        ttrsp_liegend.config(background=self.par.colorTheme)
        ttrsp_liegend.grid(row=7, column=1, padx=5, pady=5, sticky="W")

        tk.Label(top2, text="sitzend:", background=self.par.colorTheme).grid(row=8, column=0, sticky="W", padx=5, pady=5)
        ttrsp_sitzend = tk.Entry(top2)
        ttrsp_sitzend.config(background=self.par.colorTheme)
        ttrsp_sitzend.grid(row=8, column=1, padx=5, pady=5, sticky="W")


        if modify_fahrzeug == False:
            new_fahrzeug = tk.Button(top2, text="Fahrzeug hinzufügen", background="YELLOW",
                                    command= lambda: self.create_or_change_fahrzeug(top2, tkennzeichen, tfunkruf, thiorg, tcontact_name, tcontact_phone, selected_ttyp, ttrsp_liegend, ttrsp_sitzend))
            new_fahrzeug.grid(row=9, column=0, padx=5, pady=10, sticky="W")
        else:
            tkennzeichen.insert(0, self.kennzeichen)
            tfunkruf.insert(0, self.funkruf)
            thiorg.insert(0, self.hiorg)
            tcontact_name.insert(0, self.contact_name)
            tcontact_phone.insert(0, self.contact_phone)
            selected_ttyp.set(value=self.typ)
            ttrsp_liegend.insert(0, self.trsp_liegend)
            ttrsp_sitzend.insert(0, self.trsp_sitzend)

            new_fahrzeug = tk.Button(top2, text="Bearbeitung speichern", background="YELLOW",
                                        command= lambda: self.create_or_change_fahrzeug(top2, tkennzeichen, tfunkruf, thiorg, tcontact_name, tcontact_phone, selected_ttyp, ttrsp_liegend, ttrsp_sitzend))
            new_fahrzeug.grid(row=9, column=0, padx=5, pady=10, sticky="W")

        root.wait_window(top2)

   

    def create_or_change_fahrzeug(self, top2, tkennzeichen, tfunkruf, thiorg, tcontact_name, tcontact_phone, selected_ttyp, ttrsp_liegend, ttrsp_sitzend):
        """Triggered by a button in the fahrzeug input window either create or change the fahrzeug information.
        """
        
        complete = True # method should not execute top2.destroy() because then emtpy car exist, which leads to problems
        
        self.kennzeichen = tkennzeichen.get() 
        self.funkruf = tfunkruf.get()
        self.hiorg = thiorg.get()
        self.contact_name = tcontact_name.get()
        self.contact_phone = tcontact_phone.get()
        self.typ = selected_ttyp.get()
        self.trsp_liegend = ttrsp_liegend.get()
        self.trsp_sitzend = ttrsp_sitzend.get()

        if self.kennzeichen == "" or self.funkruf == "":
            complete = False 

        if complete == True:
            top2.destroy()
        else:
            tk.Label(top2, text="Angaben fehlen!", background=self.par.colorTheme).grid(row=9, column=1, padx=5, pady=10, sticky="W")
        

    def show_fahrzeug_information(self, root):
        """Display information about a car. Triggered by the "Info" button of the table. 
        """

        # creates a pop-up which shows all information with respect to a fahrzeug
        top = tk.Toplevel()
        top.config(background=self.par.colorTheme)
        top.geometry("350x400")
        top.title(f"{self.kennzeichen} / {self.funkruf}")
        top.lift(root)

        tk.Label(top, text="Kennzeichen", background=self.par.colorTheme).grid(row=0, column=0, sticky="W", padx=5, pady=5)
        tk.Label(top, text=self.kennzeichen,background=self.par.colorTheme).grid(row=0, column=1, sticky="W", padx=5, pady=5)
        tk.Label(top, text="Funkruf", background=self.par.colorTheme).grid(row=1, column=0, sticky="W", padx=5, pady=5)
        tk.Label(top, text=self.funkruf, background=self.par.colorTheme).grid(row=1, column=1, sticky="W", padx=5, pady=5)
        tk.Label(top, text=f"Hiorg", background=self.par.colorTheme).grid(row=2, column=0, sticky="W", padx=5, pady=5)
        tk.Label(top, text=self.hiorg, background=self.par.colorTheme).grid(row=2, column=1, sticky="W", padx=5, pady=5)
        tk.Label(top, text="Typ", background=self.par.colorTheme).grid(row=3, column=0, sticky="W", padx=5, pady=5)
        tk.Label(top, text=self.typ, background=self.par.colorTheme).grid(row=3, column=1, sticky="W", padx=5, pady=5)
        tk.Label(top, text="Kontaktperson", background=self.par.colorTheme).grid(row=4, column=0, sticky="W", padx=5, pady=5)
        tk.Label(top, text=self.contact_name, background=self.par.colorTheme).grid(row=4, column=1, sticky="W", padx=5, pady=5)
        tk.Label(top, text="Telefon", background=self.par.colorTheme).grid(row=5, column=0, sticky="W", padx=5, pady=5)
        tk.Label(top, text=self.contact_phone, background=self.par.colorTheme).grid(row=5, column=1, sticky="W", padx=5, pady=5)
        tk.Label(top, text="Plätze liegend", background=self.par.colorTheme).grid(row=6, column=0, sticky="W", padx=5, pady=5)
        tk.Label(top, text=self.trsp_liegend, background=self.par.colorTheme).grid(row=6, column=1, sticky="W", padx=5, pady=5)
        tk.Label(top, text="Plätze sitzend", background=self.par.colorTheme).grid(row=7, column=0, sticky="W", padx=5, pady=5)
        tk.Label(top, text=self.trsp_sitzend, background=self.par.colorTheme).grid(row=7, column=1, sticky="W", padx=5, pady=5)
        tk.Label(top, text=f"In Dienst seit {self.start_time[:10]} um {self.start_time[11:]} Uhr", background=self.par.colorTheme).grid(row=8, column=0, sticky="W", padx=5, pady=5)
        
        modify = tk.Button(top, text="Fahrzeug bearbeiten", command= lambda: (top.destroy(), self.input_window_fahrzeug(root, modify_fahrzeug=True)))
        modify.grid(row=9, column=0, sticky="W", padx=5, pady=10)


    @staticmethod
    def write_all_fahrzeuge(einsatz, fahrzeuge):
        """Stores list of fahrzeug objects into the json file by overwriting.
        """
        fahrzeug_list = []

        for fahrzeug in fahrzeuge:
            data = {
                "kennzeichen": fahrzeug.kennzeichen,
                "funkruf": fahrzeug.funkruf,
                "hiorg": fahrzeug.hiorg,
                "contact_name": fahrzeug.contact_name,
                "contact_phone": fahrzeug.contact_phone,
                "typ": fahrzeug.typ, 
                "trsp_liegend": fahrzeug.trsp_liegend,
                "trsp_sitzend": fahrzeug.trsp_sitzend,
                "start_time": fahrzeug.start_time,
                "end_time": fahrzeug.end_time
            }
            fahrzeug_list.append(data)
        
        file_path = os.path.join("data", einsatz.filename)

        with open(file_path, 'r') as f:
            loaded_data = json.load(f)

        loaded_data["fahrzeuge"] = fahrzeug_list

        with open(file_path, 'w') as f:
            json.dump(loaded_data, f)
    
        print("Done")