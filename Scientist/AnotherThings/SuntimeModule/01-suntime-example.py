# Thanks to this S.O question: https://es.stackoverflow.com/questions/387503/importerror-cannot-import-name-sun-from-suntime/387572

# We need suntime module: pip3 install suntime


import datetime

# Import suntime:
from suntime import Sun, SunTimeException

# Define latitude and longitude:
latitud = 43.36
longitud = -8.41

# Sun instance
sun = Sun(latitud, longitud)

# Set today's sunrise 
hoy_sr = sun.get_sunrise_time()

# Set today's sunset 
hoy_ss = sun.get_sunset_time()

# Print with format
print('Hoy el sol en Galicia salió a las {} y baja a las {}'.format(hoy_sr.strftime('%H:%M'), hoy_ss.strftime('%H:%M'))) 

# Result:

# Hoy el sol en Galicia salió a las 06:03 y baja a las 19:01
