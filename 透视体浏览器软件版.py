import tkinter
from webbrowser import*
#导入库
import ctypes
from ttkbootstrap import*

#创建窗口，root可替换成自己定义的窗口



def search():
    b = e1.get()
    if CheckVar1.get()==1:
        open("http://zh.m.wiki.sxisa.org/wiki/"+b)
    if CheckVar2.get()==1:
        open("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd="+b+"&fenlei=256&rsv_pq=de34903400083477&rsv_t=b4d5XteuAhcjh0%2FBpQ9QXdmyv1nYpD1DIe1eh2rdycdtB7Yo7MzO6ZHLCfw&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=18&rsv_sug1=15&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=%25E7%25BD%2591%25E6%2598%2593%25E5%2585%25AC%25E5%25BC%2580%25E8%25AF%25BE&rsp=5&inputT=3120&rsv_sug4=5028"+b)
    if CheckVar3.get()==1:
        open("https://cn.bing.com/search?q="+b+"&form=CHRDEF&sp=-1&pq=%E6%88%91&sc=8-1&qs=n&sk=&cvid=0E66E88FDBCA4485B1F4649966BC6CB8")
    if CheckVar4.get()==1:
        open("https://search.bilibili.com/all?keyword="+b+"&spm_id_from=333.1007")

    
style = Style(theme='cyborg')
root = style.master
root.title('透视体浏览器')

e1 = Entry(bootstyle="primary")
e1.place(relx=0.15, rely=0.05)

#ttk.Button(window, text="Submit", style='success.TButton').pack(side='left', padx=5, pady=10)
#ttk.Button(window, text="Submit", style='success.Outline.TButton').pack(side='left', padx=5, pady=10)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()


ch1 = Checkbutton(root,text='维基',bootstyle="warning-square-toggle",variable = CheckVar1,onvalue=1,offvalue=0)
ch2 = Checkbutton(root,text='百度',bootstyle="primary-square-toggle",variable = CheckVar2,onvalue=1,offvalue=0)
ch3 = Checkbutton(root,text='bing',bootstyle="success-square-toggle",variable = CheckVar3,onvalue=1,offvalue=0)
ch4 = Checkbutton(root,text='哔哩哔哩',bootstyle="danger-square-toggle",variable = CheckVar4,onvalue=1,offvalue=0)
ch1.place(relx=0.1, rely=0.4)
ch2.place(relx=0.1, rely=0.5)
ch3.place(relx=0.1, rely=0.6)
ch4.place(relx=0.1, rely=0.7)
#ch1.pack()
#ch2.pack()
#ch3.pack()
#ch4.pack()

button1 = Button(root, text="搜索", style="primary-outline",command=search)
button1.place(relx=0.75, rely=0.05)


root.geometry('250x250')
root.mainloop()