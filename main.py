import pandas as pd
import matplotlib.pyplot as plt
from csv_data import gdp_data, gdp_graph

while True:
    print('\nChoose between the list:')
    print('1. Total GDP data')
    print('2. GDP per capita data')
    print('3. Life expendancy data')
    print('4. GDP per capita graph')
    print('5. Life expectancy graph')
    print('6. Exit the program.')
    choose = input('Enter number between (1-6) ')

    if choose == '1':
        print(gdp_data.total())
    elif choose == '2':
        print(gdp_data.per_capita())
    elif choose == '3':
        print(gdp_data.life_expectancy())
    elif choose == '4':
        selected_countries = ['United States', 'Norway', 'Sweden', 'Japan', 'Germany']
        title = 'GDP per capita'
        df_total = gdp_data.per_capita()
        gdp_graph.capita_graph(df_total, selected_countries, title)
    elif choose == '5':
        selected_countries = ['United States', 'Norway', 'Sweden', 'Japan', 'Germany']
        title = 'Life Expectancy'
        df_total = gdp_data.life_expectancy()
        gdp_graph.expectancy_graph(df_total, selected_countries, title)
    elif choose == '6':
        print('Shutting down program.')
        break
    else:
        print('Invalid choice, please choose a number that is shown in the information provided!')