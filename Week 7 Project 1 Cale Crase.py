"""
File: stats.py
Author: Cale Crase
This is Project 1 of week 7
"""
    
def median(n):
    n.sort()
    m = len(n) // 2
    if n == 0:
        return "0"
    if len(n) % 2 == 1:
        print(n[m])
    else:
        print((n[m] + n[m - 1]) / 2)
    
def mode(n):
    if len(n) == 0:
        return "0"
    x = {}
    for number in n:
        if number in x.keys():
            x[number] = x[number] + 1
        else:
            x[number] = 1
            
    maxNumber = max(x.values())
    for key in x:
        if x[key] == maxNumber:
            print("The mode is", key)

def mean(n):
    sumOfNumber = 0.0
    n2 = len(n)
    if n2 == 0:
        return "0"
    for number in z:
        sumOfNumber += number
    return (sumOfNumber / n2)


def main():
    input("Enter any list of numbers: ")
    print("The median is", str(median))
    print("The mode is", str(mode))
    print("The mean is", str(mean))

if __name__ == "__main__":
    main()
