import sys

def treatstr(argument: any) -> int:
    lowerchars = 'abcdefghijklmnopqrstuvwxyz'
    upperchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punc = '.?!,:;-[]{}()`"\''
    space = ' '
    charcount = 0
    lowcount = 0
    uppcount = 0
    spcount = 0
    digcount = 0
    puncount = 0
    for s in argument:
        if s in lowerchars or s in upperchars or s in digits or s in space or s in punc:
            charcount += 1
        if s in lowerchars:
            lowcount += 1
        if s in upperchars:
            uppcount += 1
        if s in digits:
            digcount += 1
        if s in space:
            spcount += 1
        if s in punc:
            puncount += 1
    print(f"The text contains {charcount} characters:")
    print(f"{uppcount} upper letters")
    print(f"{lowcount} lower letters")
    print(f"{puncount}  punctuation marks")
    print(f"{spcount} spaces")
    print(f"{digcount} digits")
    

def main():
    args = sys.argv
    i = 0
    x = 0
    lowerchars = 'abcdefghijklmnopqrstuvwxyz'
    upperchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punc = '.?!,:;-[]{}()`"\''
    space = ' '
    charcount = 0
    lowcount = 0
    uppcount = 0
    spcount = 0
    digcount = 0
    puncount = 0
    for f in args:
        x += 1
    if x > 2:
        print("AssertionError: more than one arg provided")
        exit()
    if x == 2:
        treatstr(args)
    else:
        treatstr(input("What is the text to count?\n"))
	
        

if __name__ == "__main__":
    main()