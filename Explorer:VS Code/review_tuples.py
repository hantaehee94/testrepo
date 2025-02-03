tuple1 = ("disco",10.1,2)
type(tuple1)

#튜플의 각 인덱스를 출력해보자.
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

#튜플의 각 인덱스의 타입을 출력해보자.
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)
len(tuple2)
tuple21 = tuple2[:3]
print(tuple21)

#We cna sort the values in a tuple and save it to a enw tuple.
rating = (0,9,6,5,10,8,9,6,2)
rating_sorted = sorted(rating,reverse = False)
rating_sorted
reverserating_sorted = sorted(rating,reverse = True)
reverserating_sorted
