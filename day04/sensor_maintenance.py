# sensor_maintenance.py

# OBJECTIVE
# Schreibe eine Funktion mit zwei Parametern: einem rohen Sensorwert als String und einem Divisor (int).
# Die Funktion versucht, den Sensorwert in eine Zahl umzuwandeln und durch den Divisor zu teilen, und gibt bei Erfolg f'Sensorwert: {result:.2f}' zurueck.
# Bei ungueltiger Zahl (ValueError) gib 'Ungueltiger Sensorwert.' zurueck, bei Division durch 0 (ZeroDivisionError) gib 'Division durch 0 - Sensor fehlerhaft.' zurueck
# (zwei getrennte except-Bloecke, keine Buendelung noetig, da die Meldungen unterschiedlich sind).
# Egal welcher Fall eintritt oder ob alles klappt: am Ende soll IMMER print("Wartung abgeschlossen.") ausgefuehrt werden - nutze dafuer finally.
# Die Funktion muss check_sensor(raw_value, divisor) heissen.



def check_sensor(raw_value, divisor):
    try:
        raw_value = int(raw_value)
        divisor = int(divisor)
        result = raw_value / divisor

    except ValueError:
        return "Ungueltiger Sensorwert."

    except ZeroDivisionError:
        return "Division durch 0 - Sensor fehlerhaft."

    finally:
        print("Wartung abgeschlossen.")

    return f'Sensorwert: {result:.2f}'

print(check_sensor(15,0))