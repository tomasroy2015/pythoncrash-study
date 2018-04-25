num = int(input('Enter number of bottles='))

for quant in range(num,0,-1):
    if quant > 1:
        print(quant," bottles of beer on the wall,",quant," bottles of beer")
        if(quant > 2):
            suffix = str(quant)+" bottles of beer on the wall"
        else:
            suffix ="1 bottle of beer on the wall"
    elif quant == 1:
        print ("1 bottle of beer on the wall")
        suffix = " No more beer on the wall"

    print("Take one down and pass it around",suffix)
    print("----")                