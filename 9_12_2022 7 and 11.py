def fizzandbuzz():
    count = 1
    while count <= 100:
        divisibleby7 = count % 7 == 0
        divisibleby11 = count % 11 == 0
        #divisibleby3and5 = count % 7 == 0 and (count % 11 == 0)
        divisibleby7and11 =  divisibleby7 and divisibleby11
        if divisibleby7and11 :
            print("fizzbuzz", count, "is divisible by 7 and 11." )
        elif divisibleby7 :
            print("fizz", count, "is divisible by 7." )
        elif divisibleby11 :
            print("buzz", count, "is divisible by 11." )
        count += 1

fizzandbuzz()
