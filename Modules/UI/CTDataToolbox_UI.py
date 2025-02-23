# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CTDataToolbox_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)
import image_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(783, 589)
        Form.setStyleSheet(u"*{  \n"
"    font-size:13px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.csd = QTabWidget(Form)
        self.csd.setObjectName(u"csd")
        self.csd.setMinimumSize(QSize(0, 0))
        self.tbw_CSD = QWidget()
        self.tbw_CSD.setObjectName(u"tbw_CSD")
        self.verticalLayout_6 = QVBoxLayout(self.tbw_CSD)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.data_and_stat = QHBoxLayout()
        self.data_and_stat.setSpacing(9)
        self.data_and_stat.setObjectName(u"data_and_stat")
        self.gb_data_input = QGroupBox(self.tbw_CSD)
        self.gb_data_input.setObjectName(u"gb_data_input")
        self.gb_data_input.setMinimumSize(QSize(330, 0))
        self.verticalLayout_2 = QVBoxLayout(self.gb_data_input)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_load_file = QPushButton(self.gb_data_input)
        self.btn_load_file.setObjectName(u"btn_load_file")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_load_file.sizePolicy().hasHeightForWidth())
        self.btn_load_file.setSizePolicy(sizePolicy)
        self.btn_load_file.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btn_load_file)

        self.btn_clear_data = QPushButton(self.gb_data_input)
        self.btn_clear_data.setObjectName(u"btn_clear_data")
        self.btn_clear_data.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btn_clear_data)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_unit_input = QLabel(self.gb_data_input)
        self.lbl_unit_input.setObjectName(u"lbl_unit_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_unit_input.sizePolicy().hasHeightForWidth())
        self.lbl_unit_input.setSizePolicy(sizePolicy1)
        self.lbl_unit_input.setMinimumSize(QSize(140, 30))

        self.horizontalLayout_2.addWidget(self.lbl_unit_input)

        self.cmb_unit_input = QComboBox(self.gb_data_input)
        self.cmb_unit_input.addItem("")
        self.cmb_unit_input.addItem("")
        self.cmb_unit_input.addItem("")
        self.cmb_unit_input.addItem("")
        self.cmb_unit_input.addItem("")
        self.cmb_unit_input.addItem("")
        self.cmb_unit_input.setObjectName(u"cmb_unit_input")
        self.cmb_unit_input.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.cmb_unit_input)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_spatial_resolution = QLabel(self.gb_data_input)
        self.lbl_spatial_resolution.setObjectName(u"lbl_spatial_resolution")
        sizePolicy1.setHeightForWidth(self.lbl_spatial_resolution.sizePolicy().hasHeightForWidth())
        self.lbl_spatial_resolution.setSizePolicy(sizePolicy1)
        self.lbl_spatial_resolution.setMinimumSize(QSize(140, 30))

        self.horizontalLayout_3.addWidget(self.lbl_spatial_resolution)

        self.le_voxel_size = QLineEdit(self.gb_data_input)
        self.le_voxel_size.setObjectName(u"le_voxel_size")
        self.le_voxel_size.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.le_voxel_size)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.gb_data_input)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(140, 30))

        self.horizontalLayout_4.addWidget(self.label)

        self.le_volume3d = QLineEdit(self.gb_data_input)
        self.le_volume3d.setObjectName(u"le_volume3d")
        self.le_volume3d.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.le_volume3d)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_unit_display = QLabel(self.gb_data_input)
        self.lbl_unit_display.setObjectName(u"lbl_unit_display")
        sizePolicy1.setHeightForWidth(self.lbl_unit_display.sizePolicy().hasHeightForWidth())
        self.lbl_unit_display.setSizePolicy(sizePolicy1)
        self.lbl_unit_display.setMinimumSize(QSize(140, 30))

        self.horizontalLayout_5.addWidget(self.lbl_unit_display)

        self.cmb_unit_display = QComboBox(self.gb_data_input)
        self.cmb_unit_display.addItem("")
        self.cmb_unit_display.addItem("")
        self.cmb_unit_display.addItem("")
        self.cmb_unit_display.addItem("")
        self.cmb_unit_display.addItem("")
        self.cmb_unit_display.addItem("")
        self.cmb_unit_display.setObjectName(u"cmb_unit_display")
        self.cmb_unit_display.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.cmb_unit_display)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)

        self.data_and_stat.addWidget(self.gb_data_input)

        self.gb_statistics = QGroupBox(self.tbw_CSD)
        self.gb_statistics.setObjectName(u"gb_statistics")
        self.verticalLayout_5 = QVBoxLayout(self.gb_statistics)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txb_stat = QTextBrowser(self.gb_statistics)
        self.txb_stat.setObjectName(u"txb_stat")

        self.verticalLayout_3.addWidget(self.txb_stat)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_get_para = QPushButton(self.gb_statistics)
        self.btn_get_para.setObjectName(u"btn_get_para")
        self.btn_get_para.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.btn_get_para)

        self.btn_save_para = QPushButton(self.gb_statistics)
        self.btn_save_para.setObjectName(u"btn_save_para")
        self.btn_save_para.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.btn_save_para)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.data_and_stat.addWidget(self.gb_statistics)

        self.data_and_stat.setStretch(0, 4)
        self.data_and_stat.setStretch(1, 5)

        self.verticalLayout_4.addLayout(self.data_and_stat)

        self.size_scale = QHBoxLayout()
        self.size_scale.setSpacing(9)
        self.size_scale.setObjectName(u"size_scale")
        self.gb_size_scale_csd = QGroupBox(self.tbw_CSD)
        self.gb_size_scale_csd.setObjectName(u"gb_size_scale_csd")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gb_size_scale_csd.sizePolicy().hasHeightForWidth())
        self.gb_size_scale_csd.setSizePolicy(sizePolicy2)
        self.gb_size_scale_csd.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_11 = QHBoxLayout(self.gb_size_scale_csd)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tbw_size_scale_csd = QTabWidget(self.gb_size_scale_csd)
        self.tbw_size_scale_csd.setObjectName(u"tbw_size_scale_csd")
        self.tbw_log10 = QWidget()
        self.tbw_log10.setObjectName(u"tbw_log10")
        self.horizontalLayout_9 = QHBoxLayout(self.tbw_log10)
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 20, 10, 20)
        self.lbl_log10 = QLabel(self.tbw_log10)
        self.lbl_log10.setObjectName(u"lbl_log10")
        self.lbl_log10.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_9.addWidget(self.lbl_log10)

        self.spb_log10 = QSpinBox(self.tbw_log10)
        self.spb_log10.setObjectName(u"spb_log10")
        self.spb_log10.setMinimumSize(QSize(0, 30))
        self.spb_log10.setMinimum(2)
        self.spb_log10.setMaximum(10)
        self.spb_log10.setValue(5)

        self.horizontalLayout_9.addWidget(self.spb_log10)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)
        self.tbw_size_scale_csd.addTab(self.tbw_log10, "")
        self.tbw_log2 = QWidget()
        self.tbw_log2.setObjectName(u"tbw_log2")
        self.horizontalLayout_8 = QHBoxLayout(self.tbw_log2)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 20, 10, 20)
        self.lbl_log2 = QLabel(self.tbw_log2)
        self.lbl_log2.setObjectName(u"lbl_log2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_log2.sizePolicy().hasHeightForWidth())
        self.lbl_log2.setSizePolicy(sizePolicy3)
        self.lbl_log2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.lbl_log2)

        self.spb_log2 = QSpinBox(self.tbw_log2)
        self.spb_log2.setObjectName(u"spb_log2")
        self.spb_log2.setMinimumSize(QSize(0, 30))
        self.spb_log2.setMinimum(1)
        self.spb_log2.setMaximum(3)

        self.horizontalLayout_8.addWidget(self.spb_log2)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.tbw_size_scale_csd.addTab(self.tbw_log2, "")
        self.tbw_linear = QWidget()
        self.tbw_linear.setObjectName(u"tbw_linear")
        self.horizontalLayout_7 = QHBoxLayout(self.tbw_linear)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 20, 10, 20)
        self.lbl_linear = QLabel(self.tbw_linear)
        self.lbl_linear.setObjectName(u"lbl_linear")
        sizePolicy3.setHeightForWidth(self.lbl_linear.sizePolicy().hasHeightForWidth())
        self.lbl_linear.setSizePolicy(sizePolicy3)
        self.lbl_linear.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_7.addWidget(self.lbl_linear)

        self.widget = QWidget(self.tbw_linear)
        self.widget.setObjectName(u"widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.widget.setMinimumSize(QSize(150, 30))
        self.widget.setMaximumSize(QSize(150, 30))
        self.le_linear = QLineEdit(self.widget)
        self.le_linear.setObjectName(u"le_linear")
        self.le_linear.setGeometry(QRect(0, 0, 150, 30))
        self.le_linear.setMinimumSize(QSize(0, 30))
        self.lbl_unit = QLabel(self.widget)
        self.lbl_unit.setObjectName(u"lbl_unit")
        self.lbl_unit.setGeometry(QRect(120, 0, 31, 30))
        self.lbl_unit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_7.addWidget(self.widget)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.tbw_size_scale_csd.addTab(self.tbw_linear, "")

        self.horizontalLayout_11.addWidget(self.tbw_size_scale_csd)


        self.size_scale.addWidget(self.gb_size_scale_csd)

        self.gb_size_scale_fre = QGroupBox(self.tbw_CSD)
        self.gb_size_scale_fre.setObjectName(u"gb_size_scale_fre")
        self.horizontalLayout_14 = QHBoxLayout(self.gb_size_scale_fre)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.tbw_size_scale_fre = QTabWidget(self.gb_size_scale_fre)
        self.tbw_size_scale_fre.setObjectName(u"tbw_size_scale_fre")
        self.twb_bin_size = QWidget()
        self.twb_bin_size.setObjectName(u"twb_bin_size")
        self.horizontalLayout_12 = QHBoxLayout(self.twb_bin_size)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 20, 10, 20)
        self.lbl_bin_size = QLabel(self.twb_bin_size)
        self.lbl_bin_size.setObjectName(u"lbl_bin_size")
        sizePolicy3.setHeightForWidth(self.lbl_bin_size.sizePolicy().hasHeightForWidth())
        self.lbl_bin_size.setSizePolicy(sizePolicy3)
        self.lbl_bin_size.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.lbl_bin_size)

        self.widget_2 = QWidget(self.twb_bin_size)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.widget_2.setMinimumSize(QSize(150, 30))
        self.widget_2.setMaximumSize(QSize(150, 30))
        self.le_bin_size = QLineEdit(self.widget_2)
        self.le_bin_size.setObjectName(u"le_bin_size")
        self.le_bin_size.setGeometry(QRect(0, 0, 150, 30))
        self.le_bin_size.setMinimumSize(QSize(0, 30))
        self.lbl_unit_2 = QLabel(self.widget_2)
        self.lbl_unit_2.setObjectName(u"lbl_unit_2")
        self.lbl_unit_2.setGeometry(QRect(120, 0, 31, 30))
        self.lbl_unit_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.widget_2)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 2)
        self.tbw_size_scale_fre.addTab(self.twb_bin_size, "")
        self.twb_num_bins = QWidget()
        self.twb_num_bins.setObjectName(u"twb_num_bins")
        self.horizontalLayout_13 = QHBoxLayout(self.twb_num_bins)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 20, 10, 20)
        self.lbl_num_bins = QLabel(self.twb_num_bins)
        self.lbl_num_bins.setObjectName(u"lbl_num_bins")
        sizePolicy3.setHeightForWidth(self.lbl_num_bins.sizePolicy().hasHeightForWidth())
        self.lbl_num_bins.setSizePolicy(sizePolicy3)
        self.lbl_num_bins.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_13.addWidget(self.lbl_num_bins)

        self.spb_num_bins = QSpinBox(self.twb_num_bins)
        self.spb_num_bins.setObjectName(u"spb_num_bins")
        self.spb_num_bins.setMinimumSize(QSize(0, 30))
        self.spb_num_bins.setMinimum(1)
        self.spb_num_bins.setMaximum(1000)
        self.spb_num_bins.setValue(50)

        self.horizontalLayout_13.addWidget(self.spb_num_bins)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 2)
        self.tbw_size_scale_fre.addTab(self.twb_num_bins, "")

        self.horizontalLayout_14.addWidget(self.tbw_size_scale_fre)


        self.size_scale.addWidget(self.gb_size_scale_fre)

        self.size_scale.setStretch(0, 4)
        self.size_scale.setStretch(1, 5)

        self.verticalLayout_4.addLayout(self.size_scale)

        self.gb_calculate = QGroupBox(self.tbw_CSD)
        self.gb_calculate.setObjectName(u"gb_calculate")
        self.horizontalLayout_10 = QHBoxLayout(self.gb_calculate)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_cal_csd = QPushButton(self.gb_calculate)
        self.btn_cal_csd.setObjectName(u"btn_cal_csd")
        self.btn_cal_csd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.btn_cal_csd)

        self.btn_cal_frequency = QPushButton(self.gb_calculate)
        self.btn_cal_frequency.setObjectName(u"btn_cal_frequency")
        self.btn_cal_frequency.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.btn_cal_frequency)

        self.btn_cal_shape = QPushButton(self.gb_calculate)
        self.btn_cal_shape.setObjectName(u"btn_cal_shape")
        self.btn_cal_shape.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.btn_cal_shape)

        self.btn_cal_sphericity = QPushButton(self.gb_calculate)
        self.btn_cal_sphericity.setObjectName(u"btn_cal_sphericity")
        self.btn_cal_sphericity.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.btn_cal_sphericity)

        self.btn_cal_all = QPushButton(self.gb_calculate)
        self.btn_cal_all.setObjectName(u"btn_cal_all")
        self.btn_cal_all.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.btn_cal_all)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 1)
        self.horizontalLayout_10.setStretch(3, 1)
        self.horizontalLayout_10.setStretch(4, 1)

        self.verticalLayout_4.addWidget(self.gb_calculate)

        self.verticalLayout_4.setStretch(0, 5)
        self.verticalLayout_4.setStretch(1, 3)
        self.verticalLayout_4.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.csd.addTab(self.tbw_CSD, "")
        self.tbw_Skeleton = QWidget()
        self.tbw_Skeleton.setObjectName(u"tbw_Skeleton")
        self.verticalLayout_9 = QVBoxLayout(self.tbw_Skeleton)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_load_file_2 = QPushButton(self.tbw_Skeleton)
        self.btn_load_file_2.setObjectName(u"btn_load_file_2")
        sizePolicy.setHeightForWidth(self.btn_load_file_2.sizePolicy().hasHeightForWidth())
        self.btn_load_file_2.setSizePolicy(sizePolicy)
        self.btn_load_file_2.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_15.addWidget(self.btn_load_file_2)

        self.btn_clear_data_2 = QPushButton(self.tbw_Skeleton)
        self.btn_clear_data_2.setObjectName(u"btn_clear_data_2")
        self.btn_clear_data_2.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_15.addWidget(self.btn_clear_data_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tw_length = QTableWidget(self.tbw_Skeleton)
        if (self.tw_length.columnCount() < 2):
            self.tw_length.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_length.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_length.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tw_length.setObjectName(u"tw_length")

        self.verticalLayout_7.addWidget(self.tw_length)

        self.tw_volume = QTableWidget(self.tbw_Skeleton)
        if (self.tw_volume.columnCount() < 2):
            self.tw_volume.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_volume.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_volume.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tw_volume.setObjectName(u"tw_volume")

        self.verticalLayout_7.addWidget(self.tw_volume)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_cal_dis = QPushButton(self.tbw_Skeleton)
        self.btn_cal_dis.setObjectName(u"btn_cal_dis")
        self.btn_cal_dis.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_16.addWidget(self.btn_cal_dis)

        self.btn_save_length = QPushButton(self.tbw_Skeleton)
        self.btn_save_length.setObjectName(u"btn_save_length")
        self.btn_save_length.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_16.addWidget(self.btn_save_length)

        self.btn_save_volume = QPushButton(self.tbw_Skeleton)
        self.btn_save_volume.setObjectName(u"btn_save_volume")
        self.btn_save_volume.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_16.addWidget(self.btn_save_volume)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.csd.addTab(self.tbw_Skeleton, "")
        self.tbw_PNM = QWidget()
        self.tbw_PNM.setObjectName(u"tbw_PNM")
        self.verticalLayout_14 = QVBoxLayout(self.tbw_PNM)
        self.verticalLayout_14.setSpacing(7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.gb_data_input_pnm = QGroupBox(self.tbw_PNM)
        self.gb_data_input_pnm.setObjectName(u"gb_data_input_pnm")
        self.gb_data_input_pnm.setMinimumSize(QSize(330, 0))
        self.verticalLayout_10 = QVBoxLayout(self.gb_data_input_pnm)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.btn_load_file_pnm = QPushButton(self.gb_data_input_pnm)
        self.btn_load_file_pnm.setObjectName(u"btn_load_file_pnm")
        sizePolicy.setHeightForWidth(self.btn_load_file_pnm.sizePolicy().hasHeightForWidth())
        self.btn_load_file_pnm.setSizePolicy(sizePolicy)
        self.btn_load_file_pnm.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_20.addWidget(self.btn_load_file_pnm)

        self.btn_clear_data_pnm = QPushButton(self.gb_data_input_pnm)
        self.btn_clear_data_pnm.setObjectName(u"btn_clear_data_pnm")
        self.btn_clear_data_pnm.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_20.addWidget(self.btn_clear_data_pnm)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.verticalLayout_10.setStretch(0, 1)

        self.verticalLayout_14.addWidget(self.gb_data_input_pnm)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.gb_size_scale_fre_pnm = QGroupBox(self.tbw_PNM)
        self.gb_size_scale_fre_pnm.setObjectName(u"gb_size_scale_fre_pnm")
        self.horizontalLayout_17 = QHBoxLayout(self.gb_size_scale_fre_pnm)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.tbw_size_scale_fre_pnm = QTabWidget(self.gb_size_scale_fre_pnm)
        self.tbw_size_scale_fre_pnm.setObjectName(u"tbw_size_scale_fre_pnm")
        self.twb_bin_size_fre_pnm = QWidget()
        self.twb_bin_size_fre_pnm.setObjectName(u"twb_bin_size_fre_pnm")
        self.horizontalLayout_18 = QHBoxLayout(self.twb_bin_size_fre_pnm)
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(10, 20, 10, 20)
        self.lbl_bin_size_fre_pnm = QLabel(self.twb_bin_size_fre_pnm)
        self.lbl_bin_size_fre_pnm.setObjectName(u"lbl_bin_size_fre_pnm")
        sizePolicy3.setHeightForWidth(self.lbl_bin_size_fre_pnm.sizePolicy().hasHeightForWidth())
        self.lbl_bin_size_fre_pnm.setSizePolicy(sizePolicy3)
        self.lbl_bin_size_fre_pnm.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_18.addWidget(self.lbl_bin_size_fre_pnm)

        self.dsb_bin_size_fre_pnm = QDoubleSpinBox(self.twb_bin_size_fre_pnm)
        self.dsb_bin_size_fre_pnm.setObjectName(u"dsb_bin_size_fre_pnm")
        sizePolicy4.setHeightForWidth(self.dsb_bin_size_fre_pnm.sizePolicy().hasHeightForWidth())
        self.dsb_bin_size_fre_pnm.setSizePolicy(sizePolicy4)
        self.dsb_bin_size_fre_pnm.setMinimumSize(QSize(150, 30))
        self.dsb_bin_size_fre_pnm.setMaximum(10000.000000000000000)
        self.dsb_bin_size_fre_pnm.setValue(100.000000000000000)

        self.horizontalLayout_18.addWidget(self.dsb_bin_size_fre_pnm)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 2)
        self.tbw_size_scale_fre_pnm.addTab(self.twb_bin_size_fre_pnm, "")
        self.twb_num_bins_pnm = QWidget()
        self.twb_num_bins_pnm.setObjectName(u"twb_num_bins_pnm")
        self.horizontalLayout_19 = QHBoxLayout(self.twb_num_bins_pnm)
        self.horizontalLayout_19.setSpacing(3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 20, 10, 20)
        self.lbl_num_bins_fre_pnm = QLabel(self.twb_num_bins_pnm)
        self.lbl_num_bins_fre_pnm.setObjectName(u"lbl_num_bins_fre_pnm")
        sizePolicy3.setHeightForWidth(self.lbl_num_bins_fre_pnm.sizePolicy().hasHeightForWidth())
        self.lbl_num_bins_fre_pnm.setSizePolicy(sizePolicy3)
        self.lbl_num_bins_fre_pnm.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_19.addWidget(self.lbl_num_bins_fre_pnm)

        self.spb_num_bins_fre_pnm = QSpinBox(self.twb_num_bins_pnm)
        self.spb_num_bins_fre_pnm.setObjectName(u"spb_num_bins_fre_pnm")
        self.spb_num_bins_fre_pnm.setMinimumSize(QSize(0, 30))
        self.spb_num_bins_fre_pnm.setMinimum(1)
        self.spb_num_bins_fre_pnm.setMaximum(1000)
        self.spb_num_bins_fre_pnm.setValue(50)

        self.horizontalLayout_19.addWidget(self.spb_num_bins_fre_pnm)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 2)
        self.tbw_size_scale_fre_pnm.addTab(self.twb_num_bins_pnm, "")

        self.horizontalLayout_17.addWidget(self.tbw_size_scale_fre_pnm)


        self.horizontalLayout_29.addWidget(self.gb_size_scale_fre_pnm)

        self.gb_size_scale_ar = QGroupBox(self.tbw_PNM)
        self.gb_size_scale_ar.setObjectName(u"gb_size_scale_ar")
        self.horizontalLayout_21 = QHBoxLayout(self.gb_size_scale_ar)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.tbw_size_scale_ar = QTabWidget(self.gb_size_scale_ar)
        self.tbw_size_scale_ar.setObjectName(u"tbw_size_scale_ar")
        self.twb_bin_size_ar = QWidget()
        self.twb_bin_size_ar.setObjectName(u"twb_bin_size_ar")
        self.horizontalLayout_22 = QHBoxLayout(self.twb_bin_size_ar)
        self.horizontalLayout_22.setSpacing(3)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(10, 20, 10, 20)
        self.lbl_bin_size_ar = QLabel(self.twb_bin_size_ar)
        self.lbl_bin_size_ar.setObjectName(u"lbl_bin_size_ar")
        sizePolicy3.setHeightForWidth(self.lbl_bin_size_ar.sizePolicy().hasHeightForWidth())
        self.lbl_bin_size_ar.setSizePolicy(sizePolicy3)
        self.lbl_bin_size_ar.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_22.addWidget(self.lbl_bin_size_ar)

        self.dsb_bin_size_ar = QDoubleSpinBox(self.twb_bin_size_ar)
        self.dsb_bin_size_ar.setObjectName(u"dsb_bin_size_ar")
        sizePolicy4.setHeightForWidth(self.dsb_bin_size_ar.sizePolicy().hasHeightForWidth())
        self.dsb_bin_size_ar.setSizePolicy(sizePolicy4)
        self.dsb_bin_size_ar.setMinimumSize(QSize(150, 30))
        self.dsb_bin_size_ar.setMaximum(10000.000000000000000)
        self.dsb_bin_size_ar.setValue(0.250000000000000)

        self.horizontalLayout_22.addWidget(self.dsb_bin_size_ar)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 2)
        self.tbw_size_scale_ar.addTab(self.twb_bin_size_ar, "")
        self.twb_num_bins_ar = QWidget()
        self.twb_num_bins_ar.setObjectName(u"twb_num_bins_ar")
        self.horizontalLayout_23 = QHBoxLayout(self.twb_num_bins_ar)
        self.horizontalLayout_23.setSpacing(3)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(10, 20, 10, 20)
        self.lbl_num_bins_ar = QLabel(self.twb_num_bins_ar)
        self.lbl_num_bins_ar.setObjectName(u"lbl_num_bins_ar")
        sizePolicy3.setHeightForWidth(self.lbl_num_bins_ar.sizePolicy().hasHeightForWidth())
        self.lbl_num_bins_ar.setSizePolicy(sizePolicy3)
        self.lbl_num_bins_ar.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_23.addWidget(self.lbl_num_bins_ar)

        self.spb_num_bins_ar = QSpinBox(self.twb_num_bins_ar)
        self.spb_num_bins_ar.setObjectName(u"spb_num_bins_ar")
        self.spb_num_bins_ar.setMinimumSize(QSize(0, 30))
        self.spb_num_bins_ar.setMinimum(1)
        self.spb_num_bins_ar.setMaximum(1000)
        self.spb_num_bins_ar.setValue(100)

        self.horizontalLayout_23.addWidget(self.spb_num_bins_ar)

        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(1, 2)
        self.tbw_size_scale_ar.addTab(self.twb_num_bins_ar, "")

        self.horizontalLayout_21.addWidget(self.tbw_size_scale_ar)


        self.horizontalLayout_29.addWidget(self.gb_size_scale_ar)


        self.verticalLayout_14.addLayout(self.horizontalLayout_29)

        self.groupBox = QGroupBox(self.tbw_PNM)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lbl_bin_size_crys = QLabel(self.groupBox)
        self.lbl_bin_size_crys.setObjectName(u"lbl_bin_size_crys")
        sizePolicy3.setHeightForWidth(self.lbl_bin_size_crys.sizePolicy().hasHeightForWidth())
        self.lbl_bin_size_crys.setSizePolicy(sizePolicy3)
        self.lbl_bin_size_crys.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_24.addWidget(self.lbl_bin_size_crys)

        self.le_bin_size_crys = QLineEdit(self.groupBox)
        self.le_bin_size_crys.setObjectName(u"le_bin_size_crys")
        self.le_bin_size_crys.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_24.addWidget(self.le_bin_size_crys)

        self.horizontalLayout_24.setStretch(0, 1)
        self.horizontalLayout_24.setStretch(1, 2)

        self.verticalLayout_13.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(3)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lbl_bin_max = QLabel(self.groupBox)
        self.lbl_bin_max.setObjectName(u"lbl_bin_max")
        sizePolicy3.setHeightForWidth(self.lbl_bin_max.sizePolicy().hasHeightForWidth())
        self.lbl_bin_max.setSizePolicy(sizePolicy3)
        self.lbl_bin_max.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_25.addWidget(self.lbl_bin_max)

        self.le_bin_max = QLineEdit(self.groupBox)
        self.le_bin_max.setObjectName(u"le_bin_max")
        self.le_bin_max.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_25.addWidget(self.le_bin_max)

        self.horizontalLayout_25.setStretch(0, 1)
        self.horizontalLayout_25.setStretch(1, 2)

        self.verticalLayout_13.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(3)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lbl_crys_radius = QLabel(self.groupBox)
        self.lbl_crys_radius.setObjectName(u"lbl_crys_radius")
        sizePolicy3.setHeightForWidth(self.lbl_crys_radius.sizePolicy().hasHeightForWidth())
        self.lbl_crys_radius.setSizePolicy(sizePolicy3)
        self.lbl_crys_radius.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_26.addWidget(self.lbl_crys_radius)

        self.le_crys_radius = QLineEdit(self.groupBox)
        self.le_crys_radius.setObjectName(u"le_crys_radius")
        self.le_crys_radius.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_26.addWidget(self.le_crys_radius)

        self.horizontalLayout_26.setStretch(0, 1)
        self.horizontalLayout_26.setStretch(1, 2)

        self.verticalLayout_13.addLayout(self.horizontalLayout_26)

        self.tbw_pore = QTabWidget(self.groupBox)
        self.tbw_pore.setObjectName(u"tbw_pore")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(3)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lbl_pore_id = QLabel(self.tab)
        self.lbl_pore_id.setObjectName(u"lbl_pore_id")
        sizePolicy3.setHeightForWidth(self.lbl_pore_id.sizePolicy().hasHeightForWidth())
        self.lbl_pore_id.setSizePolicy(sizePolicy3)
        self.lbl_pore_id.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_27.addWidget(self.lbl_pore_id)

        self.le_pore_id = QLineEdit(self.tab)
        self.le_pore_id.setObjectName(u"le_pore_id")
        self.le_pore_id.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_27.addWidget(self.le_pore_id)

        self.horizontalLayout_27.setStretch(0, 1)
        self.horizontalLayout_27.setStretch(1, 2)

        self.verticalLayout_11.addLayout(self.horizontalLayout_27)

        self.tbw_pore.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_12 = QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.btn_load_file_multi_pore = QPushButton(self.tab_2)
        self.btn_load_file_multi_pore.setObjectName(u"btn_load_file_multi_pore")
        sizePolicy.setHeightForWidth(self.btn_load_file_multi_pore.sizePolicy().hasHeightForWidth())
        self.btn_load_file_multi_pore.setSizePolicy(sizePolicy)
        self.btn_load_file_multi_pore.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_28.addWidget(self.btn_load_file_multi_pore)

        self.btn_clear_data_multi_pore = QPushButton(self.tab_2)
        self.btn_clear_data_multi_pore.setObjectName(u"btn_clear_data_multi_pore")
        self.btn_clear_data_multi_pore.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_28.addWidget(self.btn_clear_data_multi_pore)


        self.verticalLayout_12.addLayout(self.horizontalLayout_28)

        self.tbw_pore.addTab(self.tab_2, "")

        self.verticalLayout_13.addWidget(self.tbw_pore)


        self.verticalLayout_14.addWidget(self.groupBox)

        self.gb_calculate_2 = QGroupBox(self.tbw_PNM)
        self.gb_calculate_2.setObjectName(u"gb_calculate_2")
        self.horizontalLayout_30 = QHBoxLayout(self.gb_calculate_2)
        self.horizontalLayout_30.setSpacing(5)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.btn_cal_fre_pore = QPushButton(self.gb_calculate_2)
        self.btn_cal_fre_pore.setObjectName(u"btn_cal_fre_pore")
        self.btn_cal_fre_pore.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_30.addWidget(self.btn_cal_fre_pore)

        self.btn_cal_fre_ar = QPushButton(self.gb_calculate_2)
        self.btn_cal_fre_ar.setObjectName(u"btn_cal_fre_ar")
        self.btn_cal_fre_ar.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_30.addWidget(self.btn_cal_fre_ar)

        self.btn_cal_trapped_phase = QPushButton(self.gb_calculate_2)
        self.btn_cal_trapped_phase.setObjectName(u"btn_cal_trapped_phase")
        self.btn_cal_trapped_phase.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_30.addWidget(self.btn_cal_trapped_phase)

        self.horizontalLayout_30.setStretch(0, 1)
        self.horizontalLayout_30.setStretch(1, 1)
        self.horizontalLayout_30.setStretch(2, 1)

        self.verticalLayout_14.addWidget(self.gb_calculate_2)

        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 2)
        self.verticalLayout_14.setStretch(2, 3)
        self.verticalLayout_14.setStretch(3, 1)
        self.csd.addTab(self.tbw_PNM, "")

        self.verticalLayout.addWidget(self.csd)


        self.retranslateUi(Form)

        self.csd.setCurrentIndex(0)
        self.cmb_unit_input.setCurrentIndex(1)
        self.cmb_unit_display.setCurrentIndex(2)
        self.tbw_size_scale_csd.setCurrentIndex(0)
        self.tbw_size_scale_fre.setCurrentIndex(0)
        self.tbw_size_scale_fre_pnm.setCurrentIndex(0)
        self.tbw_size_scale_ar.setCurrentIndex(0)
        self.tbw_pore.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"CTDataToolbox", None))
        self.gb_data_input.setTitle(QCoreApplication.translate("Form", u"Data input", None))
        self.btn_load_file.setText(QCoreApplication.translate("Form", u"Load Data File", None))
        self.btn_clear_data.setText(QCoreApplication.translate("Form", u"Clear Data", None))
        self.lbl_unit_input.setText(QCoreApplication.translate("Form", u"Unit of Sample Input:", None))
        self.cmb_unit_input.setItemText(0, QCoreApplication.translate("Form", u"nanometer [nm]", None))
        self.cmb_unit_input.setItemText(1, QCoreApplication.translate("Form", u"micrometer [\u03bcm]", None))
        self.cmb_unit_input.setItemText(2, QCoreApplication.translate("Form", u"millimeter [mm]", None))
        self.cmb_unit_input.setItemText(3, QCoreApplication.translate("Form", u"centimeter [cm]", None))
        self.cmb_unit_input.setItemText(4, QCoreApplication.translate("Form", u"decimeter [dm]", None))
        self.cmb_unit_input.setItemText(5, QCoreApplication.translate("Form", u"meter [m]", None))

        self.lbl_spatial_resolution.setText(QCoreApplication.translate("Form", u"Voxel Size:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Measured Volume3d:", None))
        self.lbl_unit_display.setText(QCoreApplication.translate("Form", u"Display Units:", None))
        self.cmb_unit_display.setItemText(0, QCoreApplication.translate("Form", u"nanometer [nm]", None))
        self.cmb_unit_display.setItemText(1, QCoreApplication.translate("Form", u"micrometer [\u03bcm]", None))
        self.cmb_unit_display.setItemText(2, QCoreApplication.translate("Form", u"millimeter [mm]", None))
        self.cmb_unit_display.setItemText(3, QCoreApplication.translate("Form", u"centimeter [cm]", None))
        self.cmb_unit_display.setItemText(4, QCoreApplication.translate("Form", u"decimeter [dm]", None))
        self.cmb_unit_display.setItemText(5, QCoreApplication.translate("Form", u"meter [m]", None))

        self.gb_statistics.setTitle(QCoreApplication.translate("Form", u"Statistics", None))
        self.btn_get_para.setText(QCoreApplication.translate("Form", u"Get Parameters", None))
        self.btn_save_para.setText(QCoreApplication.translate("Form", u"Save Parameters", None))
        self.gb_size_scale_csd.setTitle(QCoreApplication.translate("Form", u"CSD Size Scale", None))
        self.lbl_log10.setText(QCoreApplication.translate("Form", u"Logarithmic base 10 size scale.\n"
"Number of bins per decade", None))
        self.tbw_size_scale_csd.setTabText(self.tbw_size_scale_csd.indexOf(self.tbw_log10), QCoreApplication.translate("Form", u"Log 10", None))
        self.lbl_log2.setText(QCoreApplication.translate("Form", u"Logarithmic base 2 size scale.", None))
        self.tbw_size_scale_csd.setTabText(self.tbw_size_scale_csd.indexOf(self.tbw_log2), QCoreApplication.translate("Form", u"Log 2", None))
        self.lbl_linear.setText(QCoreApplication.translate("Form", u"Linear size scale.\n"
"Enter the size interval", None))
        self.lbl_unit.setText(QCoreApplication.translate("Form", u"mm", None))
        self.tbw_size_scale_csd.setTabText(self.tbw_size_scale_csd.indexOf(self.tbw_linear), QCoreApplication.translate("Form", u"Linear", None))
        self.gb_size_scale_fre.setTitle(QCoreApplication.translate("Form", u"Frequency Size Scale", None))
        self.lbl_bin_size.setText(QCoreApplication.translate("Form", u"Enter the size interval", None))
        self.lbl_unit_2.setText(QCoreApplication.translate("Form", u"mm", None))
        self.tbw_size_scale_fre.setTabText(self.tbw_size_scale_fre.indexOf(self.twb_bin_size), QCoreApplication.translate("Form", u"Bin Size", None))
        self.lbl_num_bins.setText(QCoreApplication.translate("Form", u"The total number of bins", None))
        self.tbw_size_scale_fre.setTabText(self.tbw_size_scale_fre.indexOf(self.twb_num_bins), QCoreApplication.translate("Form", u"Number of bins", None))
        self.gb_calculate.setTitle(QCoreApplication.translate("Form", u"Calculate", None))
        self.btn_cal_csd.setText(QCoreApplication.translate("Form", u"CSD", None))
        self.btn_cal_frequency.setText(QCoreApplication.translate("Form", u"Frequency", None))
        self.btn_cal_shape.setText(QCoreApplication.translate("Form", u"Morphology and Shape", None))
        self.btn_cal_sphericity.setText(QCoreApplication.translate("Form", u"Sphericity", None))
        self.btn_cal_all.setText(QCoreApplication.translate("Form", u"Calculate All", None))
        self.csd.setTabText(self.csd.indexOf(self.tbw_CSD), QCoreApplication.translate("Form", u"Crystal size distribution", None))
        self.btn_load_file_2.setText(QCoreApplication.translate("Form", u"Load Data File", None))
        self.btn_clear_data_2.setText(QCoreApplication.translate("Form", u"Clear Data", None))
        ___qtablewidgetitem = self.tw_length.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID of Interconnected Segment", None));
        ___qtablewidgetitem1 = self.tw_length.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"% of Total Skeleton Length", None));
        ___qtablewidgetitem2 = self.tw_volume.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"ID of Interconnected Segment", None));
        ___qtablewidgetitem3 = self.tw_volume.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"% of  Total Skeleton Volume", None));
        self.btn_cal_dis.setText(QCoreApplication.translate("Form", u"Calculate and Display Figures", None))
        self.btn_save_length.setText(QCoreApplication.translate("Form", u"Save Skeleton Length Data", None))
        self.btn_save_volume.setText(QCoreApplication.translate("Form", u"Save Skeleton Volume Data", None))
        self.csd.setTabText(self.csd.indexOf(self.tbw_Skeleton), QCoreApplication.translate("Form", u"Skeleton", None))
        self.gb_data_input_pnm.setTitle(QCoreApplication.translate("Form", u"Data input", None))
        self.btn_load_file_pnm.setText(QCoreApplication.translate("Form", u"Load Data File", None))
        self.btn_clear_data_pnm.setText(QCoreApplication.translate("Form", u"Clear Data", None))
        self.gb_size_scale_fre_pnm.setTitle(QCoreApplication.translate("Form", u"Pore Throat Frequency Size Scale", None))
        self.lbl_bin_size_fre_pnm.setText(QCoreApplication.translate("Form", u"Enter the size interval", None))
        self.tbw_size_scale_fre_pnm.setTabText(self.tbw_size_scale_fre_pnm.indexOf(self.twb_bin_size_fre_pnm), QCoreApplication.translate("Form", u"Bin Size", None))
        self.lbl_num_bins_fre_pnm.setText(QCoreApplication.translate("Form", u"The total number of bins", None))
        self.tbw_size_scale_fre_pnm.setTabText(self.tbw_size_scale_fre_pnm.indexOf(self.twb_num_bins_pnm), QCoreApplication.translate("Form", u"Number of bins", None))
        self.gb_size_scale_ar.setTitle(QCoreApplication.translate("Form", u"Aspect Ratio Frequency Size Scale", None))
        self.lbl_bin_size_ar.setText(QCoreApplication.translate("Form", u"Enter the size interval", None))
        self.tbw_size_scale_ar.setTabText(self.tbw_size_scale_ar.indexOf(self.twb_bin_size_ar), QCoreApplication.translate("Form", u"Bin Size", None))
        self.lbl_num_bins_ar.setText(QCoreApplication.translate("Form", u"The total number of bins", None))
        self.tbw_size_scale_ar.setTabText(self.tbw_size_scale_ar.indexOf(self.twb_num_bins_ar), QCoreApplication.translate("Form", u"Number of bins", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Trapped Phase", None))
        self.lbl_bin_size_crys.setText(QCoreApplication.translate("Form", u"Bin Size:", None))
        self.lbl_bin_max.setText(QCoreApplication.translate("Form", u"Maximum Bin End:", None))
        self.lbl_crys_radius.setText(QCoreApplication.translate("Form", u"Trapped Phase Radius:", None))
        self.lbl_pore_id.setText(QCoreApplication.translate("Form", u"Pore ID:", None))
        self.tbw_pore.setTabText(self.tbw_pore.indexOf(self.tab), QCoreApplication.translate("Form", u"Single Pore", None))
        self.btn_load_file_multi_pore.setText(QCoreApplication.translate("Form", u"Load data file", None))
        self.btn_clear_data_multi_pore.setText(QCoreApplication.translate("Form", u"clear data", None))
        self.tbw_pore.setTabText(self.tbw_pore.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Multi-Pore", None))
        self.gb_calculate_2.setTitle(QCoreApplication.translate("Form", u"Calculate", None))
        self.btn_cal_fre_pore.setText(QCoreApplication.translate("Form", u"Pore Throat Frequency", None))
        self.btn_cal_fre_ar.setText(QCoreApplication.translate("Form", u"Aspect Ratio Frequency", None))
        self.btn_cal_trapped_phase.setText(QCoreApplication.translate("Form", u"Trapped Phase", None))
        self.csd.setTabText(self.csd.indexOf(self.tbw_PNM), QCoreApplication.translate("Form", u"Pore-network modeling", None))
    # retranslateUi

