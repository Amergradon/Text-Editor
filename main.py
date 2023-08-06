import tkinter
import tkinter.scrolledtext
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import time

def add_time():
    texteditor.insert(END, time.strftime("%H:%M:%S"))

def save_font(fontwin, fontname, fontsize):
    texteditor.config(font=(fontname, fontsize))
    fontwin.destroy()

def selectfont():
    font_names = ["Consolas", "Arial", "Verdana", "Comic Sans MS"]
    font_size = []
    for i in range(2, 51):
        font_size.append(str(i))
    fontwin = Toplevel(window)
    fontwin.title("Text editor - Choose font")
    fontwin.config(bg="#FFFFFF")
    fontwin.attributes('-topmost', 1)

    lbl_title = Label(fontwin, bg="#FFFFFF", font=("Arial", 20), text="Font")
    lbl_title.grid(row=0, column=0, sticky="w")

    cmb_font = ttk.Combobox(fontwin, values=font_names)
    cmb_font.set(value="Consolas")
    cmb_font.grid(row=1, column=0)

    cmb_fontsize = ttk.Combobox(fontwin, values=font_size)
    cmb_fontsize.set(value="12")
    cmb_fontsize.grid(row=1, column=1)

    btn_save = ttk.Button(fontwin, text="Save and close", command=lambda: save_font(fontwin, cmb_font.get(), cmb_fontsize.get()))
    btn_save.grid(row=2, column=0, sticky="news")

    btn_close = ttk.Button(fontwin, text="Close", command=lambda: fontwin.destroy())
    btn_close.grid(row=2, column=1, sticky="news")

    fontwin.mainloop()

def thememode(mode):
    if mode == "light":
        menu_bg = "#FFFFFF"
        menu_fg = "#000000"

        menu_activebg = "#A0A0A0"
        menu_activefg = "#000000"
        texteditor.config(bg="#FFFFFF", fg="#000000")
        menu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
        filemenu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
        editmenu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
        helpmenu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
        thememenu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
        toolmenu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
    elif mode == "dark":
        menu_bg = "#404040"
        menu_fg = "#FFFFFF"

        menu_activebg = "#FFFFFF"
        menu_activefg = "#000000"
        texteditor.config(bg="#202020", fg="#FFFFFF")
        menu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
        filemenu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
        editmenu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
        helpmenu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
        thememenu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)
        toolmenu.config(bg=menu_bg, fg=menu_fg, activebackground=menu_activebg, activeforeground=menu_activefg)

    else:
        pass

def autosave_function():
    global file_dir
    if file_dir != "":
        file = open(file_dir, "w")
        file.write("")
        file.write(texteditor.get(0.0, END))
        file.close()
    if autosave.get():
        window.after(100, autosave_function)


def open_settings():
    global settings_openclose
    if settings_openclose == 1:
        frm_settings.grid(row=0, column=0, sticky="news")
        settings_openclose = 0
    else:
        frm_settings.grid_forget()
        settings_openclose = 1


def about_texteditor():
    info = """
Text Editor
Version: v4
"""
    messagebox.showinfo("Text Editor", info)


def copy_command():
    texteditor.event_generate("<<Copy>>")


def cut_command():
    texteditor.event_generate("<<Cut>>")


def paste_command():
    texteditor.event_generate("<<Paste>>")


def showtoolmenu(event):
    toolmenu.post(event.x_root, event.y_root)


def new_file():
    global file_dir
    file_dir = ""


def open_file():
    global file_dir
    file_dir = filedialog.askopenfilename(title="Open a file", filetypes=(('Text files', ".txt"), ("All", "*.*")))

    if file_dir != "":
        if messagebox.askyesno(title="Text Editor",
                               message="Do you want to close the current file and open a new project?"):
            file = open(file_dir, "r")
            texteditor.delete(0.0, END)
            texteditor.insert(END, file.read())
            file.close()


def save_file():
    global file_dir
    if file_dir == "":
        messagebox.showerror("Text Editor", "Cannot save - no file opened.")
    else:
        file = open(file_dir, "w")
        file.write("")
        file.write(texteditor.get(0.0, END))
        file.close()


def main():
    global toolmenu
    global texteditor
    global file_dir
    global frm_settings
    global settings_openclose
    global autosave
    global window
    global menu, filemenu, editmenu, helpmenu, thememenu, toolmenu
    editor_font = ("Consolas", 12)
    file_dir = ""
    settings_openclose = 1

    window = Tk()
    window.title("Text Editor")
    window.geometry("1000x500")
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    menu = Menu(window)
    window.config(menu=menu)

    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(menu=filemenu, label="File")
    filemenu.add_command(label="New", command=new_file)
    filemenu.add_command(label="Open", command=open_file)
    filemenu.add_command(label="Save", command=save_file)
    autosave = IntVar(value=0)
    filemenu.add_checkbutton(label="Autosave", variable=autosave, command=autosave_function)

    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=lambda: window.quit())

    editmenu = Menu(menu, tearoff=0)
    menu.add_cascade(menu=editmenu, label="Edit")
    editmenu.add_command(label="Cut", command=cut_command)
    editmenu.add_command(label="Copy", command=copy_command)
    editmenu.add_command(label="Paste", command=paste_command)
    editmenu.add_separator()

    thememenu = Menu(menu, tearoff=0)
    editmenu.add_cascade(menu=thememenu, label="Theme")
    themevariable = IntVar()
    thememenu.add_checkbutton(label="Light mode", variable=themevariable,command=lambda: thememode("light"), onvalue=0, offvalue=1)
    thememenu.add_checkbutton(label="Dark mode",  variable=themevariable, command=lambda: thememode("dark"), onvalue=1, offvalue=0)

    editmenu.add_command(label="Font", command=selectfont)

    editmenu.add_separator()

    editmenu.add_command(label="Add Time", command=add_time)

    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(menu=helpmenu, label="Help")
    helpmenu.add_command(label="About", command=about_texteditor)


    toolmenu = Menu(window, tearoff=0)
    toolmenu.add_command(label="Cut", command=cut_command)
    toolmenu.add_command(label="Copy", command=copy_command)
    toolmenu.add_command(label="Paste", command=paste_command)


    texteditor = tkinter.scrolledtext.ScrolledText(window, bg="#FFFFFF", borderwidth=0, font=editor_font)
    texteditor.grid(row=0, column=0, sticky="news")

    thememode("light")

    texteditor.bind("<Button-3>", showtoolmenu)
    window.mainloop()


if __name__ == '__main__':
    main()
