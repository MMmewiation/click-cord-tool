import tkinter as tk

def on_click(event):
    print(f"Clicked at: ({event.x}, {event.y})")

# Create the main window
root = tk.Tk()
root.title("Click Coordinates")

# Set the size of the window
root.geometry("1920x1080")

# Bind the left mouse button click event to the on_click function
root.bind("<Button-1>", on_click)

# Start the main event loop
root.mainloop()
