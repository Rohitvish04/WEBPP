#1.find the Reverse a string: split, index 
#input = hello there
# o/p = there Hello

def reverseStr(word):
    split = word.split()
    reversedStr = split[::-1]
    rev = ' '.join(reversedStr)
    print(rev)

reverseStr('Hello there')

# 2. code and decode words fro secuirty:
# i/p = Shivam123
# o/p = qwerrhivam123Soopu

def codeAndDecode(word):
    code = word[1:] + word[0]
    encode = 'arfer' +code + 'erhdfgdfre'
    print(encode)
    
codeAndDecode('Shivam123')
#3. Count of vowels in a string 
def countOfVowels(word):
    counter =0
    vowel = 'aeiouAEIOU'
    for char in word:
        if char in vowel:
            counter += 1

    return counter

countOfVowels('Treefhfhfhvgewwer')