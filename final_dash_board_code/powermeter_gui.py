import tkinter as tk
import webbrowser

def open_link(event):
    webbrowser.open("https://ahrneloy.github.io/")

def update_text():
    current_value = float(canvas.itemcget(text1, "text"))
    new_value = current_value + 1
    canvas.itemconfig(text1, text=str(new_value))
    root.after(1000, update_text)  # Update every 1 second (1000 milliseconds)


value = [ 11.11,
         22.22,
         33.33,
         44.44 ]


# Create the main window
root = tk.Tk()

# Set the window size
root.geometry("832x861")

# Create a Canvas widget to hold the image and text
canvas = tk.Canvas(root, width=832, height=861)
canvas.pack()

# Load and display the image
image = tk.PhotoImage(file="C:/Users/AhrNeloy/Desktop/final_dash_board_code/modbus_python_V2/Schneider_meter1.png")
canvas.create_image(0, 0, anchor="nw", image=image)

# Create and place the text labels
text1 = canvas.create_text(400, 284, text=value[0], fill="black", font=("Arial", 35, "bold"), anchor="center")
text2 = canvas.create_text(400, 361, text=value[3], fill="black", font=("Arial", 35, "bold"), anchor="center")


text3 = canvas.create_text(400, 435, text=value[1], fill="black", font=("Arial", 35, "bold"), anchor="center")
text4 = canvas.create_text(400, 512, text=value[2], fill="black", font=("Arial", 35, "bold"), anchor="center")

text4 = canvas.create_text(400, 832, text="©Azaharul Rashid", fill="#e0e0e4", font=("Arial", 22, "bold"), anchor="center")
canvas.tag_bind(text4, "<Button-1>", open_link)
canvas.tag_bind(text4, "<Enter>", lambda e: canvas.itemconfig(text4, fill="red"))
canvas.tag_bind(text4, "<Leave>", lambda e: canvas.itemconfig(text4, fill="blue"))

update_text()

# Start the main loop
root.mainloop()