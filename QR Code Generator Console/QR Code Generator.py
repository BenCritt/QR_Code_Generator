import qrcode
import os

active = True  # This flag is for the while loop.
count = 0  # This will allow for multiple new files to be generated.

while (
    active
):  # This will return false once the user indicates they have no more QR codes to create.
    data = input("Please enter your text here: ")

    # Initializes the QRCode object:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    # Adds data to the QRCode:
    qr.add_data(data)

    count += 1
    # The value of "count" increases with every pass to make sure new files are written instead of one file being rewritten.
    # Without this count integer increasing with each new QRCode generation, text would accumulate and the QRCode image overwritten.
    # The new QRCode image would then become unusable.

    # Generates the QRCode:
    qr.make(fit=True)

    # Creates an image from the QRCode that is usable by the user:
    img = qr.make_image(fill_color="black", back_color="white")

    # Gets the user's home directory:
    home_dir = os.path.expanduser("~")

    # Combines the home directory with the "Downloads" folder to create the save directory:
    save_dir = os.path.join(home_dir, "Downloads")

    # Ensures that the directory exists and creates it if it doesn't exist:
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Assigns the filename using "count" to allow for multiple unique code generations:
    filename = f"qrcode{count}.png"

    # Combines the directory and filename to create the full path:
    full_path = os.path.join(save_dir, filename)

    # Saves the QRCode image in the user's "Downloads" folder:
    img.save(full_path)

    # Asks the user if they wish to continue creating QR Codes:
    repeat = input("Would you like to enter another response? (y/n): ")

    # This ends the program:
    if repeat == "n":
        active = False

    # Any answer other than "n" is presumed to be a "yes" for the sake of usability.
