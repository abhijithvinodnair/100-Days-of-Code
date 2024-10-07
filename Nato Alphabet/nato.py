# #TODO 1. Create a dictionary in this format:
import pandas
logo = '''   _        
            | |       
 _ __   __ _| |_ ___  
| '_ \ / _` | __/ _ \ 
| | | | (_| | || (_) |
|_| |_|\__,_|\__\___/ 
                      '''
print(logo)
nato_list = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter :row.code for (index, row) in nato_list.iterrows()}
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input  = input("Please enter a word: ").upper()
nato_list = [phonetic_dict[letter] for letter in user_input]
# Or if we break it down the code looks like ->
# for letter in user_input:
#     phonetic_list = [key for (index,key) in phonetic_dict.items() if index == letter]
#     nato_list.append(phonetic_list)

print(nato_list)
