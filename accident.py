# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("/content/us_accident.csv")

# Display the first few rows of the dataset
print(data.head())

# Data Cleaning
# Convert the Start_Time and End_Time columns to datetime format with the correct format
data['Start_Time'] = pd.to_datetime(data['Start_Time'], format='%d-%m-%Y %H:%M', errors='coerce')
data['End_Time'] = pd.to_datetime(data['End_Time'], format='%d-%m-%Y %H:%M', errors='coerce')

# Drop rows where datetime conversion failed
data.dropna(subset=['Start_Time', 'End_Time'], inplace=True)

# Extract features like year, month, day, hour from Start_Time
data['Year'] = data['Start_Time'].dt.year
data['Month'] = data['Start_Time'].dt.month
data['Day'] = data['Start_Time'].dt.day
data['Hour'] = data['Start_Time'].dt.hour

# Drop unnecessary columns
data.drop(['ID', 'Start_Lat', 'Start_Lng', 'End_Lat', 'End_Lng', 'Distance(mi)', 'Description', 'Number', 'Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 'Airport_Code', 'Weather_Timestamp', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Direction', 'Wind_Speed(mph)', 'Precipitation(in)', 'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight'], axis=1, inplace=True)

# Handling missing values
data.dropna(inplace=True)

# Display the first few rows of the dataset
print(data.head())

# Display the last few rows of the dataset
print(data.tail())

print(data.shape)

# EDA and Visualization
# Plotting accidents by year
plt.figure(figsize=(10, 6))
sns.countplot(x='Year', data=data)
plt.title('Accidents by Year')
plt.xlabel('Year')
plt.ylabel('Number of Accidents')
plt.show()

# Plotting accidents by month
plt.figure(figsize=(10, 6))
sns.countplot(x='Month', data=data)
plt.title('Accidents by Month')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.show()

# Plotting accidents by day
plt.figure(figsize=(10, 6))
sns.countplot(x='Day', data=data)
plt.title('Accidents by Day')
plt.xlabel('Day')
plt.ylabel('Number of Accidents')
plt.show()

# Plotting accidents by hour
plt.figure(figsize=(10, 6))
sns.countplot(x='Hour', data=data)
plt.title('Accidents by Hour')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.show()

# Plotting accidents by weather condition
plt.figure(figsize=(10, 6))
sns.countplot(y='Weather_Condition', data=data, order=data['Weather_Condition'].value_counts().iloc[:10].index)
plt.title('Accidents by Weather Condition (Top 10)')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.show()
