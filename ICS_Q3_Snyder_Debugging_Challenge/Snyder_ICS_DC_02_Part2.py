#Alem Snyder
#is a bad person

#the recurcive definit of a sumation
def sumation(function, start, stop):
    if start == stop:
        return function(star)
    else:
        total = function(start) + sumation(function, start+1, stop)
    return total

print(sumation(lambda x : x*x, 0,100))
