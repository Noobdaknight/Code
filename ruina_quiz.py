import tkinter as tk
from tkinter import messagebox, PhotoImage

root = tk.Tk()
root.geometry("1000x500")
root.title("Ruina Quiz")

# Load background image once
bg_image = PhotoImage(file=r"C:\Users\Noah.Broughton\Downloads\Ruina_quiz\Background.png")
background = tk.Label(root, image=bg_image)
background.place(relwidth=1, relheight=1)

# Quiz data
questions = ["What is the first enemies you fight in the game?",
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
"What is the single highest rolling page in Library of Ruina",]

options_list = [["A, Zwei", "B, Hana Asocition", "C, Rats","D, Distortions",],
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
    ["A, Extraction Team leader", "B, Agent of the Head", "C, F Corp's CEO", "D, Angela's helper",],
    ["A, Serum R, K, F", "B, Serum K, F, C", "C, Serum W, R, K", "D, Serum T, L, K",],
    ["A, Pirates of Penzance","B, Harry Potter","C, The Four Divine Beasts","D, The Wizard of Oz",],
    ["A, Myo", "B, Nikolai", "C, Rudolph", "D, Maxim",],
    ["A, 49", "B, 4", "C, 5", "D, 6",],
    ["A, Furioso", "B, The Knights of the Round Table", "C, Orlando Furioso", "D, Orlando",],
    ["A, Tipereth", "B, Roland", "C, Binah", "D, Gebura",],
    ["A, The Knowning I", "B, This is this", "C, That is that", "D, Library of Ruina",],]

answers = ("C", "D", "B", "A", "B", "A", "D", "C", "B", "D", "C", "D", "B", "C", "D", "B", "B", "C", "D", "A",)

# Globals
current_question_index = 0
score = 0
result_label = None

# ==== Content Frame ====
content_frame = tk.Frame(root, bg="#7FD7DA")
content_frame.place(relx=0.5, rely=0.5, anchor="center")

question_label = tk.Label(content_frame, text="", font=('Arial', 18), bg="#7FD7DA")
question_label.pack(pady=10)

button_frame = tk.Frame(content_frame, bg="#7FD7DA")
button_frame.pack(pady=10)

buttons = []
for i in range(4):
    btn = tk.Button(button_frame, text="", font=("Arial", 14), width=25,
                    command=lambda idx=i: check_answer("ABCD"[idx]),
                    bg="#7FD7DA")
    btn.grid(row=i//2, column=i%2, padx=10, pady=5)
    buttons.append(btn)

# Creates the Restart Button
restart_btn = tk.Button(content_frame, text="Restart", font=('Arial', 14), command=lambda: restart_question())
restart_btn.pack(pady=10)
restart_btn.config(state=tk.DISABLED, bg="#7FD7DA")

def update_question():
    global current_question_index
    question_label.config(text=questions[current_question_index])
    for i, btn in enumerate(buttons):
        btn.config(text=options_list[current_question_index][i], state=tk.NORMAL)

def check_answer(selected_option):
    global score, result_label
    if selected_option == answers[current_question_index]:
        score += 1
        result_text = "Correct!"
    else:
        result_text = "Incorrect, please try again"
        restart_btn.config(state=tk.NORMAL)

    for btn in buttons:
        btn.config(state=tk.DISABLED)

    if result_label:
        result_label.destroy()
    result_label = tk.Label(content_frame, text=result_text, font=('Arial', 16), bg="#7FD7DA")
    result_label.pack(pady=5)

    root.after(1000, next_question)

def next_question():
    global current_question_index, result_label
    current_question_index += 1

    if result_label:
        result_label.destroy()

    if current_question_index < len(questions):
        update_question()
    else:
        messagebox.showinfo("Quiz Finished", f"You got {score} out of {len(questions)} correct!")
        root.mainloop.close()

def restart_question():
    global current_question_index, score
    current_question_index = 0
    score = 0
    restart_btn.config(state=tk.DISABLED)
    update_question()

# Start
update_question()
messagebox.showinfo("Welcome", "Welcome to the Quiz of Ruina")
root.mainloop()