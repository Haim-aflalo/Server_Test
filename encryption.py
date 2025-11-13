import string
from typing import final


class Encryption:

    @staticmethod
    def cesar_crypt(word,offset):
        crypted_word = []
        alphabet = list(string.ascii_lowercase)
        letters_word = list(word)
        for i in range(len(alphabet)):
            alphabet.append(alphabet[i])
            for j in letters_word:
                if alphabet[i] == j.lower():
                    crypted_word.append(alphabet[i+offset])
        final_word = ""
        for i in crypted_word[::-1]:
            final_word += str(i)
        return final_word

    @staticmethod
    def fence_crypt(word):
        letters = list(word)
        for i in letters:
            if i == " ":
                letters.remove(i)
        crypt_word = ""
        for i in range(0,len(letters),2):
            crypt_word += letters[i]
        for j in range(1,len(letters),2):
            crypt_word += letters[j]
        return crypt_word


    @staticmethod
    def fence_decrypt(word):
        decrypt_word = ""
        letters = list(word)
        flag = len(letters)
        while flag:
            for i in letters[len(letters)//2:]:
                decrypt_word += i
                flag -= 1
            for j in letters[:len(letters)//2]:
                decrypt_word += j
                flag -= 1
        return decrypt_word




