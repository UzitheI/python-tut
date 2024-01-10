hero=['janice','workout','elephant']

hero.remove('janice')

print(hero)


hero.sort()

print(hero)

#also i can reverse it

hero.sort(reverse=True)

print(hero)

matrix=[4,2,'micah', 3,100,'financier']

# matrix.sort()

# print(matrix)

finaice=['Anit','asdf','zerox','Zesty']

finaice.sort()

print(finaice)

#we can also sort it on the basis of key strokes where small a is in higher order than A

finaice.sort(key=str.lower)

print(finaice)