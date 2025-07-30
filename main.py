from opencage.geocoder import OpenCageGeocode
from tkinter import *

from pycparser.c_ast import Return


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return f'Широта: {lat}, Долгота: {lon}\n Страна: {country}\n Регион: {region}'
            else:
                return f'Широта: {lat}, Долгота: {lon}\n Страна: {country}'
        else:
            return 'Город не найден'
    except Exception as e:
        return f'Возникла ошибка: {e}'


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f'Координаты города {city}: {coordinates}')


key = '5cf6dcaf3ada4335bd40f2aeb9962d85'
city = 'Эквадор'
coordinates = get_coordinates(city, key)

window = Tk()
window.title('Координаты городов')
window.geometry('400x120')

entry = Entry()
entry.pack()
entry.bind('<Return>', show_coordinates)

button = Button(text='Поиск координат', command=show_coordinates)
button.pack()

label = Label(text='Введите город и нажмите на кнопку')
label.pack()

window.mainloop()
