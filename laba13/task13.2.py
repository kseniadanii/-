import tkinter as tk

import requests


def get_history(city):
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={city}&exintro=1&explaintext=1&exsectionformat=wiki"
    response = requests.get(url)
    data = response.json()
    pages = data["query"]["pages"]
    for page in pages.values():
        return page["extract"]


root = tk.Tk()
root.title("Исторические факты о городе")


def show_history():
    city = city_entry.get()
    history = get_history(city)
    history_label.config(text=history)


city_label = tk.Label(root, text="Введите название города:")
city_entry = tk.Entry(root)
history_button = tk.Button(root, text="Показать исторические факты", command=show_history)
history_label = tk.Label(root, wraplength=400)

city_label.pack()
city_entry.pack()
history_button.pack()
history_label.pack()

root.mainloop()
