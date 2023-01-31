class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, file_name):
        self.name=file_name
# myfile=CSVTimeSeriesFile('data.csv')
    def get_data(self):
        try:
            open_file=open(self.name, 'r')
        except:
            raise ExamException('Il file non è leggibile')
        lista_dati=[]
        n_lista=0
        for line in open_file:
            if n_lista!=0:
                elements=line.split(',')
                try:
                    elements[0]=int(float(elements[0]))
                    elements[1]=int(float(elements[1]))
                    lista_line=[]
                    lista_line.append(elements[0])
                    lista_line.append(elements[1])
                    lista_dati.append(lista_line)
                except:
                    pass

        
# def compute_daily_max_difference:
    