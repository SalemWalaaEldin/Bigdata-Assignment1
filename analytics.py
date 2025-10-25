import pandas as pd
import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: python analytics.py <path_to_csv>")
    sys.exit(1)

input_path = sys.argv[1]

try:
    df = pd.read_csv(input_path)
    print(f"Dataset loaded!!")
except Exception as e:
    print(f"Error reading dataset: {e}")
    sys.exit(1)

# Insight 1
most_sold_item = df['Item'].value_counts().idxmax()
with open("insight1.txt", "w") as f:
    f.write(f"The most sold item is: {most_sold_item}\n")
print("Insight 1 saved: Most sold item")

# Insight 2
most_payment = df['Payment Method'].value_counts().idxmax()
with open("insight2.txt", "w") as f:
    f.write(f"The most common payment method is: {most_payment}\n")
print("Insight 2 saved: Most common payment method")

# Insight 3
avg_spent = df['Total Spent'].mean()
with open("insight3.txt", "w") as f:
    f.write(f"The average total spent per transaction is: ${avg_spent:.2f}\n")
print("Insight 3 saved: Average total spent per transaction")

# Chain to next step 
try:
    print("\n moving to visualize.py with preprocessed data...")
    subprocess.run(["python", "visualize.py", input_path], check=True)
except Exception as e:
    print(f"Failed to run visualize.py: {e}")



