durability = [1, 2, 1, 4] # 돌의 내구도
dogs = [{
    "name" : "루비독",
    "age" : "95년생",
    "jump" : "3",
    "weight" : "4",
    },{
    "name" : "피치독",
    "age" : "95년생",
    "jump" : "3",
    "weight" : "3",
    },{
    "name" : "씨-독",
    "age" : "72년생",
    "jump" : "2",
    "weight" : "1",
    },{
    "name" : "코볼독",
    "age" : "59년생",
    "jump" : "1",
    "weight" : "1",
    },
]


def cross_the_stone(dogs, durability):
    answer= [i["name"] for i in dogs]
    for i in dogs:
        location =0
        while location < len(durability)-1:
            location += int(i["jump"])
            durability[location-1] -= int(i["weight"])
            if durability[location-1]<0: #물에빠짐
                del answer[answer.index(i['name'])]
                break
    return answer


print(cross_the_stone(dogs.copy(), durability.copy()))
