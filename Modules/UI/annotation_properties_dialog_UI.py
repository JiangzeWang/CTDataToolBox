# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotation_properties_dialog_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(299, 265)
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
        self.lbl_arrow_color = QLabel(Dialog)
        self.lbl_arrow_color.setObjectName(u"lbl_arrow_color")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_arrow_color.sizePolicy().hasHeightForWidth())
        self.lbl_arrow_color.setSizePolicy(sizePolicy1)
        self.lbl_arrow_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_5.addWidget(self.lbl_arrow_color)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_arrow_color_preview = QLabel(Dialog)
        self.lbl_arrow_color_preview.setObjectName(u"lbl_arrow_color_preview")
        sizePolicy1.setHeightForWidth(self.lbl_arrow_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_arrow_color_preview.setSizePolicy(sizePolicy1)
        self.lbl_arrow_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_arrow_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.lbl_arrow_color_preview)

        self.btn_arrow_color = QPushButton(Dialog)
        self.btn_arrow_color.setObjectName(u"btn_arrow_color")
        self.btn_arrow_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_3.addWidget(self.btn_arrow_color)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_annotation_size = QLabel(Dialog)
        self.lbl_annotation_size.setObjectName(u"lbl_annotation_size")
        self.lbl_annotation_size.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.lbl_annotation_size)

        self.spb_annotation_size = QSpinBox(Dialog)
        self.spb_annotation_size.setObjectName(u"spb_annotation_size")
        self.spb_annotation_size.setMinimumSize(QSize(0, 25))
        self.spb_annotation_size.setMaximumSize(QSize(16777215, 25))
        self.spb_annotation_size.setMaximum(100)
        self.spb_annotation_size.setValue(6)

        self.horizontalLayout_2.addWidget(self.spb_annotation_size)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_annotation_color = QLabel(Dialog)
        self.lbl_annotation_color.setObjectName(u"lbl_annotation_color")
        sizePolicy1.setHeightForWidth(self.lbl_annotation_color.sizePolicy().hasHeightForWidth())
        self.lbl_annotation_color.setSizePolicy(sizePolicy1)
        self.lbl_annotation_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_6.addWidget(self.lbl_annotation_color)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_annotation_color_preview = QLabel(Dialog)
        self.lbl_annotation_color_preview.setObjectName(u"lbl_annotation_color_preview")
        sizePolicy1.setHeightForWidth(self.lbl_annotation_color_preview.sizePolicy().hasHeightForWidth())
        self.lbl_annotation_color_preview.setSizePolicy(sizePolicy1)
        self.lbl_annotation_color_preview.setMinimumSize(QSize(25, 25))
        self.lbl_annotation_color_preview.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.lbl_annotation_color_preview)

        self.btn_annotation_color = QPushButton(Dialog)
        self.btn_annotation_color.setObjectName(u"btn_annotation_color")
        self.btn_annotation_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_7.addWidget(self.btn_annotation_color)


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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Label Settings", None))
        self.chk_show_arrow.setText(QCoreApplication.translate("Dialog", u"Show Label", None))
        self.lbl_arrow_color.setText(QCoreApplication.translate("Dialog", u"Arrow Color:", None))
        self.lbl_arrow_color_preview.setText("")
        self.btn_arrow_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.lbl_annotation_size.setText(QCoreApplication.translate("Dialog", u"Label Size:", None))
        self.lbl_annotation_color.setText(QCoreApplication.translate("Dialog", u"Label Color:", None))
        self.lbl_annotation_color_preview.setText("")
        self.btn_annotation_color.setText(QCoreApplication.translate("Dialog", u"Choose Color", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

