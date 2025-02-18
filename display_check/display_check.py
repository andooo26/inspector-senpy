import tkinter as tk

def color():
    current_color = canvas.cget("bg")
    new_color = 'black' if current_color == 'white' else 'white'
    canvas.config(bg=new_color)
    root.after(2000, color)

root = tk.Tk()
root.title("sample")
root.attributes("-fullscreen", True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

frame = tk.Frame(root)
frame.pack()

canvas = tk.Canvas(frame, width=width, height=height, bg='black', highlightthickness=0, relief='ridge')
canvas.pack()

root.after(2000, color)

root.mainloop()
