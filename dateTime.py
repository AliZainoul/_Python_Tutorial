from datetime import datetime

# Création d'un objet de date et heure
now = datetime.now()
print("Date and time:", now)

# Exemple d’utilisation de l'heure

# Formatage de la date et de l'heure
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

# Extraction des composants de la date et de l'heure
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)
