#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import *
import openai

openai.api_key = "your api"

messages = []

def aitext():
    user_content = entry.get()
    
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role": "assistant", "content": f": {assistant_content}"})
    
    
    label.config(state="normal") 
    label.delete("1.0", "end") 
    label.insert("end", assistant_content) 
    label.config(state="disabled")

def temp_text(e):
    entry.delete(0,"end")
    
window = tk.Tk()
window.geometry("800x400")
window.title("Minichatgpt by TCK")

label_frame = tk.Frame(window)
label_frame.pack(side="top", fill="both", expand=True)

label_scroll = tk.Scrollbar(label_frame)
label_scroll.pack(side="right", fill="y")

label = tk.Text(label_frame, font=("Arial", 14), wrap="word", height=10, width=50, bg="gray", state="disabled", yscrollcommand=label_scroll.set)

label.pack(side="left", fill="both", expand=True)
label.config(state="normal") 
label.delete("1.0", "end") 
notice = '''[한글]\n버튼을 누르고 좀 기달리시면 원하던 답변이 출력 됩니다. 감사합니다 \n\n[English]\nIf you press the button and wait for a while, the answer you want is printed out. thank you\n\n[中文]\n按完ASK鍵後請稍等一下就會顯示想要的答案在畫面了. 謝謝\n'''
label.insert("end", notice) 
label.config(state="disabled")

label_scroll.config(command=label.yview)

entry = tk.Entry(window, font=("Arial", 14), width=50)
entry.insert(0, "Ask something to AI !")
entry.pack(side="bottom")
entry.bind("<FocusIn>", temp_text) 

button = tk.Button(window, text="Ask AI", font=("Arial", 14), command=aitext)
button.pack(side="bottom")

window.attributes('-topmost',True) 
window.mainloop()
