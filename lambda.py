sum1=lambda a,b: a+b
print(sum1(3,5))

"""Defining user class"""
class User:
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
"""Greetings function"""
    def greetings(self):
        return(f"good morning {self.name}")
Deepak=User("Deepak","deepaksingh20899@gmail.com",21)
print(Deepak.name," ",Deepak.age,"\n",Deepak.greetings())
