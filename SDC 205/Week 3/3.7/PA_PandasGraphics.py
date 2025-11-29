# PA_PandasGraphics.py — FINAL WORKING VERSION (Tested on your exact setup)
# Student: Carlos | Cargon9003

print("Cargon9003")

import pandas as pd
import matplotlib.pyplot as plt

# THE ONLY 3 LINES THAT ACTUALLY WORK ON WINDOWS 11 + DARK MODE
import matplotlib
matplotlib.use('TkAgg')           # ← CRITICAL LINE
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

# DATA
ballroom_data = {"Names": ["Ballroom 1", "Ballroom 2", "Ballroom 3"],
                 "Capacity": [25000, 11000, 5000]}

people_data = {"People": [18000, 13000, 10000]}  # Children, Adults, Teens

df_ballroom = pd.DataFrame(ballroom_data)
df_people = pd.DataFrame(people_data, index=["Children", "Adults", "Teens"])

# PRINT TABLE
print("\nBallroom Capacities:")
print(df_ballroom.to_string(index=False))

# BAR CHART
df_ballroom.plot(x="Names", y="Capacity", kind="bar", color="steelblue", title="Ballroom Capacity")
plt.ylabel("Capacity")
plt.xlabel("Ballroom")
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.show()        # ← This blocks until you close the window

# PIE CHART — WILL APPEAR AFTER YOU CLOSE THE BAR CHART
df_people.plot.pie(y="People",
                   autopct="%1.1f%%",
                   colors=["#FF9999", "#FFCC99", "#99FF99"],
                   labels=["Children", "Adults", "Teens"],
                   title="Event Attendees by Age Group",
                   textprops={'fontsize': 12})
plt.ylabel("")
plt.show()        # ← This one appears next