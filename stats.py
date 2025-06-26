def count_words(book_text):
    number_of_words = 0
    words = book_text.split()
    for word in words:
        number_of_words+=1
    return number_of_words 

def count_characters(book_text):
    dict = {}
    #filling dictionary
    for character in book_text:
        if character.lower() not in dict:
            dict[character.lower()] = 1
        else:
            dict[character.lower()] += 1                 
    return dict

#returns number in list section for each char
def sort_criteria(dict_elements):   
    return dict_elements["num"]
   
def sort_dict(book_text):
    unsorted_dict = count_characters(book_text)
    list_of_dictionaries = []
    #print(f"=========\nUnsorted:\n{unsorted_dict}\n==========")
    #load list
    for key in unsorted_dict:
        dict_element = {
                    "char": None,
                    "num" : None
                    }
        dict_element["char"] = key
        dict_element["num"] = unsorted_dict[key]
        list_of_dictionaries.append(dict_element)
        
    #sort list high to low, sort criteria ["num"]
    list_of_dictionaries.sort(reverse = True, key = sort_criteria)   
    return list_of_dictionaries
 
def print_book_stats(list_of_dictionaries):
    for element in list_of_dictionaries:
        if element["char"].isalpha():
            print(f"{element['char']}: {element['num']}")
        
            
    
    
    
    
    
    
    