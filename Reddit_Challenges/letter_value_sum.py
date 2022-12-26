
letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
           'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
def get_input() ->str:
    word = str(input("Please enter a word to find the sum for: ")).lower().strip()
    return word
    
    
def check_input(word:str) ->str:
    if word.isalpha():
        # print(f"Word is all letters.")
        return word
    else:
        print("The entered word appears to have characters that are not letters. Please check input")
        raise ValueError(f"{word} is not the right value!")
        

def get_sum(word:str) ->int:
    counter=0
    for letter in word:
        # print("Letter: %s\nNumber: %d" % (letter, letters[letter]))
        counter+=letters[letter]
    return counter
    

def main()-> None:
    if __name__ == "__main__":
        #get input and check it
        res =get_input()
        print(f"The total sum for the word, {res} is: {get_sum(check_input(res))}")
        
main()