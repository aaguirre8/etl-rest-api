import pandas as pd

# Create a generic dataframe with the titanic metadata
titanic = pd.read_csv("titanic.csv")

class etl_data:
    def __init__(self, pclass):
        self.__pclass = pclass
        print('pclass:', self.__pclass)
        
    def get_details(self):
        print('dataframe filter value:', self.__pclass)
        titanic_filtered = titanic[titanic['Pclass'] == int(self.__pclass)]
        titanic_dict = titanic_filtered.to_dict(orient='index')
        return titanic_dict

etl_data_obj = etl_data('1')
print(etl_data_obj.get_details())