import pandas as pd
from pathlib import Path

root_dir = Path.cwd()
data_dir = root_dir / "csv"

data = pd.read_csv(data_dir / "data.csv")
cols = data.columns.tolist()
num_cols = len(cols)
cols = cols[num_cols-9:]
print(cols)

