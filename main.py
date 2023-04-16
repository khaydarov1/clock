import tkinter as tk
import time
import math

WIDTH = 400
HEIGHT = 400

root = tk.Tk()
root.title("Analog Clock")
canva = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canva.pack()

def update_clock():
    canva.delete("all")
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec

    canva.create_oval(2, 2, WIDTH, HEIGHT, outline="black", width=2)

    for i in range(12):
        angle = i * math.pi / 6 - math.pi / 2
        x = WIDTH / 2 + 0.7 * WIDTH / 2 * math.cos(angle)
        y = HEIGHT / 2 + 0.7 * WIDTH / 2 * math.sin(angle)
        if i == 0:
            canva.create_text(x, y - 10, text=str(i + 12), font=("Helvetica", 12))
        else:
            canva.create_text(x, y, text=str(i), font=("Helvetica", 12))

    for i in range(60):
        angle = i * math.pi / 30 - math.pi / 2
        x1 = WIDTH / 2 + 0.8 * WIDTH / 2 * math.cos(angle)
        y1 = HEIGHT / 2 + 0.8 * WIDTH / 2 * math.sin(angle)
        x2 = WIDTH / 2 + 0.9 * WIDTH / 2 * math.cos(angle)
        y2 = HEIGHT / 2 + 0.9 * WIDTH / 2 * math.sin(angle)
        if i % 5 == 0:
            canva.create_line(x1, y1, x2, y2, fill="black", width=3)
        else:
            canva.create_line(x1, y1, x2, y2, fill="black", width=1)
    hour_angle = (hour + minute / 60) * math.pi / 6 - math.pi / 2
    hour_x = WIDTH / 2 + 0.5 * WIDTH / 2 * math.cos(hour_angle)
    hour_y = HEIGHT / 2 + 0.5 * HEIGHT / 2 * math.sin(hour_angle)
    canva.create_line(WIDTH / 2, HEIGHT / 2, hour_x, hour_y, fill="black", width=4)

    minute_angle = (minute + second / 60) * math.pi / 30 - math.pi / 2
    minute_x = WIDTH / 2 + 0.7 * WIDTH / 2 * math.cos(minute_angle)
    munute_y = HEIGHT / 2 + 0.7 * HEIGHT / 2 * math.sin(minute_angle)
    canva.create_line(WIDTH / 2, HEIGHT / 2, minute_x, munute_y, fill="black", width=4)

    second_angle = second * math.pi / 30 - math.pi / 2
    second_x = WIDTH / 2 + 0.6 * WIDTH / 2 * math.cos(hour_angle)
    second_y = HEIGHT / 2 + 0.6 * HEIGHT / 2 * math.sin(hour_angle)
    canva.create_line(WIDTH / 2, HEIGHT / 2, second_x, second_y, fill="red", width=2)


canva.after(100, update_clock())

update_clock()
root.mainloop()
