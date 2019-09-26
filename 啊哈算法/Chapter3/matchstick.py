# 火柴棍问题：
def calculatestick(sticknumber):
    upperlimit = 1111
    loop = 0
    for a in range(0, upperlimit + 1):
        for b in range(0, upperlimit + 1):
            c = a + b
            if numberstick(c) == sticknumber - numberstick(a) - numberstick(b) - 4:
                loop += 1
                yield a, b, c, loop


def numberstick(number):
    totalnumberstick = 0
    if number == 0:
        return d[number]
    else:
        while number > 0:
            rev = number % 10
            number = number // 10
            totalnumberstick += d[rev]
        return totalnumberstick


numberlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sticklist = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
d = dict(zip(numberlist, sticklist))
sticknumber = 24
# print(numberstick(8))
for x in calculatestick(sticknumber):
    print("condition", x[3], "a=", x[0], "b=", x[1], "c=", x[2])