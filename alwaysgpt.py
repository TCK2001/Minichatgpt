#!/usr/bin/env python
# coding: utf-8

# In[2]:


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
    
    #print(f"GPT : {assistant_content}")
    
    label.config(state="normal") 
    label.delete("1.0", "end") 
    label.insert("end", assistant_content) 
    label.config(state="disabled")

def temp_text(e):
    entry.delete(0,"end")
    
# def update_label():
#     text = entry.get()
#     label.config(state="normal") # normal로 설정하면 해당 위젯 활성화. 
#     label.delete("1.0", "end") # 모든 글자 지우고
#     label.insert("end", text) # text를 삽입
#     label.config(state="disabled") # disabled로 설정하면 해당 위젯 비활설화 즉 사용자가 못 건듬.

# 창 생성
window = tk.Tk()
window.geometry("800x400")
window.title("Minichatgpt by TCK")

# 라벨 생성
label_frame = tk.Frame(window)
label_frame.pack(side="top", fill="both", expand=True)

# side는 위젯을 배치할 방향을 나타내며, "top", "bottom", "left", "right" 중 하나를 사용할 수 있습니다. 
#"top"을 지정하면 부모 위젯의 가장 위쪽에 배치됩니다.

# fill은 위젯이 배치될 공간을 어떻게 채울지를 나타내며, "x", "y", "both", "none" 중 하나를 사용할 수 있습니다. 
#"both"를 지정하면 부모 위젯의 모든 빈 공간을 채우도록 위젯의 크기를 늘리거나 줄입니다.

# expand는 부모 위젯의 크기가 위젯의 크기보다 클 때 위젯이 어떻게 동작할지를 결정합니다. 
# True를 지정하면 위젯이 부모 위젯의 빈 공간을 모두 채우도록 크기를 늘리고, False를 지정하면 위젯이 원래 크기를 유지합니다.

label_scroll = tk.Scrollbar(label_frame)
label_scroll.pack(side="right", fill="y")

label = tk.Text(label_frame, font=("Arial", 14), wrap="word", height=10, width=50, bg="gray", state="disabled", yscrollcommand=label_scroll.set)
# wrap 옵션을 "word"로 설정하면, tk.Text()에서 글자가 너무 길어서 화면에 안보일경우 알아서 줄 바꿈을 해줌.

label.pack(side="left", fill="both", expand=True)
label.config(state="normal") 
label.delete("1.0", "end") 
notice = '''[한글]\n버튼을 누르고 좀 기달리시면 원하던 답변이 출력 됩니다. 감사합니다 \n\n[English]\nIf you press the button and wait for a while, the answer you want is printed out. thank you\n\n[中文]\n按完ASK鍵後請稍等一下就會顯示想要的答案在畫面了. 謝謝\n'''
label.insert("end", notice) 
label.config(state="disabled")

label_scroll.config(command=label.yview)
# label_scroll 변수는 tk.Scrollbar() 위젯을 생성합니다. 
# tk.Scrollbar() 위젯은 label 변수에서 보여지는 텍스트의 스크롤바 역할을 합니다.

# 입력 창 생성
entry = tk.Entry(window, font=("Arial", 14), width=50)
entry.insert(0, "Ask something to AI !")
entry.pack(side="bottom")
entry.bind("<FocusIn>", temp_text) # 클릭하면FocusIn 바로 temp_text를 불러서 예시 문장을 지움.

# 버튼 생성
button = tk.Button(window, text="Ask AI", font=("Arial", 14), command=aitext)
button.pack(side="bottom")

window.attributes('-topmost',True) # 항상 맨 윗쪽에 있는 창
window.mainloop()


# In[ ]:





# In[ ]:




