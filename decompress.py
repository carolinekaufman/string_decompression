# Problem: https://techdevguide.withgoogle.com/paths/advanced/compress-decompression#code-challenge
"""
From Google's Technical Development Guide: Advanced Path
String Decompression

Goal: Decompress compressed strings written in the form
    num_repeats[string_to_repeat]
"""

def decompress(s):
    """
    Given a string of the form num_repeats[string_to_repeat], 
    return the decompressed string
    """
    decompressed = ""
    i = 0
    while i < len(s):
        n = 1
        num = ""
        to_repeat = ""
        if s[i].isdigit():
            while s[i].isdigit() and i < len(s):
                num += s[i]
                i += 1
            n = int(num) # get number of times to repeat
        if i < len(s) and s[i] == "[": # do not include [ in repeated string
            i += 1
        if i < len(s) and s[i].isdigit():
            to_repeat += decompress() #substring of s from [ to ]
        else:   # next char is letter
            while i < len(s) and s[i].isalpha():
                to_repeat += s[i]
                i += 1
        decompressed += to_repeat * n
        i += 1
    return decompressed

def main():
    print decompress("2[3[a]b]")

if __name__ == '__main__':
    main()