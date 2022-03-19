
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path


## - START- UI Class
class Calculator_UI():

    ## -START- Setup Layout
    def setupLayout(self):

        ## -START- Main Window Properties
        self.setObjectName("mainWindow")
        self.resize(510, 300)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)          #... Elimina el marco del Sistema Operativo
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)       #... y vuelve la ventana transparente

        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.setCentralWidget(self.centralWidget)
        ## -END- Main Window Properties


        ## -START- Title Bar
        self.titleBar = QtWidgets.QFrame(self.centralWidget)
        self.titleBar.setObjectName("titleBar")
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 510, 30))
        self.titleBar.setStyleSheet(
                                    "background-color:qlineargradient(\n"
                                    "spread:pad,\n"
                                    "x1: 0, y1: 0.8,\n"
                                    "x2: 1, y2: 0,\n"
                                    "stop: 0.1875 rgba(30, 30, 30, 255),\n"
                                    "stop:1 rgba(40, 40, 40, 255));"
                                    )

        self.titleBarDragZone = QtWidgets.QFrame(self.centralWidget)
        self.titleBarDragZone.setObjectName("titleBarDrag")
        self.titleBarDragZone.setGeometry(QtCore.QRect(50, 0, 360, 30))
        self.titleBarDragZone.setStyleSheet(
                                    "background-color:none"
                                    )

        self.titleBarIcon = QtWidgets.QFrame(self.titleBar)
        self.titleBarIcon.setObjectName("titleBarIcon")
        self.titleBarIcon.setGeometry(QtCore.QRect(0, 0, 50, 30))

        self.titleBarLabel = QtWidgets.QLabel(self.titleBar)
        self.titleBarLabel.setObjectName("titleBarLabel")
        self.titleBarLabel.setGeometry(QtCore.QRect(30, 0, 120, 30))
        self.titleBarLabel.setStyleSheet(
                                         "background-color:none;\n"
                                         "color:white;\n"
                                         )

        ## -START- Title Buttons
        self.minimizeButton = QtWidgets.QPushButton(self.titleBar)
        self.minimizeButton.setObjectName("minimizeButton")
        self.minimizeButton.setGeometry(QtCore.QRect(410, 0, 50, 30))
        self.minimizeButton.setFlat(True)
        self.minimizeButton.setStyleSheet(
                                          "QPushButton{\n"
                                          "background-color:none;\n"
                                          "border-style: inset"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "background-color:rgba(60, 60, 60, 160);\n"
                                          "}"
                                          )
        self.minimizeButton.setIcon(QtGui.QIcon("./assets/minimizeButton.png"))
        self.minimizeButton.clicked.connect(self.minimizeApp)

        self.closeButton = QtWidgets.QPushButton(self.titleBar)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setGeometry(QtCore.QRect(460, 0, 50, 30))
        self.closeButton.setFlat(True)
        self.closeButton.setStyleSheet(
                                       "QPushButton{\n"
                                       "background-color:none;\n"
                                       "border-style: inset"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color:rgba(240, 40, 40, 160);\n"
                                       "}"
                                       )
        self.closeButton.setIcon(QtGui.QIcon("./assets/closeButton.png"))
        self.closeButton.clicked.connect(self.closeApp)
        ## -END- Title Buttons

        ## -END- Title Bar


        ## -START- Calculator Frame

        ## -START- Labels
        self.calculatorFrame = QtWidgets.QFrame(self.centralWidget)
        self.calculatorFrame.setObjectName("calculatorFrame")
        self.calculatorFrame.setGeometry(QtCore.QRect(0, 30, 300, 270))
        self.calculatorFrame.setStyleSheet(
                                           "background-color:qlineargradient(\n"
                                           "spread:pad,\n"
                                           "x1: 0, y1: 0.8,\n"
                                           "x2: 1, y2: 0,\n"
                                           "stop: 0.1875 rgba(30, 60, 90, 255),\n"
                                           "stop: 1 rgba(40, 80, 120, 255));\n"
                                           "border-bottom-left-radius:6px;"
                                           )

        self.heightLabel = QtWidgets.QLabel(self.calculatorFrame)
        self.heightLabel.setObjectName("heightLabel")
        self.heightLabel.setGeometry(QtCore.QRect(60, 60, 100, 26))
        self.heightLabel.setStyleSheet(
                                       "background-color:rgb(40, 40, 40);\n"
                                       "color:white;\n"
                                       "border-radius:0px;\n"
                                       "border-top-left-radius:4px;\n"
                                       "border-bottom-left-radius:4px;\n"
                                       "padding-left:8px;"
                                       )

        self.weightLabel = QtWidgets.QLabel(self.calculatorFrame)
        self.weightLabel.setObjectName("weightLabel")
        self.weightLabel.setGeometry(QtCore.QRect(60, 120, 100, 26))
        self.weightLabel.setStyleSheet(
                                       "background-color:rgb(40, 40, 40);\n"
                                       "color:white;\n"
                                       "border-radius:0px;\n"
                                       "border-top-left-radius:4px;\n"
                                       "border-bottom-left-radius:4px;\n"
                                       "padding-left:8px;"
                                       )
        ## -END- Labels

        ## -START- Inputs
        self.heightRegEx = QtCore.QRegExp(
                                          "^(?:\\d){0,3}$"                                 ##... ALTURA
                                                                                                            ##... máx 3 enteros
                                          )
        self.heightValidator = QtGui.QRegExpValidator(self.heightRegEx)

        self.weightRegEx = QtCore.QRegExp(                                                                  ##... PESO
                                          "^(?:\\d){0,3}(?:[.,]\\d\\d?)?$"          ##... máx. 3 enteros
                                                                                                            ##... punto o coma decimal (opcional)
                                                                                                            ##... máx. 2 decimales (opcional)
                                          )
        self.weightValidator = QtGui.QRegExpValidator(self.weightRegEx)

        self.heightInput = QtWidgets.QLineEdit(self.calculatorFrame)
        self.heightInput.setObjectName("heightInput")
        self.heightInput.setGeometry(QtCore.QRect(160, 61, 80, 25))
        self.heightInput.setStyleSheet(
                                       "QLineEdit {\n"
                                       "background-color:white;\n"
                                       "border-radius:0px;\n"
                                       "border-top-right-radius:4px;\n"
                                       "border-bottom-right-radius:4px;\n"
                                       "padding-left:4px;"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "background-color:rgb(215, 215, 215)"
                                       "}"
                                       )
        self.heightInput.setDragEnabled(True)
        self.heightInput.setClearButtonEnabled(True)
        self.heightInput.setMaxLength(3)
        self.heightInput.setValidator(self.heightValidator)

        self.weightInput = QtWidgets.QLineEdit(self.calculatorFrame)
        self.weightInput.setObjectName("weightInput")
        self.weightInput.setGeometry(QtCore.QRect(160, 121, 80, 25))
        self.weightInput.setStyleSheet(
                                       "QLineEdit {\n"
                                       "background-color:white;\n"
                                       "border-radius:0px;\n"
                                       "border-top-right-radius:4px;\n"
                                       "border-bottom-right-radius:4px;\n"
                                       "padding-left:4px;"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "background-color:rgb(215, 215, 215)"
                                       "}"
                                       )
        self.weightInput.setDragEnabled(True)
        self.weightInput.setClearButtonEnabled(True)
        self.weightInput.setValidator(self.weightValidator)
        ## -END- Inputs

        ## -START- Calculator Buttons
        self.calculateButton = QtWidgets.QPushButton(self.calculatorFrame)
        self.calculateButton.setObjectName("calculateButton")
        self.calculateButton.setGeometry(QtCore.QRect(70, 190, 70, 26))
        self.calculateButton.setStyleSheet(
                                           "background-color:white;\n"
                                           "border-radius:0px;"
                                           )
        self.calculateButton.clicked.connect(self.calculatorStart)

        self.clearButton = QtWidgets.QPushButton(self.calculatorFrame)
        self.clearButton.setObjectName("clearButton")
        self.clearButton.setGeometry(QtCore.QRect(160, 190, 70, 26))
        self.clearButton.setStyleSheet(
                                       "background-color:white;\n"
                                       "border-radius:0px;"
                                       )
        self.clearButton.clicked.connect(self.clearValues)
        ## -END- Calculator Buttons

        ## -END- Calculator Frame


        ## -START- Result Frame

        ## -START- Background
        self.resultFrameOut = QtWidgets.QFrame(self.centralWidget)
        self.resultFrameOut.setObjectName("resultFrameOut")
        self.resultFrameOut.setGeometry(QtCore.QRect(300, 30, 210, 270))
        self.resultFrameOut.setStyleSheet(
                                          "background-color:rgb(50, 50, 50);\n"
                                          "border-bottom-right-radius:6px;"
                                          )

        self.resultFrameIn = QtWidgets.QFrame(self.resultFrameOut)
        self.resultFrameIn.setObjectName("resultFrameIn")
        self.resultFrameIn.setGeometry(QtCore.QRect(10, 0, 200, 270))
        self.resultFrameIn.setStyleSheet(
                                         "background-color:rgb(40, 40, 40);\n"
                                         )
        ## -END- Background


        ## -START- Output
        self.resultBmiNum = QtWidgets.QLabel(self.resultFrameIn)
        self.resultBmiNum.setObjectName("resultBmiNum")
        self.resultBmiNum.setGeometry(QtCore.QRect(40, 20, 120, 70))
        self.resultBmiNum.setStyleSheet(
                                        "background-color:none;\n"
                                        "color: white;\n"
                                        "font-size:20px;"
                                        )
        self.resultBmiNum.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.resultBmiNum2 = QtWidgets.QLabel(self.resultFrameIn)
        self.resultBmiNum2.setObjectName("resultBmiNum2")
        self.resultBmiNum2.setGeometry(QtCore.QRect(40, 50, 120, 70))
        self.resultBmiNum2.setStyleSheet(
                                         "background-color:none;\n"
                                         "color: white;\n"
                                         "font-size:18px;"
                                         )
        self.resultBmiNum2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.resultBmiCat = QtWidgets.QLabel(self.resultFrameIn)
        self.resultBmiCat.setObjectName("resultBmiNum2")
        self.resultBmiCat.setGeometry(QtCore.QRect(40, 100, 120, 70))
        self.resultBmiCat.setStyleSheet(
                                        "background-color:none;\n"
                                        "color: white;\n"
                                        "font-size:20px;"
                                        )
        self.resultBmiCat.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        ## -END- Output


        ## -START- Info Button
        self.infoButton = QtWidgets.QPushButton(self.resultFrameIn)
        self.infoButton.setObjectName("infoButton")
        self.infoButton.setGeometry(QtCore.QRect(150, 220, 40, 40))
        self.infoButton.setIcon(QtGui.QIcon("./assets/infoButton.png"))
        self.infoButton.setStyleSheet(
                                   "QPushButton{\n"
                                   "background-color:none;\n"
                                   "border-radius:6px;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:rgb(70, 70, 70)\n"
                                   "}"
                                   )
        self.infoButton.setToolTip("Rangos del IMC")
        self.infoButton.clicked.connect(self.displayInfoBmi)
        ## -END- Info Button

        ## -END- Result Frame


        QtCore.QMetaObject.connectSlotsByName(self)


    ## -END- Setup Layout


    ## -START- Setup Text
    def setupText(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("mainWindow", "Calculadora de IMC"))
        self.titleBarLabel.setText(_translate("mainWindow", "Calculadora de IMC"))
        self.heightLabel.setText(_translate("heightLabel", "Altura (cm)"))
        self.weightLabel.setText(_translate("weightLabel", "Peso (kg)"))
        self.calculateButton.setText(_translate("calculateButton", "Calcular"))
        self.clearButton.setText(_translate("clearButton", "Borrar"))
        self.resultBmiNum.setText(_translate("resultBmiNum", "En espera"))
        self.resultBmiNum2.setText(_translate("resultBmiNum2", ""))
        self.resultBmiCat.setText(_translate("resultBmiCat", ""))
    ## -END- Setup Text

