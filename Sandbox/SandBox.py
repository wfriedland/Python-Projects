#
#   SandBox.py - Final project for the Tech Academy Python course. This project did not have
#   any instructions so basically it is just fun and games with Python.
#
from datetime import datetime
from datetime import timedelta
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import urllib.request
from bs4 import BeautifulSoup
from html import parser

class sandBox:
    def Bsoup(self,e ):
        # The beautiful soup package gives you a door into a web sites
        # contents. Parsing the actual contents is not an easy task, but
        # doable.
        self.soupButton.config(state='disable')
        self.text_comments.delete(1.0,'end')
        self.labelText.set('Comments:')
        self.regxButton.config(state='enable')
        self.annieButton.config(state='enable')
        webPage = urllib.request.urlopen(self.urlString)
        soup = BeautifulSoup(webPage,'html.parser')
        titlestuff = "{}".format(soup.title)
        print (titlestuff)
        soupStr = "Processed URL with the Beautiful Soup Package\n\n"
        soupStr += "We are then able to extract data from its HTML\n\n"
        soupStr += "The following is this website's title:\n\n"
        soupStr += titlestuff
        self.text_comments.insert(END,soupStr,'colors')

    def Annies(self, e):
        #
        #  TimeDeltas are a very simple concept. So why did it give me so much trouble?
        #  First of all, the fact that timedeltas only work with timestamps from the
        #  datetime library so only common knowlege if you already know it. And secondly
        #  If reading and writing these values to and from a database the units must match
        #  exactly.
        #
        self.labelText.set('Comments:')
        self.myLabel.grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        aDayAway= timedelta(hours=23, minutes=57, seconds=23)
        annie = datetime.now() + aDayAway
        annieStr = annie.strftime("%Y-%m-%d %H:%M:%S")
        self.text_comments.delete(1.0,'end')

        str =  "Current Time:   "+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n"
        str += "Computed Time: "+annieStr
        str += "\nTime Delta: hours=23, minutes=57, seconds=23\n"

        str += "\nPyThon allows you to get a timestamp more than one place, but the \ntimedelta feature ONLY works "
        str += "with timestamps from the datetime library"
        str += "\n\nAlways specify the datetime format explicityly before Python does it for you. "

        self.text_comments.insert(END,str,'colors')

    def showURL(self,e):
        #
        # Regular Expressions are so much fun, except that I use them so infrequently I have to
        # re-learn them everytime I use  them. I had a bigger expression that took alphaNumeric
        # values as a url name as long it started with a letter, but the string did not fit in
        # this program's display.
        if self.urlOK == False:
            self.labelText.set("Enter URL as http://www.name.ext:")
            self.text_comments.delete(1.0,'end')
            self.annieButton.config(state='disable')
            self.soupButton.config(state='disable')
            self.urlOK = True;
        else:
            self.urlString = self.text_comments.get(1.0,'end')
            print (self.urlString)
            dotcom = re.compile("http://www.([A-Za-z]+).(com|COM|net|NET|ORG|org)")
            m = dotcom.match(self.urlString)
            if m:
                self.soupButton.config(state='enable')
                self.regxButton.config(state='disable')
                self.text_comments.delete(1.0,'end')
                self.labelText.set('Comments:')
                urlStr = "URL Validation test passed.\n\n"
                urlStr += "Valiation done with the following regular expression:\n\n"
                urlStr += "http://www.([A-Za-z]+).(com|COM|net|NET|ORG|org)\n\n"
                urlStr += "Press the 'Read URL' button to continue."
                self.text_comments.insert(END,urlStr,'colors')
                self.urlOK = False
            else:
                messagebox.showinfo(title = 'URL check', message = 'Please enter a valid url')





    def __init__(self, master):

        master.title('Presented by Warren Friedland')
        master.resizable(False, True)
        master.configure(background = 'lightBlue')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = 'lightBlue')
        self.style.configure('TButton', background = 'lightBlue')
        self.style.configure('TLabel', background = 'lightBlue', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file = 'littleSquarePeg.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 1, column = 0, rowspan = 3)
        ttk.Label(self.frame_header, text = 'Fun with Python', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 380,
                  text = ("Final project for the Tech Academy Python course. This project did not have  "
                          "specific instructions so it is just a review of some of the lessons learned")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        self.labelText = StringVar()
        self.myLabel = ttk.Label(self.frame_content, textvariable=self.labelText, anchor=W, width=30)
        self.labelText.set('Comments:')
        self.myLabel.grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        self.annieButton = ttk.Button(self.frame_header, text = 'Time Delta')
        self.annieButton.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.urlOK = False;
        self.regxButton = ttk.Button(self.frame_header, text = 'Validate URL')
        self.regxButton.grid(row = 5, column = 1, padx = 100, pady = 5, sticky = 's')
        self.soupButton = ttk.Button(self.frame_header, text = 'Read URL', state='disable')
        self.soupButton.grid(row = 5, column = 2, padx = 5, pady = 5, sticky = 'e')

        self.annieButton.bind('<Button-1>',self.Annies)
        self.regxButton.bind('<Button-1>',self.showURL)
        self.soupButton.bind('<Button-1>',self.Bsoup)

        self.text_comments = Text(self.frame_content, width = 60, height = 11, font = ('Arial', 10), background='yellow2')
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 10)


def main():

    root = Tk()
    sbox = sandBox(root)
    root.mainloop()

if __name__ == "__main__": main()
