class Listconcat:#create class
    
    def __init__(self,list1,list2): #create se constractor(Method) this constrator run automatically
        self.list1=list1 #create instanse variable with the self of self keyword
        self.list2=list2
        self.list3=[] #create Empty List
        
    def addlist(self): #create a method for add two List
        self.list3=self.list1+self.list2  #here arithmetic operator used to add 2 lists
        return self.list3
    
list1=[] #create two Empty set
list2=[]
number=int(input("Enter how many charater you want in List1:"))

for i in range(number):
    a=input("Enter a character:")
    list1.append(a) # append is used for add each caratcter
number1=int(input("Enter how many charater you want in List2:"))

for i in range(number1):
    a=input("Enter a character:")
    list2.append(a)


client=Listconcat(list1,list2) #creating instance variable of class
print(client.addlist()) #calling a function
