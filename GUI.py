from tkinter import *

top = Tk()
top.title("美团测评")

labelframe = LabelFrame(top, width=240, height=200)
labelframe.grid(column=0, row=0, rowspan = 8, padx = 8, pady = 8)

labelframe1 = LabelFrame(labelframe, text = "", width = 280, height = 280)
labelframe1.grid(column=0, row=0, rowspan = 6, padx=8)

label8 = Label(labelframe1, text="福州最受欢迎的商圈").grid(row=0)

button1_text = Button(labelframe1, text = '查询', font = ('宋体','12'))
button1_text.grid(column = 0, row = 1 , padx = 8, pady = 8)

label4 = Label(labelframe1, text="福州最佳美食聚集地").grid(row=2)


button2_text = Button(labelframe1, text = '查询', font = ('宋体','12'))
button2_text.grid(column = 0, row = 6, padx = 8, pady = 8)

label7 = Label(labelframe1, text="福州服饰类综合评分最高的商圈").grid(row=10)

button3_text = Button(labelframe1, text = '查询', font = ('宋体','12'))
button3_text.grid(column = 0, row = 12, padx = 8, pady = 8)

labelframe2 = LabelFrame(labelframe, text = "")
labelframe2.grid(column=1, row=0, padx = 8, sticky=N)

label8 = Label(labelframe2, text="福州人均消费（性价比最高）的前五家美食餐厅").grid(row=0)


button4_text = Button(labelframe2, text = '50以下', font = ('宋体','12'))
button4_text.grid(column = 0, row = 1, padx = 8, pady = 8)

button5_text = Button(labelframe2, text = '50-100', font = ('宋体','12'))
button5_text.grid(column = 0, row = 2, padx = 8, pady = 8)

button6_text = Button(labelframe2, text = '100-200', font = ('宋体','12'))
button6_text.grid(column = 0, row = 3, padx = 8, pady = 8)

button6_text = Button(labelframe2, text = '200以上', font = ('宋体','12'))
button6_text.grid(column = 0, row = 4, padx = 8, pady = 8)



top.mainloop()