# bereitstellungsraum
Nutzerfreundliches, simples Programm, um die Fahrzeuge eines Bereitschaftsraums zu verwalten. Ein Bereitschaftsraum ist ein Begriff des Katastrophenschutzes und beschreibt einen Ort, wo Einsatzmittel zur schnellen Anfahrt gesammelt werden. Dieses Programm ermöglicht eine einfache Übersicht. 

## Was kann das Programm? 
Das Ausführen der Datei start.py lädt ein Programm mit gewöhnlicher grafischer Nutzeroberfläche. Es kann ein Einsatz angelegt werden, welchem Fahrzeuge nach Belieben hinzugefügt werden können. Alle aktiven Fahrzeuge werden dann in einer großen Tabelle angezeigt. Aktiven Fahrzeugen kann ein Status zugewiesen werden, der dann grafisch unterlegt wird. Je nach Einstellungen des Nutzers kann das Statussystem und die zugehörigen Farben beliebig gewählt werden. Die Tabelle kann nach Fahrzeugtyp oder Status sortiert werden. Zu jedem Fahrzeug müssen Informationen zu Kennzeichen und Funkrufname angegeben werden. Zusätzlich können Informationen zu Hiorg, Fahrzeugtyp, Kontaktperson mit Telefonnummer, Anzahl der Transportskapazitäten (liegend und sitzend) eingepflegt werden. 
Alle Informationen werden in einem json-Dateiformat gespeichert, welches den Vorteil aufweist, dass es auch von Hand ausgelesen werden kann, d.h. kein Programm dazu notwendig ist. Zusätzlich kann zu jedem Zeitpunkt die aktuelle Version der Tabelle als pdf exportiert und entsprechend ausgedruckt werden.
Alte Einsätze können vom Programm auch wieder eingelesen werden. Die json-Datei kann momentan jedoch nur zur Ansicht geladen werden und die Konvertierung in pdf ist auch nicht möglich.

## Wie kann das Programm verwendet werden? 
