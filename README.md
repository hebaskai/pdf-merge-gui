# pdf-merge-gui
Little GUI to merge PDF files on a local computer (devel on PC-Win) using Python Python 3.10.9 == One static folder containing certificates, diplomas, LoR etc &amp; one dynamic folder with current CL + Resume. Whatever the HR submission system wants merged you are prepared and covered.

# PDF Merge GUI

PDF Merge GUI is a Python application that allows you to merge multiple PDF files into a single PDF document with a user-friendly graphical interface. This tool is built using Python 3.10.9 and the Tkinter library for creating the GUI.

## Description

PDF Merge GUI is a user-friendly tool developed using Python 3.10.9 for merging PDF files on a local computer. It offers a simple graphical interface that allows users to combine multiple PDF files into a single document. The tool is designed to streamline the process of merging certificates, diplomas, letters of recommendation, and other documents required for HR submissions.

The tool consists of two folders: a static folder that contains pre-existing certificates, diplomas, and other static files, and a dynamic folder where users can place their current cover letter and resume. By having a dedicated static folder and dynamic folder, users can easily merge the required files based on the specific requirements of HR submission systems.

With PDF Merge GUI, users can select the desired PDF files from the dynamic folder and combine them with the files in the static folder. The tool provides an intuitive interface for selecting files, specifying the output filename, and choosing the destination folder for the merged PDF document.

By leveraging Python 3.10.9 and the PyPDF2 library, PDF Merge GUI ensures efficient merging of PDF files while maintaining the integrity of the original documents.

Whether you need to merge files for job applications, scholarship submissions, or other HR-related processes, PDF Merge GUI offers a convenient solution to streamline the document merging process, making it easier to submit comprehensive and organized application packages.


## Features

- Select a directory and view the PDF files available for merging
- Checkbox selection to choose specific files for merging
- Specify an output filename for the merged PDF document
- Validate the output filename to ensure it is not empty
- Merge the selected PDF files into a single PDF document
- Choose the output directory for the merged PDF

## Requirements

- Python 3.10.9 or higher
- PyPDF2 library
- Tkinter library

## Installation

1. Clone the repository:

    `git clone https://github.com/hebaskai/pdf-merge-gui.git`

    Change into the project directory:

    ```bash
    cd pdf-merge-gui
    ```

2. **Install the required dependencies:**

    ```bash
    pip install PyPDF2
    ```

    _**For Anaconda users:**_

    [https://www.anaconda.com](https://www.anaconda.com)
    ```bash
    conda install -c conda-forge pypdf2
    ```

3. **Usage**

    Please update the code to meet your specific folder requirements. The current static folder is:

    ```python
    STATIC_FOLDER = "C:/temp/CV_LoS_Diplomas_etc"
    ```

    Run the program by executing the following command:

    ```bash
    python pdf_merge_gui.py
    ```

    _Note: If you use multiple monitors, look around for the little grey GUI._

    - Click the "Select Directory" button to choose a directory containing PDF files.
    - Check the PDF files you want to merge from the displayed list.
    - Enter a valid output filename in the "Output Filename" field.
    - Click the "Merge PDFs" button to merge the selected PDF files.
    - Choose the output directory for the merged PDF file in the dialog window.


**Contributing**
Contributions are welcome! If you have any suggestions or improvements, please feel free to submit a pull request.

**Acknowledgments**
The PyPDF2 library: https://pythonhosted.org/PyPDF2/
The Tkinter library: https://docs.python.org/3/library/tkinter.html

Feel free to customize and enhance the README file according to your specific project requirements and the additional information you want to include.

**Code distributed under MIT License**

Copyright (c) 2023 hebaskai

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CNTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
