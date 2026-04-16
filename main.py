# Re-run this cell
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})
crimes.head()

# Start coding here
# Use as many cells as you need
"""
Which hour has the highest frequency of crimes? Store as an integer variable called peak_crime_hour.
We see that the column TIME OCC is a str with 4 digits. We need to create a new col with the hour.
"""
crimes['hour_occ'] = (crimes['TIME OCC']).str[:2].astype(int)
peak_crime_hour = (crimes['hour_occ'].value_counts().index[0])
print(peak_crime_hour)

#Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? Save as a string variable called peak_night_crime_location.

crimes['is_night_crime'] =  crimes['hour_occ'].between(22, 24) | crimes['hour_occ'].between(0, 4)
peak_night_crime_location = (
    crimes[crimes['is_night_crime']]
    .groupby('AREA NAME')
    .size()
    .idxmax()
)
print(peak_night_crime_location)

#Identify the number of crimes committed against victims of different age groups. Save as a pandas Series called victim_ages, with age group labels "0-17", "18-25", "26-34", "35-44", "45-54", "55-64", and "65+" as the index and the frequency of crimes as the values.

victim_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64","65+"]
bins = [0, 17, 25, 34, 44, 54, 64, float('inf')]

crimes['age_group'] = pd.cut(
    crimes['Vict Age'],
    bins=bins,
    labels=victim_labels,
    right=True
)

victim_ages = crimes['age_group'].value_counts().sort_index()
print(victim_ages)
