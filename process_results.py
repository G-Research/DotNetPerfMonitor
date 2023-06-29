"""Reads the output of NuGet benchmark, calculates new data points (relative duration) and appends data to csv file
Usage:
    process_results.py results.csv data.csv
"""

import re
import sys
import os
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta

def read_results(csvPath: str) -> pd.DataFrame:
    # osName = re.search(r"results\_(.+)\.csv", csvPath).groups(1)[0]
    solutionName = Path(csvPath).stem

    df = pd.read_csv(csvPath)
    nRows = int(len(df) / 2)

    duration = [df['Total Time (seconds)'][i + nRows] for i in range(0, nRows)]
    base_duration = [df['Total Time (seconds)'][i] for i in range(0, nRows)]

    return pd.DataFrame({'version': [df['Client Version'][i + nRows] for i in range(0, nRows)],
                  'base version': [df['Client Version'][i] for i in range(0, nRows)],
                  'scenario': [df['Scenario Name'][i + nRows] for i in range(0, nRows)],
                  'solution': [solutionName for i in range(0, nRows)],
                  # 'os': [osName for i in range(0, nRows)],
                  #'timestamp': [datetime.fromisoformat(df['Test Run ID'][i + nRows]) + timedelta(seconds=i) for i in range(0, nRows)],
                  'timestamp': [df['Test Run ID'][i + nRows] for i in range(0, nRows)],
                  'duration': duration,
                  'base duration': base_duration,
                  'relative duration': [duration[i] / base_duration[i] * 100 for i in range(0, nRows)],
                  });

if __name__ == "__main__":
    input_csv_path = sys.argv[1]
    output_csv_path = sys.argv[2]
    df = read_results(input_csv_path)
    df.to_csv(output_csv_path, mode='a', index=None, header=not os.path.exists(output_csv_path))
