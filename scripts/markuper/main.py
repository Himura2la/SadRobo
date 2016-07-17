# -*- coding: utf=8 -*-
import os
import re

dialogs_path = "..\\..\\texts"
marked_up_path = "..\\..\\texts\\marked_up"

env_re_find = re.compile(r"(((^-|–).*\n)+)(\n*.*)\n*(((^-|–).*\n)+)", re.MULTILINE)
env_re_replace = \
    r"\\begin{dialog}\n\1\\end{dialog}\n\n\\begin{monolog}\4\n\\end{monolog}\n\n\\begin{dialog}\n\5\\end{dialog}"

rep_re_find = re.compile(r'(^-|–)(.*?\n)((^-|–)(.*?\n))?', re.MULTILINE)
rep_re_replace = r"\\X\2\\R\5"

existing_dialogs = {}

if not os.path.isdir(marked_up_path):
    os.makedirs(marked_up_path)


def process_dialog(title, text):
    text = re.sub(env_re_find, env_re_replace, text)
    text = re.sub(rep_re_find, rep_re_replace, text)

    target_txt_path = os.path.join(marked_up_path, title + ".tex")

    if True:  # Beware errors !!!
        with open(target_txt_path, "w", encoding='utf-8') as target:
            target.write(text)
    else:
        print("Write to " + target_txt_path + ":\n" + text + "\n" + "-"*80)
        # print("\\newdialog{%s}{%s}{Made in Python}{1}" % (number, title))


for file in os.listdir(dialogs_path):
    file_path = os.path.join(dialogs_path, file)
    if os.path.isfile(file_path):
        text = open(file_path, encoding="utf-8").read() + "\n"
        if text.find("\\begin{") < 0:  # Not marked up
            process_dialog(file.split('.')[0], text)
