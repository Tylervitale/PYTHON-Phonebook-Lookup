import csv


class phonebook:
    l = []

    def __init__(self, phone_book):  # constructor of class
        with open(phone_book) as s:
            reader = csv.reader(s)  # read csv file to list
            data = list(reader)
        data = data[1:]
        for i in data:  # for each item in list
            d = {"first": i[0], "last": i[1], "phone": i[2]}  # store in dictionary
            self.l.append(d)
            d = {}

    def binarysearch(self, arr, le, r, x):  # binary search
        if r >= le:
            mid = le + (r - le) // 2
            if arr[mid] == x:  # if element is at mid
                return mid
            elif arr[mid] > x:  # Use recursion for left part of list
                return self.binarysearch(arr, le, mid - 1, x)
            else:  # right part of list
                return self.binarysearch(arr, mid + 1, r, x)
        else:
            return -1

    def lookup(self, lastname):
        ll = []
        for i in self.l:
            ll.append(i["last"])  # store last names in list
        ind = self.binarysearch(ll, 0, len(ll), lastname)  # call binarysearch
        if ind == -1:
            return False
        else:
            return self.l[ind]["first"], self.l[ind]["last"], self.l[ind]["phone"]  # return first,last and phone number

    def reverse_lookup(self, p):
        ll = []
        for i in self.l:
            ll.append(i["phone"])  # store phone numbers in list
        newll = []
        for i in ll:
            newll.append(i)  # store in another list
        ll.sort()  # sort the list of phone numbers
        ind = self.binarysearch(ll, 0, len(ll), p)  # call binarysearch
        if ind == -1:
            return False
        else:
            i = newll.index(ll[ind])
            return self.l[i]["first"], self.l[i]["last"], self.l[i]["phone"]  # return first,last and phone number


print("Please enter the path to the phone book: ", end="")
path = input()
p = phonebook(path)
while 1:
    print("1.Search by name")  # print menu
    print("2.search by number")
    print("3.Quit")
    ch = input("Choice:")  # read choice
    if ch == "1":
        n = input("Name: ")  # if ch is 1
        n = n[1:-1]  # remove * at begin and end of input
        if not p.lookup(n):
            print(n, end="")
            print(" was not found!")
        else:
            f, l, p = p.lookup(n)
            print(f, l, end=":")
            print(p)
    elif ch == "2":
        n = input("Number: ")  # if ch is 2
        n = n[1:-1]  # remove * at begin and end of input
        if not p.reverse_lookup(n):
            print(n, end="")
            print(" was not found!")
        else:
            f, l, p = p.reverse_lookup(n)
            print(f, l, end=":")
            print(p)
    elif ch == "3":
        break
