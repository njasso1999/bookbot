with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def get_word_count(str):
    words = str.split()
    return len(words)

def get_characters(str):
    lower_str = str.lower()
    chara = {}
    for i in lower_str:
        if i in chara:
            chara[i] += 1
        else:
            chara[i] = 1
    return chara

def sort_on(dict):
    return dict['num']

def print_characters(dict):
    chara_list = []
    for i in dict:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            chara_list.append({"name": i, "num": dict[i]})
    chara_list.sort(reverse=True, key=sort_on)
    for i in chara_list:
        print(f"The '{i['name']}' character was found {i['num']} times")


print_characters(get_characters(file_contents))