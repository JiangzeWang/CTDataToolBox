# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arrow_properties_dialog_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(332, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chk_show_arrow = QCheckBox(Dialog)
        self.chk_show_arrow.setObjectName(u"chk_show_arrow")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_show_arrow.sizePolicy().hasHeightForWidth())
        self.chk_show_arrow.setSizePolicy(sizePolicy)
        self.chk_show_arrow.setMinimumSize(QSize(0, 25))
        self.chk_show_arrow.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.chk_show_arrow)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_color = QLabel(Dialog)
        self.lbl_color.setObjectName(u"lbl_color")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_color.sizePolicy().hasHeightForWidth())
        self.lbl_color.setSizePolicy(sizePolicy1)
        self.lbl_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_5.addWidget(self.lbl_color)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_color_preview = QLabel(Dialog)
        self.lbl_color_preview.setObjectName(u"lbl_color_preview")
        sizePolicy1.setHeightForWidth(self.lbl_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_color_preview.setSizePolicy(sizePolicy1)
        self.lbl_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.lbl_color_preview)

        self.btn_color = QPushButton(Dialog)
        self.btn_color.setObjectName(u"btn_color")
        self.btn_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_3.addWidget(self.btn_color)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lbl_width = QLabel(Dialog)
        self.lbl_width.setObjectName(u"lbl_width")
        self.lbl_width.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_13.addWidget(self.lbl_width)

        self.dsb_width = QDoubleSpinBox(Dialog)
        self.dsb_width.setObjectName(u"dsb_width")
        self.dsb_width.setMinimumSize(QSize(0, 25))
        self.dsb_width.setDecimals(1)
        self.dsb_width.setMinimum(0.000000000000000)
        self.dsb_width.setMaximum(100.000000000000000)
        self.dsb_width.setValue(1.000000000000000)

        self.horizontalLayout_13.addWidget(self.dsb_width)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lbl_headwidth = QLabel(Dialog)
        self.lbl_headwidth.setObjectName(u"lbl_headwidth")
        self.lbl_headwidth.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_14.addWidget(self.lbl_headwidth)

        self.dsb_headwidth = QDoubleSpinBox(Dialog)
        self.dsb_headwidth.setObjectName(u"dsb_headwidth")
        self.dsb_headwidth.setMinimumSize(QSize(0, 25))
        self.dsb_headwidth.setDecimals(1)
        self.dsb_headwidth.setMinimum(0.000000000000000)
        self.dsb_headwidth.setMaximum(100.000000000000000)
        self.dsb_headwidth.setValue(1.000000000000000)

        self.horizontalLayout_14.addWidget(self.dsb_headwidth)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lbl_headlength = QLabel(Dialog)
        self.lbl_headlength.setObjectName(u"lbl_headlength")
        self.lbl_headlength.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_15.addWidget(self.lbl_headlength)

        self.dsb_headlength = QDoubleSpinBox(Dialog)
        self.dsb_headlength.setObjectName(u"dsb_headlength")
        self.dsb_headlength.setMinimumSize(QSize(0, 25))
        self.dsb_headlength.setDecimals(1)
        self.dsb_headlength.setMinimum(0.000000000000000)
        self.dsb_headlength.setMaximum(100.000000000000000)
        self.dsb_headlength.setValue(1.000000000000000)

        self.horizontalLayout_15.addWidget(self.dsb_headlength)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_15)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Arrow Settings", None))
        self.chk_show_arrow.setText(QCoreApplication.translate("Dialog", u"Show Arrow", None))
        self.lbl_color.setText(QCoreApplication.translate("Dialog", u"Color:", None))
        self.lbl_color_preview.setText("")
        self.btn_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.lbl_width.setText(QCoreApplication.translate("Dialog", u"Width:", None))
        self.lbl_headwidth.setText(QCoreApplication.translate("Dialog", u"Headwidth:", None))
        self.lbl_headlength.setText(QCoreApplication.translate("Dialog", u"Headlength:", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

