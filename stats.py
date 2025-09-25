def number_of_words(tekst):
    words = tekst.split()
    return len(words)
def character_count(tekst):
    character_dict = {}
    small_print = tekst.lower()
    for char in small_print:
        if char.isalpha():
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    return character_dict
def sort_on(item):
    return item["num"]
def sort_character_count(character_count):
    dict_list = [{"char": char, "num": num} for char, num in character_count.items()]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list