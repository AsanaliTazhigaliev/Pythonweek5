class name():
    def __init__(self,firstname,lastname,fullname):
        self.firstname=firstname
        self.lastname=lastname
        self.fullname=fullname
    def prt(self):
        print('Hello, my name is ' + self.fullname +'. I am a student,', 'but you can call me just '+self.firstname)

Stundent=name('Asanali','Tazhigaliev','Asanali Tazhigaliev')

Stundent.prt()