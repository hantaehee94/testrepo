def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

add(5)

def mult(a,b):
    c = a * b
    print(c)
    return(c)

mult(6,7)

mult(2,3)

mult(1.2,90.456)

# str을 곱하는 경우에는 문자열을 곱해준 만큼 반복된다.
mult(2,"The Bodyguard")

def square(a):
    b = a + 1
    c = a*a+b
    print(a, "If you square + 1", c)
    return(c)

square(1)
square(2)
square(3)
square(4)


x = 5
y = square(x)
y

def mj():
    print("BFffewf")

def my1():
    print("efefew")
    return(None)

mj()
my1()

print(mj())
print(my1())


# 제곱을 출력하는 함수
def taehee(a):
    return(a*a)
print(taehee(100))

# 더하기 함수
def add(a,b):
    return(a+b)
print(add(4,5))

def con(a,b):
    return(a+b)
print(con('this',' is'))


# album, year_released 자리에는 a,b가 들어가더라도 문제없다.
def type_of_album(album, year_released):
    
    print(album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("The BodyGuard", 1981)
print(x)

# 리스트의 각 요소가 출력되는 코드임
def printlist(a):
    for b in a: # a의 각 요소가 b에 들어가 출력된다.
        print(b)

printlist([1,2,3,5,'bfb'])


def comparestrings(x, y):
    if x == y:
        return 1
    else:
        return 0

string1 = "THE"
string2 = "THE"

check = comparestrings(string1, string2)

if check == 1:
    print("The strings are the same")
else:
    print("The strings are different")

# python program to count words in a string using dictionary
def freq(string):
    words = []
    words = string.split()
    dict = {}

    for key in words:
        dict[key] = words.count(key)
    
    print("The frequency of words is:",dict)
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")