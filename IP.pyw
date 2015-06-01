import socket
from tkinter import *



hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)

fenetre = Tk()
fenetre.title('Votre IP')

fenetre.config(bg = '#1691BE')

label_ip = Label(fenetre, bg = "#1691BE", text = "Votre IP est: " + str(ip),font="arial 18 bold")
label_ip.pack(side = TOP, padx = 100, pady = 30)
label_info = Label(fenetre, text = "Cette ip peut ne pas être correcte sous Linux, de même si vous utilisez Hamachi ou Tungle pour vous connecter")
label_info.pack(side = TOP, pady = 10)

fenetre.mainloop()

