# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rectangle_properties_dialog_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(283, 248)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chk_show_rectangle = QCheckBox(Dialog)
        self.chk_show_rectangle.setObjectName(u"chk_show_rectangle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_show_rectangle.sizePolicy().hasHeightForWidth())
        self.chk_show_rectangle.setSizePolicy(sizePolicy)
        self.chk_show_rectangle.setMinimumSize(QSize(0, 25))
        self.chk_show_rectangle.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.chk_show_rectangle)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_line_style = QLabel(Dialog)
        self.lbl_line_style.setObjectName(u"lbl_line_style")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_line_style.sizePolicy().hasHeightForWidth())
        self.lbl_line_style.setSizePolicy(sizePolicy1)
        self.lbl_line_style.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_9.addWidget(self.lbl_line_style)

        self.cmb_line_style = QComboBox(Dialog)
        self.cmb_line_style.addItem("")
        self.cmb_line_style.addItem("")
        self.cmb_line_style.addItem("")
        self.cmb_line_style.addItem("")
        self.cmb_line_style.addItem("")
        self.cmb_line_style.setObjectName(u"cmb_line_style")
        sizePolicy1.setHeightForWidth(self.cmb_line_style.sizePolicy().hasHeightForWidth())
        self.cmb_line_style.setSizePolicy(sizePolicy1)
        self.cmb_line_style.setMinimumSize(QSize(0, 25))
        self.cmb_line_style.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_9.addWidget(self.cmb_line_style)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_line_width = QLabel(Dialog)
        self.lbl_line_width.setObjectName(u"lbl_line_width")
        self.lbl_line_width.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_8.addWidget(self.lbl_line_width)

        self.dsb_line_width = QDoubleSpinBox(Dialog)
        self.dsb_line_width.setObjectName(u"dsb_line_width")
        self.dsb_line_width.setMinimumSize(QSize(0, 25))
        self.dsb_line_width.setDecimals(1)
        self.dsb_line_width.setMinimum(0.000000000000000)
        self.dsb_line_width.setMaximum(10.000000000000000)
        self.dsb_line_width.setValue(1.000000000000000)

        self.horizontalLayout_8.addWidget(self.dsb_line_width)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_line_color = QLabel(Dialog)
        self.lbl_line_color.setObjectName(u"lbl_line_color")
        sizePolicy1.setHeightForWidth(self.lbl_line_color.sizePolicy().hasHeightForWidth())
        self.lbl_line_color.setSizePolicy(sizePolicy1)
        self.lbl_line_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_6.addWidget(self.lbl_line_color)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_line_color_preview = QLabel(Dialog)
        self.lbl_line_color_preview.setObjectName(u"lbl_line_color_preview")
        sizePolicy1.setHeightForWidth(self.lbl_line_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_line_color_preview.setSizePolicy(sizePolicy1)
        self.lbl_line_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_line_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.lbl_line_color_preview)

        self.btn_line_color = QPushButton(Dialog)
        self.btn_line_color.setObjectName(u"btn_line_color")
        self.btn_line_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_7.addWidget(self.btn_line_color)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Rectangle Border Settings", None))
        self.chk_show_rectangle.setText(QCoreApplication.translate("Dialog", u"Show Rectangle Border", None))
        self.lbl_line_style.setText(QCoreApplication.translate("Dialog", u"Border Style:", None))
        self.cmb_line_style.setItemText(0, QCoreApplication.translate("Dialog", u"Solid", None))
        self.cmb_line_style.setItemText(1, QCoreApplication.translate("Dialog", u"Dashed", None))
        self.cmb_line_style.setItemText(2, QCoreApplication.translate("Dialog", u"Dotted", None))
        self.cmb_line_style.setItemText(3, QCoreApplication.translate("Dialog", u"Dash-dot", None))
        self.cmb_line_style.setItemText(4, QCoreApplication.translate("Dialog", u"None", None))

        self.lbl_line_width.setText(QCoreApplication.translate("Dialog", u"Border Width:", None))
        self.lbl_line_color.setText(QCoreApplication.translate("Dialog", u"Border Color:", None))
        self.lbl_line_color_preview.setText("")
        self.btn_line_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

