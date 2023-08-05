# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mw4/gui/widgets/measure.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MeasureDialog(object):
    def setupUi(self, MeasureDialog):
        MeasureDialog.setObjectName("MeasureDialog")
        MeasureDialog.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MeasureDialog.sizePolicy().hasHeightForWidth())
        MeasureDialog.setSizePolicy(sizePolicy)
        MeasureDialog.setMinimumSize(QtCore.QSize(800, 285))
        MeasureDialog.setMaximumSize(QtCore.QSize(1600, 1230))
        MeasureDialog.setSizeIncrement(QtCore.QSize(10, 10))
        MeasureDialog.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MeasureDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(MeasureDialog)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(4, 6, 4, 6)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.measureGroup = QtWidgets.QGroupBox(MeasureDialog)
        self.measureGroup.setProperty("large", True)
        self.measureGroup.setObjectName("measureGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.measureGroup)
        self.gridLayout.setContentsMargins(5, 10, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.measureGroup)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.measureGroup)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.set3 = QtWidgets.QComboBox(self.measureGroup)
        self.set3.setMinimumSize(QtCore.QSize(0, 25))
        self.set3.setObjectName("set3")
        self.gridLayout.addWidget(self.set3, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.measureGroup)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.set0 = QtWidgets.QComboBox(self.measureGroup)
        self.set0.setMinimumSize(QtCore.QSize(150, 25))
        self.set0.setObjectName("set0")
        self.gridLayout.addWidget(self.set0, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.measureGroup)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.set1 = QtWidgets.QComboBox(self.measureGroup)
        self.set1.setMinimumSize(QtCore.QSize(150, 25))
        self.set1.setObjectName("set1")
        self.gridLayout.addWidget(self.set1, 1, 1, 1, 1)
        self.set4 = QtWidgets.QComboBox(self.measureGroup)
        self.set4.setMinimumSize(QtCore.QSize(150, 25))
        self.set4.setObjectName("set4")
        self.gridLayout.addWidget(self.set4, 1, 4, 1, 1)
        self.set2 = QtWidgets.QComboBox(self.measureGroup)
        self.set2.setMinimumSize(QtCore.QSize(0, 25))
        self.set2.setObjectName("set2")
        self.gridLayout.addWidget(self.set2, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.measureGroup)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.measureGroup)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.measure = Measure(MeasureDialog)
        self.measure.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure.sizePolicy().hasHeightForWidth())
        self.measure.setSizePolicy(sizePolicy)
        self.measure.setMinimumSize(QtCore.QSize(0, 0))
        self.measure.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.measure.setSizeIncrement(QtCore.QSize(10, 10))
        self.measure.setBaseSize(QtCore.QSize(10, 10))
        self.measure.setAutoFillBackground(True)
        self.measure.setStyleSheet("")
        self.measure.setObjectName("measure")
        self.verticalLayout.addWidget(self.measure)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(MeasureDialog)
        QtCore.QMetaObject.connectSlotsByName(MeasureDialog)

    def retranslateUi(self, MeasureDialog):
        _translate = QtCore.QCoreApplication.translate
        MeasureDialog.setWindowTitle(_translate("MeasureDialog", "Measurements"))
        self.measureGroup.setTitle(_translate("MeasureDialog", "Measurement values"))
        self.label_2.setText(_translate("MeasureDialog", "Upper middle chart"))
        self.label_3.setText(_translate("MeasureDialog", "Lower chart"))
        self.label_4.setText(_translate("MeasureDialog", "Lower middle chart"))
        self.label.setText(_translate("MeasureDialog", "Upper chart"))
        self.label_5.setText(_translate("MeasureDialog", "Middle chart"))
from gui.utilities.tools4pyqtgraph import Measure


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MeasureDialog = QtWidgets.QWidget()
    ui = Ui_MeasureDialog()
    ui.setupUi(MeasureDialog)
    MeasureDialog.show()
    sys.exit(app.exec_())
