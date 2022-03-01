import statistics
from statistics import mean
print("Select one of the DataStucture given below:\n")
option1=int(input("1.List\n2.Tuple\n3.Set\n4.Dictionary\n"))
if(option1 == 1):
    L1=[1,2,3]
    print("You have selected LIST !!")
    print("Select any list method you want to use :")
    op=int(input("1.Append\n2.Pop\n3.Clear\n4.Concatenate\n5.Sum\n6.Min\n7.Max\n8.Length\n9.Mean\n10.Median\n11.Count\n12.Insert\n13.Remove\n14.Sort\n15.Reverse sort\n"))
    if(op == 1):
        print("L1:",L1)
        a=int(input("Enter the number you want to append to list:"))
        L1.append(a)
        print("Updated List:",a)
    if(op == 2):
        print("L1 before pop:",L1)
        print("Removed value: ",L1.pop())
        print("L1 after pop:",L1)
    if(op ==3):
        print("L1 before clearing:",L1)
        L1.clear()
        print("L1 after clear:",L1)
    if(op == 4):
        L2=[3,4,5]
        print("List 1 before concatenation:",L1)
        print("List 2:",L2)
        add=L1+L2
        print("List 1 after concatenation:",add)
    if(op == 5):
        print("Elements of list:",L1)
        sums=0
        for i in range(len(L1)):
            sums+=L1[i]
        print("SUm of list: ",sums)
    if(op == 6):
        print("Elements of list:",L1)
        print("Min element of list :",min(L1))
    if(op == 7):
        print("Elements of list:",L1)
        print("Max element of list :",max(L1)) 
    if(op == 8):
        print("Elements of list:",L1)
        print("Length of List : ",len(L1))
    if(op == 9):
        print("Elements of list:",L1)
        print("Mean of list : ",mean(L1))
    if(op == 10):
        print("Elements of list:",L1)
        print("Median of list : ",statistics.median(L1))
    if(op == 11):
        L3=[2,3,4,67,2,55,55,4]
        print("Elements of list:",L3)
        n=int(input("Enter the number you want to count in List: "))
        print("The number '{}' has occured '{}' times in the list".format(n,L3.count(n)))
    if(op==12):
        #L1=[1,2,3]
        print("Elements of list:",L1)
        pos=int(input("Enter postion: "))
        value=int(input("Enter Value "))
        L1.insert(pos,value)
        print("List after inserting :",L1)
    if(op==13):
        print("Elements of list:",L1)
        rem=int(input("Enter num to remove: "))
        print("list after removing:",L1.remove(rem))
    if(op==14):
        L3=[24,3,46,67,2,55,58,4]
        print("Elements of list before sort:",L3)
        L3.sort()
        print("Elements of list after sort:",L3)
    if(op == 15):
        L3=[24,3,46,67,2,55,58,4]
        print("Elements of list before reversed sort:",L3)
        L3.reverse()
        print("Elements of list after reversed sort:",L3)
if (option1 == 2):
    print("YOu have selcted TUPLE!!")
    print("Enter a choice of tuple method you want to use from the following :")
    op=int(input("1.Count\n2.Index\n"))
    T1 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    if(op == 1):
        print("Elements of tuple:",T1)
        a=int(input("Enter the num you want to count in tuple:"))
        x=T1.count(a)
        print("Count =",x)
    if(op == 2):
        print("Elements of tuple:",T1)
        a=int(input("Enter the element you want to find index for in tuple:"))
        x=T1.index(a)
        print("Index of {} = {}".format(a,x))
if (option1 == 3):
    print("YOu have selcted SET!!")
    print("Enter a choice of set method you want to use from the following :")
    op=int(input("1.Add\n2.Clear\n3.Copy\n4.Differnece\n5.Difference_update\n6.Discard\n7.Intersection\n8.isSubset\n9.isSuperset\n10.Pop\n11.Remove\n12.Union\n13.Update\n14.symmetric_diff\n15.symmetric_diff_update\n"))
    fruits = {"apple", "banana", "cherry"}
    if(op == 1):
        print("Elements of set:",fruits)
        a=input("Enter the num you want to count in tuple:")
        fruits.add(a)
        print("Elements of set after adding :",fruits)
    if(op == 2):
        print("Elements of set:",fruits)
        fruits.clear()
        print(fruits)
    if(op==3):
        print("Elements of set:",fruits)
        x = fruits.copy()
        print("Fruits Copied Successfully to x!!")
        print("x=",x)
    if(op==4):
        print("Elements of set 1:",fruits)
        y = {"google", "microsoft", "apple"}
        print("Elements of set 2:",y)
        z = fruits.difference(y)
        print("Differnece = ",z)
    if(op==5):
        print("Elements of set 1:",fruits)
        y = {"google", "microsoft", "apple"}
        print("Elements of set 2:",y)
        fruits.difference_update(y)
        print("Differnece update = ",fruits)
    if(op == 6):
        print("Elements of set 1:",fruits)
        a=input("Enter the element you want to discard:")
        fruits.discard(a)
        print("Set after discard: ",fruits)
    if(op == 7):
        print("Elements of set 1:",fruits)
        y = {"google", "microsoft", "apple"}
        print("Elements of set 2:",y)
        z = fruits.intersection(y)
        print("Intersection: ",z)
    if(op == 8):
        x = {"a", "b", "c"}
        y = {"f", "e", "d", "c", "b", "a"}
        print("Elements of set 1:",x)
        print("Elements of set 1:",y)
        z = x.issubset(y)
        print("isSubset:",z)
    if(op == 9):
        x = {"f", "e", "d", "c", "b", "a"}
        y = {"a", "b", "c"}
        print("Elements of set 1:",x)
        print("Elements of set 1:",y)
        z = x.issuperset(y)
        print("issuperset:",z)
    if(op ==10):
        print("Elements of set:",fruits)
        fruits.pop()
        print("set after pop:",fruits)
    if(op==11):
        print("Elements of set:",fruits)
        fruits.remove("apple")
        print("set after removing apple:",fruits)
    if(op==12):
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        print("Elements of set 1:",x)
        print("Elements of set 2:",y)
        z = x.union(y)
        print("Union: ",z)
    if(op==13):
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        print("Elements of set 1:",x)
        print("Elements of set 2:",y)
        x.update(y)
        print("Update: ",x)
    if(op == 14):
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        print("Elements of set 1:",x)
        print("Elements of set 2:",y)
        z = x.symmetric_difference(y)
        print("symmetric_difference: ",z)
    if(op == 15):
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        print("Elements of set 1:",x)
        print("Elements of set 2:",y)
        z = x.symmetric_difference_update(y)
        print("symmetric_difference_update: ",z)
if (option1 == 4):
    print("YOu have selcted SET!!")
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