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
    #print(dict) 
    
    return dict
   
