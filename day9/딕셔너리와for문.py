fruit_colors = {
    "Red" : "apple",
    "Yellow" : "banana",
    "Purple" : "blueberry"
}

#키값을 출력해주세용
print(fruit_colors.keys())

for i in fruit_colors.keys():
    print(i)

color_list = list(fruit_colors.keys())
print(color_list)

color_list.append("Pink")
print(color_list)

