#Casey Krajza
#Parrallel or Intersecting Lines 

#slope = (y2 - y1) / (x2 - x1)
def slope(x1, y1, x2, y2):
    if x2 == x1:
        slope_val = 0
    else:
        slope_val = (y2 - y1) / (x2 - x1)
    return slope_val 

#main function 
def main():
    #first line 
    first = input("Enter coordinates for first line(x1 y1 x2 y2): ")
    #second line 
    second = input("Enter coordinates for second line(x1 y1 x2 y2): ")
    
    #assign first line coordinates 
    first = first.split(" ")
    f_x1, f_y1, f_x2, f_y2 = int(first[0]), int(first[1]), int(first[2]), int(first[3])
    
    #assign second line coordinates 
    second = second.split(" ")
    s_x1, s_y1, s_x2, s_y2 = int(second[0]), int(second[1]), int(second[2]), int(second[3])
    
    #figure slopes for each line 
    slope_one = slope(f_x1, f_y1, f_x2, f_y2)
    slope_two = slope(s_x1, s_y1, s_x2, s_y2)
    
    #Determine parrallel or intersecting and how many veritical lines 
    if slope_one == slope_two == 0:
        print("Parrallel - Both Vertical")
    elif slope_one == slope_two:
        print("Parrallel")
    elif slope_one == 0 or slope_two == 0:
        print("Intersecting - One Vertical")
    else:
        print("Intersecting")
        

main()