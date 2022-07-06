import tkinter as tk
def clear_l():

  #canvas1.create_oval(10,10, 400,400, fill="red")
  canvas1.create_oval(10,10, 400,400, fill="darkblue")

  label0 = tk.Label(root, text='Convert Decimal to Gary',font=('helvetica', 12, 'bold'),fg="yellow",bg='darkblue')
  canvas1.create_window(200, 60, window=label0)

  label1 = tk.Label(root, text='MAKE BY DARIUSH DERKI',bg='darkblue',font=('helvetica', 17, 'bold'),fg='red')
  canvas1.create_window(205, 95, window=label1)

  label4 = tk.Label(root, text='TEL : 09179242935',font=('Arial', 12, 'bold'),bg='darkblue',fg="yellow")
  canvas1.create_window(210, 125, window=label4)

  label1 = tk.Label(root, text=' Decimal :',font=('helvetica', 11, 'bold'), bg='blue', fg='yellow')
  canvas1.create_window(130, 155, window=label1)

  buttonAdd = tk.Button(text='Convert', command=convert, bg='red', fg='white', font=('helvetica', 10, 'bold'), width = 10)
  canvas1.create_window(220, 190, window=buttonAdd)

  label2 = tk.Label(root, text='Binary',font=('helvetica', 11, 'bold'), bg='lightgray', fg='red')
  canvas1.create_window(220, 225, window=label2)

  label3 = tk.Label(root, text=' Gary ',font=('helvetica', 11, 'bold'), bg='lightgray', fg='red')
  canvas1.create_window(220, 300, window=label3)
  label4 = tk.Label(root, text='                                           ',font=('helvetica', 15, 'bold'),bg='darkblue')
  canvas1.create_window(210, 260, window=label4)
  label5 = tk.Label(root, text='                                        ',font=('helvetica', 15, 'bold'),bg='darkblue')
  canvas1.create_window(205, 340, window=label5)

    
def convert1(number):

  def convert_gray(binary):
    binary = int(binary, 2)
    binary ^= (binary >> 1)
    return bin(binary)
  #stringnum=input("input decilam number :")
  stringnum=number
  decNum = int(stringnum)
  binary_num = bin(decNum)
  
  clear_l()
  label4 = tk.Label(root, text=binary_num[2:],font=('helvetica', 15, 'bold'),bg='orange')
  canvas1.create_window(220, 260, window=label4)  
  print("binary :",binary_num)
  gray_code = convert_gray(binary_num)
  print("                   GRAY : ",gray_code)
  return gray_code
def convert():  
    v1 = entry1.get()
    
    clear_l()
    label5 = tk.Label(root, text=convert1(v1)[2:],font=('helvetica', 15, 'bold'),bg='orange')
    canvas1.create_window(220, 340, window=label5)
    
root= tk.Tk()
root.title('CONVERT DECIMAL TO GARY')
canvas1 = tk.Canvas(root, width = 410, height = 410, bg='blue')
canvas1.pack()

entry1 = tk.Entry (root,font=('helvetica',12, 'bold'),bg='white',fg='red') 
canvas1.create_window(270, 155, window=entry1)



clear_l()
#root.mainloop()


