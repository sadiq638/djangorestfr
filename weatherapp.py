import requests
from tkinter import *
from tkinter import messagebox
master=Tk()

label=Label(master,text='Weather App',font=('verdana',40))
label.pack()
elabel=Label(master,text='Enter City Name',font=('verdana',20))
elabel.pack()
entry=Entry(master)
entry.pack()

def weatherapi():
        '''function to get weather using api and displaying weather through tkinter messagebox'''
	city=str(entry.get())
	api='7ee8a1bbf4f9a5fab0e18f261ea1633f'
	url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api
	request=requests.get(url=url)
	response=request.json()
	
	temprature=int(response['main']['temp']-273.15)
	humidity=int(response['main']['humidity'])
	ws=response['wind']['speed']
	messagebox.showinfo('weather report','TEMPRATURE : '+str(temprature)+'*C'+'\n'+'HUMIDITY: '+str(humidity)+'\n'+'WIND: '+str(ws))
button=Button(master,text='Get Current Weather',command=weatherapi)
button.pack()

mainloop()
