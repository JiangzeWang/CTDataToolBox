# CTDataToolbox

[**CTDataToolbox**](https://github.com/JiangzeWang/CTDataToolBox) is an advanced software designed for processing and analyzing high-resolution X-ray computed tomography (HRXCT) data. The software is particularly useful for researchers and professionals working in fields such as mineral analysis, material science, and geology. It allows users to perform a wide variety of data processing tasks, including crystal size distribution (CSD) analysis, frequency analysis, morphology and shape analysis, sphericity calculations, skeletonization, and pore network modeling. The tool also includes powerful visualization and data export functionalities to support efficient analysis.

## Key Features:
  - Crystal Size Distribution: Analyze particle size, volume distribution, and morphology.
  - Skeleton Analysis: Quantify phase connectivity and spatial distribution.
  - Pore-Network Modeling: Extract pore-throat parameters and simulate fluid flow.

## Installation

1. **Clone the Repository:**
   To get the latest version of the software, clone the repository:
   ```bash
   git clone https://github.com/JiangzeWang/CTDataToolbox.git
2. **Install Dependencies:**
   Install all the necessary Python libraries by running the following:
   ```bash
   pip install -r requirements.txt
3. **Run the Application:**:
   Start the software by executing the following command:
   ```bash
   python CTDataToolbox.py
   
## Getting Started
### 1.Data Preparation
- **Supported Formats:**
  - **CSD Module**: CSV, XLSX, XML (require eqdiameter, volume3d).
  - **Skeleton Module**: CSV, XLSX (require total volume, total length).
  - **PNM Module**: XLSX, XML (require eqradius, channellength).

### 2.Interface Navigation
- **Module Switch:** Use top tabs to select CSD, Skeleton, or pore network modeling.

### 3.Data Import: 
- Click the **Load Data File** button to import your CT scan data from supported file formats (CSV, Excel, or XML).
- The software will automatically detect and validate the file format and structure. If the file is valid, it will load into the application.
- Multi-sheet Handling: Manually select a worksheet if needed.

### 4. Data Processing
- **Crystal Size Distribution (CSD) Module**: 
  - **Get Parameters**: Extract statistics (crystal count, volume distribution).
  - **CSD**: For calculating the crystal size distribution.
  - **Frequency**: For evaluating the distribution of particle sizes and volumes.
  - **Shape and Morphology**:  For analyzing particle shape and structure.
  - **Sphericity**: For calculating the sphericity based on equivalent diameters.
- **Skeleton Module**:
  - **Calculate and Display Figures**: Compute volume/length contributions.
- **Pore-network modeling**: 
  - **Pore Throat Frequency**: Analyze pore-throat radius distributions.
  - **Aspect Ratio Frequency**: Analyze frequency distribution of pore-throat radius ratios.
  - **Trapped Phase**: Process trapped phase data and generate histograms.

### 5.Visualize Data
- **Visualizations**: Create various charts, including:
  - Histograms
  - Cumulative frequency plots
  - Scatter plots
  - Ternary plots for shape analysis
- **Chart Customization**: Modify styles, colors, and line types for charts to fit specific preferences.

### 6.Data Export
After analyzing and visualizing the data, you can export:
- **Export Processed Data**: Save processed data tables in CSV, Excel, or text format for further analysis.
- **Save Visualizations**: Export generated charts as image files (PNG, JPG, PDF, SVG, etc.).

## Requirements
The following dependencies are required to run CTDataToolbox:
- Python 3.10 or later
- PySide6: For the graphical user interface
- pandas: For data manipulation
- numpy: For numerical computations
- matplotlib: For data visualization
- scipy: For scientific computing
- ternary: For ternary plot visualizations
- lxml: For parsing XML files
- qtmodern: For modern Qt-style widgets

## License
This project is licensed under the **MIT License**.

*Copyright © [2025] [Jiangze Wang].*

Full text available at [LICENSE](./LICENSE)。

## Contact Us

If you have any questions or suggestions, please contact us:

- **Email**: wangjiangze@gig.ac.cn
- **GitHub Repository**: [https://github.com/JiangzeWang/CTDataToolBox](https://github.com/JiangzeWang/CTDataToolBox)
- **GitHub Issues**: [https://github.com/JiangzeWang/CTDataToolBox/issues](https://github.com/JiangzeWang/CTDataToolBox/issues)  

**Tip**: We recommend running the sample data first to get familiar with the workflow!
