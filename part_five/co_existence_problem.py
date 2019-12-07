# Author: Mamadou Bah

import string
import os


def open_file():
    '''None->file object
    Prompt the user for a file-name, and try to open that file. If the 
    file exists, it will return the file object; otherwise it will re-prompt 
    until it can successfully open the file'''

    print('>>>>>>>>>>Opening file.<<<<<<<<<<')
    print('loading, please wait.....')
    success = False
    while (success == False):
        try:
            input_file = input('Enter the name of the file: ')
            if os.path.isfile(input_file):
                fileObject = open(input_file)
                success = True
                print('>>>>>>>>>>File successfully opened!<<<<<<<<<<')
            else:
                print("File not found or problem opening the files. Try again!!!")
        except:
            print("An exception occurred")

    return fileObject


def read_file(fp):
    '''(file object)->dict
    This function will read the contents of that file line by 
    line, process them and store them in a dictionary.'''

    print('>>>>>>>>>>Reading and processing file.<<<<<<<<<<')
    print('Please wait.....')
    # Read the contents of that file line by line
    lines = [line.rstrip('\n') for line in fp]
    print("--> file reading complete!(1/3)")

    # ========================================= Contents pre-processing =============================================
    # 1. Removes all punctuation, such as “,”, “.”, “!”, apostrophes and
    # hyphens, Make everything lowercase and Split the line into words
    words = process_lines(lines)
    print("--> file processing complete!(2/3)")

    # 2. Removes the words that are not all alphabetic characters and less
    # than 2 characters and stores contents in a dictionary
    data_dict = make_dict(words)
    print("--> storing contents into dictionary complete!(3/3)")
    print(">>>>>>>>>>File successfully read and processed. Let's start!<<<<<<<<<<\n")

    return data_dict


def find_coexistance(D, query):
    '''(dict,str)->list
    Given a list of query words, this function finds the line number of all the query words'''

    result = set()
    if query in D:
        result = D[query]
    return result

##############################
# helper function
##############################


def process_lines(lines):
    '''(list)->list
    This function removes all punctuation, makes all words lower case 
    and splits the line into words'''
    processed_content = [s.translate(str.maketrans(
        '', '', string.punctuation)).lower().split() for s in lines]
    return processed_content


def is_word(word):
    '''(str)->boo
    Returns True if the given words is an alphabetic character and 
    is less than 2 characters. False otherwise'''
    return word.isalpha() == True and len(word) >= 2


def make_dict(lsw):
    '''(list)->dict
    This function add the words into a dictionary with the key being the word and 
    the value is a set of line numbers where this word has appeared.'''
    D = {}
    for line in lsw:
        for word in line:
            if is_word(word):
                try:
                    D[word].add(lsw.index(line)+1)
                except KeyError:
                    D[word] = {lsw.index(line)+1}
    return D


##############################
# main
##############################

file = open_file()
d = read_file(file)

stop_prompting_for_input = False

while(stop_prompting_for_input == False):
    query = input(
        "Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

    if(query == 'q' or query == 'Q'):
        print("Stoping program...")
        print("\n>>>>>>>>>>Program stopped!<<<<<<<<<<")
        # Stop prompting for input if user enter q or Q
        stop_prompting_for_input = True
        break

    # Split a sentence (query) and store each word in a list
    list_of_words = query.split()

    # Loop through input, find the co-occurrence
    all_sets = set()
    for query_word in list_of_words:
        all_sets = all_sets | find_coexistance(d, query_word)

    # Then convert the resulting set to a sorted list
    results = list(all_sets)
    results.sort()

    if(len(results) == 0):
        print("Word '", query, "' not in the file")

    else:
        # and print the results.
        print("The one or more words you entered coexisted in the following lines of the file:")
        [print(val, end=" ") for val in results]
    print("\n<-----------------------------------end of results!-------------------------------------------->")
