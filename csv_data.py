import pandas as pd
import matplotlib.pyplot as plt

filtered_words = 'Asia|Euro|Africa|America|income|Poor|Countries|dividend|Member|IDA|IBRD|Fragile|World|small|members|Small'
class gdp_data():
    def total():
        df = pd.read_csv('GDP_TOTAL.csv', skiprows=3, usecols=['Country Name'] + [str(x) for x in range(2010, 2023)])

        pd.options.display.float_format = '{:,.0f}'.format

        df = df.dropna()
        filtered_df = df[~df['Country Name'].str.contains(filtered_words)]
        
        df_sorted = filtered_df.sort_values(by='2022', ascending=False)
        df_sorted_reset = df_sorted.reset_index(drop=True)
        pd.set_option('display.max_rows', None)
        return df_sorted_reset
    
    def per_capita():
        
        df = pd.read_csv('GDP_PCAP.csv', skiprows=3, usecols=['Country Name'] + [str(x) for x in range(2010, 2023)])

        
        pd.options.display.float_format = '{:,.0f}'.format

        
        df = df.dropna()
        filtered_df = df[~df['Country Name'].str.contains(filtered_words, case=False)]
        
        df_sorted = filtered_df.sort_values(by='2021', ascending=False)
        df_sorted_reset = df_sorted.reset_index(drop=True)
        pd.set_option('display.max_rows', None)
        return df_sorted_reset
    
    def life_expectancy(x):
        df = pd.read_csv('Life_Expectancy.csv', skiprows=3, usecols=['Country Name'] + [str(x) for x in range(2010, 2022)])
        pd.options.display.float_format = '{:,.0f}'.format

        df = df.dropna()
        filtered_df = df[~df['Country Name'].str.contains(filtered_words, case=False)]
    
        df_sorted = filtered_df.sort_values(by='2021', ascending=False)
        df_sorted_reset = df_sorted.reset_index(drop=True)
        pd.set_option('display.max_rows', None)
        if x == 0:
            world_mean = filtered_df['2021'].mean()
            country_over_mean = df_sorted_reset[df_sorted_reset['2021'] > world_mean]
            return country_over_mean[['Country Name', '2021']]
        else:
            return df_sorted_reset
        

    def combine_data(x):
        df_life = pd.read_csv('Life_Expectancy.csv', skiprows=3, usecols=['Country Name', '2021'])
        df_life = df_life.dropna()
        filtered_life = df_life[~df_life['Country Name'].str.contains(filtered_words, case=False)]

        df_cap = pd.read_csv('GDP_PCAP.csv', skiprows=3, usecols=['Country Name', '2021'])
        df_cap = df_cap.dropna()

        df_gdp = pd.read_csv('GDP_TOTAL.csv', skiprows=3, usecols=['Country Name', '2021'])
        df_gdp = df_gdp.dropna()
        

        pd.options.display.float_format = '{:,.0f}'.format
        pd.set_option('display.max_rows', None)
        

        if x == 0:
            df_combined = pd.merge(filtered_life, df_cap, on='Country Name', suffixes=('_life', '_cap'))
            df_combined = pd.merge(df_combined, df_gdp, on='Country Name', suffixes=('_combined', '_gdp'))
            df_combined = df_combined.rename(columns={'2021_life': 'Life Expectancy', '2021_cap': 'GDP per Capita', '2021': 'GDP'})
            df_sorted = df_combined.sort_values(by=['Life Expectancy'], ascending=False)
            df_sorted_reset = df_sorted.reset_index(drop=True)
        elif x == 1:
            df_combined = pd.merge(filtered_life, df_gdp, on='Country Name', suffixes=('_life', '_gdp'))
            df_combined = df_combined.rename(columns={'2021_life': 'Life Expectancy', '2021_gdp': 'GDP'})
            df_sorted = df_combined.sort_values(by=['GDP'], ascending=False)
            df_head = df_sorted.head(10)
            df_sorted_reset = df_head.reset_index(drop=True)
        else:
            df_combined = pd.merge(filtered_life, df_cap, on='Country Name', suffixes=('_life', '_cap'))
            df_combined = df_combined.rename(columns={'2021_life': 'Life Expectancy', '2021_cap': 'GDP per Capita'})
            df_sorted = df_combined.sort_values(by=['GDP per Capita'], ascending=False)
            df_head = df_sorted.head(20)
            df_sorted_reset = df_head.reset_index(drop=True)


        return df_sorted_reset

    def low_gdp_high_life():
        df_combined = gdp_data.combine_data(0)

        condition = (df_combined['Life Expectancy'] > 75) & (df_combined['GDP'] < 1e10 ) & (df_combined['GDP per Capita'] < 1e5)

        result = df_combined[condition][['Country Name', 'Life Expectancy', 'GDP', 'GDP per Capita']]
        result_reset = result.reset_index(drop=True)

        return result_reset



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



print(gdp_data.combine_data(1))
