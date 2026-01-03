import numpy as np
import pandas as pd

def cleanPortfolio(CSV_FILE):

    CSV = pd.read_csv(CSV_FILE, skiprows=2, skipfooter=2)

    investment_names = CSV["Symbol"].tolist()
    investment_qty = CSV["Qty (Quantity)"].tolist()

    return {"names": investment_names, "qty": investment_qty}
