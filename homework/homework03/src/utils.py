import pandas as pd

def get_summary_stats(df):
    desc = df.describe()
    grouped = df.groupby('category').mean(numeric_only=True).reset_index()
    return desc, grouped