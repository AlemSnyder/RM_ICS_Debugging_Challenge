#Alem Snyder
#is a bad person

#the recurcive definit of a sumation
def sumation(function, start, stop):
    if start == stop:
        return function(start)
    else:
        total = function(start) + sumation(function, start+1, stop)
    return total

print(sumation(lambda x : 1/(100-x), 0,100))
