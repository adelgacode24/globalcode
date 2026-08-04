from pyowm import OWM

owm = OWM('3920d27143176b164a3dfd677724ab8c')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Tamale,GH')
w= observation.weather
print(w.wind())
print(w.humidity)
print(w)
