"""Looks for performance regressions in the benchmark results
Usage:
    generate_alert.py data.csv regressions.txt
"""

import sys
import pandas as pd
import plotly.express as px
import datetime;
import time;
import os;

from pathlib import Path
from io import StringIO

# number of samples needed to calculate regression
n_samples = 10

# number of days to look back when calculating regression
n_days = 14

# threshold in percents
threshold = 110

# quantile
q = 0.25

def fetch_csv(csvPath: str) -> pd.DataFrame:
    return pd.read_csv(csvPath)

def get_regression(data: pd.DataFrame) -> [str]:
    regressions = []
    grouped_data = data.groupby(["scenario", "solution"])
    for (k, d) in grouped_data:

        if len(d["relative duration"].values) < n_samples:
            continue

        # take quantile .25 from last 10 items
        result = d["relative duration"][-n_samples:].quantile(q)
        if result > threshold:
            formatters = {
                'timestamp': (lambda a : a.strftime("%Y-%m-%d %H:%M:%S ")),
                'duration': (lambda a : "{:.2f}s".format(float(a))),
                'base duration': (lambda a : "{:.2f}s".format(float(a))),
                'relative duration': (lambda a : "{:.2f}%".format(float(a))),
            }
            columns = ['timestamp', 'version', 'duration', 'base duration', 'relative duration']
            header = "Scenario = " + str(d["scenario"].values[-1]) + "\n" + \
                     "Base Version = " + str(d["base version"].values[-1]) + "\n" + \
                     "Solution = " + str(d["solution"].values[-1])
            data_string = f'{d[-n_samples:].to_string(header=True, index=False, justify="right", columns=columns, formatters=formatters)}'
            line_length = len(data_string.splitlines()[0])
            line = '-' * line_length
            regressions.append('\n' + line)
            regressions.append(header)
            regressions.append(line)
            regressions.append(data_string)
            regressions.append(line)
            regressions.append("")

    return regressions

if __name__ == "__main__":
    data = fetch_csv(sys.argv[1])
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    data = data.loc[data["scenario"] != 'warmup']

    now = datetime.datetime.now(datetime.timezone.utc)
    cutoff_date = now - datetime.timedelta(days=n_days)
    data = data.loc[data["timestamp"] > cutoff_date]

    regressions = get_regression(data)

    if regressions:
        with open(sys.argv[2], 'w') as fp:
            fp.write('\n'.join([x for x in regressions]))
    elif os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])
