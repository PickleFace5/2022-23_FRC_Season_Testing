import commands2
import wpilib
from commands2.button import JoystickButton

import constants
from commands.armTest import ArmTest
from commands.joystickDrive import JoystickDrive
from commands.keepAtZero import KeepAtZero
from commands.autoDock import StationCorrectionMobility
from commands.timedDrive import TimedDrive
from subsystems.arm import Arm
from subsystems.drivetrain import Drivetrain
from commands.joystickControlArm import JoystickControlArm
from commands.setPositions import SetPositions
from commands.changePosition import ChangePosition
from commands.moveArmCommands import MoveArm
from commands.setGrabber import SetGrabber
from commands.moveArmCommands import MoveArmToPose
from commands.moveArmCommands import MoveArmUp
from commands.holdPos import HoldPos
from commands.moveArmCommands import MoveBackToHome
from commands.moveArmCommands import PlaceCubeMid
from commands.autoDock import StationCorrection
from commands.toggleBrakeMode import ToggleBrakeMode

class RobotContainer:

    def __init__(self):

        self.driverController = wpilib.XboxController(constants.DRIVERCONTROLLERPORT)
        self.functionsController = wpilib.XboxController(constants.FUNCTIONSCONTROLLERPORT)

        self.train = Drivetrain()

        self.arm = Arm()

        self.chooser = wpilib.SendableChooser()

        stationCorrectionMobility = StationCorrectionMobility(self.train, self.arm)
        autoDoc = StationCorrection(self.train, self.arm)

        self.chooser.setDefaultOption("Auto Charge Station", autoDoc)
        self.chooser.addOption("Mobility Charging Station", stationCorrectionMobility)
        self.chooser.addOption("Timed Drive", TimedDrive(self.train))

        wpilib.SmartDashboard.putData("Autonomoose", self.chooser)

        self.train.setDefaultCommand(JoystickDrive(self.train, lambda: self.driverController.getLeftY(),
                                                   lambda: self.driverController.getRightX(),
                                                   lambda: self.driverController.getLeftBumper(),
                                                   lambda: self.driverController.getRightBumper(),
                                                   lambda: self.driverController.getAButtonReleased()))

        #self.arm.setDefaultCommand(MoveArm(self.arm))
        # self.arm.setDefaultCommand(KeepAtZero(self.arm))

        # JoystickButton(self.driverController, wpilib.XboxController.Button.kB).whenPressed(ArmTest(self.arm))

        #self.arm.setDefaultCommand(JoystickControlArm(self.arm, lambda: self.functionsController.getLeftBumper(), lambda: self.functionsController.getRightBumper(), lambda: self.functionsController.getLeftY(), lambda: -self.functionsController.getRightY(), lambda: self.functionsController.getRightTriggerAxis(), lambda: self.functionsController.getLeftTriggerAxis(), lambda: self.functionsController.getXButton(), lambda: self.functionsController.getYButton()))
        #self.arm.setDefaultCommand(HoldPos(self.arm))
        # JoystickButton(self.functionsController, wpilib.XboxController.Button.kB).whenPressed(PoseArm(self.arm, [0, 0, 0, 0, 0]))

        # JoystickButton(self.driverController, wpilib.XboxController.Button.kB).whenPressed(ArmTest(self.arm))
        # JoystickButton(self.driverController, wpilib.XboxController.Button.kA).whenPressed(SetGrabber(self.arm, lambda: self.driverController.getAButton()))

        #JoystickButton(self.driverController, wpilib.XboxController.Button.kB).whenPressed(ArmTest(self.arm))

        # JoystickButton(self.driverController, wpilib.XboxController.Button.kB).whenPressed(MoveArmUp(self.arm))
        
        #DONT DELETE ME PLZ I HAVE A WIFE AND KIDS
        #JoystickButton(self.functionsController, wpilib.XboxController.Button.kB).whenPressed(MoveArmToPose(self.arm))
        #JoystickButton(self.functionsController, wpilib.XboxController.Button.kA).whenPressed(SetGrabber(self.arm))
        #JoystickButton(self.functionsController, wpilib.XboxController.Button.kY).whenPressed(MoveBackToHome(self.arm))
        #JoystickButton(self.functionsController, wpilib.XboxController.Button.kX).whenPressed(SetPositions(self.arm, 0, 0, 0, 0))
        JoystickButton(self.functionsController,wpilib.XboxController.Button.kB).whenPressed(ArmTest(self.arm))
        #JoystickButton(self.functionsController,wpilib.XboxController.Button.kY).whenReleased(ToggleBrakeMode(self.arm))
        
        #JoystickButton(self.functionsController, wpilib.XboxController.Button.kLeftBumper).whenPressed(SetPositions(self.arm, 61869, -60707, 3571, 0))
        
       # JoystickButton(self.driverController, wpilib.XboxController.Button.kB).whenPressed(ArmTest(self.arm))


        # JoystickButton(self.driverController, wpilib.XboxController.Button.kB).whenReleased(ChangePosition(self.arm, True))
        # JoystickButton(self.driverController, wpilib.XboxController.Button.kX).whenReleased(ChangePosition(self.arm, False))

    def getAutonomousCommand(self) -> commands2.CommandBase:

        return self.chooser.getSelected()
