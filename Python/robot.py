import numpy as np

class Link():
    def __init__(self, theta=0, alpha=0, r=0, d=0) -> None:
        self.theta = theta
        self.alpha = alpha
        self.r = r
        self.d = d
    
    def Set_DH(self, theta, alpha, r, d) -> None:
        self.theta = theta
        self.alpha = alpha
        self.r = r
        self.d = d
    
class Robot():
    def __init__(self) -> None:
        
        pass
    def Setup(self):
        self.link1 = Link(0,0,0,0)
        self.link2 = Link(0,0,0,0)
        self.link3 = Link(0,0,0,0)
        self.link4 = Link(0,0,0,0)
        self.link5 = Link(0,0,0,0)
        self.link6 = Link(0,0,0,0)

    def Pose(self, ):
        
        print("Posing Robot")
        
class RobotController():
    def __init__(self) -> None:
          
        self.robot = Robot()
        pass
    
    def Get_Robot(self)-> Robot:
        return self.robot

def Motor(t, d):
    M = np.exp(-(t + d/2)*np.pi)
    print(M)
       
if __name__ == '__main__':
    
    Motor(3, 12)
    exit()
    
    rc = RobotController()
    robot = rc.Get_Robot()
    if not robot:
        print("Robot Does Not Exist")
        exit()
    
    
    