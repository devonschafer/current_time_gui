#This is built for python3, some small things between the different versions are different, just a reminder

#import guizero, the * is for importing everything instead of "from guizero import PushButton, Slider, etc.
from guizero import *
#import the time module, not really nessessary because we can import this in the next line, but I just do it anyway
import time
#from the time module also import these other classes
from time import sleep, gmtime, strftime, localtime
#import the datetime module. I think this comes in the time module as well, but I like do import this separately
import datetime

#function for displaying the current date and time, to include it updating in real time like you would want
def myfunction():
    #Date and Time
    #if you look up the time module for python, all these letters will be explained. Each letter is for something specific
    mytext.value = strftime('%B %d %A %H:%M', localtime())
    
#make the GUI window, basic
app = App(title='My DateTime GUI')

#make a text object, basic
#this 'hello world' text will display until the function takes over.
mytext = Text(app, text='Hello World')

#add this line to update the mytext object, this can be found in the Guizero Docs
mytext.repeat(100, myfunction)

#a closing statement that the Guizero module wants to display the window.
app.display()

