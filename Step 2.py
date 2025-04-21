import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

# Function to handle speech-to-text conversion
def speech_to_text():
    recognizer = sr.Recognizer()  # Initialize the recognizer
    try:
        with sr.Microphone() as source:  # Use the microphone as the input source
            result_label.config(text="Listening...")  # Update status in the UI
            app.update_idletasks()
            audio = recognizer.listen(source)  # Listen to the audio input
            text = recognizer.recognize_google(audio)  # Convert speech to text
            result_label.config(text=f"Recognized Text: {text}")  # Display the result
    except sr.UnknownValueError:
        result_label.config(text="Could not understand audio.")
    except sr.RequestError as e:
        result_label.config(text=f"Service error: {e}")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

# Create the main application window
app = tk.Tk()
app.title("Speech to Text Converter")
app.geometry("500x300")

# UI Components
header_label = tk.Label(app, text="Speech to Text Converter", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

instruction_label = tk.Label(app, text="Click the button below and speak into the microphone.", font=("Arial", 12))
instruction_label.pack(pady=5)

record_button = tk.Button(app, text="Start Recording", font=("Arial", 12), command=speech_to_text)
record_button.pack(pady=10)

result_label = tk.Label(app, text="Recognized Text will appear here.", font=("Arial", 12), wraplength=450, justify="left")
result_label.pack(pady=20)

# Run the application
app.mainloop()
