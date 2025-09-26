# Self-Learn Bot 🧠🤖

**Self-Learn Bot** is a Python-based interactive chatbot application that can answer user queries, learn from new inputs, and store knowledge locally on your device. The bot is fully offline, meaning all your interactions and data remain private and secure. It uses a local JSON knowledge base and a GUI built with **CustomTkinter**.

---

## Features ✨

* **Interactive GUI:** Clean, modern interface for a smooth user experience.
* **Offline Knowledge Base:** All data is stored locally in `knowledge_base.json`.
* **Self-Learning:** Can learn new questions and answers during runtime.
* **Smart Matching:** Uses `difflib.get_close_matches` to find the closest known questions.
* **User-Friendly:** Enter questions in the input field and get immediate responses.
* **Secure & Private:** Data is never sent to any external server.

---

## Screenshots 🖼️

<img width="783" height="521" alt="image" src="https://github.com/user-attachments/assets/a36edc33-7159-4e71-8b80-15e38fcf219d" />
<img width="397" height="510" alt="image" src="https://github.com/user-attachments/assets/8fcb11f0-b6f2-4311-9227-049bcef581ca" />
<img width="389" height="499" alt="image" src="https://github.com/user-attachments/assets/fbec6ad0-bf60-4e68-aab8-ea9bb3cc74ee" />



---

## Knowledge Base Structure 🗂️

The knowledge base is a JSON file with this structure:

```json
{
  "questions": [
    {
      "question": "hello",
      "answer": "Hello"
    },
    {
      "question": "How are you?",
      "answer": "I'm good"
    }
  ]
}
```

For multiple-choice questions:

```json
{
  "question": "Including the bottom, how many sides are on a square-based pyramid?",
  "A": "three",
  "B": "four",
  "C": "five",
  "D": "six",
  "answer": "C"
}
```

The bot will store new questions automatically.

---

## How It Works ⚙️

1. **Input Processing:** Takes user input from the GUI.
2. **Best Match Search:** Finds the closest question in the knowledge base using fuzzy matching.
3. **Response Generation:** Shows the answer if found.
4. **Training Mode:** If the question is new, prompts the user for the answer and saves it in `knowledge_base.json`.
5. **Persistence:** All data is stored offline and can only be accessed through the bot.

---

## Dependencies 📦

* Python 3.10+
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* [Pillow](https://pillow.readthedocs.io/)
* Standard Python library (`json`, `difflib`)

---

## Future Improvements 🔧

* Add voice input and output.
* Enable categorization of questions for faster search.
* Add multi-language support.
* Improve the UI with dark/light theme switching.

---

## Privacy & Security 🔒

* Everything is stored locally.
* No data is shared with external servers.
* Knowledge base is encrypted (optional feature in future versions).


---

## Author 👨‍💻

Arya Ramachandran
Email: [your.email@example.com](mailto:aryatheauthor@gmail.com)

---
