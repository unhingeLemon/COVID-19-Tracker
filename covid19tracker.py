from tkinter import *
import requests 

HEIGHT = 500
WIDTH = 600

root = Tk()
root.title('COVID-19 LIVE TRACKER')



def get_result(entry):
	url = 'https://covid-193.p.rapidapi.com/statistics'
	key = 'f511081e15msh908b491eabf7e58p1a20eejsn8dd4b50f0d1e'
	query = {"country": entry}
	params = {"country": entry}

	headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "f511081e15msh908b491eabf7e58p1a20eejsn8dd4b50f0d1e"
    }
	response = requests.get(url, params = params, headers = headers)
	result = response.json()
	""" print (result)
	print (result['response'][0]['country'])
	print (result['response'][0]['cases']['new'])
	print (result['response'][0]['cases']['active'])
	print (result['response'][0]['cases']['critical'])
	print (result['response'][0]['cases']['recovered'])
	print (result['response'][0]['cases']['total'])

	print (result['response'][0]['deaths']['new'])
	print (result['response'][0]['deaths']['total'])

	print (result['response'][0]['tests']['total'])

	print (result['response'][0]['day'])
	print (result['response'][0]['time']) """
	try:
		country = result['response'][0]['country']
		new = result['response'][0]['cases']['new']
		active = result['response'][0]['cases']['active']
		critical = result['response'][0]['cases']['critical']
		recovered =result['response'][0]['cases']['recovered']
		total = result['response'][0]['cases']['total']

		newD = result['response'][0]['deaths']['new']
		totalD = result['response'][0]['deaths']['total']

		numTest = result['response'][0]['tests']['total']

		day = result['response'][0]['day']
		time = result['response'][0]['time']

		resultString = 'Country: %s \n\nNew Cases: %s \nActive Cases: %s \nRecovered: %s \nTotal Cases: %s \n\nNew Deaths: %s \nTotal Deaths: %s \n\nNumber of Tests: %s \nTime: %s' % (country,new,active,recovered,total,newD,totalD,numTest,time)
		label['text'] = resultString
	except:
		resultString = "There was a problem retrieving that information"
		label['text'] = resultString
canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()


root.geometry('600x500')
root.resizable(0,0)


background_image = PhotoImage(file = 'landscape.png')
background_label = Label(root, image = background_image, text = 'covid-19')
background_label.place(relwidth=1,relheight =1)

frame = Frame(root, bg="#330000", bd= 5)
frame.place(relx = 0.5, rely = .1, relwidth = .75, relheight = .1, anchor = 'n')


entryText = StringVar()
entry = Entry (frame, font = ('Consolas',15),textvariable=entryText)
entry.place(relwidth=0.65, relheight = 1)
entryText.set( "Enter a Country" )

button = Button(frame, text = "Get Result", font = ('Consolas',15), command = lambda: get_result(entry.get()))
button.place(relx = .7, relwidth = 0.3, relheight = 1)

lower_frame = Frame(root, bg = "#330000", bd = 5)
lower_frame.place(relx = .5, rely = .25, relwidth = .75, relheight = .7, anchor = 'n')

label = Label(lower_frame, font = ('Consolas',15),anchor = 'nw', justify = 'left', bd = 4)
label.place( relwidth = 1, relheight = 1)


root.mainloop()