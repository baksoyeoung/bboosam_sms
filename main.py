import pandas as pd
import glob

try:
    path = './'
    files = glob.glob(path + "*.xlsx")
    excel = pd.DataFrame()

    for file_name in files:
        excel = pd.read_excel(file_name)
        
        
        

    print(excel)



except Exception as ex:
    print('error: ' + str(ex))