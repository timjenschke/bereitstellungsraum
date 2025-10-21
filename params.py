class Params:

    def __init__(self, color, fahrzeug_typs, shown_features, shown_features_name, status_system, status_colour):

        self.colorTheme = color or "#fefefb"

        # mögliche Fahrzeugtypen welche gewählt werden können; erster Fahrzeugtyp ist default
        # Sortierung in Tabelle richtet sich nach der Position in der Liste (weiter links => weiter oben)
        self.fahrzeugTypen = fahrzeug_typs or ["KTW", "MTW", "RTW", "GW-San", "ELW", "BTW", "PKW", "LKW"]

        # Position der Fahrzeug-Eigenschaften, welche in der Tabelle auf dem Dashboard angezeigt werden soll, d.h. 0 entspricht kennzeichen
        # kennzeichen, funkruf, hiorg, contact_name, contact_phone, typ, trsp_liegend, trsp_sitzend, start_time, end_time
        #self.shownFahrzeugFeatures = [0,1,2,5,6,7]
        self.shownFahrzeugFeatures = shown_features or ["kennzeichen", "funkruf", "hiorg", "typ", "trsp_liegend", "trsp_sitzend"]

        # Umbennung des Tabellenkopfs: Muss selbe Länge wie shownFahrzeugFeatures haben und chronologisch richtig sein
        self.shownFahrzeugLabels = shown_features_name or ["Kennzeichen", "Funk", "Hiorg", "Typ", "Trsp Liegend", "Trsp Sitzend"]

        # Status-System: Beliebiges System festlegen und farbliche Markierung des Status 
        # Sortierung in Tabelle richtet sich nach der Position in der Liste (weiter links => weiter oben)
        self.statusSystem = status_system or ["0","1","2","3","4","5","6","7","8","9"]
        self.statusColor = status_colour or ["#FFFFFF","#8FFA3D","#8FFA3D","#FF8F8F","#FF8F8F","#FFFFFF","#FFFFFF","#FF8F8F","#F3E883","#FFFFFF"]
  
        #self.statusSystem = ["gut", "schlecht", "unklar"]
        #self.statusColor = ["green", "red", "gray"]

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
