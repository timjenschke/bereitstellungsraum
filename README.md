# bereitstellungsraum
Simples Programm, um die Fahrzeuge eines Bereitschaftsraums zu verwalten. Ein Bereitschaftsraum ist ein Begriff des Katastrophenschutzes und beschreibt einen Ort, wo Einsatzmittel zur schnellen Anfahrt gesammelt werden. Dieses Programm ermöglicht eine einfache Übersicht. 

## Was kann das Programm? 
Das Ausführen der Datei start.py lädt ein Programm mit gewöhnlicher grafischer Nutzeroberfläche. Es kann ein Einsatz angelegt werden, welchem Fahrzeuge nach Belieben hinzugefügt werden können. 
<img width="1406" height="841" alt="startbildschirm" src="https://github.com/user-attachments/assets/e667b96f-4887-4574-bf14-48c0442c527f" />
Alle aktiven Fahrzeuge werden dann in einer großen Tabelle angezeigt. Aktiven Fahrzeugen kann ein Status zugewiesen werden, der dann grafisch unterlegt wird. Je nach Einstellungen des Nutzers kann das Statussystem und die zugehörigen Farben beliebig gewählt werden. Die Tabelle kann nach Fahrzeugtyp oder Status sortiert werden. Zu jedem Fahrzeug müssen Informationen zu Kennzeichen und Funkrufname angegeben werden. Zusätzlich können Informationen zu Hiorg, Fahrzeugtyp, Kontaktperson mit Telefonnummer, Anzahl der Transportskapazitäten (liegend und sitzend) eingepflegt werden. 
<img width="1901" height="1127" alt="fahrzeug_dashboard" src="https://github.com/user-attachments/assets/e635296e-c5e3-4e26-8121-ffdf176fd41a" />

Alle Informationen werden in einem json-Dateiformat gespeichert, welches den Vorteil aufweist, dass es auch von Hand ausgelesen werden kann, d.h. kein Programm dazu notwendig ist. Zusätzlich kann zu jedem Zeitpunkt die aktuelle Version der Tabelle als pdf exportiert und entsprechend ausgedruckt werden.

Alte Einsätze können vom Programm auch wieder eingelesen werden. Die json-Datei kann momentan jedoch nur zur Ansicht geladen werden und die Konvertierung in pdf ist auch nicht möglich.
<img width="1888" height="1131" alt="einsatz_laden" src="https://github.com/user-attachments/assets/2ab5ad4e-b258-49fd-b90b-730af73e8b4d" />


## Wie kann das Programm verwendet werden? 
Bei Einsätzen im Katastrophenschutz kann mithilfe dieses Tools ein Bereitschaftsraum im Blick gehalten werden. Alle aktiven Fahrzeuge stehen in einer Liste, welche veränderbar ist. Das Statussystem ermöglicht auch diejenigen Fahrzeuge im Blick zu behalten, die gerade unterwegs sind oder sich auf Anfahrt befinden. Es ist ein relativ abstraktes und simples Tool welches statisch verwendet werden kann. 

## Wer darf das Programm benutzen? 
Jeder, der Interesse daran hat. Geschrieben ist mit der Absicht, im Katastrophenschutz zum Einsatz zu kommen, um die eigenen Fahrzeuge zu verwalten. Fühl dich frei, es beliebig zu verändern und an deine Bedürfnisse anzupassen. Ich wäre dir dankbar, Änderungen auf github hochzuladen, damit auch andere Leute davon profitieren können. Mein Programm und auch veränderte Verisonen davon dürfen in keinem Fall zu kommerziellen Zwecken genutzt werden. 
Ich habe das Programm in meiner Freizeit geschrieben und bin kein Programmierer. Das Programm ist mit Sicherheit nicht das effizienteste und beste was diese Welt jemals gesehen hat, aber es erfüllt seinen Zweck.

## Ist das Programm sicher? 
Das Programm läuft vollständig lokal und hat keine Schnittstelle zum Internet. Alle Daten werden lokal auf der Festplatte gespeichert.
Fehler im Programm sind nicht auszuschließen, was zum Verlust oder fehlerhaften Daten führen könnte. Ich bitte darum, Fehler zu melden.
Benutzung des Programms erfolgt auf eigene Verantwortung. 

## Mögliche Features für die Zukunft?
- automatischer Installer 
- Möglichkeit Kartenauschnitte über openstreetmaps einzufügen, in welche der Bereitschaftsraum eingezeichnet werden kann.
- mehrere Bereitschafträume: extra Spalte um anzugeben, im welchem Bereitschaftraum Fahrzeug steht oder extra Fenster für jeden Bereitschaftsraum
- Notizfeld um Infos zu notieren, die während des Einsatzes eingehen
- Verfügbarkeit des Programms in mehreren Sprachen

# Wie kannst du das Programm benutzen? 
Momentan ist dies etwas umständlich, wenn du bisher keine Erfahrung mit Python hast. Die grundsätzlichen Schritte sind folgende:
1) Installiere python über die offzielle Seite und wähle die aktuellste Version. Achte darauf, bei der Installation auszuwählen, dass du die Option global path erstellen auswählst.
2) Erstelle eine virtuelle Umgebung (virtual environment) möglichst in demselben Ordner, in den du die Dateien aus diesem repository lädst.
3) Aktiviere deine virtual environment und installiere die Bibliotheken in requirements.txt.
4) Führe nun start.py aus und das Programm startet. 
Es handelt sich bei allen diesen Schritten um klassiche Schritte die auf sämtliche Programme in python zutreffen, weshalb es gute Anleitungen dafür gibt.
