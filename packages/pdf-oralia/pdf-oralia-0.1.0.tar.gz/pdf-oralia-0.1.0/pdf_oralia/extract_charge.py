import numpy as np
import pandas as pd


def extract_charge(table):
    """From pdfplumber table extract the charge dataframe"""
    df = (
        pd.DataFrame(table[1:], columns=table[0])
        .replace("", np.nan)
        .dropna(subset=["Débits"])
        .astype(
            {
                "Débits": "float64",
                "Crédits": "float64",
                "Dont T.V.A.": "float64",
                "Locatif": "float64",
                "Déductible": "float64",
            }
        )
    )
    drop_index = df[
        df["RECAPITULATIF DES OPERATIONS"].str.contains("TOTAUX", case=False)
        | df["RECAPITULATIF DES OPERATIONS"].str.contains("solde", case=False)
    ].index
    df.drop(drop_index, inplace=True)

    df[""].mask(
        df["RECAPITULATIF DES OPERATIONS"].str.contains("honoraires", case=False),
        "IMI GERANCE",
        inplace=True,
    )

    return df
