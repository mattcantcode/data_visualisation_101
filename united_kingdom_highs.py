import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/united_kingdom_07_2022_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
 
    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[4], '%Y-%m-%d')
        try:
            high = int(float(row[6]))
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
ax.set_title("Daily high temperatures, July 2022\nUnited Kingdom", fontsize=24)
ax.set_xlabel('', fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()