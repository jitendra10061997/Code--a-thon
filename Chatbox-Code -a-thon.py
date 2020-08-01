class chatbot: #create a class
    
    def __init__(self,number): #defining constractor 
        self.number=number #create a variable and this variable is used by any method is same class
        
    def printvalidation(self): #create a method for number validation
        
        if(len(self.number)==10):#check the condition the number is ==10 or not and reused variable by constractor
            
            if(self.number.isnumeric()): #check the number is numeric format or not
                
                if(self.number[0]=="7" or self.number[0]=="8" or self.number[0]=="9"):#check the condition if number is starting from 7 or 8 or 9
                    return ("valid")
                else:
                    return("You entered number is Valid")
            else:
                return("You entered number is InValid")
        else:
            return("You entered number is InValid")
print("Enetr 2 Numbers")
for i in range(2):
    a=str(input("Enter number"))
    number1=chatbot(a) 
    print(number1.printvalidation())


