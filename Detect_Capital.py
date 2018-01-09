def detectCapitalUse(word):
    if len(word)==1:
        return True
    else:
        if word[0]>='a' and word[0]<='z':
            return word.islower()
        else:
            if word[1]>='A' and word[1]<='Z':
                return word.isupper()
            else:
                s=""
                for i in range(1,len(word)):
                    s=s+word[i]
                return s.islower()
a="USA"
b="Uas"
c="sfg"
d="ewW"
e="D"
print detectCapitalUse(a)
print detectCapitalUse(b)
print detectCapitalUse(c)
print detectCapitalUse(d)
print detectCapitalUse(e)