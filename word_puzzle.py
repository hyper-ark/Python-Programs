# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section: 514
# Assignment: word puzzle – team
# Date: 20/10/2023

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")


def get_valid_letters(puzzle):
    lis_string=''
    lis=[]
    for i in puzzle:
        if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            if i not in lis:
                lis.append(i)
    for i in range(len(lis)):
        lis_string+=lis[i]
    return lis_string

def is_valid_guess(lis_string,guess):
    letters=[]
    for i in range(len(lis_string)):
        if lis_string[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            letters.append(lis_string[i])
    for i in letters:
        if i in guess and len(guess)==10:
            continue
        else:
            return False
    return True

def check_user_guess(dividend,quotient,divisor,remainder):
    if dividend == quotient * divisor + remainder:
        return True
    else:
        return False

def make_number(word,guess):
    num=''
    for i in word:
        if i in guess:
            num+=str(guess.index(i))
    return int(num)

def make_numbers(puzzle,guess):
    quotient = puzzle[:puzzle.index(",")]
    
    divisor = puzzle[puzzle.index(",")+1:puzzle.index(' ')+1]
    
    nstring=puzzle[puzzle.index('|'):]
    dividend = nstring[nstring.index('|')+2:nstring.index(',')]
    
    puzzle=puzzle[::-1]
    remainder=puzzle[:puzzle.index(',')]
    remainder=remainder[::-1]
    
    f=(make_number(dividend,guess),make_number(quotient,guess),make_number(divisor,guess),make_number(remainder,guess))
    
    return f

def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    puzzle = input("Enter a word arithmetic puzzle: \n")
    #puzzle = "RUE,EAR | RUMORS,UEII ,UKTR ,EAR ,KEOS,KAIK,USA"
    print_puzzle(puzzle)
    a = get_valid_letters(puzzle)
    guess = input("\nEnter your guess, for example ABCDEFGHIJ: ")
    if is_valid_guess(a, guess)==False:
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    else:
        dividend, quotient, divisor, remainder=make_numbers(puzzle,guess)
        if check_user_guess(dividend, quotient, divisor, remainder)==False:
            print('Try again!')
        else:
            print('Good job!')
            
    

if __name__ == '__main__':
    main()