import os
import re
import sys
import image_rc
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog, QHeaderView, QTableWidgetItem, \
    QInputDialog
import qtmodern.styles
import pandas as pd
import numpy as np
from lxml import etree

import Modules.plot
from Modules.UI.CTDataToolbox_UI import Ui_Form


class CTDataToolbox(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.filepath = None
        self.filepath2 = None
        self.data = None
        self.data2 = None
        self.sheet_name = None
        self.converted_data = None
        self.conversion_factor = self.get_conversion_factor(1, 2)
        self.data_volume = None
        self.data_length = None
        self.input_unit = "µm"
        self.display_unit = "mm"
        self.voxel_size = None
        self.voxel_size_display = None
        self.volume3d = None
        self.volume3d_display = None
        self.tw_length.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tw_volume.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.filepath_pnm = None
        self.filepath_multi_pore = None
        self.data_pore = None
        self.data_throat = None
        self.data_ar = None
        self.data_pore_multi_pore = None
        self.data_throat_multi_pore = None
        self.bind()

    def bind(self):
        self.btn_load_file.clicked.connect(self.open_file)
        self.btn_clear_data.clicked.connect(self.clear_data)
        self.btn_get_para.clicked.connect(self.get_parameters)
        self.btn_save_para.clicked.connect(self.save_parameters)
        self.btn_cal_csd.clicked.connect(self.data_process_csd)
        self.btn_cal_frequency.clicked.connect(self.data_process_frequency)
        self.btn_cal_shape.clicked.connect(self.data_process_shape)
        self.btn_cal_sphericity.clicked.connect(self.data_process_sphericity)
        self.btn_cal_all.clicked.connect(self.data_process_all)
        self.btn_load_file_2.clicked.connect(self.open_file2)
        self.btn_clear_data_2.clicked.connect(self.clear_data2)
        self.btn_cal_dis.clicked.connect(self.cal_skeleton)
        self.btn_save_length.clicked.connect(self.save_length)
        self.btn_save_volume.clicked.connect(self.save_volume)
        self.btn_load_file_pnm.clicked.connect(self.open_file_pnm)
        self.btn_clear_data_pnm.clicked.connect(self.clear_data_pnm)
        self.btn_cal_fre_pore.clicked.connect(self.data_process_fre_pore)
        self.btn_cal_fre_ar.clicked.connect(self.data_process_fre_ar)
        self.btn_load_file_multi_pore.clicked.connect(self.open_file_multi_pore)
        self.btn_clear_data_multi_pore.clicked.connect(self.clear_data_multi_pore)
        self.btn_cal_trapped_phase.clicked.connect(self.data_process_trapped_phase)

        self.cmb_unit_input.currentIndexChanged.connect(self.update_conversion_factors)
        self.cmb_unit_display.currentIndexChanged.connect(self.update_conversion_factors)

        self.le_voxel_size.textChanged.connect(self.update_voxel_size)
        self.le_volume3d.textChanged.connect(self.update_volume3d)

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setStyleSheet("""
                QMessageBox {
                    font-size: 14px;
                }
            """)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText("\n" + message)
        msg_box.setWindowTitle("Error")
        msg_box.exec()

    def open_file(self):
        filepath, _ = QFileDialog.getOpenFileName(None, "Open Data", "",
                                                  "All files (*);; CSV files (*.csv);;Excel files (*.xls *.xlsx);;XML files (*.xml)"
                                                  )
        if filepath:
            _, file_extension = os.path.splitext(filepath)
            file_extension = file_extension.lower()
            if file_extension not in ['.csv', '.xls', '.xlsx', '.xml']:
                self.show_error_message("Please select a valid file type (csv, xls, xlsx, or xml).")
            else:
                self.load_data(filepath, file_extension)
                self.filepath = filepath

    def load_data(self, filepath, file_extension):
        try:
            data = None
            sheet_name = None
            if file_extension == '.csv':
                data = pd.read_csv(filepath)
            elif file_extension in ['.xls', '.xlsx']:
                data, sheet_name = self.load_excel_file(filepath)
            elif file_extension == '.xml':
                data, sheet_name = self.load_xml_file(filepath)

            if data is not None:
                self.data = data
                self.sheet_name = sheet_name
                if sheet_name:
                    message = f"File '{os.path.basename(filepath)}' (Sheet '{sheet_name}') imported successfully!"
                else:
                    message = f"File '{os.path.basename(filepath)}' imported successfully!"
                QMessageBox.information(self, "Load Successful", message)

        except Exception as e:
            QMessageBox.critical(self, "Load Failed", f"Failed to load file: {str(e)}")
            return

        self.convert_data(self.conversion_factor)

    def clear_data(self):
        self.cmb_unit_input.setCurrentIndex(1)
        self.cmb_unit_display.setCurrentIndex(2)
        self.spb_log10.setValue(5)
        self.spb_log2.setValue(1)
        self.spb_num_bins.setValue(50)
        self.tbw_size_scale_csd.setCurrentIndex(0)
        self.tbw_size_scale_fre.setCurrentIndex(0)

        self.le_voxel_size.clear()
        self.le_volume3d.clear()
        self.le_linear.clear()
        self.le_bin_size.clear()
        self.txb_stat.clear()

        self.filepath = None
        self.data = None
        self.converted_data = None
        self.conversion_factor = self.get_conversion_factor(1, 2)
        self.input_unit = "µm"
        self.display_unit = "mm"
        self.lbl_unit.setText("mm")
        self.lbl_unit_2.setText("mm")
        self.voxel_size = None
        self.voxel_size_display = None
        self.volume3d = None
        self.volume3d_display = None

        self.plot_window_csd.close()
        self.plot_window_fre.close()
        self.plot_window_univariate_density.close()
        self.plot_window_multivariate_density.close()
        self.plot_window_shape_ternary.close()
        self.plot_window_sphericity.close()

    def get_parameters(self):
        if not self.filepath:
            self.show_error_message("Please load the file!")
            return
        if self.check_if_le_empty(self.le_voxel_size):
            return
        if self.check_if_le_empty(self.le_volume3d):
            return

        required_columns = ['eqdiameter']
        data = self.converted_data
        if not self.check_required_columns(required_columns, data):
            return

        total_numbers = len(data)
        total_volume = data["volume3d"].sum()
        min_esd = data['eqdiameter'].min()
        max_esd = data['eqdiameter'].max()
        min_volume = data['volume3d'].min()
        min_volume_percentage = (min_volume / total_volume) * 100
        max_volume = data['volume3d'].max()
        max_volume_percentage = (max_volume / total_volume) * 100
        volume_modal = total_volume / self.volume3d_display if self.volume3d_display != 0 else 0

        if self.sheet_name:
            stats_text = (
                f"File '{os.path.basename(self.filepath)}' (Sheet '{self.sheet_name}')\n"
                f"Voxel Size = {self.voxel_size_display} {self.display_unit}\n"
                f"Total measured Volume3d = {self.volume3d_display:.2f} {self.display_unit}³\n"
                f"The number of grains = {total_numbers}\n"
                f"Total Volume of grains = {total_volume:.2f} {self.display_unit}³\n"
                f"Minimum ESD = {min_esd:.2f} {self.display_unit}\n"
                f"Maximum ESD = {max_esd:.2f} {self.display_unit}\n"
                f"Minimum Volume (%) = {min_volume:.2f} {self.display_unit}³ ({min_volume_percentage:.2f}%)\n"
                f"Maximum Volume (%) = {max_volume:.2f} {self.display_unit}³ ({max_volume_percentage:.2f}%)\n"
                f"Volume modal = {volume_modal:.2f}（%)"
            )
        else:
            stats_text = (
                f"File '{os.path.basename(self.filepath)}'\n"
                f"Voxel Size = {self.voxel_size_display} {self.display_unit}\n"
                f"Total measured Volume3d = {self.volume3d_display:.2f} {self.display_unit}³\n"
                f"The number of grains = {total_numbers}\n"
                f"Total Volume of grains = {total_volume:.2f} {self.display_unit}³\n"
                f"Minimum ESD = {min_esd:.2f} {self.display_unit}\n"
                f"Maximum ESD = {max_esd:.2f} {self.display_unit}\n"
                f"Minimum Volume (%) = {min_volume:.2f} {self.display_unit}³ ({min_volume_percentage:.2f}%)\n"
                f"Maximum Volume (%) = {max_volume:.2f} {self.display_unit}³ ({max_volume_percentage:.2f}%)\n"
                f"Volume modal = {volume_modal:.2f}（%)"
            )
        self.txb_stat.setPlainText(stats_text)

    def save_parameters(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Parameters", "Parameters",
                                                   "Text Files (*.txt);;All Files (*)",
                                                   options=options)

        if file_name:
            try:
                text = self.txb_stat.toPlainText()
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(text)
                QMessageBox.information(self, "Success", "The parameters have been saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save the parameters: {e}")

    def data_process_csd(self):
        size_scale_index = self.tbw_size_scale_csd.currentIndex()
        if not self.filepath:
            self.show_error_message("Please load the file!")
            return
        if self.check_if_le_empty(self.le_voxel_size, self.le_volume3d):
            return
        if not self.check_required_columns(['eqdiameter'], self.converted_data):
            return

        eqdiameter = self.converted_data['eqdiameter']
        size_threshold = 4 * self.voxel_size_display
        esd_filtered = eqdiameter[eqdiameter >= size_threshold]
        bin_midpoints = []

        if size_scale_index == 0:
            # 对数划分
            size_interval = self.spb_log10.value()
            min_bin = 10 ** np.floor(np.log10(size_threshold))  # 数量级的起始点

            log_bins = []
            current_bin = min_bin
            while current_bin <= esd_filtered.max():
                next_bin = current_bin * 10 ** (1 / size_interval)
                log_bins.append(next_bin)
                current_bin = next_bin
            bins = np.array(log_bins)
            log_bins_log10 = np.log10(log_bins)
            log_bin_midpoints = (log_bins_log10[:-1] + log_bins_log10[1:]) / 2
            bin_midpoints = 10 ** log_bin_midpoints

        elif size_scale_index == 1:
            # Phi 划分
            size_interval = self.spb_log2.value()
            min_bin = 2 ** np.floor(np.log2(size_threshold))  # 数量级的起始点

            log_bins = []
            current_bin = min_bin
            while current_bin <= esd_filtered.max():
                next_bin = current_bin * 2 ** (1 / size_interval)
                log_bins.append(next_bin)
                current_bin = next_bin
            bins = np.array(log_bins)
            log_bins_log2 = np.log2(log_bins)
            log_bin_midpoints = (log_bins_log2[:-1] + log_bins_log2[1:]) / 2
            bin_midpoints = 2 ** log_bin_midpoints

        elif size_scale_index == 2:
            if self.check_if_le_empty(self.le_linear):
                return
            if not self.check_if_le_valid_numbers(self.le_linear):
                return
            size_interval = float(self.le_linear.text())
            # 固定间隔
            bins = np.arange(size_threshold, esd_filtered.max() + size_interval, size_interval)
            bin_midpoints = (bins[:-1] + bins[1:]) / 2

        count, _ = np.histogram(esd_filtered, bins=bins)
        volumetric_number_density = count / self.volume3d_display
        bin_widths = bins[1:] - bins[:-1]
        population_density = volumetric_number_density / bin_widths
        ln_nv = np.full_like(population_density, -np.inf, dtype=np.float64)
        nonzero_indices = population_density > 0
        ln_nv[nonzero_indices] = np.log(population_density[nonzero_indices])

        bin_labels = [f"{bins[i]:.5g}-{bins[i + 1]:.5g}" for i in range(len(bins) - 1)]
        data_csd = pd.DataFrame({
            'Bin': bin_labels,
            'Count': count,
            'Volumetric number density': volumetric_number_density,
            'Population density': population_density,
            'Midpoint': bin_midpoints,
            'ln(Population density)': ln_nv
        })

        fig = Modules.plot.plot_csd(data_csd, self.display_unit)
        self.plot_window_csd = Modules.plot.PlotWindow_CSD(fig, data_csd)
        self.plot_window_csd.show()

    def data_process_frequency(self):
        if not self.filepath:
            self.show_error_message("Please load the file!")
            return
        if not self.check_required_columns(['eqdiameter', 'volume3d'], self.converted_data):
            return

        eqdiameter = self.converted_data['eqdiameter']
        volume3d = self.converted_data['volume3d']

        if self.tbw_size_scale_fre.currentIndex() == 0:
            if self.check_if_le_empty(self.le_bin_size):
                return
            if not self.check_if_le_valid_numbers(self.le_bin_size):
                return
            bin_size = float(self.le_bin_size.text())
            bin_size_decimal_places = len(str(bin_size).split(".")[1]) if "." in str(bin_size) else 0
            min_value = np.floor(min(eqdiameter) * (10 ** bin_size_decimal_places)) / (10 ** bin_size_decimal_places)
            max_value = np.ceil(max(eqdiameter) * (10 ** bin_size_decimal_places)) / (10 ** bin_size_decimal_places)
            bins = np.arange(min_value, max_value + bin_size, bin_size)

        elif self.tbw_size_scale_fre.currentIndex() == 1:
            bin_count = self.spb_num_bins.value()
            min_value = np.floor(min(eqdiameter))
            max_value = max(eqdiameter)
            bins = np.linspace(min_value, max_value, bin_count + 1)
            bin_size = (max_value - min_value) / bin_count

        count, bin_edges = np.histogram(eqdiameter, bins=bins)
        bin_midpoints = (bins[:-1] + bins[1:]) / 2
        cumulative_count = np.cumsum(count)
        relative_frequency = count / np.sum(count)
        cumulative_frequency = np.cumsum(relative_frequency)

        sorted_indices = np.argsort(eqdiameter)
        sorted_eqdiameter = eqdiameter.iloc[sorted_indices]
        sorted_volume3d = volume3d.iloc[sorted_indices]
        cumulative_volume_ratio = np.cumsum(sorted_volume3d) / np.sum(volume3d)

        bin_labels = [f"{bins[i]:.5g}-{bins[i + 1]:.5g}" for i in range(len(bin_edges) - 1)]
        esd_frequency_data = pd.DataFrame({
            'Bin': bin_labels,
            'Bin Center': bin_midpoints,
            'Count': count,
            'Cumulative Count': cumulative_count,
            'Relative Frequency': relative_frequency,
            'Cumulative Frequency': cumulative_frequency
        })
        cumulative_volume_data = pd.DataFrame({
            'EqDiameter': sorted_eqdiameter,
            'Cumulative Frequency of Volume': cumulative_volume_ratio
        })
        fig, bar_container, legend = Modules.plot.plot_frequency(esd_frequency_data, cumulative_volume_data, bin_size,
                                                                 self.display_unit)
        self.plot_window_fre = Modules.plot.PlotWindow_Fre(fig, esd_frequency_data, cumulative_volume_data,
                                                           bar_container, legend)
        self.plot_window_fre.show()

    def data_process_shape(self):
        if not self.filepath:
            self.show_error_message("Please load the file!")
            return

        required_columns_group1 = ['length3d', 'thickness3d', 'width3d']
        required_columns_group2 = ['a', 'b', 'c']
        missing_columns = [col for col in required_columns_group1 + required_columns_group2 if
                           col not in self.converted_data.columns]
        if len(missing_columns) == 6:
            self.show_error_message("Missing columns of shape('length3d', 'thickness3d', 'width3d' or 'a', 'b', 'c')")
            return
        if set(required_columns_group1).issubset(self.converted_data.columns):
            if self.check_required_columns(required_columns_group1, self.converted_data):
                length3d = self.converted_data['length3d']
                thickness3d = self.converted_data['thickness3d']
                width3d = self.converted_data['width3d']

                width3d_thickness3d_ratio = width3d / thickness3d
                thickness3d_length3d_ratio = thickness3d / length3d

                morphologies_data = pd.DataFrame({
                    'Width3D': width3d,
                    'Thickness3D': thickness3d,
                    'Length3D': length3d,
                    'Width3D/Thickness3D': width3d_thickness3d_ratio,
                    'Thickness3D/Length3D': thickness3d_length3d_ratio,
                })

                fig_univariate_density, data_kde_width3d_thickness3d, data_kde_thickness3d_length3d, legend = Modules.plot.plot_shape_univariate_density(
                    morphologies_data)
                self.plot_window_univariate_density = Modules.plot.PlotWindow_Morphology_Univar(fig_univariate_density,
                                                                                                data_kde_width3d_thickness3d,
                                                                                                data_kde_thickness3d_length3d,
                                                                                                legend)
                self.plot_window_univariate_density.show()

                fig_univariate_multivariate, scatter, sm, cbar, data_multivariate_density = Modules.plot.plot_shape_multivariate_density(
                    morphologies_data)
                self.plot_window_multivariate_density = Modules.plot.PlotWindow_Morphology_Multi(
                    fig_univariate_multivariate, scatter, sm, cbar, data_multivariate_density)
                self.plot_window_multivariate_density.show()
        else:
            missing_in_group1 = [col for col in required_columns_group1 if col not in self.converted_data.columns]
            self.show_error_message(f"Missing columns of morphologies: {', '.join(missing_in_group1)}")

        if set(required_columns_group2).issubset(self.converted_data.columns):
            if self.check_required_columns(required_columns_group2, self.converted_data):
                a = self.converted_data['a']
                b = self.converted_data['b']
                c = self.converted_data['c']

                shape_data = pd.DataFrame({
                    'a': a,
                    'b': b,
                    'c': c
                })

                fig_shape_ternary, tax, ax_scatter, shape_ternary_data = Modules.plot.plot_shape_ternary(shape_data)
                self.plot_window_shape_ternary = Modules.plot.PlotWindow_Shape(fig_shape_ternary, shape_ternary_data,
                                                                               tax, ax_scatter)
                self.plot_window_shape_ternary.show()
        else:
            missing_in_group2 = [col for col in required_columns_group2 if col not in self.converted_data.columns]
            self.show_error_message(f"Missing columns in shape: {', '.join(missing_in_group2)}")

    def data_process_sphericity(self):
        if not self.filepath:
            self.show_error_message("Please load the file!")
            return
        if self.check_if_le_empty(self.le_voxel_size):
            return
        if not self.check_required_columns(['eqdiameter', 'sphericity'], self.converted_data):
            return
        eqdiameter = self.converted_data['eqdiameter']
        sphericity = self.converted_data['sphericity']
        size_threshold = 4 * self.voxel_size_display

        sphericity_data = pd.DataFrame({
            'EqDiameter': eqdiameter,
            'Sphericity': sphericity
        })

        fig, scatter, sm, data_sphericity_density = Modules.plot.plot_sphericity(sphericity_data, self.display_unit,
                                                                                 size_threshold)
        self.plot_window_sphericity = Modules.plot.PlotWindow_Sphericity(fig, scatter, sm, data_sphericity_density)
        self.plot_window_sphericity.show()

    def data_process_all(self):
        self.data_process_csd()
        self.data_process_frequency()
        self.data_process_shape()
        self.data_process_sphericity()

    def load_excel_file(self, filepath):
        try:
            sheet_names = pd.ExcelFile(filepath, engine='openpyxl').sheet_names
            if len(sheet_names) > 1:
                sheet_name, ok = QInputDialog.getItem(self, "Select Sheet",
                                                      "This file contains multiple sheets. Please select a sheet to analyze:",
                                                      sheet_names, 0, False)
                if ok and sheet_name:
                    data_excel = pd.read_excel(filepath, sheet_name=sheet_name, engine='openpyxl')
                    return data_excel, sheet_name
                else:
                    return None, None
            else:
                data_excel = pd.read_excel(filepath, engine='openpyxl')
                return data_excel, None

        except Exception as e:
            QMessageBox.critical(self, "Load Failed", f"Failed to load EXCEL file: {str(e)}")
            return None, None

    def load_xml_file(self, filepath):
        try:
            with open(filepath, 'r') as file:
                tree = etree.parse(file)
                root = tree.getroot()

                namespaces = {
                    'ss': 'urn:schemas-microsoft-com:office:spreadsheet'
                }

                sheets = root.findall('.//ss:Worksheet', namespaces)
                sheet_data = {}

                for sheet in sheets:
                    sheet_name = sheet.get(f'{{{namespaces["ss"]}}}Name')
                    rows = sheet.findall('.//ss:Row', namespaces)
                    data = []

                    for row in rows:
                        row_data = []
                        cells = row.findall('.//ss:Cell', namespaces)
                        for cell in cells:
                            data_elem = cell.find('.//ss:Data', namespaces)
                            row_data.append(data_elem.text if data_elem is not None else None)
                        data.append(row_data)
                    if data:
                        sheet_data[sheet_name] = pd.DataFrame(data[1:], columns=data[0])

                if len(sheet_data) > 1:
                    sheet_name, ok = QInputDialog.getItem(self, "Select Sheet",
                                                          "This file contains multiple sheets. Please select a sheet to analyze:",
                                                          list(sheet_data.keys()), 0, False)
                    if ok and sheet_name:
                        data_xml = sheet_data[sheet_name]
                        return data_xml, sheet_name
                    else:
                        return None, None
                else:
                    data_xml = list(sheet_data.values())[0]
                    return data_xml, None

        except Exception as e:
            QMessageBox.critical(self, "Load Failed", f"Failed to load XML file: {str(e)}")
            return None, None

    def check_required_columns(self, required_columns, dataframe):
        """
        Check if the specified DataFrame contains the required columns.

        Parameters:
        - required_columns: List of strings, names of the columns that must exist
        - dataframe: DataFrame object to check

        Returns:
        - Boolean: Returns True if all required columns are present, otherwise returns False and shows an error message
        """
        columns_found = [col for col in required_columns if col in dataframe.columns.str.lower()]
        if len(columns_found) < len(required_columns):
            missing_columns = [col for col in required_columns if col.lower() not in columns_found]
            self.show_error_message(f"Missing or empty column(s): {' or '.join(missing_columns)}")
            return False
        return True

    def update_voxel_size(self):
        if self.check_if_le_empty(self.le_voxel_size, show_errors=False):
            self.voxel_size = None
            self.voxel_size_display = None
            return
        if self.check_if_le_valid_numbers(self.le_voxel_size):
            self.voxel_size = float(self.le_voxel_size.text().strip())
            self.voxel_size_display = self.voxel_size * self.conversion_factor

    def update_volume3d(self):
        if self.check_if_le_empty(self.le_volume3d, show_errors=False):
            self.volume3d = None
            self.volume3d_display = None
            return
        if self.check_if_le_valid_numbers(self.le_volume3d):
            self.volume3d = float(self.le_volume3d.text().strip())
            self.volume3d_display = self.volume3d * (self.conversion_factor ** 3)

    def check_if_le_empty(self, *line_edits, show_errors=True):
        error_messages = {
            'le_voxel_size': "Voxel Size is required.",
            'le_volume3d': "Measured Volume3d is required.",
            'le_linear': "Please enter the linear size interval in 'CSD Size Scale'.",
            'le_bin_size': "Please enter the linear size interval in 'Frequency Size Scale'.",
            'le_bin_size_crys': "Please enter the Bin Size in 'Trapped Phase'.",
            'le_bin_max': "Please enter the Maximum bin End in 'Trapped Phase'.",
            'le_crys_radius': "Please enter the Trapped Phase Radius in 'Trapped Phase'.",
            'le_pore_id': "Please enter the Pore ID in 'Single Pore'.",

        }

        for line_edit in line_edits:
            text = line_edit.text().strip()
            if not text:
                object_name = line_edit.objectName()
                if show_errors and object_name in error_messages:
                    self.show_error_message(error_messages[object_name])
                return True
        return False

    def check_if_le_valid_numbers(self, *line_edits):
        for line_edit in line_edits:
            text = line_edit.text().strip()
            try:
                float(text)
            except ValueError:
                self.show_error_message(f"Invalid input: '{text}' is not a valid numerical value.")
                return False
        return True

    @staticmethod
    def get_conversion_factor(unit_input_index, unit_display_index):
        """
        获取转换因子
        """
        # 定义单位转换的因子（将其他单位转换为米）
        unit_factors = {
            0: 1e-9,  # 纳米 (nm) -> 米 (m)
            1: 1e-6,  # 微米 (μm) -> 米 (m)
            2: 1e-3,  # 毫米 (mm) -> 米 (m)
            3: 1e-2,  # 厘米 (cm) -> 米 (m)
            4: 1e-1,  # 分米 (dm) -> 米 (m)
            5: 1  # 米 (m) -> 米 (m)
        }

        unit_input_factor = unit_factors.get(unit_input_index, 1)
        unit_display_factor = unit_factors.get(unit_display_index, 2)
        conversion_factor = unit_input_factor / unit_display_factor
        return conversion_factor

    def update_conversion_factors(self):
        """
        更新单位转换因子，并自动更新数据
        """
        try:
            # 更新当前索引
            unit_input_index = self.cmb_unit_input.currentIndex()
            unit_display_index = self.cmb_unit_display.currentIndex()
            units = ['nm', 'μm', 'mm', 'cm', 'dm', 'm']

            self.conversion_factor = self.get_conversion_factor(unit_input_index, unit_display_index)
            self.input_unit = units[unit_input_index]
            self.display_unit = units[unit_display_index]
            self.lbl_unit.setText(self.display_unit)
            self.lbl_unit_2.setText(self.display_unit)

            if not self.check_if_le_empty(self.le_voxel_size, self.le_volume3d, show_errors=False):
                self.update_voxel_size()
                self.update_volume3d()
                self.convert_data(self.conversion_factor)
        except Exception as e:
            QMessageBox.critical(self, "", f"Error updating conversion factors: {e}")

    def convert_data(self, conversion_factor):
        """
        根据新的转换因子更新数据中的相关列
        """

        def apply_conversion(df, col, factor, power=1):
            return df[col] * (factor ** power)

        converted_data = self.data.copy()
        columns_to_convert = {
            'breadth3d': 1,
            'length3d': 1,
            'thickness3d': 1,
            'width3d': 1,
            'a': 1,
            'b': 1,
            'c': 1,
            'eqdiameter': 1,
            'area3d': 2,
            'volume3d': 3
        }
        new_column_names = {}
        # 遍历列，进行清理和转换
        for column in converted_data.columns:
            clean_column_name = re.sub(r'\s*\(.*?\)', '', column.lower()).strip()
            new_column_names[column] = clean_column_name

            converted_data[column] = pd.to_numeric(converted_data[column], errors='coerce')
            power = columns_to_convert.get(clean_column_name)
            if power:
                converted_data[column] = apply_conversion(converted_data, column, conversion_factor, power)

        converted_data.rename(columns=new_column_names, inplace=True)
        self.converted_data = converted_data

    def open_file2(self):
        fpath, _ = QFileDialog.getOpenFileName(None, "Open Data", "",
                                               "All files (*);; CSV files (*.csv);;Excel files (*.xls *.xlsx);;XML files (*.xml)"
                                               )
        if fpath:
            _, file_extension = os.path.splitext(fpath)
            file_extension = file_extension.lower()
            if file_extension not in ['.csv', '.xls', '.xlsx', '.xml']:
                self.show_error_message("Please select a valid file type (csv, xls, xlsx, or xml).")
            else:
                self.load_data2(fpath, file_extension)
                self.filepath2 = fpath

    def load_data2(self, filepath, file_extension):
        try:
            data = None
            sheet_name = None
            if file_extension == '.csv':
                data = pd.read_csv(filepath)
            elif file_extension in ['.xls', '.xlsx']:
                data, sheet_name = self.load_excel_file(filepath)
            elif file_extension == '.xml':
                data, sheet_name = self.load_xml_file(filepath)

            clean_column_names = [re.sub(r'\s*\(.*?\)', '', col).strip().lower() for col in data.columns]
            data.columns = clean_column_names

            # 检查所需的列是否存在
            required_columns = ['total volume', 'total length']
            if not self.check_required_columns(required_columns, data):
                return

            self.data2 = data
            if sheet_name:
                message = f"File '{os.path.basename(filepath)}' (Sheet '{sheet_name}') imported successfully!"
            else:
                message = f"File '{os.path.basename(filepath)}' imported successfully!"
            QMessageBox.information(self, "Load Successful", message)
            self.data_volume = self.data2.get('total volume')
            self.data_length = self.data2.get('total length')
            self.data_volume = pd.to_numeric(self.data_volume, errors='coerce')
            self.data_length = pd.to_numeric(self.data_length, errors='coerce')

        except Exception as e:
            QMessageBox.critical(self, "Load Failed", f"Failed to load file: {str(e)}")
            return

    def clear_data2(self):
        self.tw_length.clearContents()
        self.tw_length.setRowCount(0)  # 移除所有行
        self.tw_volume.clearContents()
        self.tw_volume.setRowCount(0)

        self.filepath2 = None
        self.data2 = None
        self.data_volume = None
        self.data_length = None

        self.plot_window_skel_length.close()
        self.plot_window_skel_volume.close()

    def cal_skeleton(self):
        if not self.filepath2:
            self.show_error_message("Please load the file!")
            return

        fig_volume, ax_volume, ax_inset_volume, ids_volume, pre_volume, arrow_annotation_volume, rect_volume, annotatation_volume = Modules.plot.plot_skeleton(
            self.data_volume, "Volume")
        fig_length, ax_length, ax_inset_length, ids_length, pre_length, arrow_annotation_length, rect_length, annotatation_length = Modules.plot.plot_skeleton(
            self.data_length, "Length")
        self.tw_length.setRowCount(len(ids_length))
        self.tw_volume.setRowCount(len(ids_volume))
        for row in range(len(ids_volume)):
            id_item = QTableWidgetItem(str(ids_volume[row]))
            pre_item = QTableWidgetItem(f"{pre_volume[row]:.5g}")
            self.tw_volume.setItem(row, 0, id_item)
            self.tw_volume.setItem(row, 1, pre_item)
        self.tw_volume.resizeColumnsToContents()
        self.tw_volume.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for row in range(len(ids_length)):
            id_item = QTableWidgetItem(str(ids_length[row]))
            pre_item = QTableWidgetItem(f"{pre_length[row]:.5g}")
            self.tw_length.setItem(row, 0, id_item)
            self.tw_length.setItem(row, 1, pre_item)
        self.tw_length.resizeColumnsToContents()
        self.tw_length.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.plot_window_skel_volume = Modules.plot.PlotWindow_Skel(fig_volume, ax_volume, ax_inset_volume,
                                                                    "% of Total Skeleton Volume",
                                                                    arrow_annotation_volume, rect_volume,
                                                                    annotatation_volume)
        self.plot_window_skel_length = Modules.plot.PlotWindow_Skel(fig_length, ax_length, ax_inset_length,
                                                                    "% of Total Skeleton Length",
                                                                    arrow_annotation_length, rect_length,
                                                                    annotatation_length)
        self.plot_window_skel_length.show()
        self.plot_window_skel_volume.show()

    def save_length(self):
        row_count = self.tw_length.rowCount()
        column_count = self.tw_length.columnCount()
        table_data = []

        for row in range(row_count):
            row_data = []
            for col in range(column_count):
                item = self.tw_length.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')  # 如果单元格为空，添加空字符串
            table_data.append(row_data)
        df = pd.DataFrame(table_data, columns=['ID of Interconnected Segment', '% of Total Skeleton Length'])
        Modules.plot.save_data(df, "% of Total Skeleton Length Data", self)

    def save_volume(self):
        row_count = self.tw_volume.rowCount()
        column_count = self.tw_volume.columnCount()

        table_data = []

        for row in range(row_count):
            row_data = []
            for col in range(column_count):
                item = self.tw_volume.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')
            table_data.append(row_data)
        df = pd.DataFrame(table_data, columns=['ID of Interconnected Segment', '% of Total Skeleton Volume'])
        Modules.plot.save_data(df, "% of Total Skeleton Volume Data", self)

    def open_file_pnm(self):
        filepath, _ = QFileDialog.getOpenFileName(None, "Open Data", "",
                                                  "All files (*);; Excel files (*.xls *.xlsx);;XML files (*.xml)"
                                                  )
        if filepath:
            _, file_extension = os.path.splitext(filepath)
            file_extension = file_extension.lower()
            if file_extension not in ['.xls', '.xlsx', '.xml']:
                self.show_error_message("Please select a valid file type (xls, xlsx, or xml).")
            else:
                self.load_data_pnm(filepath, file_extension)
                self.filepath_pnm = filepath

    def load_data_pnm(self, filepath, file_extension):
        try:
            data_pore = None
            data_throat = None
            if file_extension in ['.xls', '.xlsx']:
                data_pore, data_throat = self.load_excel_file_pnm(filepath)
            elif file_extension == '.xml':
                data_pore, data_throat = self.load_xml_file_pnm(filepath)

            if data_pore is not None and data_throat is not None:
                data_pore.columns = [col.lower().replace(" ", "").split('(')[0] for col in data_pore.columns]
                data_throat.columns = [col.lower().replace(" ", "").split('(')[0] for col in data_throat.columns]
                required_columns_pore = ['eqradius', 'volume', ]
                required_columns_throat = ['eqradius', 'channellength', 'poreid#1', 'poreid#2']
                if not self.check_required_columns2(required_columns_pore, data_pore, 'Pore Data'):
                    return
                if not self.check_required_columns2(required_columns_throat, data_throat, 'Throat Data'):
                    return
                data_pore, data_throat, data_ar = self.data_pnm(data_pore, data_throat)
                self.data_pore = data_pore
                self.data_throat = data_throat
                self.data_ar = data_ar
                QMessageBox.information(self, "Load Successful",
                                        f"File '{os.path.basename(filepath)}' imported successfully!")

        except Exception as e:
            QMessageBox.critical(self, "Load Failed", f"Failed to load file: {str(e)}")
            return

    def open_file_multi_pore(self):
        filepath, _ = QFileDialog.getOpenFileName(None, "Open Data", "",
                                                  "All files (*);; Excel files (*.xls *.xlsx);;XML files (*.xml)"
                                                  )
        if filepath:
            _, file_extension = os.path.splitext(filepath)
            file_extension = file_extension.lower()
            if file_extension not in ['.xls', '.xlsx', '.xml']:
                self.show_error_message("Please select a valid file type (xlx, xlsx, or xml).")
            else:
                self.load_data_multi_pore(filepath, file_extension)
                self.filepath_multi_pore = filepath

    def load_data_multi_pore(self, filepath, file_extension):
        try:
            data_pore_multi_pore = None
            data_throat_multi_pore = None
            if file_extension in ['.xls', '.xlsx']:
                data_pore_multi_pore, data_throat_multi_pore = self.load_excel_file_pnm(filepath)
            elif file_extension == '.xml':
                data_pore_multi_pore, data_throat_multi_pore = self.load_xml_file_pnm(filepath)

            if data_pore_multi_pore is not None and data_throat_multi_pore is not None:
                data_pore_multi_pore.columns = [col.lower().replace(" ", "").split('(')[0] for col in
                                                data_pore_multi_pore.columns]
                data_throat_multi_pore.columns = [col.lower().replace(" ", "").split('(')[0] for col in
                                                  data_throat_multi_pore.columns]
                required_columns_pore = ['eqradius', 'volume', ]
                required_columns_throat = ['eqradius', 'channellength', 'poreid#1', 'poreid#2']
                if not self.check_required_columns2(required_columns_pore, data_pore_multi_pore,
                                                    'Pore Data of Multi-Pore'):
                    return
                if not self.check_required_columns2(required_columns_throat, data_throat_multi_pore,
                                                    'Throat Data of Multi-Pore'):
                    return
                data_pore_multi_pore, data_throat_multi_pore, data_ar_multi_pore = self.data_pnm(data_pore_multi_pore,
                                                                                                 data_throat_multi_pore)
                self.data_pore_multi_pore = data_pore_multi_pore
                self.data_throat_multi_pore = data_throat_multi_pore
                QMessageBox.information(self, "Load Successful",
                                        f"File '{os.path.basename(filepath)}' imported successfully!")

        except Exception as e:
            QMessageBox.critical(self, "Load Failed", f"Failed to load file: {str(e)}")
            return

    def clear_data_pnm(self):
        self.filepath_pnm = None
        self.filepath_multi_pore = None
        self.data_pore = None
        self.data_throat = None
        self.data_ar = None
        self.data_pore_multi_pore = None
        self.data_throat_multi_pore = None

        self.dsb_bin_size_fre_pnm.setValue(100)
        self.spb_num_bins_fre_pnm.setValue(50)
        self.tbw_size_scale_fre_pnm.setCurrentIndex(0)
        self.dsb_bin_size_ar.setValue(0.25)
        self.spb_num_bins_ar.setValue(100)
        self.tbw_size_scale_ar.setCurrentIndex(0)
        self.tbw_pore.setCurrentIndex(0)

        self.le_bin_size_crys.clear()
        self.le_bin_max.clear()
        self.le_crys_radius.clear()
        self.le_pore_id.clear()

        self.plot_window_fre_pore.close()
        self.plot_window_fre_ar.close()
        self.plot_window_fre_trapped_phase.close()

    def clear_data_multi_pore(self):
        self.filepath_multi_pore = None
        self.data_pore_multi_pore = None
        self.data_throat_multi_pore = None

    def data_process_fre_pore(self):
        if not self.filepath_pnm:
            self.show_error_message("Please load the file!")
            return

        eqradius_pore = self.data_pore['eqradius']
        eqradius_throat = self.data_throat['eqradius']
        volume_pore = self.data_pore['volume']
        channel_length_throat = self.data_throat['channellength']
        max_eqradius = max(eqradius_pore.max(), eqradius_throat.max())
        min_eqradius = min(eqradius_pore.min(), eqradius_throat.min())
        bin_size = None

        if self.tbw_size_scale_fre_pnm.currentIndex() == 0:
            bin_size = self.dsb_bin_size_fre_pnm.value()
            bins = np.arange(min_eqradius, max_eqradius + bin_size, bin_size)

        elif self.tbw_size_scale_fre_pnm.currentIndex() == 1:
            bin_count = self.spb_num_bins_fre_pnm.value()
            bins = np.linspace(min_eqradius, max_eqradius, bin_count + 1)
            bin_size = (max_eqradius - min_eqradius) / bin_count

        count_pore, bins_pore = np.histogram(eqradius_pore, bins=bins)
        count_throat, bins_throat = np.histogram(eqradius_throat, bins=bins)
        bin_centers_pore = (bins_pore[:-1] + bins_pore[1:]) / 2
        bin_centers_throat = (bins_throat[:-1] + bins_throat[1:]) / 2
        cumulative_count_pore = np.cumsum(count_pore)
        cumulative_count_throat = np.cumsum(count_throat)
        relative_frequency_pore = count_pore / np.sum(count_pore)
        relative_frequency_throat = count_throat / np.sum(count_throat)
        cumulative_frequency_pore = np.cumsum(relative_frequency_pore)
        cumulative_frequency_throat = np.cumsum(relative_frequency_throat)
        bin_labels = [f"{bins[i]:.5g}-{bins[i + 1]:.5g}" for i in range(len(bins_pore) - 1)]

        sorted_eqradius_pore = np.sort(eqradius_pore)
        sorted_volume_pore = volume_pore[np.argsort(eqradius_pore)]
        cumulative_volume_pore = np.cumsum(sorted_volume_pore) / np.sum(sorted_volume_pore)

        sorted_eqradius_throat = np.sort(eqradius_throat)
        sorted_channel_length_throat = channel_length_throat[np.argsort(eqradius_throat)]
        cumulative_channel_length_throat = np.cumsum(sorted_channel_length_throat) / np.sum(
            sorted_channel_length_throat)

        pore_data = pd.DataFrame({
            'Bin': bin_labels,
            'Bin Center': bin_centers_pore,
            'Count': count_pore,
            'Cumulative Count': cumulative_count_pore,
            'Relative Frequency': relative_frequency_pore,
            'Cumulative Frequency': cumulative_frequency_pore
        })
        throat_data = pd.DataFrame({
            'Bin': bin_labels,
            'Bin Center': bin_centers_throat,
            'Count': count_throat,
            'Cumulative Count': cumulative_count_throat,
            'Relative Frequency': relative_frequency_throat,
            'Cumulative Frequency': cumulative_frequency_throat
        })

        pore_vol_data = pd.DataFrame({
            'Pore EqRadius': sorted_eqradius_pore,
            'Cumulative Frequency of Pore Body Volume': cumulative_volume_pore
        })

        throat_channel_length_data = pd.DataFrame({
            'Throat EqRadius': sorted_eqradius_throat,
            'Cumulative Frequency of Pore Throat ChannelLength': cumulative_channel_length_throat
        })

        fig, bar_container_pore, bar_container_throat, legend = Modules.plot.plot_frequency_pore(
            pore_data, throat_data,
            pore_vol_data,
            throat_channel_length_data,
            bin_size)
        self.plot_window_fre_pore = Modules.plot.PlotWindow_Fre_Pore(fig, pore_data, throat_data, pore_vol_data,
                                                                     throat_channel_length_data, bar_container_pore,
                                                                     bar_container_throat, legend)
        self.plot_window_fre_pore.show()

    def data_process_fre_ar(self):
        if not self.filepath_pnm:
            self.show_error_message("Please load the file!")
            return

        aspect_ratio = self.data_ar['ar']
        max_ar = aspect_ratio.max()
        min_ar = aspect_ratio.min()
        bin_size = None

        if self.tbw_size_scale_ar.currentIndex() == 0:
            bin_size = self.dsb_bin_size_ar.value()
            bins = np.arange(min_ar, max_ar + bin_size, bin_size)

        elif self.tbw_size_scale_ar.currentIndex() == 1:
            bin_count = self.spb_num_bins_ar.value()
            bins = np.linspace(min_ar, max_ar, bin_count + 1)
            bin_size = (max_ar - min_ar) / bin_count

        count_ar, bins_ar = np.histogram(aspect_ratio, bins=bins)
        bin_centers_ar = (bins_ar[:-1] + bins_ar[1:]) / 2
        cumulative_count_ar = np.cumsum(count_ar)
        relative_frequency_ar = count_ar / np.sum(count_ar)
        cumulative_frequency_ar = np.cumsum(relative_frequency_ar)

        bin_labels = [f"{bins[i]:.5g}-{bins[i + 1]:.5g}" for i in range(len(bins_ar) - 1)]

        data_ar = pd.DataFrame({
            'Bin': bin_labels,
            'Bin Center': bin_centers_ar,
            'Count': count_ar,
            'Cumulative Count': cumulative_count_ar,
            'Relative Frequency': relative_frequency_ar,
            'Cumulative Frequency': cumulative_frequency_ar
        })

        fig, bar_container = Modules.plot.plot_frequency_ar(data_ar, bin_size)
        self.plot_window_fre_ar = Modules.plot.PlotWindow_Fre_AR(fig, data_ar, bar_container)
        self.plot_window_fre_ar.show()

    def data_process_trapped_phase(self):
        if not self.filepath_pnm:
            self.show_error_message("Please load the file!")
            return
        if self.check_if_le_empty(self.le_bin_size_crys, self.le_bin_max, self.le_crys_radius):
            return
        if not self.check_if_le_valid_numbers(self.le_bin_size_crys, self.le_bin_max, self.le_crys_radius):
            return

        bin_size = float(self.le_bin_size_crys.text().strip())
        binx_max = float(self.le_bin_max.text().strip())
        bins = np.arange(0, binx_max + bin_size, bin_size)
        trapped_phase_radius = float(self.le_crys_radius.text().strip())
        trapped_phase_data = np.array([trapped_phase_radius])
        poreradius_data = None
        throatradius_data = None

        if self.tbw_pore.currentIndex() == 0:
            if self.check_if_le_empty(self.le_pore_id):
                return
            if not self.check_if_le_valid_numbers(self.le_pore_id):
                return
            pore_id = float(self.le_pore_id.text().strip())
            poreradius_data = self.data_pore[self.data_pore['poreid'] == pore_id]['eqradius']
            throatradius_data = self.data_ar[self.data_ar['poreid'] == pore_id]['throatradius']

        elif self.tbw_pore.currentIndex() == 1:
            if not self.filepath_multi_pore:
                self.show_error_message("Please load the multi-pore data file!")
                return
            poreradius_data = self.data_pore_multi_pore['eqradius']
            throatradius_data = self.data_throat_multi_pore['eqradius']

        count_pore, bins_pore = np.histogram(poreradius_data, bins=bins)
        count_throat, bins_throat = np.histogram(throatradius_data, bins=bins)
        count_trapped_phase, bins_trapped_phase = np.histogram(trapped_phase_data, bins=bins)
        bin_centers = (bins_pore[:-1] + bins_pore[1:]) / 2
        relative_frequency_pore = count_pore / np.sum(count_pore)
        relative_frequency_throat = count_throat / np.sum(count_throat)
        relative_frequency_trapped_phase = count_trapped_phase / np.sum(count_trapped_phase)

        bin_labels = [f"{bins[i]:.5g}-{bins[i + 1]:.5g}" for i in range(len(bins_pore) - 1)]

        pore_data = pd.DataFrame({
            'Bin': bin_labels,
            'Bin Center': bin_centers,
            'Count': count_pore,
            'Relative Frequency': relative_frequency_pore,
        })
        throat_data = pd.DataFrame({
            'Bin': bin_labels,
            'Bin Center': bin_centers,
            'Count': count_throat,
            'Relative Frequency': relative_frequency_throat,
        })
        trapped_phase_data = pd.DataFrame({
            'Bin': bin_labels,
            'Bin Center': bin_centers,
            'Count': count_trapped_phase,
            'Relative Frequency': relative_frequency_trapped_phase,
        })

        fig, bar_container_pore, bar_container_throat, bar_container_trapped_phase = Modules.plot.plot_frequency_trapped_phase(
            pore_data, throat_data, trapped_phase_data, bin_size)
        self.plot_window_fre_trapped_phase = Modules.plot.PlotWindow_Fre_Trapped_Phase(fig, pore_data, throat_data,
                                                                                       trapped_phase_data,
                                                                                       bar_container_pore,
                                                                                       bar_container_throat,
                                                                                       bar_container_trapped_phase)
        self.plot_window_fre_trapped_phase.show()

    def load_excel_file_pnm(self, filepath):
        try:
            sheet_names = pd.ExcelFile(filepath, engine='openpyxl').sheet_names
            pore_sheets = [sheet for sheet in sheet_names if 'pore' in sheet.lower()]
            throat_sheets = [sheet for sheet in sheet_names if 'throat' in sheet.lower()]

            data_pore = None
            data_throat = None

            if len(pore_sheets) == 1:
                pore_sheet = pore_sheets[0]
                data_pore = pd.read_excel(filepath, sheet_name=pore_sheet)

            if len(throat_sheets) == 1:
                throat_sheet = throat_sheets[0]
                data_throat = pd.read_excel(filepath, sheet_name=throat_sheet)

            if data_pore is None or data_throat is None:
                if data_pore is None:
                    sheet_name, ok = QInputDialog.getItem(self, "Select Sheet",
                                                          "Please select the pore data worksheet:",
                                                          sheet_names, 0, False)
                    if ok and sheet_name:
                        data_pore = pd.read_excel(filepath, sheet_name=sheet_name, engine='openpyxl')

                if data_throat is None:
                    sheet_name, ok = QInputDialog.getItem(self, "Select Sheet",
                                                          "Please select the throat data worksheet:",
                                                          sheet_names, 0, False)
                    if ok and sheet_name:
                        data_throat = pd.read_excel(filepath, sheet_name=sheet_name, engine='openpyxl')
            return data_pore, data_throat
        except Exception as e:
            QMessageBox.critical(self, "Load Failed", f"Failed to load EXCEL file: {str(e)}")
            return None, None

    def load_xml_file_pnm(self, filepath):
        try:
            with open(filepath, 'r') as file:
                tree = etree.parse(file)
                root = tree.getroot()

                namespaces = {
                    'ss': 'urn:schemas-microsoft-com:office:spreadsheet'
                }

                sheets = root.findall('.//ss:Worksheet', namespaces)
                sheet_data = {}

                for sheet in sheets:
                    sheet_name = sheet.get(f'{{{namespaces["ss"]}}}Name')
                    rows = sheet.findall('.//ss:Row', namespaces)
                    data = []

                    # Iterate through rows and extract data
                    for row in rows:
                        row_data = []
                        cells = row.findall('.//ss:Cell', namespaces)
                        for cell in cells:
                            data_elem = cell.find('.//ss:Data', namespaces)
                            row_data.append(data_elem.text if data_elem is not None else None)
                        data.append(row_data)

                    if data:
                        sheet_data[sheet_name] = pd.DataFrame(data[1:], columns=data[0])
                pore_sheets = [sheet for sheet in sheet_data if 'pore' in sheet.lower()]
                throat_sheets = [sheet for sheet in sheet_data if 'throat' in sheet.lower()]
                if len(pore_sheets) == 1:
                    data_pore = sheet_data[pore_sheets[0]]
                else:
                    data_pore = None

                if len(throat_sheets) == 1:
                    data_throat = sheet_data[throat_sheets[0]]
                else:
                    data_throat = None

                if data_pore is None or data_throat is None:
                    if data_pore is None:
                        sheet_name, ok = QInputDialog.getItem(self, "Select Sheet",
                                                              "Please select the pore data worksheet:",
                                                              list(sheet_data.keys()), 0, False)
                        if ok and sheet_name:
                            data_pore = sheet_data[sheet_name]

                    if data_throat is None:
                        sheet_name, ok = QInputDialog.getItem(self, "Select Sheet",
                                                              "Please select the throat data worksheet:",
                                                              list(sheet_data.keys()), 0, False)
                        if ok and sheet_name:
                            data_throat = sheet_data[sheet_name]
                return data_pore, data_throat

        except Exception as e:
            QMessageBox.critical(self, "Load Failed", f"Failed to load XML file: {str(e)}")
            return None, None

    @staticmethod
    def data_pnm(data_pore, data_throat):
        data_pore['eqradius'] = pd.to_numeric(data_pore['eqradius'], errors='coerce')
        data_pore['volume'] = pd.to_numeric(data_pore['volume'], errors='coerce')
        data_throat['eqradius'] = pd.to_numeric(data_throat['eqradius'], errors='coerce')
        data_throat['channellength'] = pd.to_numeric(data_throat['channellength'], errors='coerce')
        data_throat['poreradius#1'] = data_throat['poreid#1'].map(data_pore.set_index('poreid')['eqradius'])
        data_throat['poreradius#1'] = pd.to_numeric(data_throat['poreradius#1'], errors='coerce')
        data_throat['ar#1'] = data_throat['poreradius#1'] / data_throat['eqradius']
        data_throat['poreradius#2'] = data_throat['poreid#2'].map(data_pore.set_index('poreid')['eqradius'])
        data_throat['poreradius#2'] = pd.to_numeric(data_throat['poreradius#2'], errors='coerce')
        data_throat['ar#2'] = data_throat['poreradius#2'] / data_throat['eqradius']

        data_ar_1 = data_throat[['throatid', 'eqradius', 'poreid#1', 'poreradius#1', 'ar#1']].rename(
            columns={'eqradius': 'throatradius', 'poreid#1': 'poreid', 'poreradius#1': 'poreradius', 'ar#1': 'ar'})
        data_ar_2 = data_throat[['throatid', 'eqradius', 'poreid#2', 'poreradius#2', 'ar#2']].rename(
            columns={'eqradius': 'throatradius', 'poreid#2': 'poreid', 'poreradius#2': 'poreradius', 'ar#2': 'ar'})

        data_ar = pd.concat([data_ar_1, data_ar_2], ignore_index=True)

        return data_pore, data_throat, data_ar

    def check_required_columns2(self, required_columns, dataframe, sheet):
        columns_found = [col for col in required_columns if col in dataframe.columns.str.lower()]
        if len(columns_found) < len(required_columns):
            missing_columns = [col for col in required_columns if col.lower() not in columns_found]
            self.show_error_message(f"Missing or empty column(s) in '{sheet}': {' or '.join(missing_columns)}")
            return False
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':/image/logo.png'))
    main_window = CTDataToolbox()
    qtmodern.styles.light(app)
    main_window.show()
    sys.exit(app.exec())
