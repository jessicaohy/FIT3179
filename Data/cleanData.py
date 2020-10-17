# Jessica Oh Hui Yu

import pandas as pd
import datetime

def cleanData(filename):

    # read data
    df = pd.read_csv(filename)

    # remove columns
    dropList = ['iso_code', 'new_cases_smoothed', 'new_deaths_smoothed',
                'new_cases_smoothed_per_million', 'new_deaths_smoothed_per_million',
                'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
                'stringency_index', 'life_expectancy', 'human_development_index',
                'new_tests', 'total_tests', 'total_tests_per_thousand',
                'tests_per_case', 'new_tests_per_thousand',
                'positive_rate', 'tests_units', 'handwashing_facilities',
                'total_cases_per_million', 'new_cases_per_million',
                'total_deaths_per_million', 'new_deaths_per_million',
                'total_cases']
    df.drop(dropList, inplace=True, axis=1) # axis = 1 drops column

    # remove na rows
    df.dropna(subset=None, how='any', inplace=True, axis=0) # axis = 0 drops row

    # convert YYYY-MM-DD to YYYY-MM
    df['date'] = pd.to_datetime(df['date']).dt.to_period('Y')

    # remove dates that are not 2020
    df = df[(df['date'].dt.year == 2020)]

    # group by location and month
    df = df.groupby(['continent','location', 'date'], as_index=False).agg({'new_cases':'sum',
                                                                           'total_deaths':'sum',
                                                                           'new_deaths':'sum',
                                                                           'population':'mean',
                                                                           'population_density':'mean',
                                                                           'median_age' :'mean',
                                                                           'aged_65_older':'mean',
                                                                           'aged_70_older':'mean',
                                                                           'gdp_per_capita':'mean',
                                                                           'extreme_poverty':'mean',
                                                                           'cardiovasc_death_rate':'mean',
                                                                           'diabetes_prevalence':'mean',
                                                                           'female_smokers':'mean',
                                                                           'male_smokers':'mean',
                                                                           'hospital_beds_per_thousand':'mean'})

    # put into new file
    newFileName = "cleanedCovidWorld.csv"
    df.to_csv(newFileName, index=False)



################ M A I N ################
cleanData("owid-covid-data.csv")


