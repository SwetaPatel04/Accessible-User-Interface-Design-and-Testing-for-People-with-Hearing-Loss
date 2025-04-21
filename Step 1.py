import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling images

# Mapping dictionary for English text to ASL image paths
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

# Function to convert English text to ASL images
def text_to_asl_images(text):
    images = []
    for char in text.upper():
        if char in asl_mapping:
            try:
                img = Image.open(asl_mapping[char])
                img = img.resize((50, 50))  # Resize image for consistency
                images.append(ImageTk.PhotoImage(img))
            except Exception as e:
                print(f"Error loading image for '{char}': {e}")
    return images

# Function to handle button click
def convert_text():
    text = text_entry.get().strip()
    if text:
        for widget in result_frame.winfo_children():
            widget.destroy()  # Clear previous images
        
        asl_images = text_to_asl_images(text)
        if asl_images:
            for img in asl_images:
                label = tk.Label(result_frame, image=img)
                label.image = img  # Keep a reference to prevent garbage collection
                label.pack(side="left", padx=2)
        else:
            messagebox.showwarning("Conversion Error", "No valid ASL symbols found!")
    else:
        messagebox.showwarning("Input Error", "Please enter some text!")

# Create the main application window
app = tk.Tk()
app.title("Text to ASL Converter")
app.geometry("600x400")

# UI Components
header_label = tk.Label(app, text="Text to ASL Converter", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

text_label = tk.Label(app, text="Enter text to convert:", font=("Arial", 12))
text_label.pack(pady=5)

text_entry = tk.Entry(app, font=("Arial", 12), width=40)
text_entry.pack(pady=5)

convert_button = tk.Button(app, text="Convert to ASL", font=("Arial", 12), command=convert_text)
convert_button.pack(pady=10)

result_frame = tk.Frame(app)
result_frame.pack(pady=10)

# Run the application
app.mainloop()
