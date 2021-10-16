from tkinter import *
import requests
root=Tk()
root.title("Weather")
root.geometry("600x500")
#root.wm_iconbitmap("weather.ico")
#key: 523bd906b38101a5dfdabcfdac4bdb83
#api url: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def get_weather(city):
    weather_key= '523bd906b38101a5dfdabcfdac4bdb83'
    api_url='https://api.openweathermap.org/data/2.5/weather'
    parameter={'appid':weather_key,'q':city,'units':'imperial'}
    response=requests.get(api_url,parameter)
    weather=response.json()
    result['text']=info(weather)
    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])
def info(weather):
    try:
        city=weather['name']
        condition=(weather['weather'][0]['description'])
        temp=(weather['main']['temp'])
        str='''
        City:{}
        Condition:{}
        Temperature:{}'''.format(city,condition,temp)  
    except:
        str="There is some problem in retreving information."
    return str    
txt=StringVar()
f1=Frame(root,bg="sky blue",bd=5)
heading=Label(f1,text="Enter City",font="lucida 19",fg="red",bg="white")
heading.grid(row=0,column=0)
city=Entry(f1,textvar=txt,font="lucida 20")
city.grid(row=0,column=1,padx=10,pady=10)
btn=Button(f1,text="Get Weather",font="lucida 13 bold",command=lambda: get_weather(city.get()))
btn.grid(row=1,column=1)
f1.place(x=80,y=50,width=450,height=100)
f2=Frame(root,bg="sky blue",bd=5)
result=Label(f2,font="lucida 19",bg="white",justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)
f2.place(x=80,y=170,width=450,height=300)
root.mainloop()
