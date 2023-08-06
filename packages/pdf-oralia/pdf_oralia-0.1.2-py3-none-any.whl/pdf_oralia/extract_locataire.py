import pandas as pd


def parse_above_loc(content):
    row = {}
    try:
        app, loc = content.split("\n")
    except ValueError:
        row["lot"] = ""
        row["type"] = ""
        row["locataire"] = content

    else:
        app_ = app.split(" ")
        row["lot"] = app_[1]
        row["type"] = " ".join(app_[2:])
        row["locataire"] = loc
    return pd.Series(row)


def extract_situation_loc(table, mois, annee):
    """From pdfplumber table extract locataire df"""
    try:
        df = pd.DataFrame(table[1:], columns=table[0])
    except IndexError:
        print(table)
    rows = []
    for i, row in df[df["Locataires"] == "Totaux"].iterrows():
        above_row_loc = df.iloc[i - 1]["Locataires"]
        up_row = pd.concat(
            [
                row,
                parse_above_loc(above_row_loc),
            ]
        )

        rows.append(up_row)
    df_cleaned = pd.concat(rows, axis=1).T
    df_cleaned.drop(["Locataires", "", "Période"], axis=1, inplace=True)

    df_cleaned = df_cleaned.astype(
        {
            "Loyers": "float64",
            "Taxes": "float64",
            "Provisions": "float64",
            "Divers": "float64",
            "Total": "float64",
            "Réglés": "float64",
            "Impayés": "float64",
        },
        errors="ignore",
    )

    df_cleaned = df_cleaned.assign(mois=mois, annee=annee)
    return df_cleaned
