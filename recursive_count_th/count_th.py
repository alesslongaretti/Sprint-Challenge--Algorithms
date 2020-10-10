'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if there is no word return 0
    if word == "":
        return 0
    # else if the first letters are th return 1 +
    elif word[0:2] == 'th':
    # recurse and keep checking for more "th"
        return 1 + count_th(word[2:])
    else:
    # else recurse and keep checking for more "th"
        return count_th(word[1:])
    
    

