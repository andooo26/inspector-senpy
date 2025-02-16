import tkinter as tk

keys = [
    ["Esc", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"],
    ["半角/全角", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "^", "\\", "Backspace"],
    ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "@", "[", "Enter"],
    ["Caps Lock", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", ":", "]", "Enter"],
    ["Shift", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "\\", "Shift"],
    ["Ctrl", "Win", "Alt", "半角", "Space", "全角", "かな", "Alt", "Fn", "Ctrl"]
]

root = tk.Tk()
root.title("JISキーボード")

frame = tk.Frame(root)
frame.pack()

for row in keys:
    row_frame = tk.Frame(frame)
    row_frame.pack()
    for key in row:
        if key == "Space":
            button = tk.Button(row_frame, text=key, width=40, height=3)
        elif key == "Enter":
            button = tk.Button(row_frame, text=key, width=15, height=3)
        elif key == "Shift":
            button = tk.Button(row_frame, text=key, width=15, height=3)
        else:
            button = tk.Button(row_frame, text=key, width=7, height=3)
        button.pack(side=tk.LEFT, padx=2, pady=2)

root.mainloop()
