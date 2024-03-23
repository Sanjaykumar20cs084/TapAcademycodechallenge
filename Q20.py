string=input()
def palindrome(string):
    #reverse=''.join(reversed(string))
    reverse=reversed(string)
    if reverse==string:
            #print(f'given string {string} is palindrome')
            print('Palindrome')
    else:
        #print(f'given string {string} is not a palindrome')
        print('Palindrome')
palindrome(string)
