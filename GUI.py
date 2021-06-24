from tkinter import *

from hikisapi import Hikvision

class Main_window(Tk):
    
    def __init__(self):
        super().__init__()
        self.main_window = Tk()
        self.main_window.title("HIKVISION VMS")
        self.main_window.geometry('1100x700')

        self.cameras_list = Listbox(self.main_window, width=23, height=20)
        self.cameras_list.place(x=2, y=30)
        self.cameras_list_label = Label(self.main_window, text='List of cameras', bg='white', font="Arial 8")
        self.cameras_list_label.place(x=5, y=35)

        self.add_device_btn = Button(self.main_window, text="Add device", command=self.add_device_window)
        self.add_device_btn.place(x=0, y=1)

        self.del_device_btn = Button(self.main_window, text="Delete device")
        self.del_device_btn.place(x=75, y=1)
    
    def add_device_window(self):
        
        self.remove_label()
        self.device_window = Tk()
        self.device_window.title("Device add")
        self.device_window.geometry('260x180')

        self.ip = Entry(self.device_window,width=15)  
        self.ip.place(x=80, y=40)
        self.ip_lbl = Label(self.device_window, text="IP adress:")
        self.ip_lbl.place(x=13, y=38)

        self.port = Entry(self.device_window,width=3)  
        self.port.place(x=80, y=65)
        self.port_lbl = Label(self.device_window, text="Port:")
        self.port_lbl.place(x=13, y=63)

        self.user =  Entry(self.device_window,width=10)  
        self.user.place(x=80, y=90)
        self.user_lbl = Label(self.device_window, text="User:")
        self.user_lbl.place(x=13, y=88)

        self.password = Entry(self.device_window,width=10)  
        self.password.place(x=80, y=115)
        self.password_lbl = Label(self.device_window, text="Password:")
        self.password_lbl.place(x=13, y=113)

        self.add_btn = Button(self.device_window, text="Add device", command=self.add_device_to_list())
        self.add_btn.place(x=80, y=140)

        self.cancel_btn = Button(self.device_window, text="Cancel", command=self.device_window.destroy)
        self.cancel_btn.place(x=160, y=140)

    def add_device_to_list(self):
        model_name = Hikvision('192.168.1.155', 'admin', 'Admin1337')
        self.cameras_list.insert(6, model_name.get_model_name())
    def remove_label(self):
        self.cameras_list_label.configure(text="")


a = Main_window()
a.mainloop()