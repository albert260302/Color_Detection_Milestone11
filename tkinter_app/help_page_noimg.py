from tkinter import *

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

        # Calculate the new font sizes based on the window height
        title_font_size = int(24 * (event.height / 540))  # 540 is the initial canvas height
        titletext_font_size = int(14 * (event.height / 540))
        text_font_size = int(12 * (event.height / 540))  # 540 is the initial canvas height
        button_font_size = int(16 * (event.height / 540))  # 540 is the initial canvas height

        # Set the new font sizes for the text elements in the canvas
        self.itemconfig("title_tag", font=("Arial", title_font_size))
        self.itemconfig("text_tag", font=("Arial", text_font_size))
        self.itemconfig("button_tag", font=("Arial", button_font_size))
        self.itemconfig("titletext_tag", font=("Arial", titletext_font_size))

def on_back_click(event):
    print("Back button clicked!") # Replace this function with the desired action when the "Back" button is clicked
    
def on_back_enter(event):
    # Change the mouse cursor to the hand icon when hovering over the "Back" button
    mycanvas.config(cursor="hand2")
def on_back_leave(event):
    # Change the mouse cursor back to the default arrow when leaving the "Back" button
    mycanvas.config(cursor="arrow")

def main():
    global mycanvas
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe, width=720, height=540, bg="white", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)
    
    # add some widgets to the canvas
    mycanvas.create_rectangle(0, 0, 720, 67, fill="#D9D9D9", outline="#D9D9D9")
    mycanvas.create_text(360, 30, text="Help", fill="#000000", font='Arial 24', tags="title_tag")
    mycanvas.create_text(360, 90, text="Berikut beberapa cara menggunakan aplikas color detection", fill="#000000", font='Arial 12', tags="titletext_tag")
    mycanvas.create_text(180, 230, text="1. Dengan menggunakan fitur kamera", fill="#000000", font='Arial 12', tags="titletext_tag")
    mycanvas.create_text(180, 255, text="- tekan tombol START saat membuka aplikasi", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.create_text(156, 275, text="- Arahkan kamera ke benda yang dituju", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.create_text(129, 295, text="- lalu tekan tombol “take photo” ", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.create_text(520, 230, text="2. Dengan menggunakan fitur galeri", fill="#000000", font='Arial 12', tags="titletext_tag")
    mycanvas.create_text(530, 255, text="- tekan tombol START saat membuka aplikasi", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.create_text(470, 275, text="- tekan tombol “open gallery”", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.create_text(475, 295, text="- pilih gambar yang diinginkan", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.create_rectangle(26, 440, 131, 480, fill="#D9D9D9", outline="#D9D9D9", tags=["back_button"])
    mycanvas.create_text(78, 460, text="Back", fill="#000000", font='Arial 16', tags=["button_tag", "back_button"])
    mycanvas.create_rectangle(0, 494, 720, 540, fill="#D9D9D9", outline="#D9D9D9")
    mycanvas.create_text(365, 515, text="Created By ....", fill="#000000", font='Arial 12', tags="text_tag")
    mycanvas.pack()
    # tag all of the drawn widgets
    mycanvas.addtag_all("all")

    # Bind the back button to the on_back_click function
    mycanvas.tag_bind("back_button", "<Button-1>", on_back_click)
    mycanvas.tag_bind("back_button", "<Enter>", on_back_enter)
    mycanvas.tag_bind("back_button", "<Leave>", on_back_leave)

    root.mainloop()

if __name__ == "__main__":
    main()