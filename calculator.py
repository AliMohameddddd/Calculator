import tkinter as tk
import math

# Global variables for memory storage
memory = 0
memory_operation = ""

# Create a function to handle button clicks
def button_click(event):
    global memory  # Move the global statement to the beginning of the function
    # Get the text of the clicked button
    button_text = event.widget.cget("text")
    
    # Update the display area based on the button clicked
    if button_text == "=":
        try:
            # Evaluate the expression and display the result
            expression = display.get()
            result = eval(expression)
            display.set(result)
        except ZeroDivisionError:
            # Display division by zero error message
            display.set("Error: Division by zero")
            window.after(1000, lambda: display.set(""))
        except SyntaxError:
            # Display invalid input error message
            display.set("Error: Invalid input")
            window.after(1000, lambda: display.set(""))
        except:
            # Display general error message
            display.set("Error")
            window.after(1000, lambda: display.set(""))
    elif button_text == "C":
        # Clear the display area
        display.set("")
    elif button_text == "sqrt":
        # Calculate the square root of the number in the display
        try:
            number = float(display.get())
            result = math.sqrt(number)
            display.set(result)
        except:
            display.set("Error")
            window.after(1000, lambda: display.set(""))
    elif button_text == "sin":
        # Calculate the sine of the number in the display
        try:
            number = float(display.get())
            result = math.sin(math.radians(number))
            display.set(result)
        except:
            display.set("Error")
            window.after(1000, lambda: display.set(""))
    elif button_text == "cos":
        # Calculate the cosine of the number in the display
        try:
            number = float(display.get())
            result = math.cos(math.radians(number))
            display.set(result)
        except:
            display.set("Error")
            window.after(1000, lambda: display.set(""))
    elif button_text == "tan":
        # Calculate the tangent of the number in the display
        try:
            number = float(display.get())
            result = math.tan(math.radians(number))
            display.set(result)
        except:
            display.set("Error")
            window.after(1000, lambda: display.set(""))
    elif button_text == "log":
        # Calculate the logarithm (base 10) of the number in the display
        try:
            number = float(display.get())
            result = math.log10(number)
            display.set(result)
        except:
            display.set("Error")
            window.after(1000, lambda: display.set(""))
    elif button_text == "M+":
        # Add the current value to memory
        try:
            number = float(display.get())
            memory += number
            display.set("")
        except:
            display.set("Error")
            window.after(1000, lambda: display.set(""))
    elif button_text == "MR":
        # Recall the value from memory
        display.set(memory)
    elif button_text == "MC":
        # Clear the memory
        memory = 0
    elif button_text == "M-":
        # Subtract the current value from memory
        try:
            number = float(display.get())
            memory -= number
            display.set("")
        except:
            display.set("Error")
            window.after(1000, lambda: display.set(""))
    else:
        # Append the clicked button's text to the display area
        display.set(display.get() + button_text)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the display area
display = tk.StringVar()
display.set("")
display_label = tk.Label(window, textvariable=display, font=("Arial", 20), anchor="e")
display_label.pack(fill="both", expand=True)

# Create the buttons
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "^", "sqrt", "sin", "cos", "tan", "log",
    "M+", "MR", "MC", "M-"
]
buttons = []
for text in button_texts:
    button = tk.Button(window, text=text, font=("Arial", 16), padx=10, pady=10)
    button.pack(side="left", fill="both", expand=True)
    button.bind("<Button-1>", button_click)
    buttons.append(button)

# Run the application
window.mainloop()
           
