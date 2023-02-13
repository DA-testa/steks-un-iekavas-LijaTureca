# python3
from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text2):
    opening_brackets_stack = []
    ending_brackets_stack = []
   
    for i, next in enumerate(text2): 
        if next in "([{":
            # Process opening bracket, write your code here
            if next == "{" or next == "[" or next =="(":
                a=Bracket(next,i)
                opening_brackets_stack.append(a)
            pass
       
        if next in ")]}":
            # Process closing bracket, write your code here
            if next == "}" or next == "]" or next == ")":
                b=Bracket(next,i)
                ending_brackets_stack.append(b)
            if len(opening_brackets_stack) == 0 or not are_matching(str(opening_brackets_stack[-1].char),next):
                return(i+1)
            pass
            opening_brackets_stack.pop()
    
    if len(opening_brackets_stack)==0:
        return("Success")
    else:
        return(a.position)
     
def main():
    text = input()
    text2=input()
    mismatch = find_mismatch(text2)
    print(mismatch)
    
    # Printing answer, write your code here

if __name__ == "__main__":
    main()
