import numpy as np
import ternary
from PySide6.QtGui import QColor, QPalette, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QHeaderView, QHBoxLayout, \
    QTableWidgetItem, QFileDialog, QMessageBox, QColorDialog, QInputDialog, QDialog, QGridLayout, \
    QGroupBox, QSplitter
from matplotlib import colors
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
from matplotlib.colors import to_hex
from matplotlib.legend import Legend
from matplotlib.cm import ScalarMappable
from matplotlib.ticker import FuncFormatter
from scipy.stats import gaussian_kde
from Modules.UI.line_Properties_dialog_UI import Ui_Dialog as Line_ui
from Modules.UI.histogram_properties_dialog_UI import Ui_Dialog as Histogram_ui
from Modules.UI.scatter_properties_dialog_UI import Ui_Dialog as Scatter_ui
from Modules.UI.ternary_properties_dialog_UI import Ui_Dialog as Ternary_ui
from Modules.UI.arrow_properties_dialog_UI import Ui_Dialog as Arrow_ui
from Modules.UI.rectangle_properties_dialog_UI import Ui_Dialog as Rectangle_ui
from Modules.UI.annotation_properties_dialog_UI import Ui_Dialog as Annotation_ui


class PlotWindow_CSD(QWidget):
    def __init__(self, figure, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle('CSD')
        self.data = data
        self.figure = figure
        self.canvas = FigureCanvas(self.figure)

        self.gb_csd_distribution_data = QGroupBox("CSD Distribution Data", self)
        self.gb_csd_plot_data = QGroupBox("CSD Plot Data", self)
        self.tw_csd_distribution_data = QTableWidget(self)
        self.tw_csd_plot_data = QTableWidget(self)

        self.btn_save_csd_distribution_data = QPushButton("Save CSD Distribution Data", self)
        self.btn_save_csd_plot_data = QPushButton("Save CSD Plot Data", self)
        self.btn_save_figure = QPushButton("Save Figure", self)
        self.btn_modify_line = QPushButton("Format Line", self)

        self.data_csd_distribution_data = self.data[['Bin', 'Count', 'Volumetric number density', 'Population density']]
        self.data_csd_plot_data = self.data[['Midpoint', 'ln(Population density)']]
        populate_table(self.tw_csd_distribution_data, self.data_csd_distribution_data)
        populate_table(self.tw_csd_plot_data, self.data_csd_plot_data)

        self.tw_csd_distribution_data.setMinimumHeight(120)
        self.tw_csd_plot_data.setMinimumHeight(120)
        self.canvas.setMinimumSize(530, 400)

        gb_csd_distribution_data_layout = QVBoxLayout()
        gb_csd_distribution_data_layout.addWidget(self.tw_csd_distribution_data)
        self.gb_csd_distribution_data.setLayout(gb_csd_distribution_data_layout)
        gb_csd_plot_data_layout = QVBoxLayout()
        gb_csd_plot_data_layout.addWidget(self.tw_csd_plot_data)
        self.gb_csd_plot_data.setLayout(gb_csd_plot_data_layout)

        button_layout = QGridLayout()
        button_layout.addWidget(self.btn_save_csd_distribution_data, 0, 0)
        button_layout.addWidget(self.btn_save_csd_plot_data, 0, 1)
        button_layout.addWidget(self.btn_modify_line, 1, 0)
        button_layout.addWidget(self.btn_save_figure, 1, 1)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.gb_csd_distribution_data)
        main_layout.addWidget(self.gb_csd_plot_data)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        self.resize(540, 690)

        self.bind()

    def bind(self):
        self.btn_save_csd_distribution_data.clicked.connect(
            lambda: save_data(self.data_csd_distribution_data, 'CSD Distribution Data', self))
        self.btn_save_csd_plot_data.clicked.connect(lambda: save_data(self.data_csd_plot_data, 'CSD Plot Data', self))
        self.btn_save_figure.clicked.connect(lambda: save_chart(self.canvas, 'CSD Plot', self))
        self.btn_modify_line.clicked.connect(lambda: open_line_properties_dialog(self, self.figure, self.canvas, None))


class PlotWindow_Fre(QWidget):
    def __init__(self, figure, esd_frequency_data, cumulative_volume_data, bar_container, legend, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Frequency')
        self.figure = figure
        self.esd_frequency_data = esd_frequency_data
        self.cumulative_volume_data = cumulative_volume_data
        self.bar_container = bar_container
        self.canvas = FigureCanvas(self.figure)
        self.legend = legend

        self.gb_esd_distribution_data = QGroupBox("ESD Distribution Data", self)
        self.gb_cumulative_volume_data = QGroupBox("Cumulative Volume Data", self)
        self.tw_esd_distribution_data = QTableWidget(self)
        self.tw_cumulative_volume_data = QTableWidget(self)
        populate_table(self.tw_esd_distribution_data, self.esd_frequency_data)
        populate_table(self.tw_cumulative_volume_data, self.cumulative_volume_data)

        self.tw_esd_distribution_data.setMinimumHeight(120)
        self.tw_cumulative_volume_data.setMinimumHeight(120)
        self.canvas.setMinimumSize(530, 400)

        self.btn_save_esd_distribution = QPushButton("Save ESD Distribution Data", self)
        self.btn_cumulative_volume = QPushButton("Save Cumulative Volume Data", self)
        self.btn_modify_scatter = QPushButton("Format Line", self)
        self.btn_modify_histograms = QPushButton("Format Histogram", self)
        self.btn_save_figure = QPushButton("Save Figure", self)

        button_layout = QVBoxLayout()
        button_layout1 = QHBoxLayout()
        button_layout2 = QHBoxLayout()
        button_layout1.addWidget(self.btn_save_esd_distribution)
        button_layout1.addWidget(self.btn_cumulative_volume)
        button_layout2.addWidget(self.btn_modify_scatter)
        button_layout2.addWidget(self.btn_modify_histograms)
        button_layout2.addWidget(self.btn_save_figure)
        button_layout.addLayout(button_layout1)
        button_layout.addLayout(button_layout2)

        gb_esd_distribution_data_layout = QVBoxLayout()
        gb_esd_distribution_data_layout.addWidget(self.tw_esd_distribution_data)
        self.gb_esd_distribution_data.setLayout(gb_esd_distribution_data_layout)
        gb_cumulative_volume_data_layout = QVBoxLayout()
        gb_cumulative_volume_data_layout.addWidget(self.tw_cumulative_volume_data)
        self.gb_cumulative_volume_data.setLayout(gb_cumulative_volume_data_layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.gb_esd_distribution_data)
        main_layout.addWidget(self.gb_cumulative_volume_data)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        self.resize(540, 690)

        self.bind()

    def bind(self):
        self.btn_modify_scatter.clicked.connect(
            lambda: open_line_properties_dialog(self, self.figure, self.canvas, self.legend))
        self.btn_modify_histograms.clicked.connect(
            lambda: open_histogram_properties_dialog(self, self.figure, self.canvas, self.bar_container))
        self.btn_save_esd_distribution.clicked.connect(
            lambda: save_data(self.esd_frequency_data, 'ESD Distribution Data', self))
        self.btn_cumulative_volume.clicked.connect(
            lambda: save_data(self.cumulative_volume_data, 'Cumulative Volume Data', self))
        self.btn_save_figure.clicked.connect(lambda: save_chart(self.canvas, 'ESD Frequency Plot', self))


class PlotWindow_Morphology_Univar(QWidget):
    def __init__(self, figure, data1, data2, legend, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Univariate KDE Plot of Morphology')
        self.figure = figure
        self.data1 = data1
        self.data2 = data2
        self.legend = legend
        self.canvas = FigureCanvas(self.figure)

        self.gb_kde_width3d_thickness3d = QGroupBox("Width3D/Thickness3D Kernel Density Estimate(KDE) Data", self)
        self.gb_kde_thickness3d_length3d = QGroupBox("Thickness3D/Length3D Kernel Density Estimate(KDE) Data", self)
        self.tw_kde_width3d_thickness3d = QTableWidget(self)
        self.tw_kde_thickness3d_length3d = QTableWidget(self)
        populate_table(self.tw_kde_width3d_thickness3d, self.data1)
        populate_table(self.tw_kde_thickness3d_length3d, self.data2)

        self.tw_kde_width3d_thickness3d.setMinimumHeight(120)
        self.tw_kde_thickness3d_length3d.setMinimumHeight(120)
        self.canvas.setMinimumSize(530, 400)

        self.btn_save_kde_width3d_thickness3d = QPushButton("Save Width3D/Thickness3D KDE Data", self)
        self.btn_save_kde_thickness3d_length3d = QPushButton("Save Thickness3D/Length3D KDE Data", self)
        self.btn_modify_line = QPushButton("Format Line", self)
        self.btn_save_figure = QPushButton("Save Figure", self)

        gb_kde_width3d_thickness3d_layout = QVBoxLayout()
        gb_kde_width3d_thickness3d_layout.addWidget(self.tw_kde_width3d_thickness3d)
        self.gb_kde_width3d_thickness3d.setLayout(gb_kde_width3d_thickness3d_layout)
        gb_kde_thickness3d_length3d_layout = QVBoxLayout()
        gb_kde_thickness3d_length3d_layout.addWidget(self.tw_kde_thickness3d_length3d)
        self.gb_kde_thickness3d_length3d.setLayout(gb_kde_thickness3d_length3d_layout)

        button_layout = QGridLayout()
        button_layout.addWidget(self.btn_save_kde_width3d_thickness3d, 0, 0)
        button_layout.addWidget(self.btn_save_kde_thickness3d_length3d, 0, 1)
        button_layout.addWidget(self.btn_modify_line, 1, 0)
        button_layout.addWidget(self.btn_save_figure, 1, 1)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.gb_kde_width3d_thickness3d)
        main_layout.addWidget(self.gb_kde_thickness3d_length3d)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        self.resize(540, 690)

        self.bind()

    def bind(self):
        self.btn_save_kde_width3d_thickness3d.clicked.connect(
            lambda: save_data(self.data1, 'Width3D/Thickness3D KDE Data', self))
        self.btn_save_kde_thickness3d_length3d.clicked.connect(
            lambda: save_data(self.data2, 'Thickness3D/Length3D KDE Data', self))
        self.btn_modify_line.clicked.connect(
            lambda: open_line_properties_dialog(self, self.figure, self.canvas, self.legend))
        self.btn_save_figure.clicked.connect(
            lambda: save_chart(self.canvas, 'Univariate KDE Plot of Morphology', self))


class PlotWindow_Morphology_Multi(QWidget):
    def __init__(self, figure, scatter, sm, cbar, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Multivariate KDE Scatter Plot of Morphology')
        self.data = data
        self.figure = figure
        self.scatter = scatter
        self.sm = sm
        self.cbar = cbar
        self.canvas = FigureCanvas(self.figure)

        self.gb_data = QGroupBox('Multivariate Kernel Density Estimate(KDE) Data of Morphology', self)
        self.tw_data = QTableWidget(self)
        populate_table(self.tw_data, self.data)
        self.tw_data.setMinimumHeight(120)

        self.btn_save_data = QPushButton("Save Multivariate KDE Data", self)
        self.btn_modify_scatter = QPushButton("Format Scatter", self)
        self.btn_save_figure = QPushButton("Save Figure", self)

        gb_data_layout = QVBoxLayout()
        gb_data_layout.addWidget(self.tw_data)
        self.gb_data.setLayout(gb_data_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_save_data)
        button_layout.addWidget(self.btn_modify_scatter)
        button_layout.addWidget(self.btn_save_figure)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.gb_data)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        self.bind()

    def bind(self):
        self.btn_save_data.clicked.connect(lambda: save_data(self.data, 'Multivariate KDE Data of Morphology', self))
        self.btn_save_figure.clicked.connect(
            lambda: save_chart(self.canvas, 'Multivariate KDE Scatter Plot of Morphology', self))
        self.btn_modify_scatter.clicked.connect(
            lambda: open_scatter_properties_dialog(self, self.figure, self.scatter, self.sm, self.canvas))


class PlotWindow_Shape(QWidget):
    def __init__(self, figure, data, tax, ax_scatter, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Ternary Plot of Shape')
        self.figure = figure
        self.data = data
        self.tax = tax
        self.ax_scatter = ax_scatter
        self.canvas = FigureCanvas(self.figure)

        self.gb_ternary_data = QGroupBox("Ternary Data of Shape", self)
        self.tw_ternary_data = QTableWidget(self)
        populate_table(self.tw_ternary_data, self.data)

        self.tw_ternary_data.setMinimumHeight(120)
        self.canvas.setMinimumSize(530, 400)

        self.btn_save_ternary_data = QPushButton("Save Ternary Data", self)
        self.btn_modify_ternary = QPushButton("Format Ternary", self)
        self.btn_save_figure = QPushButton("Save Figure", self)

        gb_ternary_data_layout = QVBoxLayout()
        gb_ternary_data_layout.addWidget(self.tw_ternary_data)
        self.gb_ternary_data.setLayout(gb_ternary_data_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_save_ternary_data)
        button_layout.addWidget(self.btn_modify_ternary)
        button_layout.addWidget(self.btn_save_figure)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.gb_ternary_data)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        self.resize(540, 690)

        self.bind()

    def bind(self):
        self.btn_save_ternary_data.clicked.connect(lambda: save_data(self.data, 'Ternary Data of Shape', self))
        self.btn_modify_ternary.clicked.connect(
            lambda: open_ternary_properties_dialog(self, self.figure, self.tax, self.ax_scatter,
                                                   self.canvas))
        self.btn_save_figure.clicked.connect(lambda: save_chart(self.canvas, 'Ternary Plot of Shape', self))


class PlotWindow_Sphericity(QWidget):
    def __init__(self, figure, scatter, sm, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Sphericity')
        self.data = data
        self.figure = figure
        self.scatter = scatter
        self.sm = sm
        self.canvas = FigureCanvas(self.figure)

        self.gb_data = QGroupBox("Multivariate Kernel Density Estimate(KDE) Data of Sphericity", self)
        self.tw_data = QTableWidget(self)
        populate_table(self.tw_data, self.data)
        self.tw_data.setMinimumHeight(120)

        self.btn_save_data = QPushButton("Save Multivariate KDE Data", self)
        self.btn_modify_scatter = QPushButton("Format Scatter", self)
        self.btn_save_figure = QPushButton("Save Figure", self)

        gb_data_layout = QVBoxLayout()
        gb_data_layout.addWidget(self.tw_data)
        self.gb_data.setLayout(gb_data_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_save_data)
        button_layout.addWidget(self.btn_modify_scatter)
        button_layout.addWidget(self.btn_save_figure)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.gb_data)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        self.bind()

    def bind(self):
        self.btn_save_data.clicked.connect(lambda: save_data(self.data, 'Multivariate KDE Data of Sphericity', self))
        self.btn_save_figure.clicked.connect(
            lambda: save_chart(self.canvas, 'Multivariate KDE Scatter Plot of Sphericity', self))
        self.btn_modify_scatter.clicked.connect(
            lambda: open_scatter_properties_dialog(self, self.figure, self.scatter, self.sm, self.canvas))


class PlotWindow_Skel(QWidget):
    def __init__(self, figure, ax, ax_inset, title, arrow_annotation, rect, annotatation, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.title = title
        self.figure = figure
        self.ax = ax
        self.ax_insert = ax_inset
        self.arrow_annotation = arrow_annotation
        self.rectangle = rect
        self.annotation = annotatation
        self.canvas = FigureCanvas(self.figure)

        self.btn_main_properties = QPushButton("Format Main Line Plot", self)
        self.btn_inset_properties = QPushButton("Format Inset Line Plot", self)
        self.btn_arrow_properties = QPushButton("Format Arrow", self)
        self.btn_rectangle_properties = QPushButton("Format Rectangle Border", self)
        self.btn_annotation_properties = QPushButton("Format Label", self)
        self.btn_save_figure = QPushButton("Save Figure", self)

        # 创建布局
        button_layout = QGridLayout()
        button_layout.addWidget(self.btn_main_properties, 0, 0)
        button_layout.addWidget(self.btn_inset_properties, 0, 1)
        button_layout.addWidget(self.btn_arrow_properties, 0, 2)
        button_layout.addWidget(self.btn_rectangle_properties, 1, 0)
        button_layout.addWidget(self.btn_annotation_properties, 1, 1)
        button_layout.addWidget(self.btn_save_figure, 1, 2)
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        self.bind()

    def bind(self):
        self.btn_main_properties.clicked.connect(
            lambda: open_line_properties_dialog2(self, self.figure, self.ax, self.canvas, None))
        self.btn_inset_properties.clicked.connect(
            lambda: open_line_properties_dialog2(self, self.figure, self.ax_insert, self.canvas, None))
        self.btn_arrow_properties.clicked.connect(
            lambda: open_arrow_properties_dialog(self, self.figure, self.canvas, self.arrow_annotation))
        self.btn_rectangle_properties.clicked.connect(
            lambda: open_rectangle_properties_dialog(self, self.figure, self.canvas, self.rectangle))
        self.btn_annotation_properties.clicked.connect(
            lambda: open_annotation_properties_dialog(self, self.figure, self.canvas, self.annotation))
        self.btn_save_figure.clicked.connect(lambda: save_chart(self.canvas, f'{self.title} Plot', self))


class PlotWindow_Fre_Pore(QWidget):
    def __init__(self, figure, pore_data, throat_data, pore_vol_data, throat_channel_length_data, bar_container_pore,
                 bar_container_throat, legend, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Pore and Throat Frequency')
        self.figure = figure
        self.pore_data = pore_data
        self.throat_data = throat_data
        self.pore_vol_data = pore_vol_data
        self.throat_channel_length_data = throat_channel_length_data
        self.bar_container_pore = bar_container_pore
        self.bar_container_throat = bar_container_throat
        self.canvas = FigureCanvas(self.figure)
        self.legend = legend

        main_layout = QVBoxLayout(self)

        self.splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(self.splitter)

        self.left_panel = QWidget()
        self.left_panel.setMinimumWidth(460)
        left_layout = QVBoxLayout(self.left_panel)

        self.gb_pore_data = QGroupBox("Pore EqRadius Distribution Data", self)
        pore_data_layout = QVBoxLayout(self.gb_pore_data)
        self.tw_pore_data = QTableWidget(self)
        populate_table(self.tw_pore_data, self.pore_data)
        pore_data_layout.addWidget(self.tw_pore_data)

        self.gb_throat_data = QGroupBox("Throat EqRadius Distribution Data", self)
        throat_data_layout = QVBoxLayout(self.gb_throat_data)
        self.tw_throat_data = QTableWidget(self)
        populate_table(self.tw_throat_data, self.throat_data)
        throat_data_layout.addWidget(self.tw_throat_data)

        self.gb_pore_vol_data = QGroupBox("Pore Cumulative Volume Data", self)
        pore_vol_data_layout = QVBoxLayout(self.gb_pore_vol_data)
        self.tw_pore_vol_data = QTableWidget(self)
        populate_table(self.tw_pore_vol_data, self.pore_vol_data)
        pore_vol_data_layout.addWidget(self.tw_pore_vol_data)

        self.gb_throat_channel_length_data = QGroupBox("Throat Cumulative Channel Length Data", self)
        throat_channel_length_data_layout = QVBoxLayout(self.gb_throat_channel_length_data)
        self.tw_throat_channel_length_data = QTableWidget(self)
        populate_table(self.tw_throat_channel_length_data, self.throat_channel_length_data)
        throat_channel_length_data_layout.addWidget(self.tw_throat_channel_length_data)

        left_layout.addWidget(self.gb_pore_data)
        left_layout.addWidget(self.gb_throat_data)
        left_layout.addWidget(self.gb_pore_vol_data)
        left_layout.addWidget(self.gb_throat_channel_length_data)

        self.right_panel = QWidget()
        right_layout = QVBoxLayout(self.right_panel)
        self.canvas = FigureCanvas(self.figure)
        right_layout.addWidget(self.canvas)
        self.right_panel.setMinimumWidth(700)

        self.splitter.addWidget(self.left_panel)
        self.splitter.addWidget(self.right_panel)

        self.btn_save_pore = QPushButton("Save Pore EqRadius Distribution Data", self)
        self.btn_save_throat = QPushButton("Save Throat EqRadius Distribution Data", self)
        self.btn_save_pore_vol = QPushButton("Save Pore Cumulative Volume Data", self)
        self.btn_save_throat_channel = QPushButton("Save Throat Cumulative ChannelLength Data", self)
        self.btn_modify_line = QPushButton("Format Line", self)
        self.btn_modify_hist = QPushButton("Format Histogram", self)
        self.btn_save_figure = QPushButton("Save Figure", self)

        button_panel = QWidget()
        button_panel_layout = QVBoxLayout(button_panel)
        button_layout1 = QHBoxLayout()
        button_layout2 = QHBoxLayout()
        button_layout1.addWidget(self.btn_save_pore)
        button_layout1.addWidget(self.btn_save_throat)
        button_layout1.addWidget(self.btn_save_pore_vol)
        button_layout1.addWidget(self.btn_save_throat_channel)
        button_layout2.addWidget(self.btn_modify_line)
        button_layout2.addWidget(self.btn_modify_hist)
        button_layout2.addWidget(self.btn_save_figure)
        button_panel_layout.addLayout(button_layout1)
        button_panel_layout.addLayout(button_layout2)

        main_layout.addWidget(button_panel)
        self.setLayout(main_layout)

        self.bind()

    def bind(self):
        self.btn_save_pore.clicked.connect(lambda: save_data(self.pore_data, 'Pore EqRadius Distribution Data', self))
        self.btn_save_throat.clicked.connect(
            lambda: save_data(self.throat_data, 'Throat EqRadius Distribution Data', self))
        self.btn_save_pore_vol.clicked.connect(
            lambda: save_data(self.pore_vol_data, 'Pore Cumulative Volume Data', self))
        self.btn_save_throat_channel.clicked.connect(
            lambda: save_data(self.throat_channel_length_data, 'Throat Cumulative ChannelLength Data', self))
        self.btn_modify_line.clicked.connect(
            lambda: open_line_properties_dialog(self, self.figure, self.canvas, self.legend))
        self.btn_modify_hist.clicked.connect(
            lambda: open_histogram_properties_dialog(self, self.figure, self.canvas, self.bar_container_pore,
                                                     self.bar_container_throat))
        self.btn_save_figure.clicked.connect(lambda: save_chart(self.canvas, 'Pore and Throat Frequency Plot', self))


class PlotWindow_Fre_AR(QWidget):
    def __init__(self, figure, data_ar, bar_container, parent=None):
        super().__init__(parent)
        self.setWindowTitle('AR Frequency')
        self.data_ar = data_ar
        self.figure = figure
        self.bar_container = bar_container
        self.canvas = FigureCanvas(self.figure)

        main_layout = QVBoxLayout(self)

        self.splitter = QSplitter(Qt.Vertical)
        main_layout.addWidget(self.splitter)

        self.top_panel = QWidget()
        self.top_panel.setMinimumHeight(130)
        top_layout = QVBoxLayout(self.top_panel)
        self.gb_data = QGroupBox("Aspect Ratio(AR) Distribution Data", self)
        data_layout = QVBoxLayout(self.gb_data)
        self.tw_data = QTableWidget(self)
        populate_table(self.tw_data, self.data_ar)
        data_layout.addWidget(self.tw_data)
        top_layout.addWidget(self.gb_data)

        self.plot_panel = QWidget()
        plot_layout = QVBoxLayout(self.plot_panel)
        self.canvas = FigureCanvas(self.figure)
        plot_layout.addWidget(self.canvas)

        self.splitter.addWidget(self.top_panel)
        self.splitter.addWidget(self.plot_panel)

        self.btn_save_data = QPushButton("Save AR Distribution Data", self)
        self.btn_modify_hist = QPushButton("Format Histogram", self)
        self.btn_save_figure = QPushButton("Save Figure", self)

        button_panel = QWidget()
        button_panel_layout = QHBoxLayout(button_panel)
        button_panel_layout.addWidget(self.btn_save_data)
        button_panel_layout.addWidget(self.btn_modify_hist)
        button_panel_layout.addWidget(self.btn_save_figure)

        main_layout.addWidget(button_panel)
        self.setLayout(main_layout)

        self.bind()

    def bind(self):
        self.btn_save_data.clicked.connect(lambda: save_data(self.data_ar, 'AR Distribution Data', self))
        self.btn_save_figure.clicked.connect(lambda: save_chart(self.canvas, 'AR Frequency Plot', self))
        self.btn_modify_hist.clicked.connect(
            lambda: open_histogram_properties_dialog(self, self.figure, self.canvas, self.bar_container))


class PlotWindow_Fre_Trapped_Phase(QWidget):
    def __init__(self, figure, pore_data, throat_data, trapped_phase_data, bar_container_pore, bar_container_throat,
                 bar_container_trapped_phase, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Pore, Throat and Trapped Phase Frequency')
        self.figure = figure
        self.pore_data = pore_data
        self.throat_data = throat_data
        self.trapped_phase_data = trapped_phase_data
        self.bar_container_pore = bar_container_pore
        self.bar_container_throat = bar_container_throat
        self.bar_container_trapped_phase = bar_container_trapped_phase
        self.canvas = FigureCanvas(self.figure)

        main_layout = QVBoxLayout(self)

        self.splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(self.splitter)

        self.left_panel = QWidget()
        self.left_panel.setMinimumWidth(460)
        left_layout = QVBoxLayout(self.left_panel)

        self.gb_pore_data = QGroupBox("Pore EqRadius Distribution Data", self)
        pore_data_layout = QVBoxLayout(self.gb_pore_data)
        self.tw_pore_data = QTableWidget(self)
        populate_table(self.tw_pore_data, self.pore_data)
        pore_data_layout.addWidget(self.tw_pore_data)

        self.gb_throat_data = QGroupBox("Throat EqRadius Distribution Data", self)
        throat_data_layout = QVBoxLayout(self.gb_throat_data)
        self.tw_throat_data = QTableWidget(self)
        populate_table(self.tw_throat_data, self.throat_data)
        throat_data_layout.addWidget(self.tw_throat_data)

        self.gb_trapped_phase_data = QGroupBox("Trapped Phase EqRadius Distribution Data", self)
        trapped_phase_data_layout = QVBoxLayout(self.gb_trapped_phase_data)
        self.tw_trapped_phase_data = QTableWidget(self)
        populate_table(self.tw_trapped_phase_data, self.trapped_phase_data)
        trapped_phase_data_layout.addWidget(self.tw_trapped_phase_data)

        left_layout.addWidget(self.gb_pore_data)
        left_layout.addWidget(self.gb_throat_data)
        left_layout.addWidget(self.gb_trapped_phase_data)

        self.right_panel = QWidget()
        right_layout = QVBoxLayout(self.right_panel)
        self.canvas = FigureCanvas(self.figure)
        right_layout.addWidget(self.canvas)
        self.right_panel.setMinimumWidth(700)

        self.splitter.addWidget(self.left_panel)
        self.splitter.addWidget(self.right_panel)

        self.btn_save_pore = QPushButton("Save Pore EqRadius Distribution Data", self)
        self.btn_save_throat = QPushButton("Save Throat EqRadius Distribution Data", self)
        self.btn_save_crystal = QPushButton("Save Trapped Phase EqRadius Distribution Data", self)
        self.btn_modify_hist = QPushButton("Format Histogram", self)
        self.btn_save_figure = QPushButton("Save Figure", self)

        button_panel = QWidget()
        button_panel_layout = QVBoxLayout(button_panel)
        button_layout1 = QHBoxLayout()
        button_layout2 = QHBoxLayout()
        button_layout1.addWidget(self.btn_save_pore)
        button_layout1.addWidget(self.btn_save_throat)
        button_layout1.addWidget(self.btn_save_crystal)
        button_layout2.addWidget(self.btn_modify_hist)
        button_layout2.addWidget(self.btn_save_figure)
        button_panel_layout.addLayout(button_layout1)
        button_panel_layout.addLayout(button_layout2)

        main_layout.addWidget(button_panel)
        self.setLayout(main_layout)

        self.bind()

    def bind(self):
        self.btn_save_pore.clicked.connect(lambda: save_data(self.pore_data, 'Pore EqRadius Distribution Data', self))
        self.btn_save_throat.clicked.connect(
            lambda: save_data(self.throat_data, 'Throat EqRadius Distribution Data', self))
        self.btn_save_crystal.clicked.connect(
            lambda: save_data(self.trapped_phase_data, 'Trapped Phase EqRadius Distribution Data', self))
        self.btn_modify_hist.clicked.connect(
            lambda: open_histogram_properties_dialog(self, self.figure, self.canvas, self.bar_container_pore,
                                                     self.bar_container_throat, self.bar_container_trapped_phase))
        self.btn_save_figure.clicked.connect(
            lambda: save_chart(self.canvas, 'Pore, Throat and Trapped Phase Frequency Plot', self))


def open_line_properties_dialog(self, figure, canvas, legend):
    ax = figure.gca()
    lines = ax.get_lines()
    # 获取所有散点图和线条
    if len(lines) == 1:
        self.dialog = LinePropertiesDialog(figure, lines[0], canvas, legend)
        self.dialog.show()
    elif len(lines) > 1:
        line_labels = [line.get_label() if line.get_label() else f"Line {i + 1}" for i, line in enumerate(lines)]
        selected_line_label, ok = QInputDialog.getItem(self, "Select Line", "Select line to modify:", line_labels, 0,
                                                       False)
        if not ok:
            return

        selected_line = next(line for line in lines if (
            line.get_label() if line.get_label() else f"Line {lines.index(line) + 1}") == selected_line_label)
        self.dialog = LinePropertiesDialog(figure, selected_line, canvas, legend)
        self.dialog.show()


def open_line_properties_dialog2(self, figure, ax, canvas, legend):
    ax = ax
    line = ax.get_lines()
    self.linedialog = LinePropertiesDialog(figure, line[0], canvas, legend)
    self.linedialog.show()


def open_histogram_properties_dialog(self, figure, canvas, *bar_container):
    if len(bar_container) == 1:
        self.dialog = HistogramPropertiesDialog(figure, canvas, bar_container[0])
        self.dialog.show()

    elif len(bar_container) > 1:
        container_labels = [container.get_label() if container.get_label() else f"bar_container {i + 1}" for
                            i, container in enumerate(bar_container)]

        selected_container_label, ok = QInputDialog.getItem(self, "Select Bar Container",
                                                            "Please select a bar container:",
                                                            container_labels, 0, False)
        if ok and selected_container_label:
            selected_container = next(container for i, container in enumerate(bar_container)
                                      if (
                                          container.get_label() if container.get_label() else f"bar_container {i + 1}") == selected_container_label)

            # 打开对话框并传入选中的容器
            self.dialog = HistogramPropertiesDialog(figure, canvas, selected_container)
            self.dialog.show()


def open_scatter_properties_dialog(self, figure, scatter, sm, canvas):
    self.dialog = ScatterPropertiesDialog(figure, scatter, sm, canvas)
    self.dialog.show()


def open_ternary_properties_dialog(self, figure, tax, ax_scatter, canvas):
    self.current_properties = {
        'marker': 'o',
        'marker_size': 10,
        'marker_color': 'blue',
        'alpha': 0.6,
        'grid_visible': True,
        'grid_width': 0.5,
        'grid_color': "#808080"
    }

    self.dialog = TernaryPropertiesDialog(figure, tax, ax_scatter, canvas, self.current_properties)
    self.dialog.show()


def open_arrow_properties_dialog(self, figure, canvas, arrow_annotation):
    self.dialog = ArrowPropertiesDialog(figure, canvas, arrow_annotation)
    self.dialog.show()


def open_rectangle_properties_dialog(self, figure, canvas, rectangle):
    self.dialog = RectanglePropertiesDialog(figure, canvas, rectangle)
    self.dialog.show()


def open_annotation_properties_dialog(self, figure, canvas, *annotation):
    if len(annotation) == 1:
        self.dialog = AnnotationPropertiesDialog(figure, canvas, annotation[0])
        self.dialog.show()

    elif len(annotation) > 1:
        annotation_names = ['Pore volume', 'Throat ChannelLength']
        selected_name, ok = QInputDialog.getItem(self, "Select Annotation",
                                                 "Please select a annotation:",
                                                 annotation_names, 0, False)
        if ok and selected_name:
            if selected_name == "Pore volume":
                selected_annotation = annotation[0]
            elif selected_name == "Throat ChannelLength":
                selected_annotation = annotation[1]  # Second container
            self.dialog = AnnotationPropertiesDialog(figure, canvas, selected_annotation)
            self.dialog.show()


MARKER_STYLE_MAP = {
    'None': 'None',
    'Square': 's',
    'Circle': 'o',
    'Triangle_up': '^',
    'Triangle_down': 'v',
    'Diamond': 'D',
    'Triangle_left': '<',
    'Triangle_right': '>',
    'Hexagon': 'h',
    'Star': '*',
    'Pentagon': 'p',
    'Plus': '+',
    'X': 'x'
}
LINE_STYLE_MAP = {
    'Solid': '-',
    'Dashed': '--',
    'Dotted': ':',
    'Dash-dot': '-.',
    'None': 'None'
}

CMAPS = [
    ('Perceptually Uniform Sequential', ['viridis', 'plasma', 'inferno', 'magma', 'cividis']),
    ('Sequential',
     ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
    ('Sequential (2)',
     ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
      'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper']),
    ('Diverging',
     ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
    ('Cyclic', ['twilight', 'twilight_shifted', 'hsv']),
    ('Qualitative',
     ['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c']),
    ('Miscellaneous',
     ['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix',
      'brg', 'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral', 'gist_ncar'])
]


class LinePropertiesDialog(QDialog, Line_ui):
    def __init__(self, figure, line, canvas, legend):
        super().__init__()
        self.setupUi(self)

        self.figure = figure
        self.line = line
        self.canvas = canvas
        self.legend = legend

        self.ax = self.figure.gca()
        self.original_marker_visible = self.line.get_marker() not in ["none", "None", " ", ""]
        self.original_marker = self.line.get_marker()
        self.original_marker_size = self.line.get_markersize()
        self.original_marker_color = QColor(self.line.get_markerfacecolor())
        self.original_marker_edge_color = QColor(self.line.get_markeredgecolor())
        self.original_line_visible = self.line.get_linestyle() not in ["none", "None", " ", ""]
        self.original_line_style = self.line.get_linestyle()
        self.original_line_width = self.line.get_linewidth()
        self.original_line_color = QColor(self.line.get_color())

        self.init_ui()
        self.bind()

    def init_ui(self):
        self.chk_show_points.setChecked(self.original_marker_visible)
        self.cmb_marker_style.setCurrentText(next(k for k, v in MARKER_STYLE_MAP.items() if v == self.original_marker))
        self.spb_marker_size.setValue(self.original_marker_size)
        self.lbl_fill_color_preview.setStyleSheet(
            f"background-color: {self.original_marker_color.name()};")
        self.lbl_edge_color_preview.setStyleSheet(
            f"background-color: {self.original_marker_edge_color.name()};")

        self.chk_show_line.setChecked(self.original_line_visible)
        self.cmb_line_style.setCurrentText(next(k for k, v in LINE_STYLE_MAP.items() if v == self.original_line_style))
        self.dsb_line_width.setValue(self.original_line_width)
        self.lbl_line_color_preview.setStyleSheet(f"background-color: {self.original_line_color.name()};")

    def bind(self):
        self.chk_show_points.stateChanged.connect(self.toggle_points)
        self.cmb_marker_style.currentTextChanged.connect(self.change_marker_style)
        self.spb_marker_size.valueChanged.connect(self.change_marker_size)
        self.btn_fill_color.clicked.connect(self.choose_marker_color)
        self.btn_edge_color.clicked.connect(self.choose_edge_color)

        self.chk_show_line.stateChanged.connect(self.toggle_line)
        self.cmb_line_style.currentTextChanged.connect(self.change_line_style)
        self.dsb_line_width.valueChanged.connect(self.change_line_width)
        self.btn_line_color.clicked.connect(self.choose_line_color)

        self.btn_ok.clicked.connect(self.apply_and_close)
        self.btn_cancel.clicked.connect(self.cancel_and_close)
        self.btn_apply.clicked.connect(self.apply_changes)

    def toggle_points(self, state):
        visible = state == 2
        if not visible:
            self.line.set_marker('None')

        else:
            style_text = self.cmb_marker_style.currentText()
            marker = MARKER_STYLE_MAP.get(style_text)
            self.line.set_marker(marker)
            self.line.set_markersize(self.spb_marker_size.value())
            self.line.set_markerfacecolor(self.lbl_fill_color_preview.palette().color(QPalette.Window).name())
            self.line.set_markeredgecolor(self.lbl_edge_color_preview.palette().color(QPalette.Window).name())

    def change_marker_style(self, style_text):
        marker = MARKER_STYLE_MAP.get(style_text)
        self.line.set_marker(marker)

    def change_marker_size(self, size):
        self.line.set_markersize(size)

    def choose_marker_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl_fill_color_preview.setStyleSheet(f"background-color: {color.name()};")
            self.line.set_markerfacecolor(color.name())

    def choose_edge_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl_edge_color_preview.setStyleSheet(f"background-color: {color.name()};")
            self.line.set_markeredgecolor(color.name())

    def toggle_line(self, state):
        visible = state == 2
        if not visible:
            self.line.set_linestyle('None')

        else:
            style_text = self.cmb_line_style.currentText()
            linestyle = LINE_STYLE_MAP.get(style_text)
            self.line.set_linestyle(linestyle)
            self.line.set_linewidth(self.dsb_line_width.value())
            self.line.set_color(self.lbl_line_color_preview.palette().color(QPalette.Window).name())

    def change_line_style(self, style_text):
        linestyle = LINE_STYLE_MAP.get(style_text)
        self.line.set_linestyle(linestyle)

    def change_line_width(self, width):
        self.line.set_linewidth(width)

    def choose_line_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl_line_color_preview.setStyleSheet(f"background-color: {color.name()};")
            self.line.set_color(color.name())

    def update_legend(self):
        legends = self.ax.findobj(Legend)
        if legends:
            oldLegPos = self.ax.get_legend()._loc
            self.ax.get_legend().remove()
            legends = self.ax.legend()
            legends._loc = oldLegPos
            return
        legend = self.figure.findobj(Legend)
        if legend:
            legend = self.figure.legend(loc='lower right', bbox_to_anchor=(1, 0.1), bbox_transform=self.ax.transAxes)

    def apply_changes(self):
        self.update_legend()
        self.canvas.draw()

    def apply_and_close(self):
        self.apply_changes()
        self.accept()

    def cancel_and_close(self):
        # 恢复原始属性
        self.chk_show_points.setChecked(self.original_marker_visible)
        self.line.set_marker(self.original_marker)
        self.line.set_markersize(self.original_marker_size)
        self.line.set_markerfacecolor(self.original_marker_color.name())
        self.line.set_markeredgecolor(self.original_marker_edge_color.name())
        self.chk_show_line.setChecked(self.original_line_visible)
        self.line.set_linestyle(self.original_line_style)
        self.line.set_linewidth(self.original_line_width)
        self.line.set_color(self.original_line_color.name())
        self.reject()


class HistogramPropertiesDialog(QDialog, Histogram_ui):
    def __init__(self, figure, canvas, bar_container):
        super().__init__()
        self.setupUi(self)

        self.figure = figure
        self.bar_container = bar_container
        self.canvas = canvas

        bar = self.bar_container.patches[0]
        self.original_visible = bar.get_visible()
        self.original_fill_color = QColor(to_hex(bar.get_facecolor()))
        self.original_border_color = QColor(to_hex(bar.get_edgecolor()))
        self.original_border_style = bar.get_linestyle()
        self.original_border_width = bar.get_linewidth()
        self.original_alpha = bar.get_alpha()

        self.init_ui()
        self.bind()

    def init_ui(self):

        self.chk_show_histogram.setChecked(self.original_visible)
        self.lbl_fill_color_preview.setStyleSheet(f"background-color: {self.original_fill_color.name()};")
        self.lbl_border_color_preview.setStyleSheet(f"background-color: {self.original_border_color.name()};")
        self.cmb_border_style.setCurrentText(
            next(k for k, v in LINE_STYLE_MAP.items() if v == self.original_border_style))
        self.dsb_border_width.setValue(self.original_border_width)
        self.dsb_alpha.setValue(self.original_alpha)

    def bind(self):
        self.chk_show_histogram.stateChanged.connect(self.toggle_histogram)
        self.btn_fill_color.clicked.connect(self.choose_fill_color)
        self.btn_border_color.clicked.connect(self.choose_border_color)
        self.cmb_border_style.currentTextChanged.connect(self.change_border_style)
        self.dsb_border_width.valueChanged.connect(self.change_border_width)
        self.dsb_alpha.valueChanged.connect(self.change_alpha)

        self.btn_ok.clicked.connect(self.apply_and_close)
        self.btn_cancel.clicked.connect(self.cancel_and_close)
        self.btn_apply.clicked.connect(self.apply_changes)

    def toggle_histogram(self, state):
        visible = state == 2
        for bar in self.bar_container.patches:
            bar.set_visible(visible)

    def choose_fill_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl_fill_color_preview.setStyleSheet(f"background-color: {color.name()};")
            for bar in self.bar_container.patches:
                bar.set_facecolor(color.name())

    def choose_border_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl_border_color_preview.setStyleSheet(f"background-color: {color.name()};")
            for bar in self.bar_container.patches:
                bar.set_edgecolor(color.name())

    def change_border_style(self, style_text):
        linestyle = LINE_STYLE_MAP.get(style_text)
        for bar in self.bar_container.patches:
            bar.set_linestyle(linestyle)

    def change_border_width(self, width):
        for bar in self.bar_container.patches:
            bar.set_linewidth(width)

    def change_alpha(self, alpha):
        for bar in self.bar_container.patches:
            bar.set_alpha(alpha)

    def update_legend(self):
        ax = self.figure.gca()
        legends = ax.findobj(Legend)
        if legends:
            oldLegPos = ax.get_legend()._loc
            legends = ax.legend()
            legends._loc = oldLegPos
            return
        legend = self.figure.findobj(Legend)
        if legend:
            self.figure.legend(loc='lower right', bbox_to_anchor=(1, 0.1), bbox_transform=ax.transAxes)

    def apply_changes(self):
        self.update_legend()
        self.canvas.draw()

    def apply_and_close(self):
        self.apply_changes()
        self.accept()

    def cancel_and_close(self):
        # 恢复原始属性
        for bar in self.bar_container.patches:
            bar.set_visible(self.original_visible)
            bar.set_facecolor(self.original_fill_color.name())
            bar.set_edgecolor(self.original_border_color.name())
            bar.set_linestyle(self.original_border_style)
            bar.set_linewidth(self.original_border_width)
            bar.set_alpha(self.original_alpha)
        self.reject()


class ScatterPropertiesDialog(QDialog, Scatter_ui):
    def __init__(self, figure, scatter, sm, canvas):
        super().__init__()
        self.setupUi(self)

        self.figure = figure
        self.scatter = scatter
        self.scalar_mappable = sm
        self.canvas = canvas

        self.original_marker_size = self.scatter.get_sizes()[0]
        self.original_cmap = self.scatter.get_cmap().name
        self.original_alpha = self.scatter.get_alpha()

        self.init_ui()
        self.bind()

    def init_ui(self):
        self.spb_marker_size.setValue(self.original_marker_size)
        is_reversed = self.original_cmap.endswith('_r')
        base_cmap = self.original_cmap[:-2] if is_reversed else self.original_cmap
        for i, (category, maps) in enumerate(CMAPS):
            if base_cmap in maps:
                self.cmb_cmap_category.setCurrentIndex(i)
                self.update_colormap_list()
                self.cmb_cmap.setCurrentText(self.original_cmap)
                break
        self.dsb_alpha.setValue(self.original_alpha)

    def bind(self):
        self.spb_marker_size.valueChanged.connect(self.change_marker_size)
        self.cmb_cmap_category.currentIndexChanged.connect(self.update_colormap_list)
        self.cmb_cmap.currentTextChanged.connect(self.change_colormap)
        self.dsb_alpha.valueChanged.connect(self.change_alpha)

        self.btn_ok.clicked.connect(self.apply_and_close)
        self.btn_cancel.clicked.connect(self.cancel_and_close)
        self.btn_apply.clicked.connect(self.apply_changes)

    def change_marker_size(self, size):
        self.scatter.set_sizes([size])

    def update_colormap_list(self):
        self.cmb_cmap.clear()
        selected_category = self.cmb_cmap_category.currentText()
        for category, maps in CMAPS:
            if category == selected_category:
                self.cmb_cmap.addItems(maps + [f"{cmap}_r" for cmap in maps])
                break

    def change_colormap(self, cmap_name):
        # 修改散点图的颜色映射
        self.scatter.set_cmap(plt.get_cmap(cmap_name))
        self.scalar_mappable.set_cmap(cmap_name)

    def change_alpha(self, alpha):
        self.scatter.set_alpha(alpha)

    def update_legend(self):
        self.scalar_mappable.changed()

    def apply_changes(self):
        self.update_legend()
        self.canvas.draw()

    def apply_and_close(self):
        self.apply_changes()
        self.accept()

    def cancel_and_close(self):
        self.scatter.set_sizes([self.original_marker_size])
        self.scatter.set_cmap(self.original_cmap)
        self.scatter.set_alpha(self.original_alpha)
        self.reject()


class TernaryPropertiesDialog(QDialog, Ternary_ui):

    def __init__(self, figure, tax, ax_scatter, canvas, current_properties):
        super().__init__()
        self.setupUi(self)

        self.figure = figure
        self.tax = tax
        self.ax_scatter = ax_scatter
        self.canvas = canvas
        self.current_properties = current_properties.copy()

        self.init_ui()
        self.bind()

    def init_ui(self):
        self.cmb_marker_style.setCurrentText(self.current_properties['marker'])
        self.spb_marker_size.setValue(self.current_properties['marker_size'])
        self.lbl_point_color_preview.setStyleSheet(f"background-color: {self.current_properties['marker_color']};")
        self.dsb_alpha.setValue(self.current_properties['alpha'])

        self.chk_show_gridlines.setChecked(self.current_properties['grid_visible'])
        self.dsb_gridline_width.setValue(self.current_properties['grid_width'])
        self.lbl_gridlines_color_preview.setStyleSheet(f"background-color: {self.current_properties['grid_color']};")

    def bind(self):
        self.cmb_marker_style.currentTextChanged.connect(self.change_marker_style)
        self.spb_marker_size.valueChanged.connect(self.change_marker_size)
        self.btn_point_color.clicked.connect(self.choose_marker_color)
        self.dsb_alpha.valueChanged.connect(self.change_alpha)

        self.chk_show_gridlines.stateChanged.connect(self.toggle_gridlines)
        self.dsb_gridline_width.valueChanged.connect(self.change_gridline_width)
        self.btn_gridlines_color.clicked.connect(self.choose_gridline_color)

        self.btn_ok.clicked.connect(self.apply_and_close)
        self.btn_cancel.clicked.connect(self.cancel_and_close)
        self.btn_apply.clicked.connect(self.apply_changes)

    def change_marker_style(self, style_text):
        self.current_properties['marker'] = style_text

    def change_marker_size(self, size):
        self.current_properties['marker_size'] = size

    def choose_marker_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl_point_color_preview.setStyleSheet(f"background-color: {color.name()};")
            self.current_properties['marker_color'] = color.name()

    def change_alpha(self, alpha):
        self.current_properties['alpha'] = alpha

    def toggle_gridlines(self, state):
        visible = state == 2
        self.current_properties['grid_visible'] = visible

    def change_gridline_width(self, width):
        self.current_properties['grid_width'] = width

    def choose_gridline_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl_gridlines_color_preview.setStyleSheet(f"background-color: {color.name()};")
            self.current_properties['grid_color'] = color.name()

    def apply_changes(self):
        if hasattr(self.ax_scatter, 'scatter_data'):
            ternary_data = self.ax_scatter.scatter_data
        marker = MARKER_STYLE_MAP.get(self.current_properties['marker'])
        size = self.current_properties['marker_size']
        color = self.current_properties['marker_color']
        alpha = self.current_properties['alpha']
        ax = self.ax_scatter
        ax.clear()
        scale = 1.0
        ternary_fig, tax = ternary.figure(scale=scale, ax=ax)
        tax.top_corner_label("Isotropic\n(sphere)", offset=0.2)
        tax.left_corner_label("Anisotropic\n(disc)", position=(0, -0.08))
        tax.right_corner_label("Anisotropic\n(rod)", position=(1, -0.08))
        tax.left_axis_label("c/a", offset=0.15)
        tax.right_axis_label("1-(b/a)", offset=0.15)
        tax.bottom_axis_label("(a-b)/(a-c)", offset=0.08)
        tax.boundary()
        tax.scatter(ternary_data, marker=marker, color=color, s=size, alpha=alpha)

        grid_visible = self.current_properties['grid_visible']
        if grid_visible:
            tax.gridlines(color=self.current_properties['grid_color'],
                          linewidth=self.current_properties['grid_width'],
                          multiple=0.1)
        else:
            self.tax.gridlines(linestyle='None')

        tax.ticks(axis='lbr', multiple=0.1, offset=0.02, tick_formats="%.1f", clockwise=True)
        tax.clear_matplotlib_ticks()
        tax.get_axes().axis('off')
        self.canvas.figure = ternary_fig
        self.canvas.resize(self.canvas.size().width() + 1, self.canvas.size().height())  # 强制触发resize
        self.canvas.resize(self.canvas.size().width() - 1, self.canvas.size().height())
        self.canvas.draw()

    def apply_and_close(self):
        self.apply_changes()
        self.accept()

    def cancel_and_close(self):
        self.reject()  # 关闭对话框


class ArrowPropertiesDialog(QDialog, Arrow_ui):
    def __init__(self, figure, canvas, arrow_annotation):
        super().__init__()
        self.setupUi(self)
        self.figure = figure
        self.canvas = canvas
        self.arrow_annotation = arrow_annotation

        self.original_visible = self.arrow_annotation.arrowprops.get('visible', True)
        self.original_color = to_hex(self.arrow_annotation.arrow_patch.get_facecolor())
        self.original_width = self.arrow_annotation.arrowprops['width']
        self.original_headwidth = self.arrow_annotation.arrowprops['headwidth']
        self.original_headlength = self.arrow_annotation.arrowprops['headlength']

        self.init_ui()
        self.bind()

    def init_ui(self):
        self.chk_show_arrow.setChecked(self.original_visible)
        self.lbl_color_preview.setStyleSheet(f"background-color: {self.original_color};")
        self.dsb_width.setValue(self.original_width)
        self.dsb_headwidth.setValue(self.original_headwidth)
        self.dsb_headlength.setValue(self.original_headlength)

    def bind(self):
        self.chk_show_arrow.stateChanged.connect(self.toggle_arrow)
        self.btn_color.clicked.connect(self.choose_color)
        self.dsb_width.valueChanged.connect(self.change_width)
        self.dsb_headwidth.valueChanged.connect(self.change_headwidth)
        self.dsb_headlength.valueChanged.connect(self.change_headlength)

        self.btn_ok.clicked.connect(self.apply_and_close)
        self.btn_cancel.clicked.connect(self.cancel_and_close)
        self.btn_apply.clicked.connect(self.apply_changes)

    def toggle_arrow(self):
        visible = self.chk_show_arrow.isChecked()
        self.arrow_annotation.set_visible(visible)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl_color_preview.setStyleSheet(f"background-color: {color.name()};")
            self.arrow_annotation.arrow_patch.set_color(color.name())

    def change_width(self, width):
        self.arrow_annotation.arrowprops['width'] = width

    def change_headwidth(self, width):
        self.arrow_annotation.arrowprops['headwidth'] = width

    def change_headlength(self, length):
        self.arrow_annotation.arrowprops['headlength'] = length

    def apply_changes(self):
        self.canvas.draw()

    def apply_and_close(self):
        self.apply_changes()
        self.accept()

    def cancel_and_close(self):
        self.arrow_annotation.set_visible(self.original_visible)
        self.arrow_annotation.arrow_patch.set_color(self.original_color)
        self.arrow_annotation.arrowprops['width'] = self.original_width
        self.arrow_annotation.arrowprops['headwidth'] = self.original_headwidth
        self.arrow_annotation.arrowprops['headlength'] = self.original_headlength
        self.reject()


class RectanglePropertiesDialog(QDialog, Rectangle_ui):
    def __init__(self, figure, canvas, rectangle):
        super().__init__()
        self.setupUi(self)

        self.figure = figure
        self.canvas = canvas
        self.rectangle = rectangle

        self.original_line_visible = self.rectangle.get_linestyle() not in ["none", "None", " ", ""]
        self.original_line_style = self.rectangle.get_linestyle()
        self.original_line_width = self.rectangle.get_linewidth()
        self.original_line_color = QColor(to_hex(self.rectangle.get_edgecolor()))

        self.init_ui()
        self.bind()

    def init_ui(self):
        self.chk_show_rectangle.setChecked(self.original_line_visible)
        self.cmb_line_style.setCurrentText(next(k for k, v in LINE_STYLE_MAP.items() if v == self.original_line_style))
        self.dsb_line_width.setValue(self.original_line_width)
        self.lbl_line_color_preview.setStyleSheet(f"background-color: {self.original_line_color.name()};")

    def bind(self):
        self.chk_show_rectangle.stateChanged.connect(self.toggle_line)
        self.cmb_line_style.currentTextChanged.connect(self.change_line_style)
        self.dsb_line_width.valueChanged.connect(self.change_line_width)
        self.btn_line_color.clicked.connect(self.choose_line_color)

        self.btn_ok.clicked.connect(self.apply_and_close)
        self.btn_cancel.clicked.connect(self.cancel_and_close)
        self.btn_apply.clicked.connect(self.apply_changes)

    def toggle_line(self, state):
        visible = state == 2
        if not visible:
            self.rectangle.set_linestyle('None')

    def change_line_style(self, style_text):
        linestyle = LINE_STYLE_MAP.get(style_text)
        self.rectangle.set_linestyle(linestyle)

    def change_line_width(self, width):
        self.rectangle.set_linewidth(width)

    def choose_line_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lbl_line_color_preview.setStyleSheet(f"background-color: {color.name()};")
            self.rectangle.set_edgecolor(color.name())

    def apply_changes(self):
        self.canvas.draw()

    def apply_and_close(self):
        self.apply_changes()
        self.accept()

    def cancel_and_close(self):
        self.chk_show_rectangle.setChecked(self.original_line_visible)
        self.rectangle.set_linestyle(self.original_line_style)
        self.rectangle.set_linewidth(self.original_line_width)
        self.rectangle.set_edgecolor(self.original_line_color.name())
        self.reject()


class AnnotationPropertiesDialog(QDialog, Annotation_ui):
    def __init__(self, figure, canvas, annotation):
        super().__init__()
        self.setupUi(self)
        self.figure = figure
        self.canvas = canvas
        self.annotation = annotation

        self.original_arrow_visible = self.annotation.arrowprops.get('visible', True)
        self.original_arrow_color = to_hex(self.annotation.arrow_patch.get_facecolor())
        self.original_annotation_size = self.annotation.get_fontsize()
        self.original_annotation_color = self.annotation.get_color()

        self.init_ui()
        self.bind()

    def init_ui(self):
        self.chk_show_arrow.setChecked(self.original_arrow_visible)
        self.lbl_arrow_color_preview.setStyleSheet(f"background-color: {self.original_arrow_color};")
        self.spb_annotation_size.setValue(self.original_annotation_size)
        self.lbl_annotation_color_preview.setStyleSheet(f"background-color: {self.original_annotation_color};")

    def bind(self):
        self.chk_show_arrow.stateChanged.connect(self.toggle_arrow)
        self.btn_arrow_color.clicked.connect(self.choose_arrow_color)
        self.spb_annotation_size.valueChanged.connect(self.change_annotation_size)
        self.btn_annotation_color.clicked.connect(self.choose_annotation_color)

        self.btn_ok.clicked.connect(self.apply_and_close)
        self.btn_cancel.clicked.connect(self.cancel_and_close)
        self.btn_apply.clicked.connect(self.apply_changes)

    def toggle_arrow(self):
        visible = self.chk_show_arrow.isChecked()
        self.annotation.set_visible(visible)

    def choose_arrow_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.annotation.arrow_patch.set_color(color.name())
            self.lbl_arrow_color_preview.setStyleSheet(f"background-color: {color.name()};")

    def change_annotation_size(self, size):
        self.annotation.set_fontsize(size)

    def choose_annotation_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.annotation.set_color(color.name())
            self.lbl_annotation_color_preview.setStyleSheet(f"background-color: {color.name()};")

    def apply_changes(self):
        self.canvas.draw()

    def apply_and_close(self):
        self.apply_changes()
        self.accept()

    def cancel_and_close(self):
        self.annotation.set_visible(self.original_arrow_visible)
        self.annotation.arrow_patch.set_color(self.original_arrow_color)
        self.annotation.set_fontsize(self.original_annotation_size)
        self.annotation.set_color(self.original_annotation_color)
        self.reject()


def plot_csd(data, unit):
    fig, ax = plt.subplots()
    ax.plot(data['Midpoint'], data['ln(Population density)'], marker='o', color='#F47575', markeredgecolor='#7E0A0A',
            linestyle='-', linewidth=1.5)
    ax.set_xlabel(f'Equivalent Sphere Diameter (ESD, {unit})')
    ax.set_ylabel(f'Ln(population density) (n/ {unit}$^{{-4}}$)')
    ax.set_xlim(left=0)
    plt.tight_layout()

    return fig


def plot_frequency(data_esd, data_vol, bar_width, unit):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    bar_container = ax1.bar(data_esd['Bin Center'], data_esd['Count'], width=bar_width, alpha=1,
                            align='center', label='Frequency', color='#FEE53F', edgecolor='#000000',
                            linewidth=1, linestyle='-')
    ax2.plot(data_esd['Bin Center'], data_esd['Cumulative Frequency'],
             label='Cumulative Frequency',
             color='#808080', linestyle='--', linewidth=1.5, marker='None')
    ax2.plot(data_vol['EqDiameter'], data_vol['Cumulative Frequency of Volume'],
             label='Cumulative Volume',
             color='#808080', linestyle='-', linewidth=1.5, marker='None')

    ax1.set_xlabel(f'Equivalent Sphere Diameter (ESD, {unit})')
    ax1.set_ylabel('Frequency')
    ax1.set_xlim(left=0)
    ax1.set_yscale('log')
    ax1.set_ylim(0.1,
                 10 ** np.ceil(np.log10(data_esd['Count'].max())))

    ax2.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1, decimals=0))
    ax2.set_xlim(left=0)
    ax2.set_ylim(0, 1)
    ax2.set_yticks([i / 10 for i in range(11)])
    legend = ax2.legend(loc='center right', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    return fig, bar_container, legend


def plot_shape_univariate_density(data):
    fig, ax = plt.subplots()

    kde_width3d_thickness3d_ratio = gaussian_kde(data['Width3D/Thickness3D'])
    x_width3d_thickness3d = np.linspace(data['Width3D/Thickness3D'].min(), data['Width3D/Thickness3D'].max(), 150)
    density_width3d_thickness3d = kde_width3d_thickness3d_ratio(x_width3d_thickness3d)
    kde_thickness3d_length3d_ratio = gaussian_kde(data['Thickness3D/Length3D'])
    x_thickness3d_length3d = np.linspace(data['Thickness3D/Length3D'].min(), data['Thickness3D/Length3D'].max(), 150)
    density_thickness3d_length3d = kde_thickness3d_length3d_ratio(x_thickness3d_length3d)

    ax.plot(x_width3d_thickness3d, density_width3d_thickness3d, label='Width3D/Thickness3D', color='#ff7f0e')
    ax.plot(x_thickness3d_length3d, density_thickness3d_length3d, label='Thickness3D/Length3D', color='#2ca02c')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    ax.set_title('Univariate KDE Plot of Morphology')
    legend = ax.legend()
    plt.tight_layout()
    data_kde_width3d_thickness3d = pd.DataFrame({
        'Width3D/Thickness3D': x_width3d_thickness3d,
        'Density': density_width3d_thickness3d,
    })
    data_kde_thickness3d_length3d = pd.DataFrame({
        'Thickness3D/Length3D': x_thickness3d_length3d,
        'Density': density_thickness3d_length3d,
    })

    return fig, data_kde_width3d_thickness3d, data_kde_thickness3d_length3d, legend


def plot_shape_multivariate_density(data):
    fig, ax = plt.subplots()

    # 计算点密度
    x = data['Width3D/Thickness3D']
    y = data['Thickness3D/Length3D']
    xy = np.vstack([x, y])
    kde = gaussian_kde(xy)
    z = kde(xy)
    z_min, z_max = z.min(), z.max()
    z_norm_unsort = (z - z_min) / (z_max - z_min)
    idx = z_norm_unsort.argsort()
    x, y, z_norm = x[idx], y[idx], z_norm_unsort[idx]
    cmap = "Spectral_r"

    # 在 ax1 上绘制散点图
    scatter = ax.scatter(
        x,
        y,
        c=z_norm,  # 点的颜色根据计算的密度值
        cmap=cmap,
        alpha=0.8,
        edgecolor=None
    )
    # 添加 colorbar
    norm = colors.Normalize(vmin=0, vmax=1)
    sm = ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax)
    cbar.set_label('Increasing Density(normalized) →')

    ax.set_xlabel('Width3D/Thickness3D')
    ax.set_ylabel('Thickness3D/Length3D')
    ax.set_title('Multivariate KDE Scatter Plot of Morphology')
    plt.tight_layout()

    data_multivariate_density = pd.DataFrame({
        'Width3D': data['Width3D'],
        'Thickness3D': data['Thickness3D'],
        'Length3D': data['Length3D'],
        'Width3D/Thickness3D': data['Width3D/Thickness3D'],
        'Thickness3D/Length3D': data['Thickness3D/Length3D'],
        'Normalized Density': z_norm_unsort
    })

    return fig, scatter, sm, cbar, data_multivariate_density


def plot_shape_ternary(data):
    # 计算三元比值
    data['c/a'] = data['c'] / data['a']
    data['1-(b/a)'] = 1 - (data['b'] / data['a'])
    data['(a-b)/(a-c)'] = (data['a'] - data['b']) / (data['a'] - data['c'])
    ternary_data = list(zip(data['c/a'], data['1-(b/a)'], data['(a-b)/(a-c)']))

    ternary_fig, tax = ternary.figure(scale=1.0)
    ax_scatter = tax.scatter(ternary_data, marker='o', color='blue', s=10, alpha=0.6)
    ax_scatter.scatter_data = ternary_data

    ternary_fig.set_size_inches(10, 10)

    tax.top_corner_label("Isotropic\n(sphere)", offset=0.2)
    tax.left_corner_label("Anisotropic\n(disc)", position=(0, -0.08))
    tax.right_corner_label("Anisotropic\n(rod)", position=(1, -0.08))
    tax.left_axis_label("c/a", offset=0.15)
    tax.right_axis_label("1-(b/a)", offset=0.15)
    tax.bottom_axis_label("(a-b)/(a-c)", offset=0.08)
    tax.boundary()
    tax.gridlines(color="#808080", multiple=0.1)

    tax.ticks(axis='lbr', multiple=0.1, offset=0.02, tick_formats="%.1f", clockwise=True)
    tax.clear_matplotlib_ticks()
    tax.get_axes().axis('off')

    shape_ternary_data = pd.DataFrame({
        'a': data['a'],
        'b': data['b'],
        'c': data['c'],
        'c/a': data['c/a'],
        '1-(b/a)': data['1-(b/a)'],
        '(a-b)/(a-c)': data['(a-b)/(a-c)']
    })
    return ternary_fig, tax, ax_scatter, shape_ternary_data


def plot_sphericity(data, unit, size_threshold):
    fig, ax = plt.subplots()

    x = data['EqDiameter']
    y = data['Sphericity']
    xy = np.vstack([x, y])
    kde = gaussian_kde(xy)
    z = kde(xy)
    z_min, z_max = z.min(), z.max()
    z_norm_unsort = (z - z_min) / (z_max - z_min)
    idx = z_norm_unsort.argsort()
    x, y, z_norm = x[idx], y[idx], z_norm_unsort[idx]
    cmap = "Spectral_r"

    scatter = ax.scatter(
        x,
        y,
        c=z_norm,
        cmap=cmap,
        alpha=0.8,
        edgecolor=None
    )

    norm = colors.Normalize(vmin=0, vmax=1)
    sm = ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax)
    cbar.set_label('Increasing Density(normalized) →')
    ax.set_xscale('log')
    ax.set_ylim(0, 1)
    plt.xlim(size_threshold,
             right=10 ** np.ceil(np.log10(x.max())))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    ax.set_xlabel(f'Equivalent Sphere Diameter (ESD, {unit})')
    ax.set_ylabel('Sphericity')
    data_sphericity_density = pd.DataFrame({
        'EqDiameter': x,
        'Sphericity': y,
        'Normalized Density': z_norm_unsort
    })
    return fig, scatter, sm, data_sphericity_density


def plot_skeleton(data, label):
    sorted_data = data.sort_values(ascending=False).reset_index(drop=True)
    total_sum = sorted_data.sum()
    percentage = (sorted_data / total_sum) * 100
    ids = range(1, len(sorted_data) + 1)

    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot(ids, percentage, marker='o', markersize=6, color='#F47575', linestyle='-', linewidth=1.5)
    ax.set_yscale('log')
    ax_ymin = 10 ** np.floor(np.log10(percentage[percentage > 0].min()))
    ax_ymax = 10 ** np.ceil(np.log10(percentage.max()))
    ax.set_ylim(ax_ymin, ax_ymax)
    ax.set_xlim(left=0)
    ax.set_xlabel('ID of Interconnected Segment')
    ax.set_ylabel(f'% of Total Skeleton {label}')

    ax_inset = fig.add_axes([0.55, 0.56, 0.41, 0.40])  # [left, bottom, width, height]
    ax_inset.plot(ids[:10], percentage[:10], marker='o', markersize=6, color='#F47575', linestyle='-', linewidth=1.5)
    ax_inset.set_xticks(ids[:10])
    ax_inset.set_yscale('log')
    ax_inset.set_xlim(0, 10)
    ax_inset_ymin = 10 ** np.floor(np.log10(percentage[:10].min()))
    ax_inset_ymax = 10 ** np.ceil(np.log10(percentage[:10].max()))
    ax_inset.set_ylim(ax_inset_ymin, ax_inset_ymax)
    first_point_y = percentage[0]
    if first_point_y > 67:
        xytext = (2, 90)
    else:
        xytext = (2, first_point_y * 1.5)
    annotatation = ax_inset.annotate(f'{first_point_y:.2f}',
                                     xy=(1, first_point_y),
                                     xytext=xytext,
                                     color='#F47575',
                                     fontsize=10,
                                     arrowprops=dict(arrowstyle="->", color='#F47575'))

    rect = plt.Rectangle((0, ax_inset_ymin), 10.3, ax_inset_ymax - ax_inset_ymin, linestyle='--',
                         linewidth=1.5, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    10 ** np.floor(np.log10(percentage[:10].min()))
    arrow_start_x = 10.1
    arrow_start_y = 10 ** ((np.log10(ax_inset_ymax) + np.log10(ax_inset_ymin)) / 2)
    arrow_end_x = len(sorted_data) * 0.45
    arrow_end_y = 10 ** (np.log10(ax_ymin) + ((np.log10(ax_ymax) - np.log10(ax_ymin)) * 0.75))
    arrow_annotation = ax.annotate('', xy=(arrow_end_x, arrow_end_y), xytext=(arrow_start_x, arrow_start_y),
                                   arrowprops=dict(color='#000000', shrink=0.05, width=1.5, headwidth=10,
                                                   headlength=12))
    return fig, ax, ax_inset, ids, percentage, arrow_annotation, rect, annotatation


def plot_frequency_pore(pore_data, throat_data, pore_vol_data, throat_channel_length_data, bar_width):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    bar_container_pore = ax1.bar(pore_data['Bin Center'], pore_data['Relative Frequency'], width=bar_width,
                                 align='center', label='Pore Body', color='#ff7f0e', edgecolor='#000000',
                                 alpha=0.3, linewidth=1, linestyle='-')
    bar_container_throat = ax1.bar(throat_data['Bin Center'], throat_data['Relative Frequency'], width=bar_width,
                                   align='center', label='Pore Throat', color='#2ca02c', edgecolor='#000000',
                                   alpha=0.3, linewidth=1, linestyle='-')

    line_pore_volume = ax2.plot(pore_vol_data['Pore EqRadius'],
                                pore_vol_data['Cumulative Frequency of Pore Body Volume'],
                                label='Cumulative Pore Volume', color='#808080', linestyle='-',
                                linewidth=1.5,
                                marker='None')
    line_throat_channellength = ax2.plot(throat_channel_length_data['Throat EqRadius'],
                                         throat_channel_length_data[
                                             'Cumulative Frequency of Pore Throat ChannelLength'],
                                         label='Cumulative Throat ChannelLength', color='#808080',
                                         linestyle='--', linewidth=1.5,
                                         marker='None')

    ax1.set_xlabel('Radius')
    ax1.set_ylabel('Frequency(%)')

    ax1.set_xlim(left=0)
    ax1.set_ylim(bottom=0)
    ax1.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1, decimals=0))
    ax2.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1, decimals=0))
    ax2.set_xlim(left=0)
    ax2.set_ylim(0, 1)
    ax2.set_yticks([i / 10 for i in range(11)])

    handles, labels = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    handles += handles2
    labels += labels2

    legend = fig.legend(handles, labels, loc='lower right', bbox_to_anchor=(1, 0.1), bbox_transform=ax1.transAxes)
    plt.tight_layout()

    return fig, bar_container_pore, bar_container_throat, legend


def plot_frequency_ar(data_ar, bar_width):
    fig, ax = plt.subplots()
    bar_container = ax.bar(data_ar['Bin Center'], data_ar['Relative Frequency'], width=bar_width,
                           align='center', label='Aspect Ratio', color='#AFAFAF', edgecolor='#000000',
                           alpha=0.3, linewidth=1, linestyle='-')

    ax.set_xlabel('Aspect Ratio')
    ax.set_ylabel('Frequency(%)')
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1, decimals=0))
    plt.tight_layout()

    return fig, bar_container


def plot_frequency_trapped_phase(pore_data, throat_data, trapped_phase_data, bar_width):
    fig, ax = plt.subplots()
    bar_container_pore = ax.bar(pore_data['Bin Center'], pore_data['Count'], width=bar_width,
                                align='center', label='Pore Body', color='#3ABF99', edgecolor='#000000',
                                alpha=0.5, linewidth=1, linestyle='-')
    bar_container_throat = ax.bar(throat_data['Bin Center'], throat_data['Count'], width=bar_width,
                                  align='center', label='Pore Throat', color='#2C91E0', edgecolor='#000000',
                                  alpha=0.5, linewidth=1, linestyle='-')
    bar_container_trapped_phase = ax.bar(trapped_phase_data['Bin Center'], trapped_phase_data['Count'], width=bar_width,
                                         align='center', label='Trapped Phase', color='#F0A73A', edgecolor='#000000',
                                         alpha=0.5, linewidth=1, linestyle='-')
    ax.set_xlabel('Radius')
    ax.set_ylabel('Frequency')

    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    ax.legend()
    plt.tight_layout()

    return fig, bar_container_pore, bar_container_throat, bar_container_trapped_phase


def populate_table(table_widget, data):
    table_widget.setRowCount(len(data))
    table_widget.setColumnCount(len(data.columns))
    table_widget.setHorizontalHeaderLabels(data.columns)
    table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    reversed_data = data.iloc[::-1]

    for i in range(len(reversed_data)):
        for j, key in enumerate(data.columns):
            value = data.iloc[i, j]
            formatted_value = format_value(key, value)

            item = QTableWidgetItem(formatted_value)

            # 将格式化的值设置到表格中
            table_widget.setItem(i, j, item)


def format_value(key, value):
    if key in ['Bin Center', 'Midpoint', 'Width3D', 'Thickness3D', 'Length3D', 'ln(Population density)',
               'Relative Frequency', 'Cumulative Frequency', 'EqDiameter', 'Cumulative Frequency of Volume',
               'Width3D/Thickness3D', 'Thickness3D/Length3D', 'Density', 'Normalized Density', 'a', 'b', 'c', 'c/a',
               '1-(b/a)', '(a-b)/(a-c)', 'Sphericity', 'Pore EqRadius', 'Cumulative Frequency of Pore Body Volume',
               'Throat EqRadius', 'Cumulative Frequency of Pore Throat ChannelLength']:
        return f"{value:.5g}"
    elif key in ["Count", "Cumulative Count"]:
        return f'{value:.0f}'
    elif key in ["Volumetric number density", "Population density"]:
        return f'{value:.3e}'
    else:
        return str(value)


def save_data(data, default_filename, parent):
    options = QFileDialog.Options()
    safe_filename = default_filename.replace("/", "_")
    file_path, file_type = QFileDialog.getSaveFileName(parent,
                                                       f'Save {default_filename}',
                                                       safe_filename,
                                                       "CSV Files (*.csv);;Excel Files (*.xlsx);;All Files (*)",
                                                       options=options)
    if file_path:
        if file_path.lower().endswith('.csv'):
            data.to_csv(file_path, index=False)
            QMessageBox.information(parent, "Success", "Data successfully saved as a CSV file.")
        elif file_path.lower().endswith('.xlsx'):
            data.to_excel(file_path, index=False)
            QMessageBox.information(parent, "Success", "Data successfully saved as an XLSX file.")
        else:
            QMessageBox.warning(parent, "Warning", "The selected file format is unsupported.")


def save_chart(canvas, default_filename, parent):
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getSaveFileName(
        parent,
        f'Save {default_filename} Figure as',
        default_filename,
        "PNG Files (*.png);;JPG Files (*.jpg);;JPEG Files (*.jpeg);;TIF Files (*.tif);;TIFF Files (*.tiff);;PDF Files (*.pdf);;SVG Files (*.svg);;EPS Files (*.eps);;All Files (*)",
        options=options
    )
    if file_path:
        file_extension = file_path.split('.')[-1].lower()
        if file_extension == 'eps':
            canvas.figure.savefig(file_path, format='eps', pad_inches=0.5, transparent=False)
        elif file_extension in ['png', 'jpg', 'jpeg', 'tif', 'tiff']:
            canvas.figure.savefig(file_path, format=file_extension, dpi=300, pad_inches=0.5)
        elif file_extension in ['pdf', 'svg']:
            canvas.figure.savefig(file_path, format=file_extension, pad_inches=0.5, transparent=True)
        else:
            QMessageBox.warning(parent, "Warning", "The selected file format is not supported.")
            return
        QMessageBox.information(parent, "Success", "The figure has been saved successfully.")
