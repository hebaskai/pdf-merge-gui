# inventor: hebaskai
# copilot: ChatGPT 3.5 (free version)
# date created: 11-Jul-2023
# Code distributed under MIT License
# Copyright (c) 2023 hebaskai

import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

STATIC_FOLDER = "C:/temp/CV_LoS_Diplomas_etc"

def get_pdf_files(directory):
    pdf_files = []
    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            pdf_files.append(file)
    return pdf_files

pdf_files_static = get_pdf_files(STATIC_FOLDER)
selected_folder = ""

def select_directory1():
    global selected_folder
    selected_folder = select_directory()
    pdf_files = pdf_files_static + get_pdf_files(selected_folder)
    show_files(pdf_files)
    
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        return directory
    return ""
            
def show_files(files):
    global file_vars
    file_list.delete(0, tk.END)
    file_vars = []  # Create a list to hold IntVar objects
    for file in files:
        var = tk.IntVar()
        checkbox = tk.Checkbutton(root, text=file, variable=var)
        checkbox.pack(anchor="w")
        file_list.insert(tk.END, file)
        file_vars.append(var)  # Append the IntVar to the list

def merge_pdfs():
    selected_files = []
    for file, var in zip(file_list.get(0, tk.END), file_vars):
        if var.get() == 1:
            selected_files.append(file)

    if len(selected_files) == 0:
        messagebox.showwarning("No files selected", "Please select at least one PDF file!")
        return
    elif len(selected_files) > 10:
        messagebox.showwarning("Too many files selected", "Please select a maximum of three PDF files!")
        return

    output_filename = output_textbox.get()
    
    if not output_filename:
        messagebox.showwarning("Filename not entered", "Please enter a filename for the merged PDF!")
        return

    if not output_filename.endswith(".pdf"):
        output_filename += ".pdf"

    output_directory = filedialog.askdirectory()
    if output_directory:
        output_filepath = os.path.join(output_directory, output_filename)
    else:
        return

    pdfMerge = PyPDF2.PdfFileMerger()

    for filename in selected_files:
        if filename in pdf_files_static:
            filepath = os.path.join(STATIC_FOLDER, filename)
        else:
            filepath = os.path.join(selected_folder, filename)
        pdfFile = open(filepath, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfMerge.append(pdfReader)
        pdfFile.close()

    pdfMerge.write(output_filepath)
    pdfMerge.close()
    messagebox.showinfo("Merge Complete", "PDF files merged successfully!")

root = tk.Tk()

directory1_button = tk.Button(root, text="Select Directory", command=select_directory1)
directory1_button.pack()

file_list = tk.Listbox(root)
file_list.pack()

output_label = tk.Label(root, text="Output Filename:")
output_label.pack()

output_textbox = tk.Entry(root)
output_textbox.pack()

merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack()

root.mainloop()
