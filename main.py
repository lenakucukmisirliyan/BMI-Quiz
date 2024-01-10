import tkinter

window = tkinter.Tk()
window.minsize(width=250, height=250)
window.config(padx=10, pady=10)
window.title("BMI Calculator")

FONT = ("Arial", 10, "bold")

#height
height_input_label = tkinter.Label(text="Enter your height (cm)", font=FONT)
height_input_label.config(padx=20, pady=20)
height_input_label.pack()

height_input = tkinter.Entry(width=20)
height_input.focus()
height_input.pack()

#weight
weight_input_label = tkinter.Label(text="Enter your weight (kg)", font=FONT)
weight_input_label.config(padx=20, pady=20)
weight_input_label.pack()

weight_input = tkinter.Entry(width=20)
weight_input.pack()

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number")

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi,2)}. You are "
    if bmi <= 18.5:
        result_string += "underweight"
    elif 18.5 < bmi <= 24.9:
        result_string += "normal"
    elif 25.0 < bmi <= 29.9:
        result_string += "overweight"
    else:
        result_string += "obese"
    return result_string


#button
calculate_button = tkinter.Button(text="Calculate", font=FONT, command=calculate_bmi)
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()

window.mainloop()