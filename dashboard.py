import tkinter as tk
from einsatz import Einsatz
from fahrzeug import Fahrzeug
import datetime
from scrollableFrameContainer import ScrollableFrameContainer
from pdf import PDF

class Dashboard():

    def __init__(self, params, start):
        """Creates the dashboard containing a frame for general information and buttons and the table frame which display all fahrzeuge.
        params: meta parameters changing appearance 
        start: meta information with respect to shown fahrzeuge
        """
        self.root = tk.Toplevel(start)

        self.par = params

        self.root.config(bg=self.par.colorTheme)
        size = f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}"
        self.root.geometry(size)
        self.root.title("Dashboard")
        
        self.einsatz = Einsatz(self.root, self.par)
        self.root.lift() # opposite: lower()

        self.genInformation_frame = tk.Frame(self.root)
        self.genInformation_frame.config(bg=self.par.colorTheme)
        self.genInformation_frame.pack(side="top", anchor="nw") #nw = north-west --> left corner

        tk.Label(self.genInformation_frame, text="Einsatz: ", background=self.par.colorTheme).grid(row=0, column=0, sticky="W", padx=5, pady=2)
        tk.Label(self.genInformation_frame, text=self.einsatz.name, background=self.par.colorTheme).grid(row=0, column=1, sticky="ew", padx=5, pady=2)
        tk.Label(self.genInformation_frame, text="Einsatzort: ", background=self.par.colorTheme).grid(row=1, column=0, sticky="W", padx=5, pady=2)
        tk.Label(self.genInformation_frame, text=self.einsatz.location, background=self.par.colorTheme).grid(row=1, column=1, sticky="ew", padx=5, pady=0)

        self.new_fahrzeug = tk.Button(self.genInformation_frame, text="Fahrzeug hinzufügen", background="GREEN", command=self.add_fahrzeug)
        self.new_fahrzeug.grid(row=0, column=3, padx=5, pady=2, sticky="ew") # ew strechtes is horizontally = towards the size of the cell

        self.delete_fahrzeuge = tk.Button(self.genInformation_frame, text="Fahrzeug löschen", background="RED", command=self.delete_fahrzeug)
        self.delete_fahrzeuge.grid(row=1, column=3, padx=5, pady=2, sticky="ew")

        self.update_button = tk.Button(self.genInformation_frame, text="Update", background=self.par.colorTheme, command=self.update_table)
        self.update_button.grid(row=1, column=4, padx=5, pady=2, sticky="ew")

        self.criteria = tk.StringVar(value="typ")
        sorting_criteria = tk.OptionMenu(self.genInformation_frame, self.criteria, "typ", "status")
        sorting_criteria.config(highlightthickness=0, relief="flat", bg = self.par.colorTheme)
        sorting_criteria.grid(row=0, column=4, padx=5, pady=2, sticky="nsew")

        safe_fahrzeuge = tk.Button(self.genInformation_frame, text="Alle Fahrzeuge speichern", background="GRAY",
                                   command = lambda: Fahrzeug.write_all_fahrzeuge(self.einsatz, self.fahrzeuge))
        safe_fahrzeuge.grid(row=0, column=5, padx=30, pady=2, sticky="ew")

        tk.Button(self.genInformation_frame, text="Export als pdf", font=("Arial",9),
                  command= lambda: PDF(self.table_frame, self.einsatz.filename, self.sort_fahrzeuge(self.criteria.get()))).grid(row=0, column=6, padx=30, pady=2, sticky="ew")

        end_einsatz = tk.Button(self.genInformation_frame, text = "Einsatz beenden", background="GRAY",
                                   command = self.finish_einsatz)
        end_einsatz.grid(row=0, column=7, padx=30, pady=2, sticky="ew")


        # container that holds the table and enables scrolling
        self.table_scroll_frame = ScrollableFrameContainer(self.root, self.par.colorTheme)
        self.table_scroll_frame.pack(side="top", padx=5, pady=5, anchor="nw")

        self.fahrzeuge = []

        # prevent opening dashboard if einsatz-input toplevel was just closed 
        if self.einsatz.name != "":
            self.root.mainloop()
        else:
            self.root.destroy()


    def add_fahrzeug(self): 
        """Adds a new fahrzeug to self.fahrzeuge and triggers table update. 

        """
        fahrzeug = Fahrzeug(self.root, self.par, self.einsatz.name, self.einsatz.filename)
        message = ""

        #prevent adding malformed fahrzeuge (e.g. due to closed fahrzeug input window)
        if hasattr(fahrzeug, "kennzeichen") and hasattr(fahrzeug, "funkruf"): 
            #prevent fahrzeuge with same kennzeichen or funkruf
            if fahrzeug.kennzeichen not in [x.kennzeichen for x in self.fahrzeuge]:
                if fahrzeug.funkruf not in [x.funkruf for x in self.fahrzeuge]:
                    self.fahrzeuge.append(fahrzeug)
                else:
                    message = f"Funkrufname {fahrzeug.funkruf} bereits vergeben. Das neue Fahrzeug wurde gelöscht. Erstelle ein neues mit einem anderen Funkrufnamen."
            else:
                message = f"Es existiert bereits ein Fahrzeug mit dem Kennzeichen {fahrzeug.kennzeichen}. Das neue Fahrzeug wurde gelöscht. Erstelle ein neues mit einem anderen Kennzeichen."

        if message != "":
            tk.messagebox.showinfo("Fehler",  message)

        self.update_table()

    def delete_fahrzeug(self):
        """Set end_time and by that prevent fahrzeug from being shown in table.
        """
        self.top3 = tk.Toplevel(self.root)
        self.top3.config(bg=self.par.colorTheme)
        self.top3.geometry("350x400")
        self.top3.title("Fahrzeug(e) löschen")
        self.top3.lift(self.root)

        scroll_frame = ScrollableFrameContainer(self.top3, self.par.colorTheme)
        scroll_frame.pack()
        table = scroll_frame.scrollable_content_frame

        #table = tk.Frame(self.top3)
        #table.pack()

        truth_values_checkboxes = []

        def remove_fahrzeuge():
            for idx, var in truth_values_checkboxes:
                if var.get() == 1:
                    self.fahrzeuge[idx].end_time = datetime.datetime.now().isoformat()[:16]
            self.update_table()
            self.top3.destroy()
        
        tk.Label(table, text="Kennzeichen", font=("Arial", 12, "bold"), background=self.par.colorTheme).grid(row=0, column=0)
        tk.Label(table, text="Entfernen?", font=("Arial", 12, "bold"), background=self.par.colorTheme).grid(row=0, column=1)

        for idx, fahrzeug in enumerate(self.fahrzeuge):

            if fahrzeug.end_time == "":
                l = tk.Label(table, text=fahrzeug.kennzeichen, font=("Arial", 12), background=self.par.colorTheme)
                var = tk.IntVar()
                c = tk.Checkbutton(table, onvalue=1, variable=var, background=self.par.colorTheme)
                truth_values_checkboxes.append((idx, var))

                l.grid(row=idx+1, column=0, padx=5, pady=5, sticky="W")
                c.grid(row=idx+1, column=1, padx=5, pady=5)

        submit = tk.Button(self.top3, text="Ausgewählte Fahrzeuge löschen", background="RED", command= remove_fahrzeuge)
        submit.pack()


    def sort_fahrzeuge(self, criteria):
        """Sort self.fahrzeuge either by status or typ (typ of verhicle).
        A list of self.fahrzeuge is returned.
        """
        sorted_list = self.fahrzeuge.copy()
        if criteria == "typ":
            def index_typ(e):
                try:
                    return self.par.fahrzeugTypen.index(e.typ)
                except:
                    return float('inf')
            sorted_list.sort(key=index_typ)
        elif criteria == "status":
            def status_code(e):
                try:
                    return self.par.statusSystem.index(e.status.get())
                except:
                    return float('inf')
            #sorted_list.sort(key=lambda fahrzeug: fahrzeug.status.get())
            sorted_list.sort(key=status_code)
        
        return sorted_list


    def update_table(self):
        """Display the table of active fahrzeuge.
        Reads out properties of each fahrzeug by iterating through self.fahrzeuge.
        Adds info-button to each row.  
        """

        # delete widgets in table_frame if it exits to prevent overwriting
        if not hasattr(self, "table_frame"):
            self.table_frame = None
        else:
            if self.table_scroll_frame.scrollable_content_frame.winfo_exists():
                for widget in self.table_scroll_frame.scrollable_content_frame.winfo_children():
                    widget.destroy()

        self.table_frame = self.table_scroll_frame.scrollable_content_frame

        if len(self.fahrzeuge) > 0:

            # create headers
            for j, attribute in enumerate(self.par.shownFahrzeugLabels):
                e = tk.Label(self.table_frame, text= attribute,
                            font=("Arial", 12), background="GRAY",
                            borderwidth=1, relief="solid",
                            width=15)
                e.grid(row=0, column=j, sticky="nsew")

                if j == len(self.par.shownFahrzeugLabels)-1:
                    e = tk.Label(self.table_frame, text="Status",
                            font=("Arial", 12), background="GRAY",
                            borderwidth=1, relief="solid",
                            width=15)
                    e.grid(row=0, column=j+1, sticky="nsew")

            # plug in values for active fahrzeuge
            counter = 0
            for fahrzeug in self.sort_fahrzeuge(self.criteria.get()):
                
                if fahrzeug.end_time == "":
                    status_color = "white"
                    if fahrzeug.status.get() != "":
                        status_color = self.par.statusColor[self.par.statusSystem.index(fahrzeug.status.get())]

                    for j, feature in enumerate(self.par.shownFahrzeugFeatures):
                        e = tk.Label(self.table_frame, text=getattr(fahrzeug, feature),
                                    font=("Arial", 12), bg = status_color,
                                    borderwidth=1, relief="solid",
                                    width=15)   
                        e.grid(row=counter+1, column=j, sticky="nsew")

                        if j == len(self.par.shownFahrzeugFeatures)-1:
                            # set status of fahrzeug to current status ?????
                            fahrzeug.status.set(fahrzeug.status.get())
                            
                            status_frame = tk.Frame(self.table_frame, borderwidth=1, bg = status_color, relief="solid")
                            status_frame.grid(row=counter+1, column=j+1, sticky="nsew")
                            s = tk.OptionMenu(status_frame, fahrzeug.status, *self.par.statusSystem)
                            s.config(bd=0, highlightthickness=0, relief="flat", bg = status_color)
                            s.pack(fill="both", padx=1, pady=1, expand=True)

                            info_button = tk.Button(self.table_frame, text="Info", bg = status_color,
                                                    command= lambda x=fahrzeug: x.show_fahrzeug_information(self.root))
                            info_button.grid(row=counter+1, column= j+2, sticky="nsew")

                    counter += 1


    def finish_einsatz(self):
        """Finishs einsatz. 
        """
        response = tk.messagebox.askyesnocancel(title="Einsatz wirklich beenden?", message="Willst du den Einsatz wirklich beenden? Du kannst ihn danach nur noch zur Ansicht öffnen und keine Änderungen mehr vornehmen. Es wird automatisch eine pdf von der aktuellen Tabelle erstellt. Einsatz beenden?")

        if response == True:
            PDF(self.table_frame, self.einsatz.filename, self.sort_fahrzeuge(self.criteria.get()))
            self.root.destroy()
            


