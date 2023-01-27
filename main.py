import tkinter as tk
from tkinter import *
import random

MINUTE = 60
FONT_NAME = 'Courier'
TEXT_LIST = ['emery', 'jolla', 'modelled', 'stato', 'precipitated', 'amplification', 'broderick', 'brodie', 'wildfire', 'dues', 'prek', 'peterthoeny', 'designates', 'auto', 'craftsmen', 'sistema', 'abounds', 'hypocrisy', 'soundtrack', 'fife', 'nikos', 'auctioneer', 'acetylcholine', 'fiat', 'snow', 'rubber', 'equiv', 'backlinks', 'lowepro', 'serra', 'rennie', 'collier', 'shiva', 'jena', 'pebble', 'celina', 'browsing', 'endlessly', 'rowan', 'varsity', 'customise', 'cracks', 'crumpler', 'webshots', 'eatery', 'trunking', 'adolescente', 'francisco', 'realization', 'okinawa', 'mellitus', 'rhesus', 'stabilizer', 'conair', 'commercialisation', 'samui', 'issaquah', 'laps', 'palos', 'padlock', 'advice', 'nunn', 'devils', 'bong', 'carta', 'drinker', 'corkscrew', 'transitional', 'trembling', 'trickle', 'overlaid', 'talon', 'muslims', 'maximization', 'locally', 'martin', 'bimbo', 'nightlife', 'syrups', 'macht', 'happening', 'beyond', 'freud', 'curated', 'eigenvalues', 'napkin', 'msgstr', 'medusa', 'waxed', 'doubleclick', 'grandchild', 'continuum', 'goblins', 'cough', 'perry', 'nedstat', 'sibelius', 'golf', 'maui', 'dirk', 'pronunciation', 'wellbutrin', 'mchenry', 'mississippi', 'wallmounting', 'hoffmann', 'distraction', 'spout', 'somebody', 'pumpkins', 'tweaks', 'console', 'bader', 'medica', 'fenced', 'repurchase', 'septum', 'fragment', 'crippling', 'helsing', 'generalize', 'swath', 'sonics', 'ambulatory', 'millionaire', 'loophole', 'appease', 'bullet', 'powell', 'rescues', 'nicolas', 'sleek', 'mane', 'toon', 'sylvania', 'fuck', 'performance', 'sealy', 'nobody', 'encode', 'ransom', 'remanded', 'sensation', 'emerges', 'prioritize', 'gentlemen', 'gizmo', 'faso', 'unborn', 'wesley', 'promos', 'consequence', 'artest', 'jules', 'impurities', 'bernardo', 'memorials', 'premier', 'undercover', 'taylor', 'spacers', 'nhra', 'merida', 'arrays', 'kota', 'mussel', 'plas', 'michelin', 'petitioner', 'baking', 'intonation', 'channelweb', 'bombarded', 'joao', 'palpable', 'brooklyn', 'rpath', 'uncredited', 'resolve', 'carried', 'flown', 'iden', 'richey', 'tarot', 'circles', 'mnogosearch', 'britannica', 'chimes', 'enables', 'saffron', 'renovation', 'exits', 'bessemer', 'muenchen', 'pittsfield', 'attempting', 'wilmington', 'septembre', 'gaul', 'gazette']

class MainWindow:
    def __init__(self, window):
        window.title("Typing Speed Test")
        window.config(padx=50, pady=50, bg="grey")
        self.canvas = Canvas(height=200, width=800)

        self.sec = MINUTE
        
        self.cpm_label = Label(text="Correced CPM:", font=(FONT_NAME, 8), bg="grey")
        self.cpm_label.grid(row=1, column=0)
        self.cpm_entry = Label(width=5)
        self.cpm_entry.grid(row=1, column=1)

        self.wpm_label = Label(text="WPM:", font=(FONT_NAME, 8), bg="grey")
        self.wpm_label.grid(row=1, column=2)
        self.wpm_entry = Label(width=5)
        self.wpm_entry.grid(row=1, column=2, columnspan=2)

        self.time_label = Label(text="Time left:", font=(FONT_NAME, 8), bg="grey")
        self.time_label.grid(row=1, column=4)
        self.time_entry = Label(width=5, text='')
        self.time_entry.grid(row=1, column=5)
        self.text_area = Text(height=1, width=11, font = ("Times New Roman", 25))
        self.text_area.insert(tk.INSERT, TEXT_LIST[random.randrange(len(TEXT_LIST))])
        self.text_area.tag_add("center", 1.0, "end")

        self.text_area.grid(row=2, column=2, columnspan=2, pady = 10, padx = 10)
        self.text_area.tag_configure("center", justify='center')

        self.input_text = Entry(window, font = ("Times New Roman", 25), justify='center')
        self.input_text.grid(row=3, column=2, columnspan=2)
        self.input_text.bind("<Return>", self.click)
        self.input_text.bind( "<Button-1>", self.timer) 

        self.error_label = Label(text="", font=(FONT_NAME, 8), bg="grey")
        self.error_label.grid(row=4, column=2, columnspan=2)

        self.instructions = Label(text="The timer will start once you click the empty text box.\nPress enter to validate the word.", font=(FONT_NAME, 10), bg="grey")
        self.instructions.grid(row=5, columnspan=6)

        self.typed_words = []
        self.random_words = []


        
    def get_new_word(self):
        self.text_area.insert(tk.INSERT, TEXT_LIST[random.randrange(len(TEXT_LIST))])
        self.text_area.tag_add("center", 1.0, "end")
        self.text_area.configure(state ='disabled')

    def clear_text(self):
        self.input_text.delete(0, END)
        self.text_area.configure(state ='normal')
        self.text_area.delete(1.0, END)   
    
    def click(self, key):
        typed_word = self.input_text.get()
        random_word = self.text_area.get("1.0", "end-1c")
        self.error_label.configure(text='')
        if typed_word == random_word:
            self.typed_words.append(typed_word)
            self.random_words.append(random_word)
            self.clear_text()
            self.get_new_word()
        else:
            self.error_label.configure(text='Mispelled word')



    def timer(self, evt=None):
        if self.sec > 0:
            self.sec = self.sec - 1
            self.time_entry.configure(text=self.sec)
            self.canvas.after(1000, self.timer)
            if self.sec == 0:
                self.game_over()
                self.time_entry.configure(state='disabled')
    
    def game_over(self):
        self.clear_text()
        self.input_text.configure(state='disabled')
        self.cpm = round(sum(len(c) for c in self.typed_words)/MINUTE)
        self.wpm = round(len(self.typed_words)/MINUTE)
        self.cpm_entry.configure(text=self.cpm)
        self.wpm_entry.configure(text=self.wpm)




def main():
    window = Tk()
    myapp = MainWindow(window)
    window.mainloop()


if __name__ == "__main__":
    main()
