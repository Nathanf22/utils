import Levenshtein as levenshtein

saved_strings = [
    'Hello here!',
    'this is amazing',
    'how are you',
    'I take this',
    'keep working',
    'try this also',
]


search_string = 'how you are'

# def find_best(search_string, saved_string, nb = 1):
#     my_dict = {}
#     if nb == 1:
#         greater = -1
#         index = -1
#         for el in saved_string:
#             print(f'el: {el}')
#             ratio =  levenshtein.ratio(search_string, el)
#             print(f'dist: {ratio} \n')
#             if greater < ratio:
#                 greater = ratio
#                 index = saved_string.index(el)
#         return index, greater
#     else:
#         ratio_list = []
#         indexs = []
#         for num, el in enumerate(saved_string):
#             ratio = levenshtein.ratio(search_string, el)
#             index.append(num)
#             ratio_list.append(ratio)
#         return indexs, ratio_list


class SearchUtil:
    """
    A class used to manipulate strings, and make quick search


    Attributes:
    ------------
    iterator: iterator
        an iterator that contains the list of the string elements to manipulate


    Methods:
    ---------
    get_size()
        return the number of elements present in the iterator

    find_best(search_string)
        return the best corresponding string by calculating Levenshtein ratio.  

    """
    def __init__(self, iterator):
        self.iterator = iterator
        if(type(self.iterator) == list):
            print("this is a list")
        else:
            print("this is not a list")
            print("converting to list...")
            self.iterator = list(self.iterator)
        print(type(self.iterator))
    
    def get_size(self):
        return len(self.iterator)

    def find_best(self, search_string):
        greater = -1
        index = -1
        for el in self.iterator:
           #print(f'el: {el}')
            ratio =  levenshtein.ratio(search_string, el)
           # print(f'dist: {ratio} \n')
            if greater < ratio:
                greater = ratio
                index = self.iterator.index(el)
        return index, greater
        
searcher = SearchUtil(saved_strings)

print(searcher.get_size())

best_index, best_ratio = searcher.find_best(search_string)
print(f'best index: {best_index}')
 
print(f'the best match is \'{saved_strings[best_index]}\', and the ratio is {best_ratio}')

