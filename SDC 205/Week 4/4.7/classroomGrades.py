# classroomGrades.py
# Performance Assessment 4.7 - Cargon9003
# Advanced Pandas + Grouped Bar Chart

print("Cargon9003")

import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Classroom roster - 10 students
students = ['Carlos', 'Maria', 'James', 'Sofia', 'Marcus', 'Aaliyah', 'Diego', 'Isabella', 'Jayden', 'Luna']

# Create repeated student names for two subjects (Math & Science)
student_names = students * 2  # 10 students x 2 subjects = 20 rows

# Create subject list: Math for first 10, Science for next 10
subjects = ['Math'] * 10 + ['Science'] * 10

# Step 3: Create MultiIndex using student name and subject
index = pd.MultiIndex.from_arrays([student_names, subjects], names=('Student', 'Subject'))

# Step 4: Create realistic grades (0-100) for each student in Math & Science
grades = [94, 88, 76, 99, 82, 91, 85, 93, 79, 97,   # Math grades
          89, 92, 81, 95, 87, 90, 78, 96, 84, 91]   # Science grades

# Create DataFrame
df = pd.DataFrame({'Grade': grades}, index=index)

# Step 5: Display the full DataFrame
print("\nFull Classroom Roster with Grades:")
print(df)

# Step 6: Group by Subject and calculate mean grade
average_by_subject = df.groupby('Subject').mean()

# Display grouped result
print("\nAverage Grade by Subject:")
print(average_by_subject)

# Step 7: Create professional vertical bar graph
plt.figure(figsize=(8, 6))
bars = average_by_subject.plot(kind='bar', color=['#3498db', '#2ecc71'], legend=False, edgecolor='black')

plt.title("Cargon9003 - Average Grade by Subject", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Subject", fontsize=12)
plt.ylabel("Average Grade", fontsize=12)
plt.ylim(0, 100)
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels on top of bars
for bar in bars.patches:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height + 1,
             f'{height:.1f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()