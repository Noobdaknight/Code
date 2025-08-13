import tkinter as tk
from tkinter import messagebox, PhotoImage
import os

# Initialize root window
root = tk.Tk()
root.geometry("1920x1080")
root.title("Ruina Quiz")


# background images
script_dir = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(script_dir, "backgrounds")
bg_images = [
    "Question1_Background.png",
    "Question2_Background.png",
    "Question3_Background.png",
    "Question4_Background.png",
    "Question5_Background.png",
    "Question6_Background.png",
    "Question7_Background.png",
    "Question8_Background.png",
    "Question9_Background.png",
    "Question10_Background.png",
    "Question11_Background.png",
    "Question12_Background.png",
    "Question13_Background.png",
    "Question14_Background.png",
    "Question15_Background.png",
    "Question16_Background.png",
    "Question17_Background.png",
    "Question18_Background.png",
    "Question19_Background.png",
    "Question20_Background.png",
    "Question21_Background.png",
    ]

# Function to resize the image
def resize_image(image_path, width, height):
    img = PhotoImage(file=image_path)
    scale_x = max(1, img.width() // width)
    scale_y = max(1, img.height() // height)
    img_resized = img.subsample(scale_x, scale_y)
    return img_resized

for img_file in bg_images:
    full_path = os.path.join(image_folder, img_file)
    if not os.path.isfile(full_path):
        print(f"[ERROR] Missing image file: {full_path}")

# Initialize background Label
first_image_path = os.path.join(image_folder, bg_images[0])
bg_image = resize_image(first_image_path, 1000, 500)
background = tk.Label(root, image=bg_image)
background.place(relwidth=1, relheight=1)
background.lower()

# Quiz Data: Questions, Options, Answers
questions = [
    "1. What is the canonical name of the Library?",
    "2. What is the first enemies you fight in the game?",
    "3. What is the name of the Patron Librarian of the floor of Art?",
    "4. On clash lose what emotion point is generated?",
    "5. What are the special pages given upon reaching a higher emotion level? (Not EGO)",
    "6. Who is the first ego user you fight?",
    "7. What is the first abnormality you fight in game?",
    "8. What is R corps Singularity",
    "9. What is the Patron of Language's original name?",
    "10. What is the name of the Corporation that is above the rest",
    "11. How manys abnormality (Including Realization) fights are there on Hokma's floor",
    "12. Roland has a major friend who appears near the end of the game, What is their name?",
    "13. What was Binah's original ocupation",
    "14. Baral/The Executioner uses a variety of serums when fighting you. What were they?",
    "15. What are the abnormalites on Chesed's floor based on",
    "16. Who is the Leader of R Corp's Fourth Pack",
    "17. What is Boundary of Deaths Maximum Roll without Power Gain or Loss",
    "18. What is Roland inspired/based on",
    "19. Who faces L'Heure Du Loup",
    "20. What is the single highest rolling page in Library of Ruina",
    "Final Question: Do you want your results saved"
]

options_list = [
    ["A, Star of Knowledge and Death", "B, The Library of Babel", "C, The Library", "D, Tower of Babel"],
    ["A, Zwei", "B, Hana Asocition", "C, Rats", "D, Distortions"],
    ["A, Yesod", "B, Netzach", "C, Gabriel", "D, Giovanni"],
    ["A, Negative", "B, Wrathful", "C, Engulfing", "D, Positive"],
    ["A, Emotion", "B, Abnormality", "C, Speciality", "D, Memory"],
    ["A, Philip", "B, Malkuth", "C, Yujin", "D, Roland"],
    ["A, Scorched Girl", "B, Nothing there", "C, Heart of Aspiration", "D, Bloodbath"],
    ["A, Rostering", "B, Reduction", "C, Replication", "D, Rallying"],
    ["A, Gebura", "B, Kali", "C, Akali", "D, Angelica"],
    ["A, The Arbiter", "B, The Beholders", "C, The Claw", "D, The Head"],
    ["A, 5", "B, 6", "C, 4", "D, 3"],
    ["A, Ogier", "B, Astolfo", "C, Argalia", "D, Olivier"],
    ["A, Extraction Team leader", "B, Agent of the Head", "C, F Corp's CEO", "D, Angela's helper"],
    ["A, Serum R, K, F", "B, Serum K, F, C", "C, Serum W, R, K", "D, Serum T, L, K"],
    ["A, Pirates of Penzance", "B, Harry Potter", "C, The Four Divine Beasts", "D, The Wizard of Oz"],
    ["A, Myo", "B, Nikolai", "C, Rudolph", "D, Maxim"],
    ["A, 49", "B, 4", "C, 44", "D, 13"],
    ["A, Furioso", "B, The Knights of the Round Table", "C, Orlando Furioso", "D, Orlando"],
    ["A, Tipereth", "B, Yesod", "C, Binah", "D, Gebura"],
    ["A, The Knowning I", "B, Final Impromtu", "C, Please Don't Vanish Like This", "D, The Library of Ruin"],
    ["A, Yes", "B, No", "", ""]
]

answers = ["C", "C", "B", "A", "B", "A", "D", "C", "B", "D", "C", "D", "B", "C", "D", "B", "B", "C", "D", "A", "A"]

# Globals
current_question_index = 0
score = 0
name = ""
selected_option = ""

# GUI Layout
quiz_border_frame = tk.Frame(root, bg="#7FD7DA", bd=10, relief="ridge")
quiz_border_frame.place(relx=0.5, rely=0.5, anchor="center")

content_frame = tk.Frame(quiz_border_frame, bg="#7FD7DA")
content_frame.pack(padx=10, pady=10)

question_label = tk.Label(content_frame, text="", font=('Arial', 18), bg="#7FD7DA")
question_label.pack(pady=10)

button_frame = tk.Frame(content_frame, bg="#7FD7DA")
button_frame.pack(pady=10)

name_frame = tk.Frame(root, bg="#000000", bd=2, relief="groove")
name_frame.pack(pady=20)

# Name Entry 
entry_box = tk.Entry(name_frame, width=30, bg="#7FD7DA", font=("Arial", 12), relief="flat", highlightthickness=0)
entry_box.pack(side="left", padx=0)

def get_name_text():
    global name
    name = entry_box.get().strip()
    if not name:
        # Optionally show a message instead of beeping
        messagebox.showwarning("Input needed", "Please enter your name.")
        return
    entry_box.destroy()
    get_name_button.destroy()
    name_frame.destroy()

get_name_button = tk.Button(root, text="Enter", command=get_name_text, bg="#7FD7DA", font=("Arial", 12))
get_name_button.pack()

# Answer/Option Buttons
buttons = []
for i in range(4):
    btn = tk.Button(
        button_frame,
        text="",
        font=("Arial", 14),
        width=25,
        command=lambda idx=i: check_answer("ABCD"[idx]),
        bg="#7FD7DA"
    )
    btn.grid(row=i // 2, column=i % 2, padx=10, pady=5)
    buttons.append(btn)

# Restart/Retry Button
restart_btn = tk.Button(content_frame, text="Restart", font=('Arial', 14), command=lambda: restart_question())
restart_btn.pack(pady=10)
restart_btn.config(state=tk.DISABLED, bg="#7FD7DA")

# Update background image based on the current question
def update_background_image():
    global bg_image, background
    question_image_path = os.path.join(image_folder, bg_images[current_question_index])  # Get the image for the current question
    bg_image = resize_image(question_image_path, root.winfo_width(), root.winfo_height())  # Resize the image to the window size
    background.config(image=bg_image)  # Update the background image in the Label widget
    background.lower()  # Ensure the background is behind other widgets

# Quiz Logic/Question Updater
def update_question():
    question_label.config(text=questions[current_question_index])
    update_background_image()

    for i, btn in enumerate(buttons):
        btn.config(text=options_list[current_question_index][i])

    # Final question (index 20)
    if current_question_index == 20:
        buttons[2].config(state=tk.DISABLED)  # Bottom-left
        buttons[3].config(state=tk.DISABLED)  # Bottom-right
    else:
        for btn in buttons:
            btn.config(state=tk.NORMAL)  # Ensure buttons are re-enabled for all other questions


def check_answer(option):
    global score, selected_option
    selected_option = option

    if current_question_index < 20:
        if option == answers[current_question_index]:
            score += 1
        else:
            restart_btn.config(state=tk.NORMAL)

    root.after(150, next_question)

def next_question():
    global current_question_index, name

    current_question_index += 1

    if current_question_index < len(questions):
        update_question()
    else:
        if selected_option in ["A", "C"]:  # Both mean "Yes"
            if name == "":
                name = "Guest"

            scoreboard_path = os.path.join(script_dir, "scoreboard.txt")
            with open(scoreboard_path, "a") as f:
                f.write(f"{name}, scored {score} out of {len(questions)-1}\n")

        messagebox.showinfo("Quiz Finished", f"You got {score} out of {len(questions)-1} correct!")
        root.quit()

def restart_question():
    global current_question_index, score
    current_question_index = current_question_index-1
    score = score-1
    restart_btn.config(state=tk.DISABLED)
    update_question()

# Start Quiz/Program
update_question()
messagebox.showinfo("Welcome", "Welcome to the Quiz of Ruina.\nPlease insert your name at the top. \n@Copyright Project Moon, All rights reserved")

update_background_image()
root.lift()
root.focus_force()
root.mainloop()