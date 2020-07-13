def rightSlash(total):
    for i in range(int(total)):
        print("/", end="")

def leftSlash(total):
    for i in range(int(total)):
        print("\\", end="")

def space(total):
    for i in range(int(total)):
        print(" ", end = "")

def upSide(total):
    startingSpace = total/2-1
    for i in range(int(total/2)):
        space((total/2-1)-i)
        rightSlash(1)
        space(i*2)
        leftSlash(1)
        print()


def downSide(total):
    startingSpace = total-2
    for i in range(int(total/2)):
        space(i)
        leftSlash(1)
        space(startingSpace-2*i)
        rightSlash(1)
        print()

def paralellogram(total):
    if total % 2 == 0:
        upSide(total)
        downSide(total)
    else:
        print("Total can't be an odd number.")


paralellogram(20)