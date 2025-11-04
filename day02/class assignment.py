# def circle_area(radius, pi=3.14):
#     # בדיקה שהרדיוס חיובי
#     if radius <= 0:
#         return "Radius must be a positive number"

#     area = pi * (radius ** 2)
#     return area
# print(circle_area(5))  # Output: 78.5


# def square_area(side_length):
#     # בדיקה שהאורך חיובי
#     if side_length <= 0:
#         return "Side length must be a positive number"

#     area = side_length ** 2
#     return area

# print(square_area(4))


from tkinter import *

def circle_area(radius, pi=3.14):
    if radius <= 0:
        return "Radius must be a positive number"
    area = pi * (radius ** 2)
    return area

def calculate():
    try:
        r = float(entry_radius.get())
        result = circle_area(r)
        label_result.config(text=f"Area: {result}")
    except ValueError:
        label_result.config(text="Enter a valid number!")

# Window
window = Tk()
window.title("Circle Area Calculator")

# Input label + box
label_radius = Label(window, text="Enter radius:")
label_radius.pack()

entry_radius = Entry(window)
entry_radius.pack()

# Button
button_calc = Button(window, text="Calculate", command=calculate)
button_calc.pack()

# Result label
label_result = Label(window, text="Area: ")
label_result.pack()

# Start GUI
window.mainloop()
