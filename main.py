from pyowm import OWM
from pyowm.utils import config

owm = OWM('a7db22be66fff6303fa9e5f1ba632f16')
mgr = owm.weather_manager()

observation = mgr.weather_at_place(input())
w = observation.weather

wg = w.temperature('celsius');

print ("Температура: " + str(wg['temp']) + " Градусов по Цельсию " + " Давление: " + str(w.pressure['press']) + " Гектопаскаль " + "Влажность: " + str(w.humidity) + "%")
