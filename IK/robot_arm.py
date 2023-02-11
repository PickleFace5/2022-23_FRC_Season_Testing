# this is code made from a tutorial at https://nrsyed.com/2017/12/17/animating-the-jacobian-inverse-method-with-an-interactive-matplotlib-plot/
# We had a few issues with just usin ctrl+c and ctrl+v from github so I decided to make my own and change it some

import numpy as np
import math

class RobotArm:
    # like the code that this was based on we can change the place where the base arm joins to the robot
    # If no arguments, they are set to 0.
    # init class
    def __init__(self, **kwargs):
        self.xBase = kwargs.get('xBase', 0)
        self.yBase = kwargs.get('yBase', 0)
        # a list of the arm angles
        self.thetas = np.array([[]], dtype=float)
        # the matrices of the joint coordinates
        self.joints = np.array([[self.xBase, self.yBase, 0, 1]], dtype=float).T
        # a list of all the arm lengths
        self.lengths = []
        
    def add_arm_segment(self, **kwargs):
        """ add_arm_segment(length, thetaInit=0)
                Here we add another segment to the arm. We have to define the length
                and we can define the initial angle of the arm as well (which will come in hand later).
        """
        self.joints = np.append(self.joints, np.array([[0, 0, 0, 1]]).T, axis=1)
        self.lengths.append(kwargs['length'])
        