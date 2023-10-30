import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

grouped_df = df.groupby('A')

for key, item in grouped_df:
    print(grouped_df.get_group(key), "\n\n")