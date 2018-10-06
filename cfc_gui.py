
import tkinter as tk
from tkinter import font
from tkinter.ttk import *
from cfc_backend import cfc_get_truth_value, token
from wikipedia import PageError, DisambiguationError

bg_color = "#daefee"
s_color = "#95d5ed"
clr_correct = "#b7f287"
clr_false = "#efa162"
counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()


def clear_s():
    txtfields = [txt_obj, txt_obj2, txt_obj3, txt_predicate, txt_predicate2, txt_predicate3, txt_subj1, txt_subj2, txt_subj3, txt_tval1, txt_tval2, txt_tval3]
    for x in txtfields:
        x.config(bg="#ffffff")
    txtfields = [txt_tval1, txt_tval2, txt_tval3]
    for x in txtfields:
        x.delete(0,tk.END)


def clear_styles():
    clr_w = "#ffffff"
    txt_subj1.config(bg = clr_w)
    txt_predicate.config(bg=clr_w)
    txt_obj.config(bg=clr_w)
    txt_subj2.config(bg = clr_w)
    txt_predicate2.config(bg=clr_w)
    txt_obj2.config(bg=clr_w)
    txt_subj3.config(bg = clr_w)
    txt_predicate3.config(bg=clr_w)
    txt_obj3.config(bg=clr_w)
 
def run_fact_checker():
    subject1 = txt_subj1.get()
    subject2 = txt_subj2.get()
    subject3 = txt_subj3.get()

    obj1 = txt_obj.get()
    obj2 = txt_obj2.get()
    obj3 = txt_obj3.get()

    if subject1 == "" or subject2 == "" or subject3 == "":
        tk.messagebox.showerror('Error', 'Please fill out necessary information')
        return

    predicate = txt_predicate.get()
    print(f"Testing statement('{subject1}', '{predicate}', '{obj1})'")
    try:
        truthval1 = cfc_get_truth_value(subject1, obj1, token)
        truthval2 = cfc_get_truth_value(subject2, obj2, token)
        truthval3 = cfc_get_truth_value(subject3, obj3, token)
    except PageError:
        tk.messagebox.showerror("Error", "No matching entry in Wikipedia.")
    except DisambiguationError as e:
        tk.messagebox.showerror("Ambiguous Entity", str(e))

    print("Truth Values are as follows:")
    print(f"Statement 1: {truthval1}")
    print(f"Statement 2: {truthval2}")
    print(f"Statement 3: {truthval3}")

    max_val = max(truthval1, truthval2, truthval3)
    correct_elements = []
    if truthval1 == max_val:
        correct_elements = [txt_subj1, txt_obj, txt_predicate, txt_tval1]
    elif truthval2==max_val:
        correct_elements = [txt_subj2, txt_obj2, txt_predicate2, txt_tval2]
    elif truthval3==max_val:
        correct_elements = [txt_subj3, txt_obj3, txt_predicate3, txt_tval3]

    for x in correct_elements:
        x.config(bg=clr_correct)

    txt_tval1.insert(tk.END, str(truthval1))
    txt_tval2.insert(tk.END, str(truthval2))
    txt_tval3.insert(tk.END, str(truthval3))
    
    
root = tk.Tk()
root.title("Computational Fact Checker")



frame_master = tk.Frame(root, width = 1000, height="1000", bg=bg_color)
frame_master.pack(side='left')

frame_title = tk.Frame(frame_master, padx= 20, pady = 20, bg=bg_color)
frame_title.pack()

lbl_title = tk.Label(frame_title,text="Computational Fact Checking Using Knowledge Graphs", bg=bg_color, font=font.Font(weight="bold"))
lbl_title.pack()

frame_top = tk.Frame(frame_master, bg=bg_color, padx=10)
frame_top.pack(side="top")
canvasleft = tk.Frame(frame_top, bg=bg_color)
canvasleft.pack(side="left", padx=5)
lbl_subject1 = tk.Label(canvasleft,text="Subjects", bg=bg_color)
lbl_subject1.pack()
txt_subj1 = tk.Entry(canvasleft, width="40")
txt_subj2 = tk.Entry(canvasleft, width="40")
txt_subj3 = tk.Entry(canvasleft, width="40")
txt_subj1.pack()
txt_subj2.pack()
txt_subj3.pack()



canvas_mid = tk.Frame(frame_top, bg=bg_color)
canvas_mid.pack(side='left', fill='y',  padx=5)
lbl_pred = tk.Label(canvas_mid,text="Predicate", bg=bg_color)
lbl_pred.pack()
txt_predicate = tk.Entry(canvas_mid,  width="40")
txt_predicate.pack()
txt_predicate2 = tk.Entry(canvas_mid,  width="40")
txt_predicate2.pack()
txt_predicate3 = tk.Entry(canvas_mid,  width="40")
txt_predicate3.pack()

canvas_right = tk.Frame(frame_top, bg=bg_color)
canvas_right.pack(side='left', fill='y',  padx=5)
lbl_obj = tk.Label(canvas_right,text="Object", bg=bg_color)
lbl_obj.pack()
txt_obj = tk.Entry(canvas_right, width="40")
txt_obj.pack()
txt_obj2 = tk.Entry(canvas_right, width="40")
txt_obj2.pack()
txt_obj3 = tk.Entry(canvas_right, width="40")
txt_obj3.pack()

canvas_tvals = tk.Frame(frame_top, bg=bg_color)
canvas_tvals.pack(side='left', fill='y',  padx=5)
lbl_tval = tk.Label(canvas_tvals,text="Truth Value", bg=bg_color)
lbl_tval.pack()
txt_tval1 = tk.Entry(canvas_tvals, width="20")
txt_tval1.pack()
txt_tval2 = tk.Entry(canvas_tvals, width="20")
txt_tval2.pack()
txt_tval3 = tk.Entry(canvas_tvals, width="20")
txt_tval3.pack()

frame_mid = tk.Frame(frame_master, pady="15", bg=bg_color)
frame_mid.pack(side='top')
btn_go = tk.Button(frame_mid, text="Go!", command=run_fact_checker, width=50, bg=s_color)
btn_go.pack()
btn_reset = tk.Button(frame_mid, text="Reset", command=clear_s, width=50, bg=s_color)
btn_reset.pack(side="bottom")




"""
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
buttonstop = tk.Button(root, text='Stop', width=25, command=root.destroy)
buttonstop.pack()
"""

root.mainloop()