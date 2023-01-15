import pandas as pd
iris = pd.read_csv("data/iris_modified.csv" , sep = ";")
with pd.ExcelWriter( "iris2.xlsx" , engine = "openpyxl" ) as writer:
    for variety in set(iris.variety.values):
        print(variety)
        iris.loc[ iris.variety == variety ].to_excel( excel_writer = writer , sheet_name = variety )