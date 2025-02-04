# comparision operations
a = 6
a==5

b = 5
b > 3

c = 8
c >= 5

d = 8
d != 5

"ACDC" == "Body Guard"
"ACDC" != "Body Guard"

# Branching
age = 20
if age > 18:
    print("your age is above 18")
else:
    print("your age is below 18")
print("Move on")

# branching with elif
age = 30
if age > 18:
    print("18살 이상임")
elif age == 18:
    print("18살임")
else:
    print("18살 미만임")
print("Move on")

# Logical operators : and or not
album_year = 1983
if(album_year > 1979) and (album_year < 1990):
    print("The album was made in the 80's")
print("")
print("Do stuff")

album_year = 1990
if (album_year > 1989) or (album_year < 1980):
    print("Album was not made in the 80's")
else:
    print("Album was made in the 80's")

# not operator and boolean
boolean_value = False
if not boolean_value:
    print("The value is False")

is_do_not_disturb = True
if not is_do_not_disturb:
    send_notification("New message received")
