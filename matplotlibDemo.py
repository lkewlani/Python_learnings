import matplotlib.pyplot as plt

#Data for plotting
days=["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
coffee_cups = [1,3,2,4,0,1,2,]

#Create plot
plt.plot(days, coffee_cups, marker='o', color='b',linestyle='--')

plt.title("Coffee intake this week")
plt.xlabel("Days of the week")
plt.ylabel("Coffee Intake for the day")

plt.show()