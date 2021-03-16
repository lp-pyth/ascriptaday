# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 09:49:45 2021
PDFKIT (wkhtmltopdf) HTML to PDF
@author: lux
"""

#install wkhtmltopdf from https://wkhtmltopdf.org/downloads.html

import pdfkit
config = pdfkit.configuration(wkhtmltopdf=r"PATH_TO_wkhtmltopdf.exe_HERE")
url = "YOUR_URL_HERE"
path = r"PATH_TO_FOLDER_HERE"
pdfkit.from_url(url, path, configuration=config)