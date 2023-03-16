# pip install pdf2image

import os
import tempfile
from pdf2image import convert_from_path
output_folder = os.getcwd()  # current work directory


def pdf_to_png(pdf_name, source, destino):
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(pdf_path=source+"/"+pdf_name,
                                             dpi=100,
                                             output_folder=destino,
                                             fmt="png",
                                             poppler_path=output_folder + "/poppler-23.01.0/Library/bin",
                                             output_file=pdf_name[:-4],
                                             single_file=True)


for filename in os.listdir(output_folder):
    if filename.endswith(".pdf"):
        pdf_to_png(filename, output_folder, output_folder)
        
print("ok!")
