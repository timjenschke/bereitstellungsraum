# bereitstellungsraum
Nutzerfreundliches, simples Programm, um die Fahrzeuge eines Bereitschaftsraums zu verwalten. Ein Bereitschaftsraum ist ein Begriff des Katastrophenschutzes und beschreibt einen Ort, wo Einsatzmittel zur schnellen Anfahrt gesammelt werden. Dieses Programm ermöglicht eine einfache Übersicht. 

## Was kann das Programm? 
Das Ausführen der Datei start.py lädt ein Programm mit gewöhnlicher grafischer Nutzeroberfläche. Es kann ein Einsatz angelegt werden, welchem Fahrzeuge nach Belieben hinzugefügt werden können. Alle aktiven Fahrzeuge werden dann in einer großen Tabelle angezeigt. Aktiven Fahrzeugen kann ein Status zugewiesen werden, der dann grafisch unterlegt wird. Je nach Einstellungen des Nutzers kann das Statussystem und die zugehörigen Farben beliebig gewählt werden. Die Tabelle kann nach Fahrzeugtyp oder Status sortiert werden. Zu jedem Fahrzeug müssen Informationen zu Kennzeichen und Funkrufname angegeben werden. Zusätzlich können Informationen zu Hiorg, Fahrzeugtyp, Kontaktperson mit Telefonnummer, Anzahl der Transportskapazitäten (liegend und sitzend) eingepflegt werden. 
Alle Informationen werden in einem json-Dateiformat gespeichert, welches den Vorteil aufweist, dass es auch von Hand ausgelesen werden kann, d.h. kein Programm dazu notwendig ist. Zusätzlich kann zu jedem Zeitpunkt die aktuelle Version der Tabelle als pdf exportiert und entsprechend ausgedruckt werden.
Alte Einsätze können vom Programm auch wieder eingelesen werden. Die json-Datei kann momentan jedoch nur zur Ansicht geladen werden und die Konvertierung in pdf ist auch nicht möglich.

## Wie kann das Programm verwendet werden? 
Bei Einsätzen im Katastrophenschutz kann mithilfe dieses Tools ein Bereitschaftsraum im Blick gehalten werden. Alle aktiven Fahrzeuge stehen in einer Liste, welche veränderbar ist. Das Statussystem ermöglicht auch diejenigen Fahrzeuge im Blick zu behalten, die gerade unterwegs sind oder sich auf Anfahrt befinden. Es ist ein relativ abstraktes und simples Tool welches statisch verwendet werden kann. 

## Wer darf das Programm benutzen? 
Jeder, der Interesse daran hat. Geschrieben ist mit der Absicht, im Katastrophenschutz zum Einsatz zu kommen, um die eigenen Fahrzeuge zu verwalten. Fühl dich frei, es beliebig zu verändern und an deine Bedürfnisse anzupassen. Ich wäre dir dankbar, Änderungen auf github hochzuladen, damit auch andere Leute davon profitieren können. Mein Programm und auch veränderte Verisonen davon dürfen in keinem Fall zu kommerziellen Zwecken genutzt werden. 
Ich habe das Programm in meiner Freizeit geschrieben und bin kein Programmierer. Das Programm ist mit Sicherheit nicht das effizienteste und beste was diese Welt jemals gesehen hat, aber es erfüllt seinen Zweck.

## Ist das Programm sicher? 
Das Programm läuft vollständig lokal und hat keine Schnittstelle zum Internet. Alle Daten werden lokal auf der Festplatte gespeichert.
Fehler im Programm sind nicht auszuschließen, was zu Datenverlust führen könnte. Bitte Fehler melden!

## Mögliche Features für die Zukunft?
- automatischer Installer 
- Möglichkeit Kartenauschnitte über openstreetmaps einzufügen, in welche der Bereitschaftsraum eingezeichnet werden kann.
- mehrere Bereitschafträume: extra Spalte um anzugeben, im welchem Bereitschaftraum Fahrzeug steht oder extra Fenster für jeden Bereitschaftsraum
- Notizfeld um Infos zu notieren, die während des Einsatzes eingehen
- Verfügbarkeit des Programms in mehreren Sprachen

# Wie kannst du das Programm benutzen? 
Momentan ist dies leider noch relativ umständlich und erfordert ein wenig Kenntnisse von Phyton und den damti verbundenen Eigenheiten. Du musst als erstes Python installieren und bei der Installtion darauf achten, dass du ankilckst, dass eine global path variable erstellt wird. Um Python nutzen zu können, musst du eine virtual enviornment anlegen (venv). Nachdem du diese aktiviert hast, musst du die Bibliotheken in requirements.txt installieren. Nun kannst du das Dokument start.py über die Konsole ausführen. Es kann sein, dass dies zu einem Fehler führt, weil Windows das Asuführen von Skripten verhindert. Diese Einstellungen müssen dann gegebenenfalls von dir angepasst werden. 
Das ist natürlich sehr kurz gefasst. Aber zu allen diesen Schritten gibt es unzählige Anleiten auf diversen Internetseiten, da es sich um basic Dinge handelt. 
