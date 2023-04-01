from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
import os

root = Tk()

r = IntVar()
r.set("1")


def startgame(number):
    if number == 1:
        # root.destroy()
        os.system("python cpu.py")
    if number == 2:
        # root.destroy()
        os.system("python 2p.py")


def quitgame():
    messagebox.showinfo("Message", "THANK YOU FOR PLAYING")
    root.destroy()


def control():
    messagebox.showinfo(
        "CONTROLS", "MOVEMENT\nCPU -- W,S\n2 PLAYERS -- W,S/UPARROW,DOWNARROW\n4 PLAYERS -- W,S/UPARROW,DOWNARROW/O,P/N,M")


root.title("JK PING PONG")

root.attributes("-fullscreen", True)

root.configure(bg="black")

image1 = PhotoImage(file="./media/images/tkimage.png")
root.iconphoto(False, image1)
poppins_font = font.Font(family='Poppins', size=50, weight="bold")
label1 = Label(root, text="JK PING PONG", font=poppins_font,fg="white", bg="black").pack()

img = ImageTk.PhotoImage(Image.open("./media/images/imagenew2.jpg"))
imagelabel = Label(root, image=img)
imagelabel.pack()

label2 = Label(root, text="\n\n\tABOUT THE GAME :-",font=("Poppins", 20, "bold"), bg="black", fg="orange").pack(anchor="w")
label3 = Label(root, text="\t-> This is a basic ping pong game",font=("Poppins", 17), bg="black", fg="#D3D3D3").pack(anchor="w")
label5 = Label(root, text="\t-> First Player to score 5 points wins",font=("Poppins", 17), bg="black", fg="#D3D3D3").pack(anchor="w")
label6 = Label(root, text="\t-> A relax time of 3 seconds will be given at the start and also after each point\n",font=("Poppins", 17), bg="black", fg="#D3D3D3").pack(anchor="w")

label10 = Label(root, text="SELECT MODE : ", font=("Poppins", 20, "bold"), bg="black", fg="#3B71CA").pack()
# font=("Poppins", 10, "bold"),font=("Poppins", 10, "bold")
Radiobutton(root,text="CPU",font=("Poppins", 10, "bold"),  variable=r,value=1,bg="#14A44D", width=10).pack()
Radiobutton(root,text="2 PLAYERS",font=("Poppins", 10, "bold"),variable=r,value=2,bg="#14A44D", width=10).pack()
label7=Label(root,text="\n",bg="black").pack()
button1 = Button(root, text="\nCONTROLS\n", font=("Poppins", 10, "bold"), fg="white", command=control,bg="#14A44D", width=20).pack()
label8 = Label(root, text="\n", bg="black").pack()
button2 = Button(root, text="\nSTART THE GAME\n", font=("Poppins", 10, "bold"), fg="white", bg="#14A44D",command=lambda: startgame(r.get()), width=20).pack()
label9 = Label(root, text="\n", bg="black").pack()
button3 = Button(root, text="\nQUIT GAME\n", font=("Poppins", 10, "bold"), fg="white", bg="#14A44D",command=quitgame, width=20).pack()

root.mainloop()
