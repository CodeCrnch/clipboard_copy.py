import pyperclip

filename = "clipboard_texts.txt"

while True:
    pyperclip.waitForNewPaste()
    
    clipboard_text = pyperclip.paste()

    with open(filename, "a") as f:
        f.write(clipboard_text + "\n")
