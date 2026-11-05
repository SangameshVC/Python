from abc import ABC,abstractmethod
#here ABC is abstract class and abstractmethod is constructor that defines method as abstractmethod

#abstract class
class payment(ABC):
    
    #abstract method
    @abstractmethod
    def pay(self,amount):
        pass
    
class creditcardpayment(payment):
    
    def pay(self,amount):
        print(f"{amount} paid via credit card")
        
class upipayment(payment):
    
    def pay(self,amount):
        print(f"{amount} paid via upi")
        

payment1 = creditcardpayment()
payment1.pay(10000)                     #10000 paid via credit card

payment2 = upipayment()
payment2.pay(5000)                     #5000 paid via upi

# payment3 = payment()
# payment3.pay()           #TypeError: Can't instantiate abstract class payment with abstract method pay