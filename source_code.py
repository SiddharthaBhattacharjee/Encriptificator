from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
import os
from cryptography.fernet import Fernet
import random
import sys

try:
    directory = "encriptificator_keys"
    parent_dir = "C:/Users/USER/AppData/Local"
    path = os.path.join(parent_dir,directory)
    os.mkdir(path)
except:
    pass

key = b'temp'

# Creating a menu & define function for each menu item
def _main_():
    root = Tk(className="|--ENCRIPTIFICATOR BY SID--|")
    textpad = scrolledtext.ScrolledText(root, width=100, height=80)

    def open_command():
        file = filedialog.askopenfile(parent=root, mode='rb', title='Select a File')
        if file != None:
            contents = file.read()
            textpad.insert('1.0', contents)
            file.close()

    def save_command():
        file = filedialog.asksaveasfile(mode='w') #check
        if file != None:
            # slice off the last character from get, as an extra return is added
            data = textpad.get('1.0', END + '-1c')
            file.write(data)
            file.close()

    def enc_save():
        file = filedialog.asksaveasfile(mode='w') #check
        if file != None:
            # slice off the last character from get, as an extra return is added
            seed = random.randint(100000000,999999999)
            data = textpad.get('1.0', END + '-1c')
            key = Fernet.generate_key()
            fernet = Fernet(key)
            data_s = fernet.encrypt(data.encode())
            s1 = str(data_s)
            l1 = s1.split("'")
            s2 = l1[1]
            data_f = str(seed)+'\n'+s2
            file.write(data_f)
            with open(f"C:/Users/USER/AppData/Local/encriptificator_keys/{seed}.txt",'w') as f:
                k_1 = str(key)
                l_1 = k_1.split("'")
                k_f = l_1[1]
                f.write(k_f)
                f.close()
            file.close()

    def enc_o():
        global key
        def sk():
            global key
            file1 = filedialog.askopenfile(parent=root_p, mode='rb', title='Select a File')
            if file1 != None:
                key = file1.read()
                fernet = Fernet(key)
                decMessage = fernet.decrypt(encMessage).decode()
                            
                textpad.insert('1.0', decMessage)
                file.close()
                root_p.destroy()
        def ca():
            root_p.destroy()

        
        file = filedialog.askopenfile(parent=root, mode='rb', title='Select a File')
        if file != None:
            global key
            em = file.readlines()
            encMessage = em[1]
            s = str(em[0])
            s01 = s.split("'")
            seed = s01[1]
            seed1 = seed[0:9]
            try:
                global key
                f = open(f"C:/Users/USER/AppData/Local/encriptificator_keys/{seed1}.txt",'rb')
                key = f.read()
                fernet = Fernet(key)
                decMessage = fernet.decrypt(encMessage).decode()
                            
                textpad.insert('1.0', decMessage)
                file.close()
            except:
                root_p = Tk()
                root_p.title = 'Key Input'

                t1 = Label(root_p, text = "NO KEY FOUND IN THE SYSTEM FOR THE ENCRIPTED FILE YOU WANT TO OPEN").pack()
                t2 = Label(root_p, text = "Select Key file to decrypt the file you want to open").pack()
                b1 = Button(root_p, text = 'select key', command = sk)
                b2 = Button(root_p, text = 'cancel', command = ca)
                b1.pack()
                b2.pack()
                
                root_p.mainloop()
                


    def exit_command():
        if messagebox.askokcancel('Quit','Do you really want to quit'):
            root.destroy()


    def contact_command():
        label = messagebox.showinfo('Contacts','''Instagram : @progamersid_x
        Email : siddharthabhatt3456@gmail.com
        Whatsaap : 7002744892''')


    def capitalise_text():
        data = textpad.get('1.0', END + '-1c')
        textpad.delete('1.0', END)
        Data = data.upper()
        textpad.insert('1.0',Data)

    def small_text():
        data = textpad.get('1.0', END + '-1c')
        textpad.delete('1.0', END)
        Data = data.lower()
        textpad.insert('1.0',Data)

    def clear_text():
        textpad.delete('1.0', END)

    def Res():
        root.geometry('333x222')
    def B2N():
        root.geometry('690x1000')
    def Full():
        root.geometry('2100x1000')

    def Navigate():
        label = messagebox.showinfo('Navigation',os.getcwd())


    def rClicker(e):
        # right click context menu for all Tk Entry and Text widgets

        try:
            def rClick_Copy(e, apnd=0):
                e.widget.event_generate('<Control-c>')

            def rClick_Cut(e):
                e.widget.event_generate('<Control-x>')

            def rClick_Paste(e):
                e.widget.event_generate('<Control-v>')

            e.widget.focus()

            nclst=[
                   (' Cut', lambda e=e: rClick_Cut(e)),
                   (' Copy', lambda e=e: rClick_Copy(e)),
                   (' Paste', lambda e=e: rClick_Paste(e)),
                   ]

            rmenu = Menu(None, tearoff=0, takefocus=0)

            for (txt, cmd) in nclst:
                rmenu.add_command(label=txt, command=cmd)

            rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

        except TclError:
            print (' - rClick menu, something wrong')
            pass

        return "break"


    def rClickbinder(r):

        try:
            for b in [ 'Text', 'Entry', 'Listbox', 'Label']: #
                r.bind_class(b, sequence='<Button-3>',
                             func=rClicker, add='')
        except TclError:
            print (' - rClickbinder, something wrong')
            pass
    def new():
        exec('_main_()')
        
        
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='Files',menu=filemenu) #assigned all

    editmenu = Menu(menu)
    menu.add_cascade(label='Edit', menu=editmenu)#assigned all

    editmenu.add_command(label='Capitalise Text',command=capitalise_text)#assigned
    editmenu.add_command(label='Lower Text',command=small_text)#assigned
    editmenu.add_command(label='Clear Text',command=clear_text)#assigned

    viewmenu = Menu(menu)
    menu.add_cascade(label='View',menu=viewmenu)#assigned all

    viewmenu.add_command(label='Compact View',command=Res)#assigned
    viewmenu.add_command(label='Normal View',command=B2N)#assigned
    viewmenu.add_command(label='Full View',command=Full)#assigned


    menu.add_command(label='Navigate',command=Navigate)#assigned


    #*** done in new***
    filemenu.add_command(label='New',command=new) #assigned
    filemenu.add_command(label='Open...',command=open_command) #assigned
    filemenu.add_command(label='Open encripted file',command=enc_o)
    savemenu = Menu(filemenu)
    filemenu.add_cascade(label='Save Options',menu=savemenu)
    savemenu.add_command(label='normal Save',command=save_command)#assigned
    savemenu.add_command(label='Encrypt & Save',command=enc_save)
    
    filemenu.add_separator() # new command
    filemenu.add_command(label='Exit',command=exit_command) #assigned

    helpmenu = Menu(menu)

    helpmenu.add_command(label='contact support',command=contact_command) #assigned


    root.bind('<Button-3>',rClicker, add='')

    textpad.pack()

    root.mainloop()
    #***Upto Here***
#main
_main_()
