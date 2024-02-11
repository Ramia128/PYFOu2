import pandas as pd
import matplotlib.pyplot as plt

filtered_words = 'Asia|Euro|Africa|America|income|Poor|Countries|dividend|Member|IDA|IBRD|Fragile|World|small|members|Small'
class gdp_data():
    def total():
        ## Läser csv filen och filtrerar till country name, country code och 2010 - 2022
        df = pd.read_csv('GDP_TOTAL.csv', skiprows=3, usecols=['Country Name'] + [str(x) for x in range(2010, 2023)])

        ## Tar bort decimalen så det blir enklare att läsa
        pd.options.display.float_format = '{:,.0f}'.format

        ##  Filtrerar bort NaN
        df = df.dropna()
        filtered_df = df[~df['Country Name'].str.contains(filtered_words)]
        
        ## Sorterar den maximala GDP utifrån år 2022
        df_sorted = filtered_df.sort_values(by='2022', ascending=False)
        df_sorted_reset = df_sorted.reset_index(drop=True)
        pd.set_option('display.max_rows', None)
        return df_sorted_reset
    
    def per_capita():
        ## Läser csv filen och filtrerar till country name, country code och 2010 - 2022
        df = pd.read_csv('GDP_PCAP.csv', skiprows=3, usecols=['Country Name'] + [str(x) for x in range(2010, 2023)])

        ## Tar bort decimalen så det blir enklare att läsa
        pd.options.display.float_format = '{:,.0f}'.format

        ##  Filtrerar bort NaN
        df = df.dropna()
        filtered_df = df[~df['Country Name'].str.contains(filtered_words, case=False)]
        ## Sorterar livslängden enligt tabellens data
        df_sorted = filtered_df.sort_values(by='2021', ascending=False)
        df_sorted_reset = df_sorted.reset_index(drop=True)
        pd.set_option('display.max_rows', None)
        return df_sorted_reset
    
    def life_expectancy(x):
        ## Läser csv filen och filtrerar till country name, country code och 2010 - 2022
        df = pd.read_csv('Life_Expectancy.csv', skiprows=3, usecols=['Country Name'] + [str(x) for x in range(2010, 2022)])
        ## Tar bort decimalen så det blir enklare att läsa
        pd.options.display.float_format = '{:,.0f}'.format

        ##  Filtrerar bort NaN
        df = df.dropna()
        filtered_df = df[~df['Country Name'].str.contains(filtered_words, case=False)]
        ## Sorterar livslängden enligt tabellens data
        df_sorted = filtered_df.sort_values(by='2021', ascending=False)
        df_sorted_reset = df_sorted.reset_index(drop=True)
        pd.set_option('display.max_rows', None)
        if x == 0:
            world_mean = filtered_df['2021'].mean()
            country_over_mean = df_sorted_reset[df_sorted_reset['2021'] > world_mean]
            return country_over_mean[['Country Name', '2021']]
        else:
            return df_sorted_reset



class gdp_graph():
    def life_capita_graph(df_cap, df_life, countries, title_cap, title_life):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))       
        df_cap_countries = df_cap[df_cap['Country Name'].isin(countries)]
        df_cap_plot = df_cap_countries.set_index('Country Name').transpose()
        df_cap_plot = df_cap_plot.apply(pd.to_numeric, errors='coerce')

        df_cap_plot.plot(style='-', ax=ax1)

        ax1.set_title(title_cap)
        ax1.set_xticks(range(0, len(df_cap_plot.index), 1), df_cap_plot.index[::1])
        ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        ax1.yaxis.set_major_formatter(lambda x, pos: f'{x/1e3:.0f}K')
        ax1.set_ylabel('Dollars')

        df_life_countries = df_life[df_life['Country Name'].isin(countries)]
        df_life_plot = df_life_countries.set_index('Country Name').transpose()
        df_life_plot = df_life_plot.apply(pd.to_numeric, errors='coerce')

        df_life_plot.plot(style='-', ax=ax2)

        ax2.set_title(title_life)
        ax2.set_xticks(range(0, len(df_life_plot.index), 1), df_life_plot.index[::1])
        ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        ax2.yaxis.set_major_formatter('{:.0f}'.format)
        ax2.set_ylabel('Years')

        plt.tight_layout()
        plt.show()
