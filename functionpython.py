def fahr2celcius(fahr):
    celcius = (5*(fahr - 32))/9
    return celcius

print('100 fahr =',round(fahr2celcius(100),2),'degree celcius')

def adjacentSum(a):
    sum=0
    for i in a:
        sum+=i
    return sum

print('Sum all value in list is :',adjacentSum([2,3,4,8]))


def adjacentNumSum(list_num):
    if not list_num:
        return list_num
    new_list=[list_num[0]]
    for elem in list_num[1:] :
        if elem !=new_list[-1]:
            new_list.append(elem)
    return new_list

print(adjacentNumSum([]))