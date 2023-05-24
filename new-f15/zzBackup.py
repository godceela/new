import os
import tkinter as tk
import pyautogui

root = tk.Tk()

# Create your form elements
# ...

def capture_screenshot():
    # Hide the window temporarily (optional)
    root.withdraw()

    # Capture the screenshot of the form
    screenshot = pyautogui.screenshot()

    # Show the window again (optional)
    root.deiconify()

    # Get the user's "Documents" folder path
    documents_path = os.path.expanduser("~/Documents")

    # Specify the file path for the image
    file_path = os.path.join(documents_path, "form_screenshot.jpg")

    # Save the screenshot as a JPEG image
    screenshot.save(file_path)

    print(f"Screenshot saved as {file_path}")

# Create a button to capture the screenshot
button = tk.Button(root, text="Capture Screenshot", command=capture_screenshot)
button.pack()

root.mainloop()
