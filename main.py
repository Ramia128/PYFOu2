from csv_data import gdp_data, gdp_graph

while True:
    print('\nChoose between the list:')
    print('1. Total GDP data')
    print('2. GDP per capita data')
    print('3. Life expendancy data')
    print('4. GDP per capita and Life expectancy graph')
    print('5. Life expendancy over world mean')
    print('6. High life low GDP/Capita data')
    print('7. Top 10 GDP and their life expectancy data')
    print('8. Top 20 GDP per Capita and their life expectancy data')
    print('9. Exit the program.')
    choose = input('Enter number between (1-9) ')

    if choose == '1':
        print(gdp_data.total())
    elif choose == '2':
        print(gdp_data.per_capita())
    elif choose == '3':
        x = 1
        print(gdp_data.life_expectancy(x))
    elif choose == '4':
        x = 1
        selected_countries = ['United States', 'Norway', 'Sweden', 'Japan', 'Germany']
        title_cap = 'GDP per capita'
        title_life = 'Life Expectancy'
        df_cap = gdp_data.per_capita()
        df_life = gdp_data.life_expectancy(x)
        gdp_graph.life_capita_graph(df_cap, df_life, selected_countries, title_cap, title_life)
    elif choose == '5':
        x = 0
        print(gdp_data.life_expectancy(x))
    elif choose == '6':
        print(gdp_data.low_gdp_high_life())
    elif choose == '7':
        print(gdp_data.combine_data(1))
    elif choose == '8':
        print(gdp_data.combine_data(2))
    elif choose == '9':
        print('Shutting down program.')
        break
    else:
        print('Invalid choice, please choose a number that is shown in the information provided!')