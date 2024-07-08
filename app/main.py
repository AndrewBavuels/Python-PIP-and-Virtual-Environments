import utils
import charts
import pandas as pd

def run():
    df = pd.read_csv('data.csv')
    df_filtered = df[df['Continent'] == 'Africa']

    countries = df_filtered['Country'].values
    percentages = df_filtered['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)

    country = input('Type Country => ')
    print(country)

    result = utils.population_by_country(df, country)

    if not result.empty:
        country_data = result.iloc[0]  # Use .iloc[0] to access the first row as a Series
        print(country_data)
        labels, values = utils.get_population(country_data)
        charts.generate_bar_chart(country_data['Country'], labels, values)

if __name__ == '__main__':
    run()
