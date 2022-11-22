class CSVfile():
    
    def __init__(self, file_name):
        self.name=file_name

    def get_data(self):
        


myfile=CSVfile('shampoo_sales.csw')
print(myfile.name)