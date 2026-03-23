import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create dataset (changed names)
data = {
    "Name": ["Anu", "Karthik", "Meena", "Ravi", "Sneha"],
    "Maths": [85, 88, 70, 95, 60],
    "Science": [78, 92, 65, 89, 75],
    "English": [90, 79, 72, 93, 68]
}

df = pd.DataFrame(data)

# Step 2: Calculate Total and Average
df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

# Step 3: Assign Grades
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Average"].apply(get_grade)

# Step 4: Find Topper
topper = df.loc[df["Average"].idxmax()]

# Step 5: Display Results
print("Student Data:\n")
print(df)

print("\nTopper Details:\n")
print(topper)

# Step 6: Add your own line
print("\nProject done by me for learning purpose")

# Step 7: Visualization (changed title)
plt.bar(df["Name"], df["Average"])
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.title("My Student Analysis Project")
plt.show()
