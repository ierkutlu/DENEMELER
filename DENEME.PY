import pandas as pd
dosya_yolu='/Users/macibo/Desktop/deneme.xlsx'
veri=pd.ExcelFile(dosya_yolu)
print(veri.sheet_names)
