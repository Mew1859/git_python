score =float(input("Enter Your Score = "))
if (score>=0 and score<=49):
    print("Grade F")
elif (score>=50 and score<=54):
    print("Grade D")    
elif (score>=55 and score<=59):
    print("Grade D+")    
elif (score>=60 and score<=64):
    print("Grade C")            
elif (score>=65 and score<=69):
    print("Grade C+")    
elif (score>=70 and score<=74):
    print("Grade B")    
elif (score>=75 and score<=79):
    print("Grade B+")     
elif (score<=80 and score>=100):
    print("Grade A")
else:           
    print("Please try again")