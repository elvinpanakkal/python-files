lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","Karen","jim","jim","Oscar","toby"]

friends.insert(1,"Kelly")
friends.append("Creed")
friends.sort()

#friends.extend(lucky_numbers)
lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)


friends2 = friends.copy()



friends.remove("toby")
friends.pop()
#friends.clear()
print(friends)


print(friends.index("kevin"))
print(friends.count("jim"))