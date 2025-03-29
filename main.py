"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    data = []

    # open file using file I/O and read it into the `data` list
    file = open(filename, "r")
    data = file.read().split("\n")
    file.close()

    # Use `filter_nondigits` to clean the data and remove invalid entries, 
    # save the output to a new variable
    clean_data = filter_nondigits(data)

    if not clean_data:
        print("Error! No rates counted")
      

    # plot this data to explore changes in heart rate for this file, 
    # save this visualization to the "images" folder
    plt.figure(figsize=(10, 5))
    plt.plot(clean_data, marker='o', linestyle='-', color='b', label="Heart Rate")
    plt.xlabel("Time (5 min intervals)")
    plt.ylabel("Heart Rate (BPM)")
    plt.title("Heart Rate Data from " + filename)
    plt.legend()
    plt.grid(True)

    plt.savefig("images/" + filename.split("/")[-1].replace(".txt", ".png"))
    plt.close()

    # calculate the average, maximum, and standard deviation of this 
    # file using the functions you've wrote
    avg_hr = average(clean_data)
    max_hr = maximum(clean_data)
    std_dev_hr = standard_deviation(clean_data)

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr

if __name__ == "__main__":
    print(run("data/phase0.txt"))
    print(run("data/phase1.txt"))
    print(run("data/phase2.txt"))
    print(run("data/phase3.txt"))
