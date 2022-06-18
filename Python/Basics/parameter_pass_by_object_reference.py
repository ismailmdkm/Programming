def fun1(string):
    '''Immutable variable'''
    print(id(string))
    string = "GeeksforGeeks"
    print(id(string))
    print("Inside Function:", string)


def fun2(list):
    '''Mutable variable'''
    print(id(list))
    list.append(50)
    print(id(list))
    print("Inside Function", list)


string = "Geeks"
print(id(string))
fun1(string)
print("Outside Function:", string)
mylist = [10, 20]
print(id(mylist))
fun2(mylist)
print("Outside Function:", mylist)
