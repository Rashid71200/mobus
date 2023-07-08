import tkinter as tk

root = tk.Tk()
root.geometry("800x800")

main_frame = tk.Frame(root, bg="red")
main_frame.pack(expand=True, fill="both")

n_frame = tk.Frame(main_frame, bg="blue", width=400, height=400)
n_frame.pack(pady=200)

label = tk.Label(n_frame, text="hello")
label.pack()

root.mainloop()