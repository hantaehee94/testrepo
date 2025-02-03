# dictionary는 key로 tuple을 사용할 수 있다.
dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(dict)

# key를 사용할 때 key가 string이면 따움표가 필요하며, 튜플 형태면 필요하지 않다.
dict[(0,1)] # 6

# 예제에서는 백슬레쉬를 통한 줄바꿈으로 가독성을 향상시켰지만, 굳이 그럴 필요는 없음ㅇㅇ
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
# 나는 아래처럼 할거임
# 이게 훨씬 좋은 듯
release_year_dict = {
    "Thriller": "1982", "Back in Black": "1980",
    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",
    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976",
    "Saturday Night Fever": "1977", "Rumours": "1977"
}
release_year_dict
release_year_dict["The Dark Side of the Moon"]

#Get all the keys in dictionary
release_year_dict.keys()

# append(add) a new key value pair in the dictionary
release_year_dict["Graduation"] = '2007'
print(release_year_dict)

# delete a key value pair in the dictionary
del(release_year_dict["Thriller"])
release_year_dict

# verify the key is in the dictionary
'The Bodyguard' in release_year_dict