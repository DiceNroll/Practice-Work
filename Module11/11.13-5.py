from math import pi

EarthVolume = 1.08321 * 10 ** 12
PlanetVolume = float(input('Введите радиус случайной планеты: '))**3 * 4 / 3 * pi
if EarthVolume > PlanetVolume: print('Объем планеты Земля больше в', round(EarthVolume/PlanetVolume,3))
if EarthVolume < PlanetVolume: print('Объем планеты Земля меньше в', round(PlanetVolume/EarthVolume,3))
