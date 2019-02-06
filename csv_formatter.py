import pandas as pd
import glob

def to_csv(csvfile, file_name):
    csvfile.csv.to_csv(file_name)

class CsvFile(object):

    def __init__(self, file_path, header):
        if isinstance(file_path, str):
            self.csv = pd.read_csv(file_path, header=header)
        else:
            self.csv = file_path

    def merge_col(self, col, name, spacer = ','):
        if not isinstance(col, list) or (isinstance(col, list) and len(col) < 2):
            print("type error")
        else:
            holder = self.csv[col[0]].astype(str)
            for idx, header in enumerate(col):
                if idx > 0:
                    holder += spacer + self.csv[header].astype(str)
            self.csv[name] = holder
    
    def delete(self, col):
        if isinstance(col, list):
            col = list(col)
        self.csv.drop(col)

class CsvHandler(object):

    def __init__(self, csv_files):
        self.pile = []
        if csv_files == "*.csv":
            csv_files = [i for i in glob.glob('*.{}'.format("csv"))]
        self.uni_headers = CsvFile(csv_files[0], 0).csv.columns.values
        for fil in csv_files:
            new_file = CsvFile(fil, 0)
            if (self.uni_headers == new_file.csv.columns.values).all():
                self.pile.append(new_file.csv)
            else:
                print(fil + " headers mismatch")
    
    @property
    def merge(self):
        return CsvFile(pd.concat(self.pile, ignore_index=True), 0)


if __name__ == "__main__":
    mypile = CsvHandler("*.csv")
    mycsv = mypile.merge
    mycsv.merge_col(['location_address1', 'location_city'], 'combined_address')
    mycsv.csv.to_csv('D2D.csv')