# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'line_Properties_dialog_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QDoubleSpinBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(342, 294)
        Dialog.setStyleSheet(u"*{  \n"
"    font-size:13px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_symbol = QWidget()
        self.tab_symbol.setObjectName(u"tab_symbol")
        self.verticalLayout = QVBoxLayout(self.tab_symbol)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chk_show_points = QCheckBox(self.tab_symbol)
        self.chk_show_points.setObjectName(u"chk_show_points")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_show_points.sizePolicy().hasHeightForWidth())
        self.chk_show_points.setSizePolicy(sizePolicy)
        self.chk_show_points.setMinimumSize(QSize(0, 25))
        self.chk_show_points.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.chk_show_points)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_point_style = QLabel(self.tab_symbol)
        self.lbl_point_style.setObjectName(u"lbl_point_style")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_point_style.sizePolicy().hasHeightForWidth())
        self.lbl_point_style.setSizePolicy(sizePolicy1)
        self.lbl_point_style.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.lbl_point_style)

        self.cmb_marker_style = QComboBox(self.tab_symbol)
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
        sizePolicy1.setHeightForWidth(self.cmb_marker_style.sizePolicy().hasHeightForWidth())
        self.cmb_marker_style.setSizePolicy(sizePolicy1)
        self.cmb_marker_style.setMinimumSize(QSize(0, 25))
        self.cmb_marker_style.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.cmb_marker_style)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_point_size = QLabel(self.tab_symbol)
        self.lbl_point_size.setObjectName(u"lbl_point_size")
        self.lbl_point_size.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.lbl_point_size)

        self.spb_marker_size = QSpinBox(self.tab_symbol)
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
        self.lbl_fill_color = QLabel(self.tab_symbol)
        self.lbl_fill_color.setObjectName(u"lbl_fill_color")
        sizePolicy1.setHeightForWidth(self.lbl_fill_color.sizePolicy().hasHeightForWidth())
        self.lbl_fill_color.setSizePolicy(sizePolicy1)
        self.lbl_fill_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_5.addWidget(self.lbl_fill_color)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_fill_color_preview = QLabel(self.tab_symbol)
        self.lbl_fill_color_preview.setObjectName(u"lbl_fill_color_preview")
        sizePolicy1.setHeightForWidth(self.lbl_fill_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_fill_color_preview.setSizePolicy(sizePolicy1)
        self.lbl_fill_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_fill_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.lbl_fill_color_preview)

        self.btn_fill_color = QPushButton(self.tab_symbol)
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
        self.lbl_edge_color = QLabel(self.tab_symbol)
        self.lbl_edge_color.setObjectName(u"lbl_edge_color")
        sizePolicy1.setHeightForWidth(self.lbl_edge_color.sizePolicy().hasHeightForWidth())
        self.lbl_edge_color.setSizePolicy(sizePolicy1)
        self.lbl_edge_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_10.addWidget(self.lbl_edge_color)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_edge_color_preview = QLabel(self.tab_symbol)
        self.lbl_edge_color_preview.setObjectName(u"lbl_edge_color_preview")
        sizePolicy1.setHeightForWidth(self.lbl_edge_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_edge_color_preview.setSizePolicy(sizePolicy1)
        self.lbl_edge_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_edge_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.lbl_edge_color_preview)

        self.btn_edge_color = QPushButton(self.tab_symbol)
        self.btn_edge_color.setObjectName(u"btn_edge_color")
        self.btn_edge_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_11.addWidget(self.btn_edge_color)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.tabWidget.addTab(self.tab_symbol, "")
        self.tab_line = QWidget()
        self.tab_line.setObjectName(u"tab_line")
        self.verticalLayout_3 = QVBoxLayout(self.tab_line)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.chk_show_line = QCheckBox(self.tab_line)
        self.chk_show_line.setObjectName(u"chk_show_line")
        sizePolicy.setHeightForWidth(self.chk_show_line.sizePolicy().hasHeightForWidth())
        self.chk_show_line.setSizePolicy(sizePolicy)
        self.chk_show_line.setMinimumSize(QSize(0, 25))
        self.chk_show_line.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_3.addWidget(self.chk_show_line)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_line_style = QLabel(self.tab_line)
        self.lbl_line_style.setObjectName(u"lbl_line_style")
        sizePolicy1.setHeightForWidth(self.lbl_line_style.sizePolicy().hasHeightForWidth())
        self.lbl_line_style.setSizePolicy(sizePolicy1)
        self.lbl_line_style.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_9.addWidget(self.lbl_line_style)

        self.cmb_line_style = QComboBox(self.tab_line)
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

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_line_width = QLabel(self.tab_line)
        self.lbl_line_width.setObjectName(u"lbl_line_width")
        self.lbl_line_width.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_8.addWidget(self.lbl_line_width)

        self.dsb_line_width = QDoubleSpinBox(self.tab_line)
        self.dsb_line_width.setObjectName(u"dsb_line_width")
        self.dsb_line_width.setMinimumSize(QSize(0, 25))
        self.dsb_line_width.setDecimals(1)
        self.dsb_line_width.setMinimum(0.000000000000000)
        self.dsb_line_width.setMaximum(10.000000000000000)
        self.dsb_line_width.setValue(1.000000000000000)

        self.horizontalLayout_8.addWidget(self.dsb_line_width)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_line_color = QLabel(self.tab_line)
        self.lbl_line_color.setObjectName(u"lbl_line_color")
        sizePolicy1.setHeightForWidth(self.lbl_line_color.sizePolicy().hasHeightForWidth())
        self.lbl_line_color.setSizePolicy(sizePolicy1)
        self.lbl_line_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_6.addWidget(self.lbl_line_color)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_line_color_preview = QLabel(self.tab_line)
        self.lbl_line_color_preview.setObjectName(u"lbl_line_color_preview")
        sizePolicy1.setHeightForWidth(self.lbl_line_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_line_color_preview.setSizePolicy(sizePolicy1)
        self.lbl_line_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_line_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.lbl_line_color_preview)

        self.btn_line_color = QPushButton(self.tab_line)
        self.btn_line_color.setObjectName(u"btn_line_color")
        self.btn_line_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_7.addWidget(self.btn_line_color)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_line, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

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

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)
        self.cmb_marker_style.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Line Settings", None))
        self.chk_show_points.setText(QCoreApplication.translate("Dialog", u"Show Points", None))
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
        self.lbl_fill_color.setText(QCoreApplication.translate("Dialog", u"Fill Color:", None))
        self.lbl_fill_color_preview.setText("")
        self.btn_fill_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.lbl_edge_color.setText(QCoreApplication.translate("Dialog", u"Edge Color:", None))
        self.lbl_edge_color_preview.setText("")
        self.btn_edge_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_symbol), QCoreApplication.translate("Dialog", u"Symbol", None))
        self.chk_show_line.setText(QCoreApplication.translate("Dialog", u"Show Line", None))
        self.lbl_line_style.setText(QCoreApplication.translate("Dialog", u"Line Style:", None))
        self.cmb_line_style.setItemText(0, QCoreApplication.translate("Dialog", u"Solid", None))
        self.cmb_line_style.setItemText(1, QCoreApplication.translate("Dialog", u"Dashed", None))
        self.cmb_line_style.setItemText(2, QCoreApplication.translate("Dialog", u"Dotted", None))
        self.cmb_line_style.setItemText(3, QCoreApplication.translate("Dialog", u"Dash-dot", None))
        self.cmb_line_style.setItemText(4, QCoreApplication.translate("Dialog", u"None", None))

        self.lbl_line_width.setText(QCoreApplication.translate("Dialog", u"Line Width:", None))
        self.lbl_line_color.setText(QCoreApplication.translate("Dialog", u"Line Color:", None))
        self.lbl_line_color_preview.setText("")
        self.btn_line_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_line), QCoreApplication.translate("Dialog", u"Line", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

