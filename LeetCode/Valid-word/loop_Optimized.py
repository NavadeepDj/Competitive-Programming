def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel = ['a', 'e', 'i', 'o', 'u']
        if word.isalnum() == False:
            return False
        v = 0
        c = 0
        result1 = False
        result2 = False

        for i in word:
            if v == 1:
                result1 = True
            if i.lower() in vowel:
                v = v + 1
        for i in word:
            if c == 1:
                result2 = True
            if i.lower() not in vowel:
                c = c + 1
        if result1 and result2 == True:
            return True
        else:
            return False
