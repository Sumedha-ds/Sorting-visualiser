import tkinter as tk
import random
import time

def selection_sort(arr, canvas):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            highlight_bars(arr, canvas, i, j, min_idx)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_canvas(arr, canvas)
        time.sleep(speed_slider.get())

def bubble_sort(arr, canvas):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            highlight_bars(arr, canvas, j, j+1)
        update_canvas(arr, canvas)
        time.sleep(speed_slider.get())

def update_canvas(arr, canvas):
    canvas.delete("all")
    bar_width = canvas_width / len(arr) * 0.8
    spacing = canvas_width / len(arr) * 0.2
    height_scale = canvas_height / max(arr)
    for i, val in enumerate(arr):
        x0 = i * (bar_width + spacing) + spacing / 2
        y0 = canvas_height - val * height_scale
        x1 = x0 + bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
    root.update()

def highlight_bars(arr, canvas, idx1, idx2, min_idx=None):
    canvas.delete("all")
    bar_width = canvas_width / len(arr) * 0.8
    spacing = canvas_width / len(arr) * 0.2
    height_scale = canvas_height / max(arr)
    for i, val in enumerate(arr):
        x0 = i * (bar_width + spacing) + spacing / 2
        y0 = canvas_height - val * height_scale
        x1 = x0 + bar_width
        y1 = canvas_height
        if i == idx1 or i == idx2:
            color = "red"
        elif min_idx is not None and i == min_idx:
            color = "green"
        else:
            color = "blue"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    root.update()
    time.sleep(speed_slider.get() / 2)

def start_sorting():
    global arr
    arr = [int(x) for x in input_entry.get().split()]
    algo = algo_var.get()
    if algo == 'Selection Sort':
        selection_sort(arr, canvas)
    elif algo == 'Bubble Sort':
        bubble_sort(arr, canvas)

# GUI setup
root = tk.Tk()
root.title("Sorting Algorithm Visualization")

canvas_height = 400
canvas_width = 800
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack(pady=20)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter numbers separated by spaces:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(input_frame, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)

algo_frame = tk.Frame(root)
algo_frame.pack(pady=10)

algo_var = tk.StringVar(value='Selection Sort')
tk.Radiobutton(algo_frame, text="Selection Sort", variable=algo_var, value='Selection Sort').grid(row=1, column=0, padx=10, pady=5)
tk.Radiobutton(algo_frame, text="Bubble Sort", variable=algo_var, value='Bubble Sort').grid(row=1, column=1, padx=10, pady=5)

speed_frame = tk.Frame(root)
speed_frame.pack(pady=10)

tk.Label(speed_frame, text="Speed:").grid(row=2, column=0, padx=10, pady=10)
speed_slider = tk.Scale(speed_frame, from_=0.1, to=1.0, resolution=0.1, orient=tk.HORIZONTAL)
speed_slider.grid(row=2, column=1, padx=10, pady=10)

start_button = tk.Button(root, text="Start Sorting", command=start_sorting)
start_button.pack(pady=20)

root.mainloop()
