import tkinter as tk
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
import datetime

class PDF:

    def __init__(self, frame, filename, sorted_fahrzeuge):
        time = datetime.datetime.now().isoformat()[:16]

        for i in range(len(sorted_fahrzeuge)-1,-1,-1):
             if sorted_fahrzeuge[i].end_time != "":
                  sorted_fahrzeuge.pop(i)

        filename = filename.replace(".json", "") 
        filename = filename + f"_v_{time[11:13]}{time[14:16]}.pdf"

        data = []
        rows = frame.grid_size()[1]
        cols = frame.grid_size()[0] - 1 # exclude info button

        for r in range(rows):
            row_data = []
            for c in range(cols):
                # get slaves at position (r,c) --> will be the tk.Label()
                    widget = frame.grid_slaves(row=r, column=c)
                    if widget:
                        try:
                            # status column is the only column where this will fail
                            row_data.append(widget[0].cget("text")) 
                        except: 
                            status = sorted_fahrzeuge[r-1].status.get()
                            row_data.append(str(status))
                    else:
                        row_data.append("")
            data.append(row_data)

        self.pdf = SimpleDocTemplate(filename, pagesize=A4)
        table = Table(data)
        table.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ]))

        title = Paragraph(f"Einsatz: {filename}")
        info = Paragraph(f"Standpunkt vom {time[:10]} um {time[11:16]} Uhr.")
        aktiv = Paragraph(f"Aktive Fahrzeuge: {len(sorted_fahrzeuge)}")
        spacer = Spacer(1, 12)

        self.pdf.build([title, info, aktiv, spacer, table])

