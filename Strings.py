# Reversing a String
""" 
def reverseString(str):
    n = len(str)
    ans = ""
    i = 0

    while i < n:
        j = i
        s = 0
        # Skip multiple spaces.
        while j < n and str[j] == ' ':
            j += 1
            s += 1
        currentWord = ""

        # Get the current word.
        while j < n and str[j] != ' ':
            currentWord += str[j]
            j += 1

        # Add current word in the ans with a space.
        if len(currentWord) != 0:
            ans = currentWord + " " + s * " " + ans

        i = j + 1

    if len(ans) == 0:
        return ans
    
    # Remove the last space.
    return ans[:-1]
    
str = input("Enter the sentence: ")
print(reverseString(str)) 
"""

""" 
def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string(input_string):
    return input_string[::-1]


original_str = "Hello, World!"
reversed_str = reverse_string(original_str)
reversed_stri = reverse_string(original_str)
print("Original string:", original_str)
print("Reversed string:", reversed_str)
print("Reversed string:", reversed_stri)
"""


# Isomorphic Strings =  if one-to-one mapping is possible for every character of the first string to every character of the second string

""" 
def areIsomorphic(str1, str2):
    n = len(str1)
    m = len(str2)

    if (m != n):
      return False

    for i in range(n):
        first = str1[i]
        second = str2[i]

        for j in range(m):
            if(str1[j] == first and str2[j] != second):
                return False

            if(str2[j] == second and str1[j] != first):
                return False
                
    return True

str1,str2 = input(), input()
print(areIsomorphic(str1,str2))
"""

# Check If One String Is A Rotation Of Another String

""" def isCyclicRotation(p , q):
    n = len(p)
    for j in range(n):
        isRotationPossible = 1

        for i in range(n):
            if p[(i+j) % n] != q[i]:
                isRotationPossible = 0
                break

        if isRotationPossible:
            return True
    return False

p, q = input(), input()
print(isCyclicRotation(p,q))  """


# Anagram Pairs = The strings form an anagram pair if the letters of one string can be rearranged to form another string
""" 
def Anagram(str1, str2) :
	str1 = sorted(str1)
	str2 = sorted(str2)
	print(str1),print(str2)

	if(str1 == str2):
		return True
	else:
		return False

str1, str2 = input(), input()
print(Anagram(str1,str2))


def isAnagram(self, s, t):
    if len(s) != len(t):
        return False

    freq = [0] * 26
    for i in range(len(s)):
        freq[ord(s[i])-ord('a')] += 1
        freq[ord(t[i])-ord('a')] -= 1
        
    for i in range(len(freq)):
        if freq[i] != 0:
            return False

str1, str2 = input(), input()
print(isAnagram(str1,str2))

"""
""" 
def find_anagram_pairs(words):
    # Dictionary to store sorted word as key and original words as values
    anagrams = {}
    
    # Iterate through each word in the list
    for word in words:
        # Sort the word
        sorted_word = ''.join(sorted(word))
        # Add the original word to the dictionary under the sorted word key
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    print(anagrams)
    
    # Collect all anagram pairs
    anagram_pairs = []
    for key, value in anagrams.items():
        if len(value) > 1:
            for i in range(len(value)):
                for j in range(i + 1, len(value)):
                    anagram_pairs.append((value[i], value[j]))
    
    return anagram_pairs

# Example usage
words = ["listen", "silent", "enlist", "google", "gogole", "cat", "act", "tac"]
print("Anagram pairs:", find_anagram_pairs(words))
"""
