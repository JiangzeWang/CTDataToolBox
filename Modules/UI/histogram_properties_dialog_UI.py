# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'histogram_properties_dialog_UI.ui'
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
        Dialog.resize(332, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chk_show_histogram = QCheckBox(Dialog)
        self.chk_show_histogram.setObjectName(u"chk_show_histogram")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_show_histogram.sizePolicy().hasHeightForWidth())
        self.chk_show_histogram.setSizePolicy(sizePolicy)
        self.chk_show_histogram.setMinimumSize(QSize(0, 25))
        self.chk_show_histogram.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.chk_show_histogram)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_fill_color = QLabel(Dialog)
        self.lbl_fill_color.setObjectName(u"lbl_fill_color")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_fill_color.sizePolicy().hasHeightForWidth())
        self.lbl_fill_color.setSizePolicy(sizePolicy1)
        self.lbl_fill_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_5.addWidget(self.lbl_fill_color)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_fill_color_preview = QLabel(Dialog)
        self.lbl_fill_color_preview.setObjectName(u"lbl_fill_color_preview")
        sizePolicy1.setHeightForWidth(self.lbl_fill_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_fill_color_preview.setSizePolicy(sizePolicy1)
        self.lbl_fill_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_fill_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.lbl_fill_color_preview)

        self.btn_fill_color = QPushButton(Dialog)
        self.btn_fill_color.setObjectName(u"btn_fill_color")
        self.btn_fill_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_3.addWidget(self.btn_fill_color)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_border_color = QLabel(Dialog)
        self.lbl_border_color.setObjectName(u"lbl_border_color")
        sizePolicy1.setHeightForWidth(self.lbl_border_color.sizePolicy().hasHeightForWidth())
        self.lbl_border_color.setSizePolicy(sizePolicy1)
        self.lbl_border_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_10.addWidget(self.lbl_border_color)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_border_color_preview = QLabel(Dialog)
        self.lbl_border_color_preview.setObjectName(u"lbl_border_color_preview")
        sizePolicy1.setHeightForWidth(self.lbl_border_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_border_color_preview.setSizePolicy(sizePolicy1)
        self.lbl_border_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_border_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.lbl_border_color_preview)

        self.btn_border_color = QPushButton(Dialog)
        self.btn_border_color.setObjectName(u"btn_border_color")
        self.btn_border_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_11.addWidget(self.btn_border_color)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lbl_Border_style = QLabel(Dialog)
        self.lbl_Border_style.setObjectName(u"lbl_Border_style")
        sizePolicy1.setHeightForWidth(self.lbl_Border_style.sizePolicy().hasHeightForWidth())
        self.lbl_Border_style.setSizePolicy(sizePolicy1)
        self.lbl_Border_style.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_12.addWidget(self.lbl_Border_style)

        self.cmb_border_style = QComboBox(Dialog)
        self.cmb_border_style.addItem("")
        self.cmb_border_style.addItem("")
        self.cmb_border_style.addItem("")
        self.cmb_border_style.addItem("")
        self.cmb_border_style.addItem("")
        self.cmb_border_style.setObjectName(u"cmb_border_style")
        sizePolicy1.setHeightForWidth(self.cmb_border_style.sizePolicy().hasHeightForWidth())
        self.cmb_border_style.setSizePolicy(sizePolicy1)
        self.cmb_border_style.setMinimumSize(QSize(0, 25))
        self.cmb_border_style.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_12.addWidget(self.cmb_border_style)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lbl_border_width = QLabel(Dialog)
        self.lbl_border_width.setObjectName(u"lbl_border_width")
        self.lbl_border_width.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_13.addWidget(self.lbl_border_width)

        self.dsb_border_width = QDoubleSpinBox(Dialog)
        self.dsb_border_width.setObjectName(u"dsb_border_width")
        self.dsb_border_width.setMinimumSize(QSize(0, 25))
        self.dsb_border_width.setDecimals(1)
        self.dsb_border_width.setMinimum(0.000000000000000)
        self.dsb_border_width.setMaximum(10.000000000000000)
        self.dsb_border_width.setValue(1.000000000000000)

        self.horizontalLayout_13.addWidget(self.dsb_border_width)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_alpha = QLabel(Dialog)
        self.lbl_alpha.setObjectName(u"lbl_alpha")
        self.lbl_alpha.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_8.addWidget(self.lbl_alpha)

        self.dsb_alpha = QDoubleSpinBox(Dialog)
        self.dsb_alpha.setObjectName(u"dsb_alpha")
        self.dsb_alpha.setMinimumSize(QSize(0, 25))
        self.dsb_alpha.setMaximumSize(QSize(16777215, 25))
        self.dsb_alpha.setDecimals(1)
        self.dsb_alpha.setMaximum(1.000000000000000)
        self.dsb_alpha.setSingleStep(0.100000000000000)
        self.dsb_alpha.setValue(0.700000000000000)

        self.horizontalLayout_8.addWidget(self.dsb_alpha)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Histogram Settings", None))
        self.chk_show_histogram.setText(QCoreApplication.translate("Dialog", u"Show Histogram", None))
        self.lbl_fill_color.setText(QCoreApplication.translate("Dialog", u"Fill Color:", None))
        self.lbl_fill_color_preview.setText("")
        self.btn_fill_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.lbl_border_color.setText(QCoreApplication.translate("Dialog", u"Border Color:", None))
        self.lbl_border_color_preview.setText("")
        self.btn_border_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.lbl_Border_style.setText(QCoreApplication.translate("Dialog", u"Border Style:", None))
        self.cmb_border_style.setItemText(0, QCoreApplication.translate("Dialog", u"Solid", None))
        self.cmb_border_style.setItemText(1, QCoreApplication.translate("Dialog", u"Dashed", None))
        self.cmb_border_style.setItemText(2, QCoreApplication.translate("Dialog", u"Dotted", None))
        self.cmb_border_style.setItemText(3, QCoreApplication.translate("Dialog", u"Dash-dot", None))
        self.cmb_border_style.setItemText(4, QCoreApplication.translate("Dialog", u"None", None))

        self.lbl_border_width.setText(QCoreApplication.translate("Dialog", u"Border Width:", None))
        self.lbl_alpha.setText(QCoreApplication.translate("Dialog", u"Alpha:", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

