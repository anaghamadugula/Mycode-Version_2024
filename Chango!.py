from currency_converter import CurrencyConverter
import tkinter as tk
c = CurrencyConverter()
#print(c.convert(12,"USD","INR"))

#App Setup
app = Flask(__name__)
Scss(app)

window = tk.Tk()
window.geometry("1920x1080")
window.title("Chango!")

def clicked():
    amount = int(entry1.get())
    cur1 = entry2.get()
    cur2 = entry3.get()
    data = c.convert(amount, cur1, cur2)
    label4 = tk.Label(window,text=data,font="times 30 bold").place(x=50,y=530)

label = tk.Label(window,text="Chango!",font="times 80 bold").place(x=530,y=50)
label1 = tk.Label(window,text="Enter amount here: ",font="times 24 bold").place(x=420,y=200)
entry1 = tk.Entry(window)

label2 = tk.Label(window,text="Enter your currency here: ",font="times 24 bold").place(x=335,y=300)
entry2 = tk.Entry(window)

label3 = tk.Label(window,text="Enter your desired currency: ",font="times 24 bold").place(x=295,y=400)
entry3 = tk.Entry(window)

button = tk.Button(window,text="Click",font="times 35 bold",command=clicked).place(x=660,y=500)
entry1.place(x=850, y= 217)
entry2.place(x=850, y= 317)
entry3.place(x=850, y= 417)
window.mainloop()
