import math;

def average(data: list) -> float:
    if not data:
        return []
    
    average = 0
    for num in data: 
        average += num

    return round(average / len(data), 2)


def maximum(data: list) -> float:
   if not data:
       return []
   
   maxVal =data[0]
   for num in data:
       if num > maxVal:
        maxVal = num

   return max(data)


def variance(data: list) -> float:
    if not data: 
        return []
    
    avg = average(data)
    square_diff = 0

    for num in data:
        square_diff += (num - avg) ** 2
    
    return round(square_diff / len(data), 2)


def standard_deviation(data: list) -> float:
    if not data:
        return []
    
    var = variance(data) 
    return round(math.sqrt(var), 2)
    
