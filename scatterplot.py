import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [50, 55, 65, 70, 72, 78, 85, 88, 92, 95]

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(study_hours, test_scores, color='blue', marker='o')
plt.xlabel("Study Hours")
plt.ylabel("Test Scores")
plt.title("Study Hours vs Test Scores")
plt.grid(True)
plt.show()

# Observations:
# The scatter plot shows a positive correlation between study hours and test scores.
# As the study hours increase, the test scores tend to increase, indicating that more study hours lead to better performance.