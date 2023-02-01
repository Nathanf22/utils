import Levenshtein as levenshtein

str1 = 'But I have promises to keep, and miles to go before I sleep.'
str2 = 'But I have many promises to keep, and miles to run before sleep.'

edit_distance = levenshtein.distance(str1, str2)
similarity_ratio = levenshtein.ratio(str1, str2)


saved_strings = [
    'Hello here!',
    'this is amazing',
    'how are you',
    'I take this',
    'keep working',
    'try this also',
]


search_string = 'how you are'

def find_best(search_string, saved_string, nb = 1):
    my_dict = {}
    if nb == 1:
        greater = -1
        index = -1
        for el in saved_string:
            print(f'el: {el}')
            ratio =  levenshtein.ratio(search_string, el)
            print(f'dist: {ratio} \n')
            if greater < ratio:
                greater = ratio
                index = saved_string.index(el)
        return index, greater
    else:
        ratio_list = []
        indexs = []
        for num, el in enumerate(saved_string):
            ratio = levenshtein.ratio(search_string, el)
            index.append(num)
            ratio_list.append(ratio)
        return indexs, ratio_list

best_index, best_ratio = find_best(search_string, saved_strings)
print(f'best index: {best_index}')
 
print(f'the best match is {saved_strings[best_index]}, and the ratio is {best_ratio}')
