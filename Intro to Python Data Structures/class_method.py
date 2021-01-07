class Ajitesh:
 
    surname= "Mishra"
    def __init__(self,name,height):
        self.name= name +" "+ self.surname
        self.height = height
    
    def show(self):
        print(self.name +"'s height is "+str(self.height))
    
    def show_name(self):
        return self.name

    @classmethod
    def show_extra(cls):
        cls.surname = "Shukla"

Ajitesh.show_extra()
Aj= Ajitesh("Sajal",5.9)
Pj= Ajitesh('Pranjal',5.6)
Aj.show() , Pj.show()



