from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab

class Draw():
    def __init__(self,root):

        self.root = root
        self.root.title("Painter")
        # self.root.geometry("810x530")
        self.root.configure(background="white")

        #variables for pointer and eraser
        self.pointer = "black"
        self.erase = "white"

        #for tkinter window
        text = Text(root)
        text.tag_configure("tag_name",justify="center",font=('arial',25),background='#292826',foreground='orange')
        text.insert("1.0","Drawing App in Python")

        text.tag_add("tag_name","1.0","end")
        text.pack()

        #pick a color for drawing from control panel
        self.pick_color = LabelFrame(self.root,text='Colors',font=('arial',15),bd=5,relief=RIDGE,bg="white")
        self.pick_color.place(x=0, y=40, width=90, height=190)

        colors = ['blue','red','green', 'orange','violet','black','yellow','purple','pink','gold']
        i=j=0
        for color in colors:
            Button(self.pick_color, bg=color, bd=2, relief=RIDGE, width=3, command=lambda col=color:self.select_color(col)).grid(row=i, column=j)
            i+=1
            if i==5:
                i=0
                j+=1
        
        #erase button
        self.eraser_btn = Button(self.root, text="Eraser", bd=4, bg="white", command=self.eraser, width=9, relief=RIDGE)
        self.eraser_btn.place(x=0, y=197)

        #reset button to clear the entire screen
        self.clear_btn = Button(self.root, text="Clear Screen", bd=4, bg="white", command=lambda : self.background.delete('all'),width=9, relief=RIDGE)
        self.clear_btn.place(x=0, y=227)

        #save button for saving the image
        self.save_btn = Button(self.root, text="Save", bd=4, bg="white", command=self.save_drawing, width=9, relief=RIDGE)
        self.save_btn.place(x=0, y=257)

        #background button for choosing color of the canvas
        self.bg_btn = Button(self.root, text="Background", bd=4, bg="white", command = self.canvas_color, width=9, relief=RIDGE)
        self.bg_btn.place(x=0, y=287)

        #scale for pointer and eraser size
        self.pointer_frame = LabelFrame(self.root, text='size', bd=5, bg="white", font=('arial',15,'bold'), relief=RIDGE)
        self.pointer_frame.place(x=0, y=320, height=200, width=70)

        self.pointer_size = Scale(self.pointer_frame, orient=VERTICAL, from_=48, to=0, length=168)
        self.pointer_size.set(1)
        self.pointer_size.grid(row=0, column=1, padx=15)

        #defining a background color for the canvas
        self.background = Canvas(self.root, bg="white", bd=5, relief=GROOVE, height=470, width=680)
        self.background.place(x=80, y=40)

        self.background.bind("<B1-Motion>",self.paint)


    #funtions are defined here
    #paint function for drawing the lines on canvas
    def paint(self,event):
        x1,y1 = (event.x-2), (event.y-2)
        x2,y2 = (event.x+2), (event.y+2)

        self.background.create_oval(x1, y1, x2, y2, fill=self.pointer, outline=self.pointer, width=self.pointer_size.get())

    #function for choosing the color of pointer
    def select_color(self,col):
        self.pointer = col
    
    #function for defining the eraser
    def eraser(self):
        self.pointer = self.erase

    #funtion for choosing the background color of the canvas
    def canvas_color(self):
        color = colorchooser.askcolor()
        self.background.configure(background=color[1])
        self.erase = color[1]

    #function for saving the image file
    def save_drawing(self):
        try:
            # self.background.update()
            file_ss = filedialog.asksaveasfilename(defaultextension='jpg')
            # print(file_ss)
            x = self.root.winfo_rootx() + self.background.winfo_x()
            y = self.root.winfo_rooty() + self.background.winfo_y()

            x1 = x + self.background.winfo_width()
            y1 = y + self.background.winfo_height()

            ImageGrab.grab().crop((x, y, x1, y1)).save(file_ss)
            messagebox.showinfo("Screenshot successfully save as"+str(file_ss))
        
        except:
            print("error in saving the screenshot")

if __name__ == "__main__":
    root = Tk()
    p = Draw(root)
    root.mainloop()