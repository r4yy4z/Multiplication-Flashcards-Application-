# Multiplication Flash Cards Application
# Code by: Rayyan Moinudeen


# importing tkinter
import tkinter as tk
from tkinter import ttk
from random import randint
from tkinter import END


# setting up the tkinter window
root = tk.Tk()
root.title("Multiplication Flash Cards")
root.iconbitmap("bulb.ico")
root.geometry("900x750")
title = tk.Label(root, text="Multiplication Flash Cards", font=("Calibri", 30), background="light blue")
title.pack(pady=20)
title = tk.Label(root, text="Note: This Flash Cards application is only for educational purposes!", font=("Arial", 10))
title.pack(pady=5)


# asking the user for their name
label = tk.Label(root, text= "Enter Your Name:")
label.config(font=("Old Roman Times", 12))
label.pack()
entry = ttk.Entry(root)
entry.pack()


# notifying that the user has entered their name 
def show_entry():
	print("The user's name is:", entry.get())
show_button = ttk.Button(root, text="OK", command=show_entry)
show_button.pack()


# multiplication questions
questions = [
    (("1 x 1 ="), 1),
    (("1 x 2 ="), 2),
    (("1 x 3 ="), 3),
    (("1 x 4 ="), 4),
    (("1 x 5 ="), 5),
    (("1 x 6 ="), 6),
    (("1 x 7 ="), 7),
    (("1 x 8 ="), 8),
    (("1 x 9 ="), 9),
    (("1 x 10 ="), 10),
    (("1 x 11="), 11),
    (("1 x 12 ="), 12),

    (("2 x 1 ="), 2),
    (("2 x 2 ="), 4),
    (("2 x 3 ="), 6),
    (("2 x 4 ="), 8),
    (("2 x 5 ="), 10),
    (("2 x 6 ="), 12),
    (("2 x 7 ="), 14),
    (("2 x 8 ="), 16),
    (("2 x 9 ="), 18),
    (("2 x 10 ="), 20),
    (("2 x 11="), 22),
    (("2 x 12 ="), 24),

    (("3 x 1 ="), 3),
    (("3 x 2 ="), 6),
    (("3 x 3 ="), 9),
    (("3 x 4 ="), 12),
    (("3 x 5 ="), 15),
    (("3 x 6 ="), 18),
    (("3 x 7 ="), 21),
    (("3 x 8 ="), 24),
    (("3 x 9 ="), 27),
    (("3 x 10 ="), 30),
    (("3 x 11="), 33),
    (("3 x 12 ="), 36),

    (("4 x 1 ="), 4),
    (("4 x 2 ="), 8),
    (("4 x 3 ="), 12),
    (("4 x 4 ="), 16),
    (("4 x 5 ="), 20),
    (("4 x 6 ="), 24),
    (("4 x 7 ="), 28),
    (("4 x 8 ="), 32),
    (("4 x 9 ="), 36),
    (("4 x 10 ="), 40),
    (("4 x 11="), 44),
    (("4 x 12 ="), 48),

    (("5 x 1 ="), 5),
    (("5 x 2 ="), 10),
    (("5 x 3 ="), 15),
    (("5 x 4 ="), 20),
    (("5 x 5 ="), 25),
    (("5 x 6 ="), 30),
    (("5 x 7 ="), 35),
    (("5 x 8 ="), 40),
    (("5 x 9 ="), 45),
    (("5 x 10 ="), 50),
    (("5 x 11="), 55),
    (("5 x 12 ="), 60),

    (("6 x 1 ="), 6),
    (("6 x 2 ="), 12),
    (("6 x 3 ="), 18),
    (("6 x 4 ="), 24),
    (("6 x 5 ="), 30),
    (("6 x 6 ="), 36),
    (("6 x 7 ="), 42),
    (("6 x 8 ="), 48),
    (("6 x 9 ="), 54),
    (("6 x 10 ="), 60),
    (("6 x 11="), 66),
    (("6 x 12 ="), 72),

    (("7 x 1 ="), 7),
    (("7 x 2 ="), 14),
    (("7 x 3 ="), 21),
    (("7 x 4 ="), 28),
    (("7 x 5 ="), 35),
    (("7 x 6 ="), 42),
    (("7 x 7 ="), 49),
    (("7 x 8 ="), 56),
    (("7 x 9 ="), 63),
    (("7 x 10 ="), 70),
    (("7 x 11="), 77),
    (("7 x 12 ="), 84),

    (("8 x 1 ="), 8),
    (("8 x 2 ="), 16),
    (("8 x 3 ="), 24),
    (("8 x 4 ="), 32),
    (("8 x 5 ="), 40),
    (("8 x 6 ="), 48),
    (("8 x 7 ="), 56),
    (("8 x 8 ="), 64),
    (("8 x 9 ="), 72),
    (("8 x 10 ="), 80),
    (("8 x 11="), 88),
    (("8 x 12 ="), 96),

    (("9 x 1 ="), 9),
    (("9 x 2 ="), 18),
    (("9 x 3 ="), 27),
    (("9 x 4 ="), 36),
    (("9 x 5 ="), 45),
    (("9 x 6 ="), 54),
    (("9 x 7 ="), 63),
    (("9 x 8 ="), 72),
    (("9 x 9 ="), 81),
    (("9 x 10 ="), 90),
    (("9 x 11="), 99),
    (("9 x 12 ="), 108),

    (("10 x 1 ="), 10),
    (("10 x 2 ="), 20),
    (("10 x 3 ="), 30),
    (("10 x 4 ="), 40),
    (("10 x 5 ="), 50),
    (("10 x 6 ="), 60),
    (("10 x 7 ="), 70),
    (("10 x 8 ="), 80),
    (("10 x 9 ="), 90),
    (("10 x 10 ="), 100),
    (("10 x 11="), 110),
    (("10 x 12 ="), 120),

    (("11 x 1 ="), 11),
    (("11 x 2 ="), 22),
    (("11 x 3 ="), 33),
    (("11 x 4 ="), 44),
    (("11 x 5 ="), 55),
    (("11 x 6 ="), 66),
    (("11 x 7 ="), 77),
    (("11 x 8 ="), 88),
    (("11 x 9 ="), 99),
    (("11 x 10 ="), 110),
    (("11 x 11="), 121),
    (("11 x 12 ="), 132),

    (("12 x 1 ="), 12),
    (("12 x 2 ="), 24),
    (("12 x 3 ="), 36),
    (("12 x 4 ="), 48),
    (("12 x 5 ="), 60),
    (("12 x 6 ="), 72),
    (("12 x 7 ="), 84),
    (("12 x 8 ="), 96),
    (("12 x 9 ="), 108),
    (("12 x 10 ="), 120),
    (("12 x 11="), 132),
    (("12 x 12 ="), 144),
]
count = len(questions)
random_question = randint(0, count - 1)
question_count = 0
corr_answer_count = 0


# creating the multiplication question label
multiplication_question = tk.Label(root, text="", font=("Helvetica", 36))
multiplication_question.pack(pady=50)


# creating a button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)


# entry widget
label = ttk.Label(root, text= "Enter Your Answer:")
label.config(font=("Old Roman Times", 12))
label.pack()
my_entry = ttk.Entry(root, font = ('Roboto',18))
my_entry.pack(pady=20)


# defining the next button
def next_question():
    global random_question
    global question_count
    random_question = randint(0, count - 1)
    multiplication_question.config(text=questions[random_question][0])
    question_count = question_count + 1
    my_entry.delete(0, END)
    answer_label.config(text="")
    hint_label.config(text="")  


# creating a button to go to the next card
next_button = ttk.Button(button_frame, text="Next", command=next_question)
next_button.grid(row=0, column=1)


# defining the answer button
def answer():
    global corr_answer_count
    user_answer = my_entry.get().capitalize()
    correct_answer = str(questions[random_question][1])  
    
    if user_answer == correct_answer:
        answer_label.config(text=f"Correct! {questions[random_question][0]} {correct_answer}")
        corr_answer_count = corr_answer_count + 1
        
    else:
        answer_label.config(text=f"Incorrect! {questions[random_question][0]} is not {user_answer}")
    score_label.config(text=f"Score: " + str(corr_answer_count) + "/" + str(question_count))


# creating an answer button
answer_button = ttk.Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

# answer label
answer_label = tk.Label(root, text="", font=("Helvetica", 18))
answer_label.pack(pady=20)


# defining the hint button
def hint():
    question_temp = questions[random_question][0]
    temp1 = question_temp.replace(" ","")
    temp2 = temp1.replace("=", "")
    splited_question = temp2.split("x")
    repeated_addition = " + ".join([splited_question[0] for _ in range(int(splited_question[1]))])
    hint_label.config(text=f"Hint: {repeated_addition}")


# creating a hint button
hint_button = ttk.Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)


# creating a hint label
hint_label = tk.Label(root, text="", font=("Helvetica", 12))
hint_label.pack(pady=20)


# score label
score_label = tk.Label(root, text="", font=("Helvetica", 12))
score_label.pack(pady=20)


# calling everything with the main loop
root.mainloop()