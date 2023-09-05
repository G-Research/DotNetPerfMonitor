"""Save benchmark results to a file."""
import csv
from datetime import datetime


def camel_casify_solution_name(string):
    """This method converts a string to camel case"""
    parts = string.split('_')
    camel_case_parts = [part.capitalize() for part in parts[:-1]]
    return ''.join(camel_case_parts)


def print_csv_content(file_path):
    """Prints content of csv file for debugging purposes"""
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)


def save_benchmark_results(file_path, benchmark_duration, benchmark_base_duration, sdk_version, sdk_daily_version, test_case_name, test_scenario):
    """Saves bencharmk results to a csv file

    Args:
        file_path (_type_): _description_
    """
    # Get the benchmark results and create a row data
    # row_data = [version,base version,scenario,test case,timestamp,duration,base duration,relative duration]
    version = sdk_daily_version
    base_version = sdk_version
    timestamp = datetime.utcnow().isoformat(timespec='seconds')
    scenario = test_scenario
    test_case = test_case_name
    duration = benchmark_duration
    base_duration = benchmark_base_duration
    relative_duration = abs(base_duration - duration)
    benchmark_results = [version, base_version, scenario, test_case,
                         timestamp, duration, base_duration, relative_duration]

    with open(file_path, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(benchmark_results)

    print_csv_content(file_path)
