import tkinter as tk
from tkinter import filedialog
import requests

class CloudUploader:
    def __init__(self, root):
        self.root = root
        self.root.title("Cloud Uploader")
        self.root.geometry("400x200")
        self.root.configure(bg="black")

        self.filepath = ""

        self.upload_button = tk.Button(
            root, text="Choose File", command=self.choose_file,
            bg="darkblue", fg="white", font=("Helvetica", 12), relief="flat", padx=10, pady=5, highlightthickness=0, borderwidth=0
        )
        self.upload_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.send_button = tk.Button(
            root, text="Send", command=self.send_file,
            bg="darkblue", fg="white", font=("Helvetica", 12), relief="flat", padx=10, pady=5, highlightthickness=0, borderwidth=0
        )
        self.send_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.status_label = tk.Label(root, text="", bg="black", fg="white", font=("Helvetica", 10))
        self.status_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def choose_file(self):
        self.filepath = filedialog.askopenfilename()
        if self.filepath:
            self.status_label.config(text="File chosen: " + self.filepath.split("/")[-1])
        else:
            self.status_label.config(text="No file chosen.")

    def send_file(self):
        if self.filepath:
            self.status_label.config(text="Uploading...")
            webhook_url = "ENTER YOUR DISCORD WEBHOOK"
            with open(self.filepath, "rb") as f:
                file_data = {"file": f}
                response = requests.post(webhook_url, files=file_data)

            if response.status_code == 204:
                self.status_label.config(text="Upload successful!")
            else:
                self.status_label.config(text="Upload failed.")
        else:
            self.status_label.config(text="No file to upload.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CloudUploader(root)
    root.mainloop()
