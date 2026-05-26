#Step 1: Load the datasets
import pandas as pd
import matplotlib.pyplot as plt
import pathlib as pb

unemp_df = pd.read_csv("Unemployment Per State.csv")
obes_pov_income_df = pd.read_csv("Obes, Pov, Income in U.S.csv")

#Step 2: Clean the datasets
#Step 2.1: Remove duplicates for both
unemp_df.drop_duplicates(inplace=True)
obes_pov_income_df.drop_duplicates(inplace=True)
#Step 2.2: Remove rows with missing info for both
unemp_df.dropna(inplace=True)
obes_pov_income_df.dropna(inplace=True)

#Step 3: Merge the datasets
#Step 3.1: Adjust index of df based on columns
unemp_df.set_index("State", inplace=True)
obes_pov_income_df.set_index("State", inplace=True)
#Step 3.2: Merge the datasets using join()
merged_data=obes_pov_income_df.join(unemp_df, lsuffix="_obesity", rsuffix="_unemployment")

#Step 4: Aggregates new dataset
#Step 4.1: Select state to groupby() the data
grouped_data = merged_data.groupby("State")
#Step 4.2: Use agg() to aggregate at least 2 new columns
aggregated_data = merged_data.groupby('State').agg(
   Avg_Obesity_Rate=('Obesity Rate', 'mean'),
   Avg_Unemployment_Rate=('Percent (%) of Labor Force Unemployed in State', 'mean')
)
#Step 4.3: Print new df
print(aggregated_data)
#Extra: Use the first 5 states to limit the column
top_states = aggregated_data.head(5)

#Step 5: Create visualizations for the new columns
#Step 5.1: Create a bar graph
plt.bar(top_states.index, top_states['Avg_Obesity_Rate'])
#Step 5.2: Include a title and axes
plt.title("Obesity Rates Based On The First 5 States")
plt.ylabel("Percentages of Obesity Rates")
#Step 5.3: Save data as jpg
plt.savefig("ObesityinTop5.jpg")
plt.show()

#Step 5a: Create visualizations for the new columns
#Step 5.1b: Create a bar graph
plt.bar(top_states.index, top_states['Avg_Unemployment_Rate'])
#Step 5.2b: Include a title
plt.title("Unemployment Rates Based On The First 5 States")
plt.ylabel("Percentages of Unemployment Rates")
#Step 5.3b: Save data as a jpg
plt.savefig("UnemploymentinTop5.png")
plt.show()

#Step 6:Print findings based on bar graph to user
print(f"The bar graph titled 'Obesity Rates Based On The First 5 States' shows obesity rates amongst the first 5 states in the dataset.")
print(f"The first 5 states were the following: Alabama, Alaska, Arizona, Arkansas, and California.")
print(f"I wanted to delve into obesity rates as I had done a project in another class discussing obesity and felt that it is a health issue that does not get enough traction.")
print(f"There are many effects obesity causes such as an increase in cardiovascular diseases and people don't realize how severe it can be.")
print(f"You can't see the exact percentages but you can get a rough estimate of the percentages based on the other states. Alabama has the highest obesity rate amongst the 5 with roughly ~38% and Caifornia has the lowest with ~27%.")
print(f"The bar graph titled 'Unemployment Rates Based On The First 5 States' shows unemployment rates amongst the first 5 states in the dataset.")
print(f"Just like the first chart, the states are the following: Alabama, Alaska, Arizona, Arkansas, and California. ")
print(f"This bar graph shows which states have higher levels of unemployment.")
print(f"Again, you can't see exact percentages but can get a feel for it. Alaska has the highest with ~7.8 and Arizona and Arkansas are about the same with ~6%.")
print(f"I wanted to compare both obesity and unemployment rates to try to see if there is any correlation between the two. As I believe that there would be since junk food typically ends up being on the cheaper end, which may mean that people that are unemployed may lean towards purchasing junk foods instead of healthier produce as produce is more expensive. ")