import tkinter as tk
import keyboard
import threading

keys = [
    ["esc", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"],
    ["半角/全角", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "^", "\\", "backspace"],
    ["tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "@", "[", "enter"],
    ["caps lock", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", ":", "]", "enter"],
    ["shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "\\", "right shift"],
    ["ctrl", "left windows", "alt", "無変換", "space", "変換", "ひらがな", "right alt", "fn", "right ctrl"]
]

root = tk.Tk()
root.title("キーボードテスト")

pressed_keys = set()

def update_button_color(key, color):
    if key in buttons:
        for button in buttons[key]:
            button.config(bg=color)

label = tk.Label(root, font=("Arial", 16))
label.pack(pady=20)

def key_pressed(event):
    key = event.name
    label.config(text=f"押されたキー: {key}")

    pressed_keys.add(key)
    update_button_color(key, 'lightgreen')

def key_released(event):
    pass

def listen_for_key():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key_pressed(event)
        elif event.event_type == keyboard.KEY_UP:
            key_released(event)

key_thread = threading.Thread(target=listen_for_key, daemon=True)
key_thread.start()

frame = tk.Frame(root)
frame.pack()

buttons = {}

for row in keys:
    row_frame = tk.Frame(frame)
    row_frame.pack()
    for key in row:
        if key == "space":
            button = tk.Button(row_frame, text=key, width=40, height=3)
        elif key == "enter":
            button = tk.Button(row_frame, text=key, width=15, height=3)
        elif key == "shift":
            button = tk.Button(row_frame, text=key, width=15, height=3)
        else:
            button = tk.Button(row_frame, text=key, width=7, height=3)

        button.pack(side=tk.LEFT, padx=2, pady=2)

        buttons[key] = [button]

root.mainloop()
