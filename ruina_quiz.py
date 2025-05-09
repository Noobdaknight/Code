import tkinter as tk
from tkinter import messagebox

# Saved list for questions
questions = ("What is the first enemies you fight in the game?",
"What is the second rank of danger the Library achieves?",
"What is the name of the Patron Librarian of the floor of Art?",
"On clash lose what emotion point is generated?",
"What are the special pages given after reaching a higher emotion level?",
"Who is the first ego user you fight?",
"What is the first abnormality you fight in game?",
"What is R corps Singularity",
"What is Gebura's original name?",
"What is the name of the Corporation that is above the rest",
"How manys abnormality fights are there on Hokma's floor",
"Roland has one major friend who appears late into the game, Who is he?",
"What was Binah's original ocupation",
"Baral/The Executioner uses a variety of serums when fighting you. What were they?",
"What are the abnormalites on Chesed's floor based on",
"Who is the Leader of R Corp's Fourth Pack",
"What is Boundary of Deaths Maximum Roll without Power Gain or Loss",
"What is Roland inspired/based on",
"Who faces L'Heure Du Loup",
"What is the single highest rolling page in Library of Ruina",)

# Saved list for answers
options_list = [
    ["A, Zwei", "B, Hana Asocition", "C, Rats","D, Distortions"],
    ["A, Impuritus", "B, Canard", "C, Plague", "D, Urban Myth"],
    ["A, Yesod", "B, Netzach", "C, Gabriel", "D, Giovanni"],
    ["A, Negative", "B, Wrathful", "C, Engulfing", "D, Positive"],
    ["A, Emotion", "B, Abnormality", "C, Speciality", "D, Memory"],
    ["A, Philip", "B, Malkuth", "C, Yujin", "D, Roland"],
    ["A, Scorched Girl","B, Nothing there","C, Heart of Aspiration","D, Bloodbath",],
    ["A, Rostering","B, Reduction","C, Replication","D, Relic",],
    ["A, Geburah", "B, Kali", "C, Akali", "D, Angelica",],
    ["A, The Arbiter", "B, The Beholders", "C, The Claw", "D, The Head",],
    ["A, 5", "B, 6", "C, 4", "D, 3",],
    ["A, Angelica", "B, Angelica", "C, Argalia", "D, Olivier",],
    ["A, Extraction Team leader", "B, Head's Agent", "C, F Corp's CEO", "D, Angela's helper",],
    ["A, Serum R, K, F", "B, Serum K, F, C", "C, Serum W, R, K", "D, Serum T, L, K",],
    ["A, Pirates of Penzance","B, Harry Potter","C, The Four Divine Beasts","D, The Wizard of Oz",],
    ["A, Myo", "B, Nikolai", "C, Rudolph", "D, Maxim",],
    ["A, 49", "B, 4", "C, 5", "D, 6",],
    ["A, Furioso", "B, The Knights of the Round Table", "C, Orlando Furioso", "D, Orlando",],
    ["A, Tipereth", "B, Roland", "C, Binah", "D, Gebura",],
    ["A, The Knowning I", "B, This is this", "C, That is that", "D, Library of Ruina",],
]

# Saved variables
answers = ("C", "D", "B", "A", "B", "A", "D", "C", "B", "D", "C", "D", "B", "C", "D", "B", "B", "C", "D", "A",)
current_question_index = 0
score = 0

root = tk.Tk()
root.geometry("1000x500")
root.title("Ruina Quiz")

# Lebel to welcome the user
def welcome():
    messagebox.showinfo("Welcome", "Welcome to the Quiz of Ruina")

# Add a label for the image
image_label = tk.Label(root)
image_label.pack(pady=20) # Adds space before the options

# Lebel to display the question
question_label = tk.Label(root, text=questions[current_question_index], font=('Arial', 18))
question_label.pack(padx=20, pady=20)

# Frame for the buttons
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

# Create button variables for options
btn1 = tk.Button(buttonframe, text="", font=("Arial", 18,))
btn2 = tk.Button(buttonframe, text="", font=("Arial", 18,))
btn3 = tk.Button(buttonframe, text="", font=("Arial", 18,))
btn4 = tk.Button(buttonframe, text="", font=("Arial", 18,))

# Restary button
restart_btn = tk.Button(root, text="Restart?", font=('Arial', 18,), command=lambda:restart_question())
restart_btn.pack(padx=50, pady=10)

#  Attach button actions for each answer option
btn1.config(command=lambda: check_answer("A"))
btn2.config(command=lambda: check_answer("B"))
btn3.config(command=lambda: check_answer("C"))
btn4.config(command=lambda: check_answer("D"))

# Grid layout for the buttons
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)
btn2.grid(row=1, column=1, sticky=tk.W+tk.E)
btn3.grid(row=1, column=2, sticky=tk.W+tk.E)
btn4.grid(row=1, column=3, sticky=tk.W+tk.E)

# Pack the button frame
buttonframe.pack(fill='x',)

# function to update the buttons and question
def update_question():
    global current_question_index
    question_label.config(text=questions[current_question_index])

    # Update the button texts based on the options for the current question
    btn1.config(text=options_list[current_question_index][0])
    btn2.config(text=options_list[current_question_index][1])
    btn3.config(text=options_list[current_question_index][2])
    btn4.config(text=options_list[current_question_index][3])

# Fuction to handle button clicks
def check_answer(selected_option):
    global current_question_index, score
    correct_answer = answers[current_question_index]

    if selected_option == correct_answer:
        score += 1 # Increment score if the answer is correct
        result_text = "Correct!"
    else:
        result_text = "Incorrect, please try again"
        restart_btn.config(state=tk.NORMAL) # Enables the restart button

    # Answer buttons disbaled until next question
    btn1.config(state=tk.DISABLED)
    btn2.config(state=tk.DISABLED)
    btn3.config(state=tk.DISABLED)
    btn4.config(state=tk.DISABLED)

    # Show the result on screen
    result_label = tk.Label(root, text=result_text, font=('Arial', 18))
    result_label.pack(padx=50, pady=20)

    # After a short delay, move to the next question (or reset if the last question)
    root.after(1000, next_question)

def restart_question():
    global current_question_index, score
    current_question_index = 0 #
    score = 0 # Reset the score
    restart_btn.config(state=tk.DISABLED)
    update_question()

def next_question():
    global current_question_index

    current_question_index += 1 # Move to the next question
    if current_question_index < len(questions):
        # Clear the previous result label
        for widget in root.winfo_children():
            if isinstance(widget, tk.Label) and widget != question_label:
                widget.destroy()
        update_question() # Update the questions and options
    else:
        # Displays the final results and score
        messagebox.showinfo("Quiz Finished", f"you got {score} out of {len(questions)} correct!")
        root.mainloop.close()

        
    btn1.config(state=tk.NORMAL)
    btn2.config(state=tk.NORMAL)
    btn3.config(state=tk.NORMAL)
    btn4.config(state=tk.NORMAL)

# Start by updating the question and options
update_question()

# Welcome the user
welcome()

root.mainloop()