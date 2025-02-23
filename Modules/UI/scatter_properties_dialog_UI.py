# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scatter_properties_dialog_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(370, 284)
        Dialog.setStyleSheet(u"*{  \n"
"    font-size:13px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_point_size = QLabel(Dialog)
        self.lbl_point_size.setObjectName(u"lbl_point_size")
        self.lbl_point_size.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.lbl_point_size)

        self.spb_marker_size = QSpinBox(Dialog)
        self.spb_marker_size.setObjectName(u"spb_marker_size")
        self.spb_marker_size.setMinimumSize(QSize(0, 25))
        self.spb_marker_size.setMaximumSize(QSize(16777215, 25))
        self.spb_marker_size.setMaximum(100)
        self.spb_marker_size.setValue(6)

        self.horizontalLayout_2.addWidget(self.spb_marker_size)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_cmap_category = QLabel(Dialog)
        self.lbl_cmap_category.setObjectName(u"lbl_cmap_category")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_cmap_category.sizePolicy().hasHeightForWidth())
        self.lbl_cmap_category.setSizePolicy(sizePolicy)
        self.lbl_cmap_category.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_5.addWidget(self.lbl_cmap_category)

        self.cmb_cmap_category = QComboBox(Dialog)
        self.cmb_cmap_category.addItem("")
        self.cmb_cmap_category.addItem("")
        self.cmb_cmap_category.addItem("")
        self.cmb_cmap_category.addItem("")
        self.cmb_cmap_category.addItem("")
        self.cmb_cmap_category.addItem("")
        self.cmb_cmap_category.addItem("")
        self.cmb_cmap_category.setObjectName(u"cmb_cmap_category")

        self.horizontalLayout_5.addWidget(self.cmb_cmap_category)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_cmap = QLabel(Dialog)
        self.lbl_cmap.setObjectName(u"lbl_cmap")
        sizePolicy.setHeightForWidth(self.lbl_cmap.sizePolicy().hasHeightForWidth())
        self.lbl_cmap.setSizePolicy(sizePolicy)
        self.lbl_cmap.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_7.addWidget(self.lbl_cmap)

        self.cmb_cmap = QComboBox(Dialog)
        self.cmb_cmap.setObjectName(u"cmb_cmap")

        self.horizontalLayout_7.addWidget(self.cmb_cmap)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_alpha = QLabel(Dialog)
        self.lbl_alpha.setObjectName(u"lbl_alpha")
        self.lbl_alpha.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_6.addWidget(self.lbl_alpha)

        self.dsb_alpha = QDoubleSpinBox(Dialog)
        self.dsb_alpha.setObjectName(u"dsb_alpha")
        self.dsb_alpha.setMinimumSize(QSize(0, 25))
        self.dsb_alpha.setMaximumSize(QSize(16777215, 25))
        self.dsb_alpha.setDecimals(1)
        self.dsb_alpha.setMaximum(1.000000000000000)
        self.dsb_alpha.setSingleStep(0.100000000000000)
        self.dsb_alpha.setValue(0.300000000000000)

        self.horizontalLayout_6.addWidget(self.dsb_alpha)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_4.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_4.addWidget(self.btn_cancel)

        self.btn_apply = QPushButton(Dialog)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_4.addWidget(self.btn_apply)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Scatter Settings", None))
        self.lbl_point_size.setText(QCoreApplication.translate("Dialog", u"Point Size:", None))
        self.lbl_cmap_category.setText(QCoreApplication.translate("Dialog", u"ColorMap Category:", None))
        self.cmb_cmap_category.setItemText(0, QCoreApplication.translate("Dialog", u"Perceptually Uniform Sequential", None))
        self.cmb_cmap_category.setItemText(1, QCoreApplication.translate("Dialog", u"Sequential", None))
        self.cmb_cmap_category.setItemText(2, QCoreApplication.translate("Dialog", u"Sequential (2)", None))
        self.cmb_cmap_category.setItemText(3, QCoreApplication.translate("Dialog", u"Diverging", None))
        self.cmb_cmap_category.setItemText(4, QCoreApplication.translate("Dialog", u"Cyclic", None))
        self.cmb_cmap_category.setItemText(5, QCoreApplication.translate("Dialog", u"Qualitative", None))
        self.cmb_cmap_category.setItemText(6, QCoreApplication.translate("Dialog", u"Miscellaneous", None))

        self.lbl_cmap.setText(QCoreApplication.translate("Dialog", u"Colormap:", None))
        self.lbl_alpha.setText(QCoreApplication.translate("Dialog", u"Alpha:", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

