import sys
import subprocess
import pandas as pd
import os

# Load dataset 
if len(sys.argv) > 1:
    input_csv = sys.argv[1]
else:
    input_csv = "data_raw.csv"  

if not os.path.exists(input_csv):
    raise FileNotFoundError(f"File not found: {input_csv}")

# Ingest Data 
df = pd.read_csv(input_csv)
print(f"ingested {len(df)} rows and {len(df.columns)} columns from {input_csv}")

#chain to next step
print("moving to preprocess.py ...")
subprocess.run(["python", "Preprocess.py", input_csv])

