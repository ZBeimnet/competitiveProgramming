def main():
    x = input().split()
    length = int(x[0])
    width = int(x[1])
    cover = int(x[2])
    print(checkLength(length, cover) * checkWidth(width, cover))

def checkLength(length, cover):
    noOfCoverInY = 1
    coverLength = cover
    
    if(length <= coverLength):
        return noOfCoverInY
    else:
        for i in range(1, length):
            if(coverLength < length):
                noOfCoverInY += 1
                coverLength += cover
            else:
                break
    return noOfCoverInY

def checkWidth(width, cover):
    noOfCoverInX = 1
    coverWidth = cover
    
    if(width <= coverWidth):
        return noOfCoverInX
    else:
        for i in range(1, width):
            if(coverWidth < width):
                noOfCoverInX += 1
                coverWidth += cover
            else:
                break
    return noOfCoverInX

main()
