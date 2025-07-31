import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


root = tk.Tk()
root.title("Emergency QR Card Generator")
root.geometry("1000x800")
selected_image_path = None

#adding labels
def grab_labels():
    global entry_name, entry_address, entry_zipcode, entry_city, entry_state, entry_bloodtype, entry_allergies, entry_conditions, entry_phone, entry_pronouns, entry_primcontact, entry_primcontact_rela, entry_primcontact_phone, entry_seccontact, entry_seccontact_rela, entry_seccontact_phone  

    tk.Label(root, text = "Full name").pack()
    entry_name = tk.Entry(root)
    entry_name.pack()

    tk.Label(root, text = "Address. Include unit number if applicable.").pack()
    entry_address = tk.Entry(root)
    entry_address.pack()

    tk.Label(root, text = "Zip Code").pack()
    entry_zipcode = tk.Entry(root)
    entry_zipcode.pack()

    tk.Label(root, text = "City").pack()
    entry_city = tk.Entry(root)
    entry_city.pack()

    tk.Label(root, text = "State").pack()
    entry_state = tk.Entry(root)
    entry_state.pack()

    tk.Label(root, text = "Blood Type").pack()
    entry_bloodtype = tk.Entry(root)
    entry_bloodtype.pack()

    tk.Label(root, text = "Allergies").pack()
    entry_allergies = tk.Entry(root)
    entry_allergies.pack()

    tk.Label(root, text = "Conditions").pack()
    entry_conditions = tk.Entry(root)
    entry_conditions.pack()

    tk.Label(root, text = "Phone Number").pack()
    entry_phone = tk.Entry(root)
    entry_phone.pack()

    tk.Label(root, text = "Pronouns").pack()
    entry_pronouns = tk.Entry(root)
    entry_pronouns.pack()

    tk.Label(root, text = "Primary Contact").pack()
    entry_primcontact = tk.Entry(root)
    entry_primcontact.pack()

    tk.Label(root, text = "Primary Contact Relationship").pack()
    entry_primcontact_rela = tk.Entry(root)
    entry_primcontact_rela.pack()

    tk.Label(root, text = "Primary Contact Phone").pack()
    entry_primcontact_phone = tk.Entry(root)
    entry_primcontact_phone.pack()

    tk.Label(root, text = "Secondary Contact").pack()
    entry_seccontact = tk.Entry(root)
    entry_seccontact.pack()

    tk.Label(root, text = "Secondary Contact Relationship").pack()
    entry_seccontact_rela = tk.Entry(root)
    entry_seccontact_rela.pack()

    tk.Label(root, text = "Secondary Contact Phone").pack()
    entry_seccontact_phone = tk.Entry(root)
    entry_seccontact_phone.pack()

def choose_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(
        title="Choose a picture to include",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if selected_image_path:
        messagebox.showinfo("Image Selected", f"Added image:\n{selected_image_path}")

def generate_card():
    name = entry_name.get()
    address = entry_address.get()
    zip = entry_zipcode.get()
    city = entry_city.get()
    state = entry_state.get()
    blood_type = entry_bloodtype.get()
    allergies = entry_allergies.get()
    conditions = entry_conditions.get()
    phone = entry_phone.get()
    pronouns = entry_pronouns.get()
    prim_contact = entry_primcontact.get()
    prim_contact_rela = entry_primcontact_rela.get()
    prim_contact_phone = entry_primcontact_phone.get()
    sec_contact = entry_seccontact.get()
    sec_contact_rela = entry_seccontact_rela.get()
    sec_contact_phone = entry_seccontact_phone.get()

    from PIL import Image, ImageDraw, ImageFont

    # Create blank image
    card = Image.new("RGB", (600, 400), color=(255, 255, 255))
    draw = ImageDraw.Draw(card)

    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()

    data = f"""EMERGENCY INFO CARD

    - Personal Info -
      Name: {name}
      Address: {address}, {city}, {state} {zip}
      Phone: {phone}
      Allergies: {allergies}
      Conditions: {conditions}
      Blood Type: {blood_type}
      Pronouns: {pronouns}

    - Contacts -
      Primary Contact: {prim_contact} - {prim_contact_rela}
      Phone: {prim_contact_phone}

      Secondary Contact: {sec_contact} - {sec_contact_rela}
      Phone: {sec_contact_phone}
    """

    if not all([
        name.strip(), address.strip(), zip.strip(), city.strip(), state.strip(),
        blood_type.strip(), allergies.strip(), conditions.strip(), phone.strip(),
        pronouns.strip(), prim_contact.strip(), prim_contact_rela.strip(),
        prim_contact_phone.strip(), sec_contact.strip(), sec_contact_rela.strip(),
        sec_contact_phone.strip()
    ]):
        messagebox.showerror("Missing Info", "Please fill in all fields.")
    elif not selected_image_path:
        messagebox.showerror("Missing Image", "Please select an image to include on the card.")
    else:
        draw.multiline_text((20, 20), data, fill=(0, 0, 0), font=font, spacing=4)
        try:
            user_img = Image.open(selected_image_path)
            user_img.thumbnail((100, 100))
            card.paste(user_img, (card.width - 120, 20))
            card.save("emergency_card.png")
            messagebox.showinfo("Success", "Emergency card saved as 'emergency_card.png'")
        except Exception as e:
            messagebox.showerror("Image Error", f"Failed to paste image: {e}")
    
    return
    
grab_labels()
tk.Button(root, text="Add Image to Card", command=choose_image).pack()
tk.Button(root, text= "Generate", command=generate_card).pack()
root.mainloop()