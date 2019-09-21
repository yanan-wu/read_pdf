# -*- coding: utf-8 -*

import pdfplumber
import pandas as pd


def open_pdf():
    pdf = pdfplumber.open("../file/sample.pdf")
    p0 = pdf.pages[0]
    table = p0.extract_table()
    df = pd.DataFrame(table[1:], columns=table[0])
    print(df.head())

    text = p0.extract_text()
    print(text)

open_pdf()