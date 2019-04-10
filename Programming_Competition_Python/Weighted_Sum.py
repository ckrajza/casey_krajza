#Casey Krajza
#Weighted Sum 

def main():
    #Multiply each digit in a number by the position 
    num = input("Enter a positive number: ")

    #additional variables 
    total = 0 #total of weight number 
    seq = 1 #what to multiple the number by 

    #for each loop to prodcue weighted sum 
    for i in num:
        total += int(i) * seq #add digit by position 
        seq += 1 #increase position count 
    
    #print out weighted sum 
    print("Weighted sum is " + str(total))
    
main() 