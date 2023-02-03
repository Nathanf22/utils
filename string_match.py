import Levenshtein as levenshtein
import itertools

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
        return the best corresponding index string by calculating Levenshtein ratio.  

    find_best_string(self, search_string)
        return the best corresponding index string by calculating Levenshtein ratio.

    """
    def __init__(self, iterator):
        """
        when initializing, convert iterator to list if not.

        Args:
            iterator (list | tuple | set): an iterator containing the data
        
        Raises:
            TypeError: iterator must be list, tuple or set
        """
        if type(iterator) != list and type(iterator) != tuple and type(iterator) != set :
            raise TypeError("Iterator must be list, tuple or set")
        self.iterator = iterator
        if(type(self.iterator) == list):
            print("this is a list")
        else:
            print("this is not a list")
            print("converting to list...")
            self.iterator = list(self.iterator)
        print(type(self.iterator))
    
    def get_size(self):
        """
        get the size of the iterator.

        Returns:
            int: the number of element in the iterator
        """
        return len(self.iterator)

    def find_best(self, search_string):
        """
        find the ratio and index of the best matching

        Args:
            search_string (string): the string to search in the data

        Returns:
            tuple: (index, greater) index is the index of the best matching in the iterator, and greater is the ratio coresponding
        """
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

    def find_best_string(self, search_string):
        """
        find the best string in iterator

        Args:
            search_string (string): the string to search in the data

        Returns:
            string: the best matching string in the data
        """
        index, greater = self.find_best(search_string)
        return self.iterator[index]
    
    def replace_iterator(self, new_iterator):
        """

        Args:
            new_iterator (list | tuple | set): iterator to replace the current iterator
        """
        self.__init__(new_iterator)
    
    def add_to_iterator(self, iterator):
        """_summary_

        Args:
            iterator (list | tuple | set): iterator to add to the current iterator

        Raises:
            TypeError: iterator must be list, tuple or set
        """
        if type(iterator) != list and type(iterator) != tuple and type(iterator) != set :
            raise TypeError("Iterator must be list, tuple or set")
        else:
            if type(iterator) != list:
                iterator = list(iterator)
            self.iterator = list(itertools.chain(self.iterator, iterator))
        
searcher = SearchUtil(saved_strings)

print(searcher.get_size())

best_index, best_ratio = searcher.find_best(search_string)
print(f'best index: {best_index}')
 
print(f'the best match is \'{saved_strings[best_index]}\', and the ratio is {best_ratio}')

print(f'adding new values to iterator..')
searcher.add_to_iterator(['first added', 'how you are', 'something else'])
print('values added')
print(f'the new best matching string is : \'{searcher.find_best_string(search_string)}\' ')
