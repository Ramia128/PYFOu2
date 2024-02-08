import pandas as pd
import matplotlib.pyplot as plt

class gdp_data():
    def total():
        ## Läser csv filen och filtrerar till country name, country code och 1960 - 2022
        df = pd.read_csv('GDP_TOTAL.csv', skiprows=3, usecols=['Country Name'] + [str(x) for x in range(1960, 2023)])

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
        df = pd.read_csv('GDP_PCAP.csv', skiprows=3, usecols=['Country Name'] + [str(x) for x in range(1960, 2023)])

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
        df = pd.read_csv('Life_Expectancy.csv', skiprows=3, usecols=['Country Name'] + [str(x) for x in range(1960, 2022)])

        ## Tar bort decimalen så det blir enklare att läsa
        pd.options.display.float_format = '{:,.0f}'.format

        ## Fyller NaN values till 0
        df = df.fillna(0)

        ## Sorterar livslängden enligt tabellens data
        df_sorted = df.sort_values(by='2021', ascending=False)
        pd.set_option('display.max_rows', None)
        return df_sorted

class gdp_graph():
    def capita_graph(df, countries, title):
        fig, ax = plt.subplots(figsize=(10, 5))       
        df_countries = df[df['Country Name'].isin(countries)]
        df_plot = df_countries.set_index('Country Name').transpose()
        df_plot = df_plot.apply(pd.to_numeric, errors='coerce')

        df_plot.plot(style='-', ax=ax)

        plt.title(title)
        plt.xticks(range(0, len(df_plot.index), 6), df_plot.index[::6])
        plt.legend()
        ax.yaxis.set_major_formatter(lambda x, pos: f'{x/1e3:.0f}K')
        plt.tight_layout()
        plt.show()

    def expectancy_graph(df, countries, title):
        fig, ax = plt.subplots(figsize=(10, 5))       
        df_countries = df[df['Country Name'].isin(countries)]
        df_plot = df_countries.set_index('Country Name').transpose()
        df_plot = df_plot.apply(pd.to_numeric, errors='coerce')

        df_plot.plot(style='-', ax=ax)

        plt.title(title)
        plt.xticks(range(0, len(df_plot.index), 10), df_plot.index[::10], rotation=45)
        plt.legend()
        ax.yaxis.set_major_formatter(lambda x, pos: f'{x/1:.0f}')
        plt.tight_layout()
        plt.show()