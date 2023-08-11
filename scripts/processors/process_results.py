"""Reads the output of NuGet benchmark, calculates new data points (relative duration) and appends data to csv file
Usage:
    process_results.py results.csv data.csv
"""

# import re
import sys
import os
from pathlib import Path
import pandas as pd
# from datetime import datetime, timedelta


def read_results(csv_path: str) -> pd.DataFrame:
    """_summary_

    Args:
        csv_path (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    # osName = re.search(r"results\_(.+)\.csv", csvPath).groups(1)[0]
    solution_name = Path(csv_path).stem

    df = pd.read_csv(csv_path)
    n_rows = int(len(df) / 2)

    duration = [df['Total Time (seconds)'][i + n_rows]
                for i in range(0, n_rows)]
    base_duration = [df['Total Time (seconds)'][i] for i in range(0, n_rows)]

    return pd.DataFrame({'version': [df['Client Version'][i + n_rows] for i in range(0, n_rows)],
                         'base version': [df['Client Version'][i] for i in range(0, n_rows)],
                         'scenario': [df['Scenario Name'][i + n_rows] for i in range(0, n_rows)],
                         'test case': [solution_name for i in range(0, n_rows)],
                         # 'os': [osName for i in range(0, nRows)],
                         # 'timestamp': [datetime.fromisoformat(df['Test Run ID'][i + nRows]) + timedelta(seconds=i) for i in range(0, nRows)],
                         'timestamp': [df['Test Run ID'][i + n_rows] for i in range(0, n_rows)],
                         'duration': duration,
                         'base duration': base_duration,
                         'relative duration': [duration[i] / base_duration[i] * 100 for i in range(0, n_rows)],
                         })


if __name__ == "__main__":
    INPUT_CSV_PATH = sys.argv[1]
    OUTPUT_CSV_PATH = sys.argv[2]
    data_frame = read_results(INPUT_CSV_PATH)
    data_frame.to_csv(OUTPUT_CSV_PATH, mode='a', index=None,
                      header=not os.path.exists(OUTPUT_CSV_PATH))
