import tkinter as tk


def cria_tela():
	myWindow = tk.Tk()
	myWindow.title("VOLT")
	myWindow.configure(bg="#1E90FF")
	myWindow.geometry("800x600")

	return myWindow

def main():
	tela = cria_tela()
	tela.mainloop()

main()
# class SimpleApp(object):
#     def __init__(self, master, **kwargs):
#         title=kwargs.pop('title')
#         frame=tk.Frame(master, **kwargs)
#         frame.pack()
#         self.label = tk.Label(frame, text=title)
#         self.label.pack(padx=500,pady=500)


# if __name__=='__main__':
#     root = tk.Tk()
#     app = SimpleApp(root,title='Hello, world')
#     root.mainloop()