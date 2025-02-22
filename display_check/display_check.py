import tkinter as tk
import sys

def changeColor():
    current_color = canvas.cget("bg")
    if current_color == 'black':
        new_color = 'white'
    elif current_color == 'white':
        new_color = 'red'
    elif current_color == 'red':
        new_color = 'yellow'
    elif current_color == 'yellow':
        new_color = 'blue'
    elif current_color == 'blue':
        new_color = 'black' 
    canvas.config(bg=new_color)
    root.after(2000, changeColor)

def on_key_press(event):
    root.quit()

root = tk.Tk()
root.title("sample")
root.attributes("-fullscreen", True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

frame = tk.Frame(root)
frame.pack()

canvas = tk.Canvas(frame, width=width, height=height, bg='black', highlightthickness=0, relief='ridge')
canvas.pack()

root.bind("<KeyPress>", on_key_press)

root.after(2000, changeColor)

root.mainloop()
