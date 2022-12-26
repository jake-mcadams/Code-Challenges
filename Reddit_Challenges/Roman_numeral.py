#Numerals
from typing import List


numeral= {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def get_numerals() ->List[str]:
    print("Please provide two roman numeral to compare: ")
    num_one:str = str(input("Numeral One: ")).upper()
    num_two:str = str(input("Numeral Two: ")).upper()
    # print(f"{num_one},{num_two}")
    res_one = check_numerals(num_one)
    res_two = check_numerals(num_two)
    if res_one > res_two:
        print(f"{num_one}: {res_one} is larger than {num_two}: {res_two}")
    else:
        print(f"{num_one}: {res_one} is not larger than {num_two}: {res_two}")

#Check input provided
def check_numerals(num:str) ->int:
    if len(num)>1:
        total = 0
        for x in num:
            if x in numeral:
                total+=numeral.get(x)
        return total
    else:
        if num in numeral:
            return numeral.get(num)
        else:
            raise ValueError(f"{num} is not in the list of numerals!")


def main() ->None:
    if __name__ == "__main__":
        get_numerals()

main()