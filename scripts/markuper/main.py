import os

dialogs_path = "..\\..\\dialogs"
pictures_path = "..\\..\\pictures"
texts_path = "..\\..\\texts"


def process_dialog():
    if title in existing_dialogs:
        return
    print(number, title, txt_path, pic_path)



existing_pics = {file.split(".")[0] for file in os.listdir(pictures_path)}
existing_texts = {file.split(".")[0] for file in os.listdir(texts_path)}
existing_dialogs = existing_pics & existing_texts

for folder in os.listdir(dialogs_path):
    txt_path, pic_path = [None] * 2
    number, title = folder.split(". ")
    dialog_folder = os.path.join(dialogs_path, folder)
    for file in os.listdir(dialog_folder):
        extension = file.split(".")[-1].lower()
        file_path = os.path.join(dialog_folder, file)
        if extension == "txt":
            txt_path = file_path
        elif extension in {"png", "jpg"}:
            pic_path = file_path
    if txt_path is not None and pic_path is not None:
        process_dialog()
    else:
        print("Inconsistent folder:", dialog_folder)
