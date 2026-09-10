import pandas as pd

class ExcelParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        try:
            df = pd.read_excel(self.file_path)
            return df
        except Exception as e:
            raise Exception(f"Error parsing Excel file: {e}")

# Example usage:
# parser = ExcelParser('timetable.xlsx')
# data = parser.parse()
# print(data)