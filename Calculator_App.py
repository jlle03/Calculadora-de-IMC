

from PyQt5 import QtCore, QtWidgets
from Calculator_UI import *

class Calculator_App(QtWidgets.QMainWindow, Calculator_UI):

    def __init__(self):
        super().__init__()
        self.setupLayout()
        self.setupText()

        self.titleBarDragZone.installEventFilter(self)

    ## -START- Event Handler
    def eventFilter(self, obj, event):
        if obj == self.titleBarDragZone:

            if (event.type() == QtCore.QEvent.MouseButtonPress
            and event.button() == QtCore.Qt.LeftButton):
                self.windowPosition = event.pos()
                return False

            elif (event.type() == QtCore.QEvent.MouseMove
            and self.windowPosition != None):
                self.move(self.pos() + event.pos() - self.windowPosition)
                return False

            elif (event.type() == QtCore.QEvent.MouseButtonRelease
            and self.windowPosition != None):
                self.windowPosition = None
                return False

        return False
    ## -END- Event Handler


    ## -START- Title Bar Buttons Func.
    def minimizeApp(self):
        self.showMinimized()

    def closeApp(self):
        self.close()
    ## -END- Title Bar Buttons Func.


    ## -START- Calculator Func.
    def calculatorStart(self):
        bmi = self.calculateBMI()
        if bmi != None:
            bmiCategory = self.evaluateBMI(bmi)

            _translate = QtCore.QCoreApplication.translate
            self.resultBmiNum.setText(_translate("resultBmiNum", "Su IMC es:"))
            self.resultBmiNum2.setText(_translate("resultBmiNum2", "{}".format(bmi)))
            self.resultBmiCat.setText(_translate("resultBmiCat", "{}".format(bmiCategory)))

    def calculateBMI(self):
        try:
            height = float(self.heightInput.text())
            weight = float(self.weightInput.text().replace(",", "."))

            if height == 0 or weight == 0:
                self.displayErrorInvalidValue()
                return None

            else:
                bmi = (weight) / (height * 0.01) ** 2       ##... Fórmula IMC:
                                                        ##... Peso (en kg) dividido para altura (en m) al cuadrado

                bmi = round(bmi, 1)
                return bmi

        except ValueError:
            self.displayErrorInvalidValue()
            return None


    def evaluateBMI(self, bmi):

        if bmi < 18.5:
            return "Bajo peso"

        elif bmi >= 18.5 and bmi < 25:
            return "Peso normal"

        elif bmi >= 25 and bmi < 30:
            return "Sobrepeso"

        elif bmi >= 30:
            return "Obesidad"

    def clearValues(self):
        self.heightInput.clear()
        self.weightInput.clear()
        self.setupText()
    ## -END- Calculator Func.


    ## -START- Pop-Ups
    def displayErrorInvalidValue(self):
        errorDialog = QtWidgets.QMessageBox(self)
        errorDialog.setWindowTitle("Error")
        errorDialog.setIcon(QtWidgets.QMessageBox.Critical)
        errorDialog.setStandardButtons(QtWidgets.QMessageBox.Close)
        errorDialog.setText("Inserte valores válidos")
        errorDialog.show()

    def displayInfoBmi(self):
        bmiInfo = QtWidgets.QMessageBox(self)
        bmiInfo.setWindowTitle("Información")
        bmiInfo.setIcon(QtWidgets.QMessageBox.Information)
        bmiInfo.setStandardButtons(QtWidgets.QMessageBox.Close)
        bmiInfo.setText("Rangos del Índice de Masa Corporal:\n"
                        "\n\n"
                        "Menos de 18.5 = Bajo peso\n"
                        "\n"
                        "18.5 - 24.9 = Peso normal\n"
                        "\n"
                        "25 - 29.9 = Sobrepeso\n"
                        "\n"
                        "Más de 30 = Obesidad"
                        )
        bmiInfo.show()
    ## -END- Pop-Ups

