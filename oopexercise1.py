class rocket():
    def __init__(self):
        self.x=[0]
        self.y=[0]
        
    def setxy(self,x,y):
        self.x.append(x)
        self.y.append(y)
    def printrocket(self):
        print ('x coordinate of rocket is =',self.x)
        print ('y coordintate of rocket is =',self.y)
b=rocket()
b.printrocket()
b.setxy(2,9)
b.setxy(3,9)
b.setxy(4,9)


b.printrocket()


