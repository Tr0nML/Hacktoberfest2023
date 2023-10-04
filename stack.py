class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__top == self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    
    def push(self,data):
        if(self.is_full()):
            print("STack is Full")
        else:
            self.__top +=1
            self.__elements[self.__top]=data
        
    def pop(self):
        if(self.is_empty()):
            print("The Stack is Empty")
        else:
            data= self.__elements[self.__top]
            self.__top=-1
            return data
        
    def display(self):
        if(self.is_empty()):
            print("The Stack is Empty !!!")
        else:
            index=self.__top
            while(index >= 0):
                print(self.__elements[index])
                index-=1

s1=Stack(5)
s1.pop()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)

s1.push(60)
s1.display()