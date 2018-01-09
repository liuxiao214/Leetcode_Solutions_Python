class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def getnumber(s):
            sreal="0"
            svirtual="0"
            for i in range(len(s)):
                if s[i]=='+':
                    sreal=s[0:i]
                    svirtual=s[i+1:len(s)-1]
            return int(sreal),int(svirtual)
        a_real,a_virtual=getnumber(a)
        b_real,b_virtual=getnumber(b)
        real=a_real*b_real-a_virtual*b_virtual
        virtual=a_virtual*b_real+b_virtual*a_real
        result=str(real)+"+"+str(virtual)+"i"
        return result

class Solution1(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ra,ia=map(int,a[0:-1].split('+'))
        rb,ib=map(int,b[0:-1].split('+'))
        return str(ra*rb-ia*ib)+"+"+str(ia*rb+ib*ra)+"i"

s=Solution1()
a="1+-1i"
b="0+0i"
print s.complexNumberMultiply(a, b)