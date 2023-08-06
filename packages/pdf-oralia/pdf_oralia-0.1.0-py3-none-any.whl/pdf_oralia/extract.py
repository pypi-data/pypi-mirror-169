from pathlib import Path

import pdfplumber

from .extract_charge import extract_charge
from .extract_locataire import extract_situation_loc

charge_table_settings = {
    "vertical_strategy": "lines",
    "horizontal_strategy": "text",
}


def extract_from_pdf(pdf, charge_dest, location_dest):
    """Build charge_dest and location_dest xlsx file from pdf"""
    loc_table = []
    for page in pdf.pages:
        situation_loc_line = [
            l
            for l in page.extract_text().split("\n")
            if "SITUATION DES LOCATAIRES" in l
        ]
        if situation_loc_line:
            mois, annee = situation_loc_line[0].split(" ")[-2:]
            if loc_table:
                loc_table += page.extract_table()[1:]
            else:
                loc_table = page.extract_table()

        if "HONORAIRES" in page.extract_text():
            df_charge = extract_charge(page.extract_table(charge_table_settings))
            df_charge.to_excel(charge_dest, sheet_name="Charges", index=False)
            print(f"{charge_dest} saved")

    df_loc = extract_situation_loc(loc_table, mois=mois, annee=annee)
    df_loc = df_loc.assign()
    df_loc.to_excel(location_dest, sheet_name="Location", index=False)
    print(f"{location_dest} saved")


def extract_save(pdf_file, dest):
    """Extract charge and locataire for pdf_file and put xlsx file in dest"""
    pdf_file = Path(pdf_file)
    xls_charge = dest / f"{pdf_file.stem.replace(' ', '_')}_charge.xlsx"
    xls_locataire = dest / f"{pdf_file.stem.replace(' ', '_')}_locataire.xlsx"

    pdf = pdfplumber.open(pdf_file)
    extract_from_pdf(pdf, xls_charge, xls_locataire)
