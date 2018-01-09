import collections
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        item=2002
        a=[]
        list3=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    a.append(i)
                    a.append(j)
                    if (i+j)<item:
                        item=i+j
                    break
        k=0
        while(k<len(list1)-1):
            if a[k]+a[k+1]==item:
                list3.append(list1[a[k]])
            k=k+2
        return list3    

class Solution1(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index1={value:key for key,value in enumerate(list1)}
        best=2002
        answer=[]
        for k,v in enumerate(list2):
            item=index1.get(v,2002)
            if k+item < best:
                best=k+item
                answer=[v]
            elif k+item==best:
                answer.append(v)
        return answer
    
s=Solution()
print s.findRestaurant(["123","Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Burger King", "Tapioca Express", "Shogun"])
s2=Solution1()
print s.findRestaurant(["123","Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Burger King", "Tapioca Express", "Shogun"])

c = collections.Counter()  # 创建一个空的Counter类
c = collections.Counter('gallahad')  # 从一个可iterable对象（list、tuple、dict、字符串等）创建
print c
c = collections.Counter({'a': 4, 'b': 2})  # 从一个字典对象创建
print c
c = collections.Counter(a=4, b=2)  # 从一组键值对创建
print c