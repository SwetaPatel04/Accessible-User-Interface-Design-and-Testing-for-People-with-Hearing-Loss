import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import speech_recognition as sr

# ASL Image Mapping Dictionary
asl_mapping = {
    '1': 'hand1.png', '2': 'hand2.png', '3': 'hand3.png', 
    '4': 'hand4.png', '5': 'hand5.jpg', '6': 'hand6.png', 
    '7': 'hand7.png', '8': 'hand8.png', '9': 'hand9.png', 
    '0': 'hand0.png'
}

# Step 1: Convert Text to ASL Images
def text_to_asl_images(text):
    images = []
    for char in text:
        if char in asl_mapping:
            try:
                img = Image.open(asl_mapping[char])
                img = img.resize((150, 150))  # Resize images to fit in the UI
                images.append(ImageTk.PhotoImage(img))
            except Exception as e:
                print(f"Error loading image for '{char}': {e}")
    return images

# Step 2: Convert Speech to Text
def speech_to_text():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            # Calibrate the microphone for ambient noise
            result_label.config(text="Calibrating microphone...")
            app.update_idletasks()
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Microphone calibrated.")
            
            # Start listening
            result_label.config(text="Listening...")
            app.update_idletasks()
            audio = recognizer.listen(source)
            
            # Save the recorded audio for debugging
            with open("test_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
            
            result_label.config(text="Recognizing speech...")
            app.update_idletasks()
            text = recognizer.recognize_google(audio, language="en-US")
            print(f"Recognized text: {text}")
            return text
    except sr.UnknownValueError:
        print("Speech was unclear.")
        return "Speech was unclear. Please try again."
    except sr.RequestError as e:
        print(f"Speech recognition service error: {e}")
        return f"Service error: {e}"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"An unexpected error occurred: {e}"

# Step 3: Speech to ASL Conversion
def speech_to_asl():
    result_label.config(text="Processing speech...")
    app.update_idletasks()
    text = speech_to_text()
    if text and not text.startswith("Speech was unclear"):
        for widget in result_frame.winfo_children():
            widget.destroy()  # Clear previous images
        
        asl_images = text_to_asl_images(text)
        if asl_images:
            for img in asl_images:
                label = tk.Label(result_frame, image=img)
                label.image = img  # Keep reference to avoid garbage collection
                label.pack(side="left", padx=2)
            result_label.config(text="ASL Translation Complete!")
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
