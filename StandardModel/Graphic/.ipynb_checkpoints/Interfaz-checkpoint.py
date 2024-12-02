from tkinter import *

def MiInterfaz():
	root=Tk()
	
	root.title("Modelo Estándar")
	root.config(bg="steel blue")
	root.resizable(False,False)
	root.geometry("1289x823")
	
	Base = PhotoImage(file="StandardModel/Graphic/BG.png")
	Label(root, image=Base,bd=0).place(x=0, y = 0)
	
	FrameTwo=Frame(root,bg='Gray25', width=200, height=200)
	FrameTwo.config(bd=16,relief="ridge")
	FrameTwo.pack(side="left",anchor="nw")
	ImagenTwo = PhotoImage(file="StandardModel/Graphic/Ciencias.png")
	Label(FrameTwo, image=ImagenTwo).place(x=0, y = 0)
	
	FrameThree=Frame(root,bg='Gray25', width=200, height=200)
	FrameThree.config(bd=16,relief="ridge")
	FrameThree.pack(side="right",anchor="ne")
	ImagenThree = PhotoImage(file="StandardModel/Graphic/UNAM.png")
	Label(FrameThree, image=ImagenThree).place(x=0, y = 0)
	
	FrameOne=Frame(root,bg='Gray25', width=651, height=250)
	FrameOne.config(bd=16,relief="ridge")
	FrameOne.pack(side="top",anchor="n")
	LabelOneOne=Label(FrameOne, text="Mi primer paquete", font=("fixedsys", 29), fg="white", bg=FrameOne.cget("bg"), bd=0)
	LabelOneOne.place(x=100,y=50)
	LabelOneTwo=Label(FrameOne, text="(Modelo Estándar)", font=("fixedsys", 25), fg="white", bg=FrameOne.cget("bg"), bd=0)
	LabelOneTwo.place(x=100,y=100)
	
	##Siempre al final
	root.mainloop()

if __name__ == "__main__":
    app = MiInterfaz()
    app.iniciar()