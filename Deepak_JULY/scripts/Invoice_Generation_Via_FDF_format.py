from os import remove
from os import system
import fdfgen

#Get field Name by command: pdftk [file_name] dump_data_fields
#Download PDFTK: https://www.pdflabs.com/tools/pdftk-server/
field_names = ["Registered Shareholder Name"]
all_fields = []
#Prompt the user to provide values for the respective fields
for i in range(len(field_names)):
     field_value = raw_input(field_names[i] + ": ")
     all_fields.append((field_names[i], field_value))
#Create FDF file with these fields
fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
fdf_file = open("file_fdf.fdf","w")
fdf_file.write(fdf_data)
fdf_file.close()
#Run pdftk system command to populate the pdf file. The file "file_fdf.fdf" is pushed in to "input_pdf.pdf" thats generated as a new "output_pdf.pdf" file.
pdftk_cmd = "pdftk forms.pdf fill_form file_fdf.fdf output output_pdf.pdf flatten"

#pdftk_cmd = "pdftk {input_pdf} fill_form file_fdf.fdf output {output_pdf} flatten".format(output_pdf = PDF_OutputOrder_file, input_pdf = "GMO_SGM_MM_PurchaseOrder_BUY_Format.pdf")
system(pdftk_cmd)
remove("file_fdf.fdf")