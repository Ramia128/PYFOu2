import pandas as pd
import matplotlib.pyplot as plt

class gdp_data():
    def total():
        ## Läser csv filen och filtrerar till country name, country code och 1960 - 2022
        df = pd.read_csv('GDP_TOTAL.csv', skiprows=3, usecols=['Country Name', 'Country Code'] + [str(x) for x in range(1960, 2023)])

        ## Tar bort decimalen så det blir enklare att läsa
        pd.options.display.float_format = '{:,.0f}'.format

        ## Fyller NaN values till 0
        df = df.fillna(0)

        ## Sorterar den maximala GDP utifrån år 2022
        df_sorted = df.sort_values(by='2022', ascending=False)
        pd.set_option('display.max_rows', None)
        return df_sorted
    
    def per_capita():
        ## Läser csv filen och filtrerar till country name, country code och 1960 - 2022
        df = pd.read_csv('GDP_PCAP.csv', skiprows=3, usecols=['Country Name', 'Country Code'] + [str(x) for x in range(1960, 2023)])

        ## Tar bort decimalen så det blir enklare att läsa
        pd.options.display.float_format = '{:,.0f}'.format

        ## Fyller NaN values till 0
        df = df.fillna(0)

        ## Sorterar den maximala GDP per capita utifrån år 2022
        df_sorted = df.sort_values(by='2022', ascending=False)
        pd.set_option('display.max_rows', None)
        return df_sorted
    
    def life_expectancy():
        ## Läser csv filen och filtrerar till country name, country code och 1960 - 2022
        df = pd.read_csv('Life_Expectancy.csv', skiprows=3, usecols=['Country Name', 'Country Code'] + [str(x) for x in range(1960, 2023)])

        ## Tar bort decimalen så det blir enklare att läsa
        pd.options.display.float_format = '{:,.0f}'.format

        ## Fyller NaN values till 0
        df = df.fillna(0)

        ## Sorterar livslängden enligt tabellens data
        df_sorted = df.sort_values(by='2021', ascending=False)
        pd.set_option('display.max_rows', None)
        return df_sorted

print(gdp_data.life_expectancy())