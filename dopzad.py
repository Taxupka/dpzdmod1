grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
ots = sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
alp = list(sorted(students))
st = {alp[0]:ots[0], alp[1]:ots[1],alp[2]:ots[2],alp[3]:ots[3],alp[4]:ots[4]}
print(st)