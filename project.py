from tkinter import*

window = Tk()
window.title("Calculator")
window.geometry("400x300")
def product():
    num1 = entry1.get()
    num2 = entry2.get()
    
    if num1 and num2: 
        product = int(num1) * int(num2)
        result_text.delete(1.0, END)
        result_text.insert(END, "Product:", product)


window = Tk()
window.title("Calculator")
window.geometry("400x300")

Label(window, text="First Number:").pack()
entry1 = Entry(window)
entry1.pack()
Label(window, text="Second Number:").pack()
entry2 = Entry(window)
entry2.pack()
Button(window, text="Calculate", command = product).pack()
result_text = Text(window, height=2, width=30)
result_text.pack()

window.mainloop()