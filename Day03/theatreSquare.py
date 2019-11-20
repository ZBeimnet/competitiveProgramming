def main():
    value = input().split()
    length = int(value[0])
    width = int(value[1])
    cover = int(value[2])
    print(checkLength(length, cover) * checkWidth(width, cover))

def checkLength(length, cover):
    noOfCoverInY = 1
    
    if(length <= cover):
        return noOfCoverInY
    else:
        if(length % cover != 0):
            noOfCoverInY += length // cover
        else:
            noOfCoverInY = length // cover
    return noOfCoverInY

def checkWidth(width, cover):
    noOfCoverInX = 1
    
    if(width <= cover):
        return noOfCoverInX
    else:
        if(width % cover != 0):
            noOfCoverInX += width // cover
        else:
            noOfCoverInX = width // cover
    return noOfCoverInX

main()
