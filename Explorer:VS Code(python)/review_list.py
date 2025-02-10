reviewlist = ["The Bodyguard", 7.0, 1992,[1,2],("A",1)]
print('the same element using negative and positive indexing:\n Postive[0]:',reviewlist[0],
'\n Negative[-5]:' , reviewlist[-5]  )
print('the same element using negative and positive indexing:\n Postive[1]:',reviewlist[1],
'\n Negative[-4]:' , reviewlist[-4]  )
print('the same element using negative and positive indexing:\n Postive:[2]',reviewlist[2],
'\n Negative[-3]:' , reviewlist[-3]  )
reviewlist[3:5]

# extend는 각 element를 추가한다.
reviewlist.extend([10000,29424])
print(reviewlist)

# append는 list안에 list를 추가한다. 이 말은 list는 다른 list 속에 들어갈 수 있다는 것을 의미한다.
reviewlist.append([9999,275555])
print(reviewlist)

# list의 element를 변경하는 것도 가능하다. "The Bodyguard"를 "Bodyguard"로 변경했다.
reviewlist[0] = "Bodyguard"
print(reviewlist)

# del을 사용하여 element를 삭제할 수 있다. 이땐 del.이 아닌 del(reviewlist[n])을 사용한다.
print('Before del:',reviewlist)
del(reviewlist[7])
print('After del: ',reviewlist)

# Split을 사용하여 string을 list로 변환할 수 있다.
'hard rock'.split()
# 그렇다면 리스트 안의 element를 나눠볼까? 'Bodyguard'를 g를 기준으로 나눠보자.
reviewlist[0].split('g')
print(reviewlist[0].split('g'),'After split:',reviewlist)
"""
insight : split은 영구적인 변화를 주지 않는다. 그냥 보여주는 것 뿐이다.
그렇다면 split된 element를 저장하려면 어떻게 해야 할까?
아마 다른 변수에 저장하면 될 것 같다. 도전해보자.
"""
split_reviewlist = reviewlist[0].split('g')
print('After split:',split_reviewlist)
split_reviewlist.append(reviewlist[1:])
print('After append:',split_reviewlist)
# 흠... 이게 맞는 방법인진 모르겠지만 지금 내 수준에서의 최선이다.