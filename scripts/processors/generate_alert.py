"""Looks for performance regressions in the benchmark results
Usage:
    generate_alert.py data.csv regressions.txt
"""

import sys
import datetime
# import time
import os
import pandas as pd
# import plotly.express as px
# from pathlib import Path
# from io import StringIO

# number of samples needed to calculate regression
N_SMAPLES = 10

# number of days to look back when calculating regression
N_DAYS = 14

# threshold in percents
TRESHOLD = 110

# quantile
Q = 0.25


def fetch_csv(csv_path: str) -> pd.DataFrame:
    """_summary_

    Args:
        csvPath (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    return pd.read_csv(csv_path)


def get_regression(data: pd.DataFrame) -> [str]:
    """_summary_

    Args:
        data (pd.DataFrame): _description_

    Returns:
        [str]: _description_
    """
    _regressions = []
    grouped_data = data.groupby(["scenario", "test case"])
    for (group_key, group_data) in grouped_data:

        if len(group_data["relative duration"].values) < N_SMAPLES:
            continue

        # take quantile .25 from last 10 items
        result = group_data["relative duration"][-N_SMAPLES:].quantile(Q)
        if result > TRESHOLD:

            formatters = {
                'timestamp': (lambda a: a.strftime("%Y-%m-%d %H:%M:%S ")),
                'duration': (lambda a: f"{float(a):.2f}s"),
                'base duration': (lambda a: f"{float(a):.2f}s"),
                'relative duration': (lambda a: f"{float(a):.2f}%"),
            }
            columns = ['timestamp', 'version', 'duration',
                       'base duration', 'relative duration']
            header = "Scenario = " + str(group_data["scenario"].values[-1]) + "\n" + \
                     "Base Version = " + str(group_data["base version"].values[-1]) + "\n" + \
                     "Test case = " + str(group_data["test case"].values[-1])
            data_string = f'{group_data[-N_SMAPLES:].to_string(header=True, index=False, justify="right", columns=columns, formatters=formatters)}'
            line_length = len(data_string.splitlines()[0])
            line = '-' * line_length
            _regressions.append('\n' + line)
            _regressions.append(header)
            _regressions.append(line)
            _regressions.append(data_string)
            _regressions.append(line)
            _regressions.append("")

    return _regressions


if __name__ == "__main__":
    csv_data = fetch_csv(sys.argv[1])
    csv_data["timestamp"] = pd.to_datetime(csv_data["timestamp"])
    csv_data = csv_data.loc[csv_data["scenario"] != 'warmup']

    now = datetime.datetime.now(datetime.timezone.utc)
    cutoff_date = now - datetime.timedelta(days=N_DAYS)
    csv_data = csv_data.loc[csv_data["timestamp"] > cutoff_date]

    regressions = get_regression(csv_data)

    if regressions:
        with open(sys.argv[2], 'w', encoding='utf-8') as fp:
            fp.write('\n'.join(regressions))
    elif os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])
