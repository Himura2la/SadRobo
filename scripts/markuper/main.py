import os
import re
import shutil

dialogs_path = "..\\..\\dialogs"
pictures_path = "..\\..\\pictures"
texts_path = "..\\..\\texts"

env_re_find = re.compile(r"((-.*\n)+)(\n*.*)\n*((-.*\n)+)")
env_re_replace = \
    r"\\begin{dialog}\n\1\\end{dialog}\n\n\\begin{monolog}\3\n\\end{monolog}\n\n\\begin{dialog}\n\4\\end{dialog}"

rep_re_find = re.compile(r'(^-)(.*?\n)((^-)(.*?\n))?', re.MULTILINE)
rep_re_replace = r"\\X\2\\R\5"


def process_dialog():
    if title in existing_dialogs:
        return
    # number, title, txt_path, pic_path
    text = open(txt_path, encoding="utf-8").read() + "\n"
    text = re.sub(env_re_find, env_re_replace, text)
    text = re.sub(rep_re_find, rep_re_replace, text)

    target_txt_path = os.path.join(texts_path, title + ".txt")
    target_pic_path = os.path.join(pictures_path, title + "." + pic_path.split(".")[-1].lower())

    if False: # Beware errors
        with open(target_txt_path, "w") as target:
            target.write(text)
        shutil.copy(pic_path, target_pic_path)
    else:
        print("Copy " + pic_path + " --> " + target_pic_path)
        print("Write to " + target_txt_path + ":\n" + text + "\n" + "-"*80)



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
