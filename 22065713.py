
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 01:32:07 2024

@author: kurva
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns

# Load the data
data = pd.read_csv(
    "C:\\Users\\kurva\\Downloads\\DATA HANDLING AND VISUVALIZATION\\PROJECT\\DATA.txt")

# Convert the data frame into a NumPy array
data_array = np.array(data)

# Get the unique major categories
categories = np.unique(data_array[:, 3])

# Create an empty list to store the results
results = []

# Loop through each category
for category in categories:
    # Filter the data array by the category
    category_data = data_array[np.where(data_array[:, 3] == category)]

    # Calculate the mean, median income and unemployment rate for the category
    mean_median = np.mean(category_data[:, 8].astype(float))
    mean_unemployment = np.mean(category_data[:, 20].astype(float))

    # Append the results to the list
    results.append([category, mean_median, mean_unemployment])

# Convert the results list into a NumPy array
results_array = np.array(results)

# Create a figure with multiple subplots using GridSpec
fig = plt.figure(figsize = (25, 20))  # Adjusted figure size
gs = GridSpec(2, 3, figure = fig)

# Define the axes
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax4 = fig.add_subplot(gs[1, 0])
ax5 = fig.add_subplot(gs[1, 1])
ax6 = fig.add_subplot(gs[1, 2])

# Plot 1: Bar chart of top 10 majors by median income
top_10 = data.sort_values(by = "Median", ascending = False).head(10)
sns.barplot(x = "Median", y = "Major", data = top_10,
            color = "blue", label = "Median income", ax = ax1)
ax1.set_xlabel("Median income ($)", fontweight = 'bold')
ax1.set_ylabel("Major", fontweight = 'bold')
ax1.set_title("TOP 10 MAJOR COURSES BY MEDIAN INCOME", fontweight = 'bold')
ax1.invert_yaxis()

# Plot 2: Histogram of percentage of women in each major category
sns.histplot(x = "ShareWomen", data = data, bins = 25, edgecolor = "black",
             kde = True, label = "Frequency", legend = True, ax = ax2, color = 'skyblue')
ax2.set_xlabel("Percentage of women (%)", fontweight = 'bold')
ax2.set_ylabel("Count", fontweight = 'bold')
ax2.set_title("DISTRIBUTION OF % OF WOMEN IN EACH MAJOR CATEGORY",
              fontweight = 'bold')

# Plot 3: Box plot of Men with Low wage jobs
top_15 = data.sort_values(by = "Men", ascending = False).head(15)
sns.boxplot(x = "Men", y = "Low_wage_jobs", data = top_15, ax = ax3, palette = 'viridis')
ax3.set_xticklabels(ax3.get_xticklabels(), rotation = 45)
ax3.set_xlabel("Men", fontweight = 'bold')
ax3.set_ylabel("Low_wage_jobs", fontweight = 'bold')
ax3.set_title("MEN WITH LOW WAGE JOBS", fontweight = 'bold')

# Plot 4: Create a line plot
data_sorted = data.sort_values('Low_wage_jobs')
last_10_majors = data_sorted.tail(10)
sns.lineplot(x = last_10_majors['Low_wage_jobs'],
             y = last_10_majors['Major'], ax = ax4)
ax4.set_xlabel('Low_wage_jobs', fontweight = 'bold')
ax4.set_ylabel('Major', fontweight = 'bold')
ax4.set_title('LOW WAGE JOBS FOR MAJOR COURSES', fontweight = 'bold')

# Plot 5: Pie chart of number of majors in each major category
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
           0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
ax5.pie(data["Major_category"].value_counts(), labels = data["Major_category"].value_counts().index, explode = explode,
        autopct = "%1.1f%%", startangle = 45, colors = sns.color_palette("viridis", len(data["Major_category"].value_counts().index)))
ax5.set_title("NUMBER OF MAJORS IN EACH CATEGORY", fontweight='bold')

# Explaining the graphs
ax6.grid(False)
ax6.axis('off')
ax6.text(0.1, 0.4, 'THESE ARE THE SUBJECTS ON WHICH HUMAN RACE IS ON FOR THEIR LIFE AND MONEY : \n\n PLOT 1: \n The high median income of petroleum engineers can be attributed to the nature of their work, \n the physical and mental demands of the job, and their level of education. \n\n PLOT 2: \n Women Dominate Employment Within each and every field compared to Mens shows Women too \n getting Freedom from some traditional barrages  in some parts of Eastern Countries. \n\n PLOT 3: \n Most of the mens are working for 48K i.e 86648 Mens. \n\n PLOT 4: \n History subject has lowest salary ever recorded compared to Psychology Subject.\n\n PLOT 5: \n Students loves to choose Engineering first and Interdisciplinary Last, may be for evolving world!.', verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5), fontsize=14, fontweight='bold', visible=True)

# Add overall title
fig.suptitle('ARE THESE THE TOP SUBJECTS IN THE WORLD? \n\n Kurva Pavan Kumar \n\n Student ID: 22065713',
             fontsize = 20, fontweight = 'bold')

# save the figure
plt.savefig('22065713.png', dpi = 300, bbox_inches = 'tight')
