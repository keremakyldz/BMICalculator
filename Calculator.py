from tkinter import *

#window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=300)

#creating empty spaces for grid rows
for i in range(11):
    window.grid_rowconfigure(i,weight=1)

#creating empty spaces for grid columns
for i in range(8):
    window.grid_columnconfigure(i,weight=1)


#weight label

weight_label = Label(text="Enter Your Weight(kg)")
weight_label.config(font=("Arial",11,"italic"))
weight_label.grid(row=1,column=4)

#height label

height_label = Label(text="Enter Your Height(cm)")
height_label.config(font=("Arial",11,"italic"))
height_label.grid(row=3,column=4)

#Kg text

kg_entry = Entry(width=20)
kg_entry.grid(row=2,column=4)

#Height entry

height_entry = Entry(width=20)
height_entry.grid(row=4,column=4)

#Result

result_label = Label(text="")
result_label.grid(row=6,column=4)

#BMI calculator button
def button_clicked():
    try:
        a = float(kg_entry.get())
        b = float(height_entry.get()) / 100
        bmi = a / (b ** 2)

        if 0 < bmi < 18.5:
            result_text = f"BMI: {bmi:.2f} - Underweight"
        elif 18.5 <= bmi < 25:
            result_text = f"BMI: {bmi:.2f} - Healthy weight"
        elif 25 <= bmi < 30:
            result_text = f"BMI: {bmi:.2f} - Overweight"
        elif bmi >= 30:
            result_text = f"BMI: {bmi:.2f} - Obesity"
        else:
            result_text = f"Enter a valid number"

        result_label.config(text=result_text)


    except ValueError:
        result_label.config(text="Please enter valid numbers for weight and height.")

calculate = Button(text="Calculate",command=button_clicked,font=("Arial",8,"italic"))
calculate.grid(row=5,column=4)

mainloop()