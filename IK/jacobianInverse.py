import numpy as np
import math
from robot_arm import *
import pygame

xOffset = 250
yOffset = 250
Arm = RobotArm(xBase=xOffset, yBase=yOffset)

Arm.add_arm_segment(length=75, thetaInit=math.radians(20))
Arm.add_arm_segment(length=75, thetaInit=math.radians(45))
Arm.add_arm_segment(length=75, thetaInit=math.radians(45))
Arm.update_joint_coords()

target = Arm.joints[:, [-1]]

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Robot Arm Inverse Kinematics")
window.fill((255,255,255))

reach = sum(Arm.lengths)
print("\n" + str(Arm.joints))
print("\n [0][0]" + str(Arm.joints[0][0]))
print("\n [0][1]" + str(Arm.joints[0][1]))
print("\n [0][2]" + str(Arm.joints[0][2]))
print("\n [0][3]" + str(Arm.joints[0][3]))

def move_to_target():
    global Arm, target, reach

    distPerUpdate = 0.02 * reach

    if np.linalg.norm(target - Arm.joints[:, [-1]]) > 0.02 * reach:
        targetVector = (target - Arm.joints[:, [-1]])[:3]
        targetUnitVector = targetVector / np.linalg.norm(targetVector)
        deltaR = distPerUpdate * targetUnitVector
        J = Arm.get_jacobian()
        JInv = np.linalg.pinv(J)
        deltaTheta = JInv.dot(deltaR)
        Arm.update_theta(deltaTheta)
        Arm.update_joint_coords()

# add limits
Arm.add_limits()
Arm.def_joint_limit(0, -math.pi, math.pi)


targetPt = (250, 250)

running = True
while running:
    window.fill((255,255,255))
    pygame.draw.circle(window, (255, 0, 0), (250, 250), reach, 5)
    pygame.draw.circle(window, (0, 255, 0), (xOffset, yOffset), 5)

    # draw arm
    for i in range(len(Arm.lengths)):
        pygame.draw.line(window, (0, 0, 255), (Arm.joints[0][i], Arm.joints[1][i]), (Arm.joints[0][i+1], Arm.joints[1][i+1]), 5)

    #draw target
    pygame.draw.circle(window, (0, 0, 0), targetPt, 7)

    # draw joints
    for i in range(len(Arm.joints)):
        pygame.draw.circle(window, (0, 255, 255), (Arm.joints[0][i], Arm.joints[1][i]), 5)
    
    # Run IK code
    move_to_target()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("DOWN!")
            print(str(pygame.mouse.get_pos()))
            print("x =" + str(pygame.mouse.get_pos()[0]))
            print("y =" + str(pygame.mouse.get_pos()[1]))
            click = pygame.mouse.get_pos()
            print(str(click))
            targetPt = (click[0], click[1])
            target = np.array([[click[0],click[1], 0, 1]]).T
            print(str(target))
            print(str(Arm.joints))

            distPerUpdate = 0.02 * reach

            if np.linalg.norm(target - Arm.joints[:, [-1]]) > 0.02 * reach:
                targetVector = (target - Arm.joints[:, [-1]])[:3]
                targetUnitVector = targetVector / np.linalg.norm(targetVector)
                deltaR = distPerUpdate * targetUnitVector
                J = Arm.get_jacobian()
                JInv = np.linalg.pinv(J)
                deltaTheta = JInv.dot(deltaR)
                Arm.update_theta(deltaTheta)
                Arm.update_joint_coords()
            
            print("targetVector \n" + str(targetVector))
            print("targetUnitVector \n" + str(targetUnitVector))
            print("deltaR \n" + str(deltaR))
            print("deltaTheta \n" + str(deltaTheta))
            print("THETAS! " + str(Arm.thetas))

            print("Limits" + str(Arm.get_joint_limits()))

            Arm.get_angles()
    pygame.display.flip()