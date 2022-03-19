
from PyQt5 import QtGui, QtWidgets
from Calculator_App import *


if __name__ == "__main__":
    import sys
    import ctypes

    appID = "project.bmi_calculator"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appID)

    appInstance = QtWidgets.QApplication(sys.argv)
    appInstance.setWindowIcon(QtGui.QIcon("./assets/appIcon_Color.png"))
    appWindow = Calculator_App()
    appWindow.show()
    sys.exit(appInstance.exec_())

