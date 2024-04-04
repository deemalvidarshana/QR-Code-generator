import os
from tkinter import Tk, Label, Button, Entry, Frame
import qrcode
from PIL import Image, ImageTk

# Function to generate QR code from URL
def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Function to update the display with the new QR code image
def update_display(frame, img):
    for widget in frame.winfo_children():
        widget.destroy()
        
    image = ImageTk.PhotoImage(image=img)
    image_label = Label(frame, image=image, bg="#f9fafc")
    image_label.image = image
    image_label.pack(padx=10, pady=10)
    
    # Add a download button
    download_button = Button(frame, text="Download", command=lambda: save_qr_code(img), bg="#4caf50", fg="#fff", bd=0, padx=10, pady=5, activebackground="#3bc746", font=("Helvetica", 12, "bold"))
    download_button.pack(pady=10)

# Function to save the QR code image in Downloads directory
def save_qr_code(img):
    # Get the user's downloads directory
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    filename = os.path.join(downloads_dir, "qr_code.png")
    img.save(filename)
    print(f"QR code saved as {filename}")

# Function to handle the generation and display of QR codes for URLs
def generate_and_display():
    input_text = entry.get()
    urls = input_text.split(',')
    for url in urls:
        img = generate_qr_code(url.strip())
        update_display(display_frame, img)

# Main GUI Application
root = Tk()
root.title("URL QR Code Generator")

# Styling
root.configure(bg="#f9fafc")
root.geometry("500x680")

main_frame = Frame(root, bg="#f9fafc")
main_frame.pack(padx=20, pady=20)

label = Label(main_frame, text="Enter the URL you want to generate QR code :", bg="#f9fafc", fg="#333", font=("Helvetica", 14))
label.pack()

entry = Entry(main_frame, width=50, bd=2, relief="solid", font=("Helvetica", 12))
entry.pack()

generate_button = Button(main_frame, text="Generate QR Codes", command=generate_and_display, bg="#4caf50", fg="#fff", bd=0, padx=10, pady=5, activebackground="#3bc746", font=("Helvetica", 12, "bold"))
generate_button.pack(pady=20)

display_frame = Frame(root, bg="#f9fafc", bd=2, relief="solid")
display_frame.pack(fill="both", expand=True)

root.mainloop()
