import json
from difflib import get_close_matches
import customtkinter as CTk
from PIL import Image

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

global theme_color
theme_color = "#101010"

#main codes
class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Self-Learn Bot")
        self.geometry("355x400")
        self.config(bg="#101010")
        #self.resizable(0, 0)
        self.show_homepage()

    def do_task_on_enter(self, event):
        self.do_task()

    def show_homepage(self):
        self.clear_frame()
        self.clear_frame()
        top_bar = CTk.CTkFrame(
            self, width=200, height=40, fg_color="transparent",
            bg_color=theme_color
        )
        top_bar.pack(padx=15, pady=10)

        back_icon_path = "bg.png"
        back_icon_image = Image.open(back_icon_path)
        back_icon = CTk.CTkImage(light_image=back_icon_image)  
        button_back = CTk.CTkButton(
            top_bar, image=back_icon, width=30, height=40, text=None,
            bg_color=theme_color, hover_color=theme_color, fg_color=theme_color,
            corner_radius=40
        )
        button_back.grid(row=0, column=0, padx=0, pady=0)

        title_label = CTk.CTkLabel(
            top_bar, text=f"AutoBot", font=("Arial Bold", 25), 
            fg_color=theme_color, bg_color=theme_color, 
            wraplength=300, corner_radius=20
        )
        title_label.grid(row=0, column=1, padx=20, pady=10)

        operations_icon_path = "operations.png"
        operations_icon_image = Image.open(operations_icon_path)
        operations_icon = CTk.CTkImage(light_image=operations_icon_image) 

        global button_operations
        button_operations = CTk.CTkButton(
            top_bar, image=operations_icon, width=30, height=40, text=None,
            bg_color=theme_color, hover_color="#1b1b1b", fg_color=theme_color,
            corner_radius=40
        )
        button_operations.grid(row=0, column=2, padx=0, pady=0)
        
        global home_page_entry
        home_page_entry = CTk.CTkEntry(
            self, bg_color=theme_color, corner_radius=20, 
            width=1000, height=70, justify="left", font=("Arial Bold", 17), fg_color="#1b1b1b"
        )
        home_page_entry.pack(padx=10, pady=0)        

        def on_entry_click(event):
            if home_page_entry.get() == "Type here & enter to execute...":
                home_page_entry.delete(0, CTk.END)
        
        home_page_entry.focus()
        home_page_entry.insert(0, "Type here & enter to execute...")
        home_page_entry.bind("<FocusIn>", on_entry_click)
        home_page_entry.bind("<Return>", self.do_task_on_enter)
        
        branding = CTk.CTkLabel(
            self, text="Product of The Automation Company", font=("Arial Bold", 15),
            bg_color=theme_color
        )
        branding.pack(padx=0, pady=5)

        def hide_result_button():
            home_page_entry.delete(0, CTk.END)
            self.result_button.pack_forget()

        def show_result_button():
            self.result_button.pack(padx=10, pady=10)

        def on_button_click():
            hide_result_button()

        self.result_button = CTk.CTkButton(
            self, text=f" ", width=1000, height=80, font=("Arial Bold", 17), fg_color=theme_color, 
            bg_color=theme_color, corner_radius=20, hover_color="#6F1C1C", command=on_button_click
        )
        self.result_button.pack(padx=10, pady=10)

        def on_button_click():
            self.result_button.pack_forget()
        self.result_button.pack_forget()
        
        title_label = CTk.CTkLabel(
            self, text=f"\nTip : type a command, press enter to execute, once done click on the output button to delete it\n",
            font=("Arial Bold", 15), fg_color="#1a1a1a", bg_color=theme_color, width=1000,
            wraplength=300, corner_radius=20,
        )
        title_label.pack(side='bottom',padx=10, pady=10)

    def do_task(self):
        query = home_page_entry.get().lower()
        knowledge_base: dict = load_knowledge_base('knowledge_base.json')
        user_input = query
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            self.result_button.pack(padx=10, pady=10)
            self.result_button.configure(
                text=(answer), fg_color="#1b1b1b"
            )
        else:
            self.result_button.pack(padx=10, pady=10)
            self.result_button.configure(
                text=("Answer not found. Train the model."), fg_color="#1b1b1b"
            )
            dialog = CTk.CTkInputDialog(text="Train Jace to respond to this question", title="Test")
            new_answer = dialog.get_input()  # waits for input

            if new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question":user_input, "answer":new_answer})
                save_knowledge_base("knowledge_base.json", knowledge_base)
                print(f"Jace : Response added")
                self.result_button.configure(
                    text=("Response added."), fg_color="#1b1b1b"
                )

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.pack_forget()

#__main__ execution
app = App()
app.title("Self-Learn Bot v0.1.101")
app.mainloop()