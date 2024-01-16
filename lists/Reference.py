#whenever we are assigning a variable containing value to another value, we are passing in the reference variable


marks=['1','200','320','400']


cheese=marks


cheese[2]='apple'

print(marks)

#here even tho the change didnt happen in marks but happned in cheese, the effect was seen in marks because the cheese variable actually contains the reference to the marks variable and it is not the copy of the marks variable


