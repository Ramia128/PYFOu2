import pandas as pd
import matplotlib.pyplot as plt
from csv_data import gdp_data, gdp_graph

while True:
    print('\nChoose between the list:')
    print('1. Total GDP data')
    print('2. GDP per capita data')
    print('3. Life expendancy data')
    print('4. GDP per capita and Life expectancy graph')
    print('5. Exit the program.')
    choose = input('Enter number between (1-5) ')

    if choose == '1':
        print(gdp_data.total())
    elif choose == '2':
        print(gdp_data.per_capita())
    elif choose == '3':
        print(gdp_data.life_expectancy())
    elif choose == '4':
        selected_countries = ['United States', 'Norway', 'Sweden', 'Japan', 'Germany']
        title_cap = 'GDP per capita'
        title_life = 'Life Expectancy'
        df_cap = gdp_data.per_capita()
        df_life = gdp_data.life_expectancy()
        gdp_graph.life_capita_graph(df_cap, df_life, selected_countries, title_cap, title_life)
    elif choose == '5':
        print('Shutting down program.')
        break
    else:
        print('Invalid choice, please choose a number that is shown in the information provided!')