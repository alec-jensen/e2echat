from tkinter import *


class ChatRoom(object):

    def __init__(self):
        self.top = Tk()

        self.top.title('WhatChat')
        self.top.geometry('400x600')

        self.message_show = Frame(self.top)
        self.message_sr = Scrollbar(self.message_show)
        self.message_sr.pack(side=RIGHT, fill=Y)
        self.message_text = Text(self.message_show, height=20, width=50,
                                 font=('SimHei', 15))
        self.message_text.config(state=DISABLED)
        self.message_sr.config(command=self.message_text.yview)
        self.message_text.pack(side=LEFT, fill=X)
        self.message_show.pack(anchor=N)

        self.message_input = Frame(self.top)
        self.message_ipt_text = Text(self.message_input, height=15, width=47,
                                     font=('SimHei', 15))
        self.send_msg = Button(self.message_input, text='Send',
                               command=self.send_message,
                               fg='white', bg='blue')
        self.send_msg.pack(side=RIGHT)
        self.message_ipt_text.pack(side=LEFT, fill=X)
        self.message_input.pack(anchor=N)
        self.top.bind('<Return>', self.entersend)

    def entersend(self, e):
        self.send_message()

    def send_message(self):
        pass

    def recv_message(self):
        pass
