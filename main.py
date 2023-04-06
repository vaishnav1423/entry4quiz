import tkinter as tk
import json, os

DB_FILE_PATH = 'quiz.json'
window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")
window.configure(bg='#d3d037')
frame = tk.Frame(bg='#d3d037')


def add_quest():
  if (os.path.file(DB_FILE_PATH)):
    f = open(DB_FILE_PATH)
    data = json.load(f)
  else:
    data = []
  if (question_entry.get() != '' and option1_entry.get() != ''
      and option2_entry.get() != '' and option3_entry.get() != ''
      and option4_entry.get() != ''):
    question = question_entry.get()
    option1 = option1_entry.get()
    option2 = option1_entry.get()
    option3 = option1_entry.get()
    option4 = option1_entry.get()


title_label = tk.Label(frame,
                       text="Quiz",
                       bg='#d3d037',
                       font={"Arial", 40},
                       fg='#FF3399')
question = tk.Label(frame, text="Question", bg='#d3d037', font={"Arial", 16})
question_entry = tk.Entry(frame, font={"Arial", 16})
option1_entry = tk.Entry(frame, font={"Arial", 16})
option1_label = tk.Label(frame,
                         text="Option1",
                         bg='#d3d037',
                         font={"Arial", 16})
option2_entry = tk.Entry(frame, font={"Arial", 16})
option2_label = tk.Label(frame,
                         text="Option2",
                         bg='#d3d037',
                         font={"Arial", 16})
option3_entry = tk.Entry(frame, font={"Arial", 16})
option3_label = tk.Label(frame,
                         text="Option3",
                         bg='#d3d037',
                         font={"Arial", 16})
option4_entry = tk.Entry(frame, font={"Arial", 16})
option4_label = tk.Label(frame,
                         text="Option4",
                         bg='#d3d037',
                         font={"Arial", 16})

add_button = tk.Button(frame,
                       text="Add Next",
                       bg='#333333',
                       fg='#FF3399',
                       font={"Arial", 12},
                       command=add_quest)

title_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
question.grid(row=1, column=0)
question_entry.grid(row=1, column=1, columnspan=3, pady=7)
option1_label.grid(row=2, column=0, pady=7)
option1_entry.grid(row=2, column=1, pady=7)
option2_label.grid(row=3, column=0, pady=7)
option2_entry.grid(row=3, column=1, pady=7)
option3_label.grid(row=4, column=0, pady=7)
option3_entry.grid(row=4, column=1, pady=7)
option4_label.grid(row=5, column=0, pady=7)
option4_entry.grid(row=5, column=1, pady=7)
add_button.grid(row=6, column=0, columnspan=2, pady=30)
frame.pack()
tk.mainloop()
