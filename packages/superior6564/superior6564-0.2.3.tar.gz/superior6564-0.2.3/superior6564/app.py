"""
:authors: Superior_6564
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2022 Superior_6564
"""
import dearpygui.dearpygui as dpg
import webbrowser
import os
import requests
import itertools
import subprocess
import sys


def run():
    dpg.create_context()

    with open("NotoSans-Regular.ttf", "wb") as f:
        f.write(requests.get('https://github.com/Superior-GitHub/superior6564/raw/main/superior6564/app/NotoSans-Regular.ttf').content)

    big_let_start = 0x00C0  # Capital "A" in cyrillic alphabet
    big_let_end = 0x00DF  # Capital "Я" in cyrillic alphabet
    small_let_end = 0x00FF  # small "я" in cyrillic alphabet
    remap_big_let = 0x0410  # Starting number for remapped cyrillic alphabet
    alph_len = big_let_end - big_let_start + 1  # adds the shift from big letters to small
    alph_shift = remap_big_let - big_let_start  # adds the shift from remapped to non-remapped

    def to_cyr(instr):  # conversion function
        out = []  # start with empty output
        for i in range(0, len(instr)):  # cycle through letters in input string
            if ord(instr[i]) in range(big_let_start, small_let_end + 1):  # check if the letter is cyrillic
                out.append(chr(ord(instr[i]) + alph_shift))  # if it is change it and add to output list
            else:
                out.append(instr[i])  # if it isn`t don`t change anything and just add it to output list
        return ''.join(out)  # convert list to string

    with dpg.font_registry():
        with dpg.font("NotoSans-Regular.ttf", 20) as default_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
            biglet = remap_big_let  # Starting number for remapped cyrillic alphabet
            for i1 in range(big_let_start, big_let_end + 1):  # Cycle through big letters in cyrillic alphabet
                dpg.add_char_remap(i1, biglet)  # Remap the big cyrillic letter
                dpg.add_char_remap(i1 + alph_len, biglet + alph_len)  # Remap the small cyrillic letter
                biglet += 1  # choose next letter

    def print_name_def(name: str):
        print("-", end="")
        for i in range(len(name)):
            print("-", end="")
        print("-")
        print(f"|{name}|")
        print("-", end="")
        for i in range(len(name)):
            print("-", end="")
        print("-")

    def generator_ru_words():
        print("Start generator of words")
        with open("russian_nouns.txt", "wb") as f:
            f.write(requests.get('https://raw.githubusercontent.com/Superior-GitHub/Superior6564/main/superior6564/russian_nouns.txt').content)

        with open("degget_elite.jpg", "wb") as f:
            f.write(requests.get('https://github.com/Superior-GitHub/superior6564/raw/main/superior6564/degit_Elite.jpg').content)

        width, height, channels, data = dpg.load_image('degget_elite.jpg')

        with dpg.texture_registry():
            dpg.add_static_texture(width, height, data, tag="image_100", parent="generator_group")

        def print_value():
            print_name_def("Generator of words")
            raw_letters = dpg.get_value('Input all letters')
            raw_length = dpg.get_value('Input length of words')

            if raw_letters == '':
                raw_letters = "ëóïîãð" # "лупогр"
                print(f"Example letters: {to_cyr(raw_letters)}")
            else:
                print(f"Input all letters: {to_cyr(raw_letters)}")

            if raw_length == '':
                raw_length = 3
                print(f"Example length of words: {raw_length}")
            else:
                print(f"Input length of words: {raw_length}")

            all_of_letters = to_cyr(raw_letters)
            length_of_words = int(raw_length)

            with open('russian_nouns.txt', encoding='utf-8') as f1:
                with open("results_gen_ru_words.txt", "w", encoding='utf-8') as f2:
                    list_of_ru_words = []
                    number_of_words_txt = 51301
                    for j in range(number_of_words_txt):
                        if j != (number_of_words_txt - 1):
                            list_of_ru_words.append(f1.readline()[0:-1])
                        else:
                            list_of_ru_words.append(f1.readline()[0:])
                    f2.write(f"Слова из {length_of_words} букв:\n")
                    words = set(itertools.permutations(all_of_letters, r=length_of_words))
                    count_2 = 1
                    for word in words:
                        count = 0
                        generate_word = "".join(word)
                        for j in range(len(list_of_ru_words)):
                            if generate_word == list_of_ru_words[j] and count == 0:
                                f2.write(f"{count_2} слово: {generate_word}\n")
                                count += 1
                                count_2 += 1

            with open('results_gen_ru_words.txt', encoding='utf-8') as f3:
                dpg.delete_item('text_group', children_only=True)
                left_pos = 525
                right_pos = 245
                f3.readline()
                count = 0
                for line in f3.readlines():
                    dpg.add_text(pos=[left_pos, right_pos], default_value=line[:-1], parent='text_group')
                    right_pos += 20
                    count += 1
                    if count == 8:
                        left_pos += 170
                        right_pos = 245
                print(f"Count of words: {count}")

        combo_values = ["3", "4", "5", "6", "7"]
        dpg.add_text(tag="Text for writing letters", pos=[210, 215], default_value="Write all of letters which do you have:", parent="generator_group")
        dpg.add_input_text(tag="Input all letters", width=300, height=300, pos=[210, 245], parent="generator_group")
        dpg.add_text(tag="Text for choosing length of words", pos=[210, 275], default_value="Choose length of words which do you need:", parent="generator_group")
        dpg.add_combo(tag="Input length of words", width=300, pos=[210, 305], items=combo_values, parent="generator_group")
        dpg.add_button(tag="Button for sending parameters", label="Send parameters", callback=print_value, pos=[295, 340], parent="generator_group")
        dpg.add_text(tag="Text for results", pos=[525, 215], default_value="Results:", parent="generator_group")
        dpg.add_image(tag="Image of Elite Degget", texture_tag="image_100", pos=[0, 215], parent="generator_group")
        dpg.draw_line(p1=(190, 181), p2=(510, 181), parent="generator_group")
        dpg.draw_line(p1=(190, 380), p2=(510, 380), parent="generator_group")
        dpg.draw_line(p1=(510, 181), p2=(510, 380), parent="generator_group")
        dpg.draw_line(p1=(510, 181), p2=(805, 181), parent="generator_group")
        dpg.draw_line(p1=(510, 380), p2=(805, 380), parent="generator_group")
        dpg.draw_line(p1=(805, 181), p2=(805, 380), parent="generator_group")
        dpg.bind_font(default_font)
        dpg.bind_item_font("Input all letters", default_font)
        with dpg.group(tag='text_group', parent="generator_group"):
             pass

    def get_info():
        print("Start get_info")

        def open_home_page():
            webbrowser.open_new_tab("https://github.com/Superior-GitHub/Superior6564")

        def open_download_url():
            webbrowser.open_new_tab("https://github.com/Superior-GitHub/Superior6564/archive/refs/heads/main.zip")

        def open_wiki():
            webbrowser.open_new_tab("https://github.com/Superior-GitHub/superior6564/wiki")

        with open("readme.md", "wb") as f:
            f.write(requests.get('https://raw.githubusercontent.com/Superior-GitHub/superior6564/main/README.md').content)

        path = os.getcwd() + "/readme.md"
        line_need = []
        name_need = ["Name", "Vers", "Desc", "Home", "Down", "Wiki", "Auth", "Lice"]

        with open(path) as f:
            for i in range(19):
                line = f.readline()
                if line[:4] in name_need:
                    line_need.append(line)

        with open(path) as f:
            dictionary = {"Name": line_need[0], "Version": line_need[1], "Description": line_need[2],
                          "Home-Page": line_need[3], "Download-URL": line_need[4], "Wiki": line_need[5],
                          "Author": line_need[6], "Author-email": line_need[7], "License": line_need[8]}
        dpg.add_text(tag="Name", pos=[5, 40], default_value=dictionary["Name"], parent="info_group")
        dpg.add_text(tag="Version", pos=[5, 60], default_value=dictionary["Version"], parent="info_group")
        dpg.add_text(tag="Home-Page", pos=[5, 80], default_value=dictionary["Home-Page"][:10], parent="info_group")
        dpg.add_text(tag="Download-URL", pos=[5, 100], default_value=dictionary["Download-URL"][:14], parent="info_group")
        dpg.add_text(tag="Wiki", pos=[5, 120], default_value=dictionary["Wiki"][:6], parent="info_group")
        dpg.add_text(tag="Author", pos=[5, 140], default_value=dictionary["Author"], parent="info_group")
        dpg.add_text(tag="Author-email", pos=[5, 160], default_value=dictionary["Author-email"], parent="info_group")
        dpg.add_text(tag="License", pos=[5, 180], default_value=dictionary["License"][:-19], parent="info_group")
        dpg.add_button(tag="Open Home-Page", label="Open", callback=open_home_page, pos=[100, 80], parent="info_group")
        dpg.add_button(tag="Open Download-URL", label="Open", callback=open_download_url, pos=[120, 100], parent="info_group")
        dpg.add_button(tag="Open Wiki", label="Open", callback=open_wiki, pos=[45, 120], parent="info_group")
        dpg.draw_line(p1=(270, -10), p2=(270, 182), parent="info_group")

    def install_package():
        print("Start installing of package")

        def get_and_install():
            print_name_def("Install of package")
            dpg.delete_item("install_error", children_only=True)
            package = dpg.get_value("Input name of package")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
                print(f"Package {package} installed.")
                dpg.add_text(tag="Good description 1", pos=[285, 160], default_value=f"Package {package} installed.", parent="install_error")
            except subprocess.CalledProcessError:
                print("ERROR: Bad name.")
                print("Write the correct name of the package.")
                dpg.add_text(tag="Error description 1", pos=[285, 160], default_value="ERROR: Bad name.", parent="install_error")
                dpg.add_text(tag="Error description 2", pos=[285, 180], default_value="Write the correct name of the package.", parent="install_error")
            except "Requirement already satisfied":
                print("Requirement already satisfied")

        dpg.add_text(tag="Install package", pos=[285, 20], default_value="Install packages:", parent="install_package")
        dpg.add_text(tag="Install package description", pos=[285, 40], default_value="Write the correct name of the package:", parent="install_package")
        dpg.add_input_text(tag="Input name of package", width=265, height=300, pos=[285, 70], parent="install_package")
        dpg.add_button(tag="Button for sending name of package", label="Send", callback=get_and_install, pos=[285, 105], parent="install_package")
        dpg.add_text(tag="Text for status of installing", pos=[285, 135], default_value="Status:", parent="install_package")
        dpg.draw_line(p1=(550, -10), p2=(550, 182), parent="install_package")
        with dpg.group(tag="install_error"):
            pass

    def pip_upgrade():
        print("Start pip upgrading")

        def upgrade():
            print_name_def("Pip upgrade")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            print("Pip upgraded")
            dpg.add_text(tag="Text of status for pip upgrading", pos=[560, 110], default_value="Pip upgraded", parent="pip_upgrade")

        dpg.add_text(tag="Pip upgrade", pos=[560, 20], default_value="Pip upgrade:", parent="pip_upgrade")
        dpg.add_text(tag="Pip upgrade description", pos=[560, 40], default_value="Click on the button to upgrade pip.", parent="pip_upgrade")
        dpg.add_button(tag="Button for upgrading pip", label="Send", callback=upgrade, pos=[660, 65], parent="pip_upgrade")
        dpg.add_text(tag="Text for status of upgrading", pos=[560, 90], default_value="Status:", parent="pip_upgrade")

    with dpg.window(tag='main_window', label="Main", width=820, height=455, no_move=True, no_resize=True, no_close=True):
        dpg.add_text(tag="Information", pos=[5, 20], default_value="Information:")
        get_info()
        generator_ru_words()
        install_package()
        pip_upgrade()
        with dpg.group(tag='info_group'):
            pass
        with dpg.group(tag='generator_group'):
            pass
        with dpg.group(tag='install_package'):
            pass
        with dpg.group(tag="pip_upgrade"):
            pass

    dpg.create_viewport(title='App', width=831, height=455, resizable=False)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
