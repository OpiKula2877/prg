def sumOfNums(x, y):
    return x+y
s=sumOfNums
p=print
p(s(s(5, -14), s(9, -6)))

def sumOfNums2(*nums):
    return sum(nums)
p(sumOfNums2(5, -14, 9, -6))

def XXX(**hodn):
    return hodn
p(XXX(Kokos = 2, Jablko = 4, Pomeranc = 1))

def businessCard(**person):
    print("*"*30)
    print("* First name:", person["firstName"])
    print("* Last name:", person["lastName"])
    print("* Job:", person["job"])
    print("*"*30)

businessCard(firstName="Petr", lastName="Horak", job="Programmer")
businessCard(lastName="Novotna", job="Teacher", firstName="Anna")