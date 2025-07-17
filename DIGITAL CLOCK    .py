#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from time import strftime


# In[2]:


#creating tkinter window
digital_clock = Tk()
digital_clock.geometry("600x300")
digital_clock.title('Digital Clock')

#displaying time on the label
def time():
    string = strftime('%H:%M:%S %p') #%H = HOUR, %M=MINUTE,%S=SECONDS,%p=am or pm
    lable.config(text = string)
    lable.after(1000, time)
    
#Increase the user experience designing the label widget
lable = Label(digital_clock, font = ('calibri', 40, 'bold'), background = '#DB1860', foreground = 'black')

#Clock at the centre of the tinker window
lable.pack(anchor = 'center')
time()

mainloop()

