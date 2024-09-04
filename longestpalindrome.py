input_string=input()
def longestPalindrome(s):
    if s==s[::-1]:
        return s
    l=longestPalindrome(s[1:])
    r=longestPalindrome(s[:-1])
    if len(l)>len(r):
        return l
    else:
        return r
print(longestPalindrome(input_string))