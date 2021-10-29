from tkinter import *
from tkinter import filedialog, ttk, messagebox
from tkinter.ttk import *
import tkinter as tk
import csv

import defs.database
from defs.check import calcTime, logCheck, checkTimeDif
from defs.database import insertDataBase

#################################################################################

def get_file_csv(file_entry):
    file_name = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                           filetype=(("csv files", "*.csv"),
                                                     ("All Files", "*.*")))
    entry_csv["text"] = file_name
    file_entry.delete(0, END)
    file_entry.insert(0, file_name)
    return None


def reader_csv():
    file = entry_csv["text"]
    csv_file = r"{}".format(file)

    if csv_file[-4:] == ".csv":

        with open(file, "r", encoding='utf-8') as file:

            error_log = list()

            reader = csv.DictReader(file)
            key_set = set()

            for row in reader:
                id = row["id_usuario"]
                initial_dat = row["data_inicio"]
                final_dat = row["data_fim"]
                initial_time = row["hora_inicio"]
                final_time = row["hora_fim"]
                row["total_hora"] = calcTime(final_time, initial_time)
                work_time = calcTime(final_time, initial_time)

                if logCheck(id, initial_dat, final_dat, key_set, error_log):
                    if checkTimeDif(initial_time, final_time):
                        insertDataBase(id, initial_dat, initial_time, final_dat, final_time, work_time)
    labelView()

def info_table():
    tv.delete(*tv.get_children())
    query = "SELECT * FROM employee"
    rows = defs.database.allUser(query)
    for r in rows:
        tv.insert("", "end", values=r)

def search_view():
    tv2.delete(*tv2.get_children())
    row = defs.database.searchUser(search.get())
    if row[1] == [(None,)]:
        messagebox.showerror("Search Error", "Matricula Invalida")
    else:
        tv2.insert("", "end", values=(row[0], row[1]))

def clearEntry():
    entry_csv.delete(0, END)

def clearSearch():
    search.delete(0, END)

def labelView():
    Label(ws, text='Uploaded Successfully!', foreground='green').place(width=200, height=18, x=235, y=115)


###############################################################################

ws = Tk()
ws.title('CSV READER')
ws.geometry('600x700')
ws.pack_propagate(False)
ws.resizable(0, 0)

style = Style()
style.configure('W.TButton', foreground='green', background='green')

entry_csv = Entry(ws, text="")
entry_csv.place(width=340, height=25, x=100, y=40)

search = Entry(ws, text="")
search.place(width=450, height=25, x=17, y=165)


#############################################################################

bt_choose = Button(ws, text="Choose", command=lambda: get_file_csv(entry_csv))
bt_choose.place(width=60, height=25, x=450, y=40)

bt_upload = Button(ws, text="Upload", style='W.TButton', command=lambda: [reader_csv(), clearEntry(), info_table()])
bt_upload.place(width=150, height=30, x=225, y=80)

bt_search = Button(ws, text="Search", command=lambda: [search_view(), clearSearch()])
bt_search.place(width=100, height=25, x=470, y=165)

bt_update = Button(ws, text="Update", command=lambda: info_table())
bt_update.place(width=150, height=30, x=225, y=600)

############################################################################

sep = ttk.Separator(ws, orient='horizontal')
sep.place(width=700, height=0, x=0, y=145)

##############################################################################

frame2 = tk.Label(ws)
frame2.place(height=80, width=560, x=17, y=210)

tv2 = ttk.Treeview(frame2, columns=('MT', 'TTH'), show='headings')
tv2.place(height=80, width=560, x=17, y=210)

tv2.column('MT', width=100, anchor=tk.CENTER)
tv2.column('TTH', width=450, anchor=tk.CENTER)
tv2.heading('MT', text='MATRICULA', anchor=tk.CENTER)
tv2.heading('TTH', text='TOTAL HORA', anchor=tk.CENTER)
tv2.pack()

###############################################################################

frame1 = tk.Label(ws)
frame1.place(height=250, width=560, x=17, y=300)

tv = ttk.Treeview(frame1,columns=('ID', 'MT', 'DS', 'HS', 'DE', 'HE', 'TH'), show='headings')
tv.place(height=250, width=560, x=17, y=300)

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv.yview)
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv.xview)
tv.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")
tv.column('ID', width=15, anchor=tk.CENTER)
tv.column('MT', width=85, anchor=tk.CENTER)
tv.column('DS', width=85, anchor=tk.CENTER)
tv.column('HS', width=85, anchor=tk.CENTER)
tv.column('DE', width=85, anchor=tk.CENTER)
tv.column('HE', width=85, anchor=tk.CENTER)
tv.column('TH', width=85, anchor=tk.CENTER)
tv.heading('ID', text='ID', anchor=tk.CENTER)
tv.heading('MT', text='MAT', anchor=tk.CENTER)
tv.heading('DS', text='DT_START', anchor=tk.CENTER)
tv.heading('HS', text='HR_START', anchor=tk.CENTER)
tv.heading('DE', text='DT_END', anchor=tk.CENTER)
tv.heading('HE', text='HR_END', anchor=tk.CENTER)
tv.heading('TH', text='TOTALH', anchor=tk.CENTER)
info_table()
tv.pack()

ws.mainloop()