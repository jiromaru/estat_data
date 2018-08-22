from tkinter import *
from tkinter import ttk
from get_dict import get_dict

def mk_display():

    select_list=[]
    label_list=[]
    def show_selection():
        global data_dict,appId
        lb.delete(1, END)
        appId=EditBox1.get()
        search_wd=EditBox2.get()
        print("appId : " + appId)
        print("検索ワード : " + search_wd)
        data_dict=get_dict(search_wd,appId)

        for data in data_dict.keys():
            lb.insert(END,data)

    def get_id():

        for i in lb.curselection():
            select_list.append(data_dict[lb.get(i)])
            label_list.append(lb.get(i))
            print("選択項目 : " + "/".join(label_list))
            root.destroy()

    root = Tk()
    root.title('Scrollbar')
    root.geometry("1000x700")

    # Frame1
    frame1 = ttk.Frame(root, padding=1)
    frame1.grid(column=0, row=0, sticky=(N, S, E, W))

    #Label1
    label = Label(frame1,text="【appId】",font=("",10),height=2).grid(column=0, row=0, sticky="w")

    #エントリー1
    EditBox1 = Entry(frame1,width=50)
    EditBox1.grid(column=0, row=1)

    # Frame2
    frame2 = ttk.Frame(root, padding=1)
    frame2.grid(column=0, row=1, sticky=(N, S, E, W))
    
    #Label2
    label = Label(frame2,text="【検索ワード】",font=("",10),height=2).grid(column=0, row=0, sticky="w")

    #エントリー2
    EditBox2 = Entry(frame2)
    EditBox2.grid(column=0, row=1)

    #Button
    button2 = ttk.Button(frame2, text='検索', command=show_selection)
    button2.grid(column=2,row=1, columnspan=2)

    # Frame3
    frame3 = ttk.Frame(root, padding=1)
    frame3.grid(column=0, row=2, sticky=(N, S, E, W))

    # Listbox
    lb = Listbox(frame3,selectmode=MULTIPLE,height=20,width=170)
    lb.grid(row=0, column=0)

    # Scrollbar
    scrollbar = ttk.Scrollbar(frame3,orient=VERTICAL,command=lb.yview)
    lb['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=0,column=1,sticky=(N,S))

    #Button
    button3 = ttk.Button(frame3, text='OK', command=get_id)
    button3.grid(row=1, column=0, columnspan=2)

    root.mainloop()
    
    return select_list,appId

