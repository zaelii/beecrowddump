a, b, c = map(float, input().split())

if((a+b) > c) and ((a+c) > b) and ((b+c) > a):
    perimetro = a+b+c
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((a+b)*c)/2
    print("Area = {:.1f}".format(area))

