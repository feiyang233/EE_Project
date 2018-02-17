import mysqlwrite
import copy
import uniform
import tkinter as tk


window = tk.Tk()
window.title('Welcome')
window.geometry('450x400')

var_list = tk.StringVar()
var_list.set(('E1-06','BIZ2-B1','CANTEEN','ARTS-CTN-02','LT4','YIH-05','SDE1-05','I3-02','CCELIB-CL-05'))

tk.Label(window, text='location: ').place(x=50, y= 20)
tk.Label(window, text='Date: ').place(x=50, y= 60)
lb=tk.Listbox(window,listvariable=var_list)
lb.place(x=130, y= 160)

var_location = tk.StringVar()
var_location.set('E1-06')
entry_location= tk.Entry(window, textvariable=var_location)
entry_location.place(x=160, y=20)

var_date = tk.StringVar()
var_date.set('20180203')
entry_date = tk.Entry(window, textvariable=var_date)
entry_date.place(x=160, y=60)

def print_selection():
    value = lb.get(lb.curselection())   #获取当前选中的文本
    var_location.set(value)     #为label设置值

def run():
	date=var_date.get()
	location=var_location.get()
	var_list.set('')
	try:
		filename=copy.copy(date,location)
		
		lb.insert('end', 'download success')
		lb.insert('end', '')

		uniform.unify(filename)
		lb.insert('end', 'preprocess success')
		lb.insert('end', '')

		mysqlwrite.mysqlwrite(filename,location)
		lb.insert('end', 'writeMySQL success')
		lb.insert('end', '')

	except ValueError:
		var_list.set('invalid_address')



def reset():
	var_list.set(('E1-06','BIZ2-B1','CANTEEN','ARTS-CTN-02','LT4','YIH-05','SDE1-05','I3-02','CCELIB-CL-05'))
	

btn_run = tk.Button(window, text='run', command=run)
btn_run.place(x=150, y=100)
btn_reset = tk.Button(window, text='reset', command=reset)
btn_reset.place(x=250, y=100)

btn_input = tk.Button(window, text='input', command=print_selection)
btn_input.place(x=350, y=100)

window.mainloop()


