import customtkinter
from math import *

app = customtkinter.CTk()
app.geometry('360x390')
app.title('Calculator')
def calcular():
    calcuator = output.get('0.0', 'end')
    result = eval(calcuator)
    output.delete('0.0', 'end')
    output.insert('0.0', result)
Font1 = ('Gotham Pro',20,'bold')

output = customtkinter.CTkTextbox(app, width=340, height=60,corner_radius=10, border_width=2, border_color='#000000', font=Font1)
output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)


button_1 = customtkinter.CTkButton(app,text='1', command= lambda:output.insert('end', 1),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_1.grid(row=1, column=0, padx=5, pady=5)


button_2 = customtkinter.CTkButton(app,text='2', command= lambda:output.insert('end', 2),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_2.grid(row=1, column=1, padx=5, pady=5)


button_3 = customtkinter.CTkButton(app,text='3', command=lambda:output.insert('end', 3),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_3.grid(row=1, column=2, padx=5, pady=5)


button_4 = customtkinter.CTkButton(app,text='4', command=lambda:output.insert('end', 4),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_4.grid(row=2, column=0, padx=5, pady=5)


button_5 = customtkinter.CTkButton(app,text='5', command=lambda:output.insert('end', 5),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_5.grid(row=2, column=1, padx=5, pady=5)


button_6 = customtkinter.CTkButton(app,text='6', command=lambda:output.insert('end', 6),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_6.grid(row=2, column=2, padx=5, pady=5)


button_7 = customtkinter.CTkButton(app,text='7', command=lambda:output.insert('end', 7),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_7.grid(row=3, column=0, padx=5, pady=5)


button_8 = customtkinter.CTkButton(app,text='8', command=lambda:output.insert('end', 8),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_8.grid(row=3, column=1, padx=5, pady=5)


button_9 = customtkinter.CTkButton(app,text='9', command=lambda:output.insert('end', 9),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_9.grid(row=3, column=2, padx=5, pady=5)


button_0 = customtkinter.CTkButton(app, text='0', command= lambda:output.insert('end', 0),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_0.grid(row=4, column=0, padx=5, pady=5)


button_delete = customtkinter.CTkButton(app,text='Clear', command=lambda:output.delete('0.0', 'end'),fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_delete.grid(row=4, column=1, padx=5, pady=5)


button_calculator = customtkinter.CTkButton(app,text='=', command=calcular, fg_color="#000000", corner_radius=10, width=80, height=55, font=Font1)
button_calculator.grid(row=4, column=2, padx=5, pady=5)


button_sum = customtkinter.CTkButton(app,text='+', command=lambda:output.insert('end', '+'),fg_color="#FF4500",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=Font1)
button_sum.grid(row=1, column=3, padx=5, pady=5)


button_s = customtkinter.CTkButton(app,text='-', command=lambda:output.insert('end', '-'),fg_color="#FF4500",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=Font1)
button_s.grid(row=2, column=3, padx=5, pady=5)


btn_multip = customtkinter.CTkButton(app,text='x', command=lambda:output.insert('end', '*'),fg_color="#FF4500",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=Font1)
btn_multip.grid(row=3, column=3, padx=5, pady=5)


button_divide = customtkinter.CTkButton(app,text='/', command=lambda:output.insert('end', '/'),fg_color="#FF4500",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=Font1)
button_divide.grid(row=4, column=3, padx=5, pady=5)

button_cos = customtkinter.CTkButton(app,text='cos',command=lambda:output.insert('end',':)'),fg_color="#FF4500",hover_color="#EA5738",corner_radius=10, width=80, height=55, font=Font1)
button_cos.grid(row=5,column=3, padx=5, pady=5)

button_sin = customtkinter.CTkButton(app,text='sin',command=lambda:output.insert('end',':)'),fg_color="#FF4500",hover_color="#EA5738",corner_radius=10, width=80, height=55, font=Font1)
button_sin.grid(row=5,column=2, padx=5, pady=5)
button_st = customtkinter.CTkButton(app,text='**',command=lambda:output.insert('end',':)'),fg_color="#FF4500",hover_color="#EA5738",corner_radius=10, width=80, height=55, font=Font1)
button_st.grid(row=5,column=1, padx=5, pady=5)


app.mainloop()