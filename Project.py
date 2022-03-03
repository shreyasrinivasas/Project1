import statistics
from statistics import mean
def TakeInputforList():
    n=int(input("Enter the number of elemnets in List :"))
    L1=[]
    for i in range(1,n+1):
        x=int(input("Enter value of element i: "))
        L1.append(x)
    return L1


def Append():
    L1=TakeInputforList()
    a=int(input("Enter the number you want to append to list:"))
    L1.append(a)
    print("Updated List:",a)
def Pop():
    L1=TakeInputforList()
    print("List before pop:",L1)
    L1.pop()
    print("List after pop:",L1)
def Clear():
    L1=TakeInputforList()
    print("L1 before clearing:",L1)
    L1.clear()
    print("L1 after clear:",L1)
def Concatenate():
    L1=TakeInputforList()
    L2=TakeInputforList()
    print("List 1: ",L1)
    print("List 2: ",L2)
    L3=L1+L2
    print("Concatenated List: ",L3)
def Sums():
    L1=TakeInputforList()
    print("Elements of list:",L1)
    sums=0
    for i in range(len(L1)):
        sums+=L1[i]
    print("Sum of list:",sums)
def Min():
    L1=TakeInputforList()
    print("Elements of list:",L1)
    print("Min element of list :",min(L1))
def Max():
    L1=TakeInputforList()
    print("Elements of list:",L1)
    print("Min element of list :",max(L1))
def Len():
    L1=TakeInputforList()
    print("Length of List : ",len(L1))
def Mean():
    L1=TakeInputforList()
    print("Elements of list:",L1)
    print("Mean of list : ",mean(L1))
def Median():
    L1=TakeInputforList()
    print("Elements of list:",L1)
    print("Median of list : ",statistics.median(L1))
def Count():
    Count()
def Insert():
    L1=TakeInputforList()
    print("Elements of list:",L1)
    pos=int(input("Enter postion: "))
    value=int(input("Enter Value: "))
    L1.insert(pos,value)
    print("List after inserting :",L1)
def Remove():
    L1=TakeInputforList()
    print("Elements of list:",L1)
    rem=int(input("Enter num to remove: "))
    print("list after removing:",L1.remove(rem))
def Sort():
    L1=TakeInputforList()
    print("Elements of list:",L1)
    L1.sort()
    print("Elements of list after sort:",L1)
def ReversedSort():
    L1=TakeInputforList()
    print("Elements of list before reversed sort:",L1)
    L1.reverse()
    print("Elements of list after reversed sort:",L1)
#=========================TUPLE==========================
def TakeInputforTuple():
    n=int(input("Enter the number of elemnets in Tuple :"))
    L1=[]
    T1=()
    for i in range(1,n+1):
        x=int(input("Enter value of element i: "))
        L1.append(x)
    T1=tuple(L1)
    return T1


def CountTuple():
    T1=TakeInputforTuple()
    a=int(input("Enter the num you want to count in tuple:"))
    x=T1.count(a)
    print("Count =",x)

def IndexTuple():
    T1=TakeInputforTuple()
    print("Elements of tuple:",T1)
    a=int(input("Enter the element you want to find index for in tuple:"))
    x=T1.index(a)
    print("Index of {} = {}".format(a,x))
#===========================Tuple-end========================
#==========================SET=========================
def TakeInputforSet():
    n=int(input("Enter the number of elemnets in Set :"))
    L1=[]
    S1=set()
    for i in range(1,n+1):
        x=int(input("Enter value of element i: "))
        L1.append(x)
    S1=set(L1)
    print(S1)
    return S1


def Add():
    S1=TakeInputforSet()
    a=input("Enter the num you want to add in tuple:")
    S1.add(a)
    print("Elements of set after adding :",S1)
def Clear():
    S1=TakeInputforSet()
    print("Set before clearing:",S1)
    S1.clear()
    print("Set after clearing:",S1)
def Copy():
    x = S1.copy()
    print("Element Copied Successfully to x!!")
    print("x=",x)
def Difference():
    S1=TakeInputforSet()
    S2=TakeInputforSet()
    print("Elements of set 1:",S1)
    print("Elements of set 2:",S2)
    S1.difference(S2)
    print("Differnece = ",S1)
def DifferenceUpdate():
    S1=TakeInputforSet()
    S2=TakeInputforSet()
    print("Elements of set 1:",S1)
    print("Elements of set 2:",S2)
    S1.difference_update(S2)
    print("Differnece Update = ",S1)
def Discard():
    S1=TakeInputforSet()
    a=input("Enter the element you want to discard:")
    S1.discard(a)
    print("Set after discard: ",S1)
def Intersection():
    S1=TakeInputforSet()
    S2=TakeInputforSet()
    print("Elements of set 1:",S1)
    print("Elements of set 2:",S2)
    S1.intersection(S2)
    print("Intersection: ",S1)
def isSubset():
    S1=TakeInputforSet()
    S2=TakeInputforSet()
    print("Elements of set 1:",S1)
    print("Elements of set 2:",S2)
    x=S1.issubset(S2)
    print("isSubset:",x)
def isSuperset():
    S1=TakeInputforSet()
    S2=TakeInputforSet()
    print("Elements of set 1:",S1)
    print("Elements of set 2:",S2)
    x=S1.issuperset(S2)
    print("isSubset:",x)
def PopSet():
    S1=TakeInputforSet()
    S1.pop()
    print("set after pop:",S1)
def RemoveSet():
    S1=TakeInputforSet()
    print("Elements of set:",S1)
    a=input("Enter the element you want to discard:")
    S1.remove(a)
    print("set after removing apple:",S1)
def Union():
    S1=TakeInputforSet()
    S2=TakeInputforSet()
    print("Elements of set 1:",S1)
    print("Elements of set 2:",S2)
    z = S1.union(S2)
    print("Union: ",z)
def UpdateSet():
    S1=TakeInputforSet()
    S2=TakeInputforSet()
    print("Elements of set 1:",S1)
    print("Elements of set 2:",S2)
    S1.update(S2)
    print("Update: ",x)
def symmetricDiff():
    S1=TakeInputforSet()
    S2=TakeInputforSet()
    print("Elements of set 1:",S1)
    print("Elements of set 2:",S2)
    z = x.symmetric_difference(y)
    print("symmetric_difference: ",z)
def symmetricDiffUpdate():
    S1=TakeInputforSet()
    S2=TakeInputforSet()
    print("Elements of set 1:",S1)
    print("Elements of set 2:",S2)
    z = x.symmetric_difference(y)
    print("symmetric_difference: ",z)
#======================================================
print("Select one of the DataStucture given below:\n")
option1=int(input("1.List\n2.Tuple\n3.Set\n4.Dictionary\n"))
if(option1 == 1):
    L1=[1,2,3]
    print("You have selected LIST !!")
    print("Select any list method you want to use :")
    op=int(input("1.Append\n2.Pop\n3.Clear\n4.Concatenate\n5.Sum\n6.Min\n7.Max\n8.Length\n9.Mean\n10.Median\n11.Count\n12.Insert\n13.Remove\n14.Sort\n15.Reverse sort\n"))
    if(op == 1):
        Append()
    if(op == 2):
        Pop()
    if(op ==3):
        Clear()
    if(op == 4):
        Concatenate()
    if(op == 5):
        Sums()
    if(op == 6):
        Min()
    if(op == 7):
        Max()
    if(op == 8):
        Len()
    if(op == 9):
        Mean()
    if(op == 10):
        Median()
    if(op == 11):
        Count()
    if(op==12):
        Insert()
    if(op==13):
        Remove()
    if(op==14):
        Sort()
    if(op == 15):
        ReversedSort()
if (option1 == 2):
    print("YOu have selcted TUPLE!!")
    print("Enter a choice of tuple method you want to use from the following :")
    op=int(input("1.Count\n2.Index\n"))
    if(op == 1):
        CountTuple()
    if(op == 2):
        IndexTuple()
if (option1 == 3):
    print("YOu have selcted SET!!")
    print("Enter a choice of set method you want to use from the following :")
    op=int(input("1.Add\n2.Clear\n3.Copy\n4.Differnece\n5.Difference_update\n6.Discard\n7.Intersection\n8.isSubset\n9.isSuperset\n10.Pop\n11.Remove\n12.Union\n13.Update\n14.symmetric_diff\n15.symmetric_diff_update\n"))
    if(op == 1):
        Add()
    if(op == 2):
        Clear()
    if(op==3):
        Copy()
    if(op==4):
        Difference()
    if(op==5):
        DifferenceUpdate()
    if(op == 6):
        Discard()
    if(op == 7):
        Intersection()
    if(op == 8):
        isSubset()
    if(op == 9):
        isSuperset()
    if(op ==10):
        PopSet()
    if(op==11):
        RemoveSet()
    if(op==12):
        Union()
    if(op==13):
        UpdateSet()
    if(op == 14):
        symmetricDiff()
    if(op == 15):
       symmetricDiffUpdate()
if (option1 == 4):
    print("YOu have selcted DICTIONARY!!")
    print("Enter a choice of Dictioanry method you want to use from the following :")
    op=int(input("1.Clear\n2.Copy\n3.fromkeys\n4.get\n5.items\n6.keys\n7.pop\n8.popitem\n9.setdefault()\n10.update\n11.values\n"))
    D1 = {"brand": "Ford","model": "Mustang","year": 1964}
    if(op == 1):
        D1.clear()
        print(D1)
    if(op == 2):
        x = D1.copy()
        print(x)
    if(op == 3):
        x = ('key1', 'key2', 'key3')
        y = 0
        thisdict = dict.fromkeys(x, y)
        print(thisdict)
    if(op == 4):
        x = D1.get("model")
        print(x)
    if(op == 5):
        print(D1)
        x = D1.items()
        print(x)
    if(op == 6):
        print(D1)
        x = D1.keys()
        print(x)
    if(op == 7):
        print(D1)
        x = D1.pop("model")
        print(x)
    if(op == 8):
        print(D1)
        x = D1.popitem()
        print(x)
    if(op == 9):
        print(D1)
        x = D1.setdefault("model", "Bronco")
        print(x)
    if(op == 10):
        print(D1)
        D1.update({"color": "White"})
        print(D1)
    if(op == 11):
        print(D1)
        x = D1.values()
        print(x)
