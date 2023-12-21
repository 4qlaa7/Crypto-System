import tkinter as tk
from tkinter import ttk

class CryptoChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Chat App")

        # Create a StringVar to store the selected crypto technique
        self.crypto_technique_var = tk.StringVar()

        # Create a dropdown menu for crypto techniques
        crypto_label = tk.Label(root, text="Crypto Technique:")
        crypto_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        crypto_options = ["AES", "RSA", "DES","RC-4" , "ELGAMMAL"]  # Add more as needed
        crypto_dropdown = ttk.Combobox(root, textvariable=self.crypto_technique_var, values=crypto_options)
        crypto_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        crypto_dropdown.set(crypto_options[0])  # Set default value

        # Create a text box for messages
        message_label = tk.Label(root, text="Message:")
        message_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.message_entry = tk.Entry(root, width=40)
        self.message_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Create a chat window
        self.chat_window = tk.Text(root, height=15, width=50, state=tk.DISABLED)
        self.chat_window.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Create a send button
        send_button = tk.Button(root, text="Send", command=self.send_message)
        send_button.grid(row=3, column=0, columnspan=2, pady=10)

    def send_message(self):
        message = self.message_entry.get()
        crypto_technique = self.crypto_technique_var.get()

        # Perform crypto operations on the message using the selected technique
        # You can add the crypto logic here based on the selected technique
        
        # Display the message in the chat window
        self.display_message(f"{crypto_technique}: {message}")

    def display_message(self, message):
        self.chat_window.config(state=tk.NORMAL)
        self.chat_window.insert(tk.END, message + "\n")
        self.chat_window.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoChatApp(root)
    root.mainloop()
