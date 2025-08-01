
import os
import re
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import Button,StringVar,Label,Radiobutton,messagebox
from tkinter.filedialog import *
from pywhispercpp.model import Model
from pywhispercpp.utils import output_vtt
from tkinter import filedialog

def run():
    # user selects file
    ftypes=(('mp3','.mp3'),('all','.*'),('m4a','.m4a'),("wav",'.wav'))
    var1=StringVar()
    fname=filedialog.askopenfilename(parent=root,initialdir = "~/Music",filetypes=ftypes,title='Select audio file',typevariable=var1)
    x = ""
    if len(fname) > 3:
        x = mytest(fname) # test to see if the file can be converted
        # messagebox.showinfo("Note","Operation Cancelled")

    if len(x) > 3:
        answer = messagebox.askyesno("Process file?",x)
        if answer == True:
            vttGO(x) # process the file


tiny_model = Model(
    model="MODELS/ggml-tiny.bin",
    models_dir="MODELS",
    params_sampling_strategy=0,
    redirect_whispercpp_logs_to=False
)

#base_model = Model(
#    model="MODELS/ggml-base.en.bin",
#    models_dir="MODELS",
#    params_sampling_strategy=0,
#    redirect_whispercpp_logs_to=False
#)


turbo_model = Model(
    model="MODELS/ggml-large-v3-turbo.bin",
    models_dir="MODELS",
    params_sampling_strategy=0,
    redirect_whispercpp_logs_to=False
)

 #test if whispercpp can process the File
def mytest(input_f):
    try:
        segments = tiny_model.transcribe(input_f,duration_ms=1000)
        #print(segments)
        print("File veridicated")
    except:
        print("File not veridicated")
        messagebox.showinfo("Note","Invalid File Type")
        input_f = ""
    return input_f

# process
def vttGO(input_f):
    segments = turbo_model.transcribe(input_f, new_segment_callback=print) #callback function that will be called when a new segment is generated
    out_f = output_vtt(segments, input_f)
    f = (str(out_f))
    out_txt = re.sub("\....\.vtt", ".txt", f) # rename file
    os.rename(out_f,out_txt)

    Label(myframe,text=f'\n{out_txt}',font="courier 12 bold",background="white").pack()

    messagebox.showinfo("Done","New File Generated")


def label(anchor,words):
    var = StringVar()
    var.set(words)
    tk.Label(anchor,textvariable = var,fg = "black", font = "lato 12 bold",bg="white",).pack(padx=2, pady=2)


root = tk.Tk()
root.title("WaldenSTT Beta: Turbo Edition")
root.config(bg="white")
root.geometry("600x600+50+50")
root.geometry("800x400")
label(root,"")

# interface heading
tk.Label(root,text="WALDEN Speech to Text Control Panel",fg = "brown", font = "lato 14 bold",bg="white").pack(padx=2, pady=2)
label(root,"\nConvert a 60 minute mp3 to text\n in less than 20 minutes!")
label(root,"")


# Buttons to control the interface
button_frame = tk.Frame(root,relief=GROOVE,background="white")
button_frame.pack(pady=5,side="top")
tk.Button(button_frame, text = "Exit", command = "exit",fg = "black", font = "lato 11",bd = 2, bg = "white").pack(padx=5, pady=5, side="right")
tk.Button(button_frame, text = "Run", command = run,fg = "black", font = "lato 11",bd = 2, bg = "white").pack(padx=5, pady=5,side="left")


# Make a spot to print out the finished files
label(root,"Output")
myframe = tk.Frame(root,border="4",width="500",height="300",relief=GROOVE,background="white")
myframe.pack(pady=5,fill="both",expand=True)

label(root,"")


root.mainloop()
