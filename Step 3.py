import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import speech_recognition as sr

# ASL Image Mapping Dictionary
asl_mapping = {
    'A': 'a.jpg', 'B': 'b.jpg', 'C': 'c.jpg', 
    'D': 'd.jpg', 'E': 'e.jpg', 'F': 'f.jpg', 
    'G': 'g.jpg', 'H': 'h.jpg', 'I': 'i.jpg',
    'J': 'j.jpg', 'K': 'k.jpg', 'L': 'l.jpg', 
    'M': 'm.jpg', 'N': 'n.jpg', 'O': 'o.jpg', 
    'P': 'p.jpg', 'Q': 'q.jpg', 'R': 'r.jpg', 
    'S': 's.jpg', 'T': 't.jpg', 'U': 'u.jpg', 
    'V': 'v.jpg', 'W': 'w.jpg', 'X': 'x.jpg', 
    'Y': 'y.jpg', 'Z': 'z.jpg', 
    '1': '1.jpg', '2': '2.jpg', '3': '3.jpg', 
    '4': '4.jpg', '5': '5.jpg', '6': '6.jpg', 
    '7': '7.jpg', '8': '8.jpg', '9': '9.jpg', 
    '0': '0.jpg'
}

# Step 1: Convert Text to ASL Images
def text_to_asl_images(text):
    images = []
    for char in text.upper():
        if char in asl_mapping:
            try:
                img = Image.open(asl_mapping[char])
                img = img.resize((50, 50))  # Resize images to fit in the UI
                images.append(ImageTk.PhotoImage(img))
            except Exception as e:
                print(f"Error loading image for '{char}': {e}")
    return images

# Step 2: Convert Speech to Text
def speech_to_text():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            result_label.config(text="Listening...")
            app.update_idletasks()
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError as e:
        return f"Service error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

# Step 3: Speech to ASL Conversion
def speech_to_asl():
    result_label.config(text="Processing speech...")
    app.update_idletasks()
    text = speech_to_text()
    if text and not text.startswith("Could not"):
        for widget in result_frame.winfo_children():
            widget.destroy()  # Clear previous images
        
        asl_images = text_to_asl_images(text)
        if asl_images:
            for img in asl_images:
                label = tk.Label(result_frame, image=img)
                label.image = img  # Keep reference to avoid garbage collection
                label.pack(side="left", padx=2)
        else:
            result_label.config(text="No valid ASL symbols found!")
    else:
        result_label.config(text=text)

# Create the main application window
app = tk.Tk()
app.title("Speech to ASL Converter")
app.geometry("800x400")

# UI Components
header_label = tk.Label(app, text="Speech to ASL Converter", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

instruction_label = tk.Label(app, text="Click the button below to speak.", font=("Arial", 12))
instruction_label.pack(pady=5)

convert_button = tk.Button(app, text="Start Speech to ASL", font=("Arial", 12), command=speech_to_asl)
convert_button.pack(pady=10)

result_frame = tk.Frame(app)
result_frame.pack(pady=20)

result_label = tk.Label(app, text="ASL Translation will appear here.", font=("Arial", 12), wraplength=500, justify="left")
result_label.pack(pady=10)

# Run the application
app.mainloop()
