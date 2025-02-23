# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ternary_properties_dialog_UI.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(339, 348)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_point_style = QLabel(self.groupBox)
        self.lbl_point_style.setObjectName(u"lbl_point_style")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_point_style.sizePolicy().hasHeightForWidth())
        self.lbl_point_style.setSizePolicy(sizePolicy)
        self.lbl_point_style.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.lbl_point_style)

        self.cmb_marker_style = QComboBox(self.groupBox)
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.addItem("")
        self.cmb_marker_style.setObjectName(u"cmb_marker_style")
        sizePolicy.setHeightForWidth(self.cmb_marker_style.sizePolicy().hasHeightForWidth())
        self.cmb_marker_style.setSizePolicy(sizePolicy)
        self.cmb_marker_style.setMinimumSize(QSize(0, 25))
        self.cmb_marker_style.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.cmb_marker_style)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_point_size = QLabel(self.groupBox)
        self.lbl_point_size.setObjectName(u"lbl_point_size")
        self.lbl_point_size.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.lbl_point_size)

        self.spb_marker_size = QSpinBox(self.groupBox)
        self.spb_marker_size.setObjectName(u"spb_marker_size")
        self.spb_marker_size.setMinimumSize(QSize(0, 25))
        self.spb_marker_size.setMaximumSize(QSize(16777215, 25))
        self.spb_marker_size.setMaximum(100)
        self.spb_marker_size.setValue(6)

        self.horizontalLayout_2.addWidget(self.spb_marker_size)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_point_color = QLabel(self.groupBox)
        self.lbl_point_color.setObjectName(u"lbl_point_color")
        sizePolicy.setHeightForWidth(self.lbl_point_color.sizePolicy().hasHeightForWidth())
        self.lbl_point_color.setSizePolicy(sizePolicy)
        self.lbl_point_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_6.addWidget(self.lbl_point_color)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_point_color_preview = QLabel(self.groupBox)
        self.lbl_point_color_preview.setObjectName(u"lbl_point_color_preview")
        sizePolicy.setHeightForWidth(self.lbl_point_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_point_color_preview.setSizePolicy(sizePolicy)
        self.lbl_point_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_point_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.lbl_point_color_preview)

        self.btn_point_color = QPushButton(self.groupBox)
        self.btn_point_color.setObjectName(u"btn_point_color")
        self.btn_point_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_7.addWidget(self.btn_point_color)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_alpha = QLabel(self.groupBox)
        self.lbl_alpha.setObjectName(u"lbl_alpha")
        self.lbl_alpha.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_8.addWidget(self.lbl_alpha)

        self.dsb_alpha = QDoubleSpinBox(self.groupBox)
        self.dsb_alpha.setObjectName(u"dsb_alpha")
        self.dsb_alpha.setMinimumSize(QSize(0, 25))
        self.dsb_alpha.setMaximumSize(QSize(16777215, 25))
        self.dsb_alpha.setDecimals(1)
        self.dsb_alpha.setMaximum(1.000000000000000)
        self.dsb_alpha.setSingleStep(0.100000000000000)
        self.dsb_alpha.setValue(0.300000000000000)

        self.horizontalLayout_8.addWidget(self.dsb_alpha)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.chk_show_gridlines = QCheckBox(self.groupBox_2)
        self.chk_show_gridlines.setObjectName(u"chk_show_gridlines")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chk_show_gridlines.sizePolicy().hasHeightForWidth())
        self.chk_show_gridlines.setSizePolicy(sizePolicy1)
        self.chk_show_gridlines.setMinimumSize(QSize(0, 25))
        self.chk_show_gridlines.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.chk_show_gridlines)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_gridline_width = QLabel(self.groupBox_2)
        self.lbl_gridline_width.setObjectName(u"lbl_gridline_width")
        self.lbl_gridline_width.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_9.addWidget(self.lbl_gridline_width)

        self.dsb_gridline_width = QDoubleSpinBox(self.groupBox_2)
        self.dsb_gridline_width.setObjectName(u"dsb_gridline_width")
        self.dsb_gridline_width.setMinimumSize(QSize(0, 25))
        self.dsb_gridline_width.setDecimals(1)
        self.dsb_gridline_width.setMinimum(0.000000000000000)
        self.dsb_gridline_width.setMaximum(10.000000000000000)
        self.dsb_gridline_width.setValue(1.000000000000000)

        self.horizontalLayout_9.addWidget(self.dsb_gridline_width)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_gridlines_color = QLabel(self.groupBox_2)
        self.lbl_gridlines_color.setObjectName(u"lbl_gridlines_color")
        sizePolicy.setHeightForWidth(self.lbl_gridlines_color.sizePolicy().hasHeightForWidth())
        self.lbl_gridlines_color.setSizePolicy(sizePolicy)
        self.lbl_gridlines_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_5.addWidget(self.lbl_gridlines_color)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_gridlines_color_preview = QLabel(self.groupBox_2)
        self.lbl_gridlines_color_preview.setObjectName(u"lbl_gridlines_color_preview")
        sizePolicy.setHeightForWidth(self.lbl_gridlines_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_gridlines_color_preview.setSizePolicy(sizePolicy)
        self.lbl_gridlines_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_gridlines_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.lbl_gridlines_color_preview)

        self.btn_gridlines_color = QPushButton(self.groupBox_2)
        self.btn_gridlines_color.setObjectName(u"btn_gridlines_color")
        self.btn_gridlines_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_3.addWidget(self.btn_gridlines_color)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.groupBox_2)

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

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        self.cmb_marker_style.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Ternary Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Scatter", None))
        self.lbl_point_style.setText(QCoreApplication.translate("Dialog", u"Point Style:", None))
        self.cmb_marker_style.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.cmb_marker_style.setItemText(1, QCoreApplication.translate("Dialog", u"Square", None))
        self.cmb_marker_style.setItemText(2, QCoreApplication.translate("Dialog", u"Circle", None))
        self.cmb_marker_style.setItemText(3, QCoreApplication.translate("Dialog", u"Triangle_up", None))
        self.cmb_marker_style.setItemText(4, QCoreApplication.translate("Dialog", u"Triangle_down", None))
        self.cmb_marker_style.setItemText(5, QCoreApplication.translate("Dialog", u"Diamond", None))
        self.cmb_marker_style.setItemText(6, QCoreApplication.translate("Dialog", u"Triangle_left", None))
        self.cmb_marker_style.setItemText(7, QCoreApplication.translate("Dialog", u"Triangle_right", None))
        self.cmb_marker_style.setItemText(8, QCoreApplication.translate("Dialog", u"Hexagon", None))
        self.cmb_marker_style.setItemText(9, QCoreApplication.translate("Dialog", u"Star", None))
        self.cmb_marker_style.setItemText(10, QCoreApplication.translate("Dialog", u"Pentagon", None))
        self.cmb_marker_style.setItemText(11, QCoreApplication.translate("Dialog", u"Plus", None))
        self.cmb_marker_style.setItemText(12, QCoreApplication.translate("Dialog", u"X", None))

        self.lbl_point_size.setText(QCoreApplication.translate("Dialog", u"Point Size:", None))
        self.lbl_point_color.setText(QCoreApplication.translate("Dialog", u"Point Color:", None))
        self.lbl_point_color_preview.setText("")
        self.btn_point_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.lbl_alpha.setText(QCoreApplication.translate("Dialog", u"Alpha:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Gridlines", None))
        self.chk_show_gridlines.setText(QCoreApplication.translate("Dialog", u"Show Gridlines", None))
        self.lbl_gridline_width.setText(QCoreApplication.translate("Dialog", u"Gridline Width:", None))
        self.lbl_gridlines_color.setText(QCoreApplication.translate("Dialog", u"Gridlines Color:", None))
        self.lbl_gridlines_color_preview.setText("")
        self.btn_gridlines_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

