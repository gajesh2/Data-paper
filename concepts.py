import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Apple', 'Banana', 'Grapes', 'Orange']
sizes = [30, 25, 20, 25]  # Percentages of students
colors = ['red', 'yellow', 'purple', 'orange']
explode = (0.1, 0, 0, 0)  # Highlight the Apple section

# Create the pie chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True)
plt.title("Favorite Fruits of 100 Students")
plt.show()