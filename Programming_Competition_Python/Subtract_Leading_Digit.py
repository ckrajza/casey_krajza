#Casey Krajza 
#Subtract Leading Digit

def main():
    #ask for starting number and end number 
    start = input("Enter a starting number: ")
    end = int(input("Enter an end number: "))

    #other variables 
    seq = 0 #sequence number 
    total = int(start) #initialization of total with starting number 

    #while loop 
    while total > end:
        temp = int(start[0])
        total -= temp 
        start = str(total)
        seq += 1

    #Print out sequence count 
    print("Total sequence count is " + str(seq))
    
main()