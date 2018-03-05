import mysqlwrite
import copy #从共享文档下载解压
import uniform
import main_rate
import tkinter as tk

op0=['CELC','E1','E2','E3','E4','E5','EW2','SDE1','SDE2','SDE3','EA','E2A','E1A','E3A','E4A',\
        'EW1','TLAB','UCC','YSTCM','LT1','LT2','LT3','LT4','LT5','LT6','LT7','LT7A']
op1=['CL','KR11','CCELIB','KR12A','S2S']
op2=[]
op3=[]
op4=[]
op5=[]
op6=[]
op7=[]
OPTION_dic = {
    'ENGADM':op0,
    'CCELIB':op1,
    'FBA':op2,
    'SCI':op3,
    'ARTS':op5,
    'MEDFOD':op6,
    'Utown':op7
}
OPTIONS = ["ENGADM","CCELIB","FBA","ARTS","MEDFOD","SCIYIH","Utown"]

OPTIONS_floor=['01','02','03','04','05','06','07']

window = tk.Tk()
window.title('Welcome')
window.geometry('450x450')

var_list = tk.StringVar()
var_list.set(('E1-06','CANTEEN','ARTS-CTN-02','LT4','YIH-02','I3-02','CCELIB-CL-05'))

tk.Label(window, text='Zone: ').place(x=50, y= 20)
tk.Label(window, text='Building: ').place(x=50, y= 60)
tk.Label(window, text='Floor: ').place(x=50, y= 100)
tk.Label(window, text='Date: ').place(x=50, y= 140)
tk.Label(window, text='Hot place: ').place(x=50, y= 250)

lb=tk.Listbox(window,listvariable=var_list)
lb.place(x=130, y= 200)

variable_zone = tk.StringVar()
variable_zone.set('Zone') # default value
option_zone =tk.OptionMenu(window, variable_zone,*OPTIONS)
option_zone.place(x=160, y=20)

var_build = tk.StringVar()
var_build.set('Building')
option_build =tk.OptionMenu(window, var_build,'Building')
option_build.place(x=160, y=60)

var_floor = tk.StringVar()
var_floor.set('Floor')
option_floor =tk.OptionMenu(window, var_floor,*OPTIONS_floor)#*就是未知参数个数时使用的
option_floor.place(x=160, y=100)

var_date = tk.StringVar()
var_date.set('20180301')
entry_date = tk.Entry(window, textvariable=var_date)
entry_date.place(x=160, y=140)

var_location=''
def quick_run():
	date=var_date.get()
	value = lb.get(lb.curselection())   #获取当前选中的文本
	location=value   #为label设置值
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

		main_rate.rate(filename) #计算速率
		lb.insert('end', 'Rate success')
		lb.insert('end', '')


	except ValueError:
		var_list.set('invalid_address')
    
    
def run():
	date=var_date.get()
	location=var_build.get()+'-'+var_floor.get()   #need change
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

		main_rate.rate(filename) #计算速率
		lb.insert('end', 'Rate success')
		lb.insert('end', '')


	except ValueError:
		var_list.set('invalid_address')

def reset():
	var_list.set(('E1-06','CANTEEN','ARTS-CTN-02','LT4','YIH-02','I3-02','CCELIB-CL-05'))

def ok1():
	print(variable_zone.get())
	if variable_zone.get()=='ENGADM':
		option_build =tk.OptionMenu(window, var_build,*op0)
		option_build.place(x=160, y=60)
	elif variable_zone.get()=='CCELIB':
		option_build =tk.OptionMenu(window, var_build,*op1)
		option_build.place(x=160, y=60)


def ok2():
	build=var_build.get()
	

button1 = tk.Button(window, text="OK", command=ok1)
button1.place(x=400,y=20)

button2 = tk.Button(window, text="OK", command=ok2)
button2.place(x=400,y=60)

btn_run = tk.Button(window, text='run', command=run)
btn_run.place(x=150, y=170)
btn_reset = tk.Button(window, text='reset', command=reset)
btn_reset.place(x=250, y=170)

btn_input = tk.Button(window, text='input', command=quick_run)
btn_input.place(x=350, y=170)



window.mainloop()


