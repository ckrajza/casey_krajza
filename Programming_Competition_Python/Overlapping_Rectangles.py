#Casey Krajza 
#Overlapping Rectangles 

def main():
    #ask for coordinates of first rectangle and assign to rec 1
    rec_1 = input("Enter coordinates of first rectangle(x1 y1 x2 y2): ")
    #ask for coordinates of second rectangle and assign to rec 2 
    rec_2 = input("Enter coordinates of second rectangle(x1 y1 x2 y2): ")
    
    #split rec 1 and rec 2 of spaces " "
    rec_1 = rec_1.split(" ")
    rec_2 = rec_2.split(" ")
    
    #assign values of rec 1 and rec 2 to absolute int variables 
    r1_x1, r1_y1, r1_x2, r1_y2 = int(rec_1[0]), int(rec_1[1]), int(rec_1[2]), int(rec_1[3])
    r2_x1, r2_y1, r2_x2, r2_y2 = int(rec_2[0]), int(rec_2[1]), int(rec_2[2]), int(rec_2[3])
    
    #calculate the area of rectangle one and rectangle two     
    area_one = abs((r1_x1 - r1_x2) * (r1_y1 - r1_y2))
    area_two = abs((r2_x1 - r2_x2) * (r2_y1 - r2_y2))
    
    #Calculate overlapping area by finding 
        # minimum of upper right minus maximum of lower left 
        # multiplied by 
        # minimum of lower right minus maximum of upper left 
    area_ovr = (min(r1_x2,r2_x2) - max(r1_x1,r2_x1)) * (min(r1_y2,r2_y2) - max(r1_y1,r2_y1))
    
    #calculate total area by adding area of rectangle one to area of rectangle two 
        # then subtracting area of overlapping rectangle 
    total_area = (area_one + area_two) - area_ovr
    
    #print out the overlapping area 
    print("The overlapped area is " + str(area_ovr))
    #print out the total area 
    print("The total area is " + str(total_area))
    
main() 