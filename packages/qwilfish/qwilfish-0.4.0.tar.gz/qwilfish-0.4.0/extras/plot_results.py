import glob
import matplotlib.pyplot as plt
import random
import re
import sqlite3
import statistics

'''
Script that will read data from a number of database files and produce some
results based on the contents. Results will be stored in respective files
either as text or as plots.

Out files:
    time_stats.txt - Basic statistics about elapsed time
'''

MAIN_TABLE = 0
GRPC_TABLE = 0
CONF_TABLE = 0

WANTED_COLS = ["caseno",
               "timestamp",
               "fitness_score",
               "result",
               "mab.<letter>.z",
               "mab.<letter>.e",
               "mab.<letter>.b",
               "mab.<letter>.r",
               "mab.<letter>.k"]

def main():
    # Get all the database files in the current folder
    databases = glob.glob("./*.db")

    # Keep only the columns of interest from the databases that where found
    databases_filtered = []
    for db in databases:
        databases_filtered.append(extract_cols(db))

    # Calculate statistics on the timing, write to file
    calculate_time_stats(databases_filtered)

    # Calculate some basic statistics on failed/passed test cases
    calculate_results_stats(databases_filtered)

    # Calculate average mab switch state across campaigns, plot vs testcase
    plot_avg_switch_states(databases_filtered)

    # Calculate average mab switch state across testcase, show in boxplot
    boxplot_switch_states(databases_filtered)

    # Plot the memory usage and the fitness function from a random campaign
    plot_mem_usage_fitness(databases_filtered)



def extract_cols(database):
    cols = {}

    # Connect to the database
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Get the tables from the database
    c.execute("SELECT name FROM sqlite_master WHERE type=\"table\";")
    tables = [table[0] for table in c.fetchall()]
    #main_table = tables[MAIN_TABLE][0]
    #grpc_table = tables[GRPC_TABLE][0]
    #conf_table = tables[CONF_TABLE][0]

    # Extract wanted columns from tables
    for table in tables:
        for colname in WANTED_COLS:
            c.execute(f"PRAGMA table_info(\"{table}\");")
            if colname not in [n[1] for n in c.fetchall()]:
                continue
            c.execute(f"SELECT \"{colname}\" from \"{table}\";")
            cols.update({colname: [d[0] for d in c.fetchall()]})

    # Close the database
    c.close()
    conn.close()

    return cols



def convert_mab_switch_names(names):
    # Assume names is a list of strings (or dict keys) of the format
    # "mab.<some-symbol-name>.<a-possible-expansion-for-the-symbol>"

    if isinstance(names, str):
        names_list = [names]
    else:
        names_list = names

    labels = [str(name).split(".")[2] for name in names_list]
    labels = [re.sub("[<>]", "", label) for label in labels]
    labels = [str(label).split("-")[2].capitalize() for label in labels]

    if isinstance(names, str):
        return labels[0]
    else:
        return labels



def calculate_time_stats(databases):
    campaign_deltas = []
    case_deltas = []
    for db in databases:
        timestamps = db["timestamp"]
        campaign_deltas.append(float(timestamps[-1]) - float(timestamps[0]))

        for i in range(1, len(timestamps)-1):
            case_deltas.append(float(timestamps[i]) - float(timestamps[i-1]))

    campaign_delta = (statistics.mean(campaign_deltas),
                      statistics.pstdev(campaign_deltas))
    case_delta = (statistics.mean(case_deltas),
                  statistics.pstdev(case_deltas))

    with open("time_stats.txt", "w") as f:
        f.write("Campaign delta:\n")
        f.write(f"    mean: {campaign_delta[0]}\n")
        f.write(f"    sdev: {campaign_delta[1]}\n")
        f.write("Case delta:\n")
        f.write(f"    mean: {case_delta[0]}\n")
        f.write(f"    sdev: {case_delta[1]}\n")

def calculate_results_stats(databases):
    registered_fails = 0
    registered_mem_inc = 0
    mem_slice_len = 1000

    for db in databases:
        results = db["result"]
        registered_fails += results.count("FAIL")


def plot_avg_switch_states(databases):
    # Get a list of case numbers
    caseno = databases[0]["caseno"]

    for colname in WANTED_COLS:
        # Only interested in mab switch columns
        if not colname.startswith("mab."):
            continue

        # Store mab values in a list of tuples, tuple[0] is campaign 1 etc...
        mabs = []
        for db in databases:
            mabs.append(db[colname])

        # Calculate the mean+sdev across the different campaigns (each tuple)
        # mab_mean[0] will be the mean value for caseno 1 across the campaigns
        mab_mean = []
        #mab_lo = []
        #mab_hi = []
        for vals in list(zip(*mabs)):
            mab_mean.append(statistics.mean(vals))
            #mab_lo.append(statistics.mean(vals) - statistics.pstdev(vals))
            #mab_hi.append(statistics.mean(vals) + statistics.pstdev(vals))

        # General configuration for plotting
        fig, ax = plt.subplots()
        ax.set_title(f"{convert_mab_switch_names(colname)} " +
                     "MAB Switch Activity")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        # Configure X-axis
        ax.set_xlabel("Case Number")
        ax.set_xlim(0)
        x_max = len(caseno)
        ax.xaxis.set_ticks([0, x_max//4, x_max//2, 3*x_max//4, x_max])
        # Configure Y-axis
        ax.set_ylabel("Campaign-Mean")
        ax.set_ylim([0, 1.1])
        # Plot!
        ax.plot(caseno, mab_mean, '-')
        # ax.fill_between(caseno, mab_lo, mab_hi, alpha=0.5)
        # Save!
        fig.savefig(f"{convert_mab_switch_names(colname)}.pdf",
                    format="pdf",
                    bbox_inches="tight")

        # Reset
        plt.clf()
        plt.close()



def boxplot_switch_states(databases):
    mab_stats = {}
    for colname in WANTED_COLS:
        # Only interested in mab switch columns
        if not colname.startswith("mab."):
            continue

        # Store mab values in a list of tuples, tuple[0] is campaign 1 etc...
        mab_means = []
        for db in databases:
            mab_means.append(statistics.fmean(db[colname]))

        mab_stats.update({colname: mab_means})

    # General configuration for plotting
    fig, ax = plt.subplots()
    ax.set_title("MMSS distribution across campaigns")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # Configure Y-axis
    ax.set_ylabel("Mean MAB Switch State (MMSS)")
    ax.set_ylim([0, 1.1])

    ax.boxplot(mab_stats.values(), widths=0.3, patch_artist=True,
               showcaps=False,
               medianprops={"color": "black", "linewidth": 2.0},
               boxprops={"facecolor": "white", "edgecolor": "gray",
                         "linewidth": 2.0},
               whiskerprops={"color": "gray", "linewidth": 2.0})
    labels = convert_mab_switch_names(mab_stats.keys())
    ax.set_xticklabels(labels=labels, rotation=45, ha="right")

    # Reset
    plt.tight_layout()
    fig.savefig("switch_activity_boxplot.pdf", format="pdf",
                bbox_inches="tight")
    plt.clf()
    plt.close()



def plot_mem_usage_fitness(databases):
    # Pick a database randomly
    index = random.randrange(0, len(databases)-1)
    database = databases[index]
    # Get the case number vector
    caseno = database["caseno"]

    # General configuration for plotting
    fig, (ax1, ax2) = plt.subplots(2,1)

    # Configure memory usage plot
    ax1.set_title(f"Example from campaign #{index}")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    # Configure X-axis
    ax1.set_xlabel("Case Number")
    ax1.set_xlim(0)
    x_max = len(caseno)
    ax1.xaxis.set_ticks([0, x_max//4, x_max//2, 3*x_max//4, x_max])
    # Configure Y-axis
    ax1.set_ylabel("Memory usage [KiB]")

    # Configure fitness function plot
    ax2.set_title(f"Example from campaign #{index}")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    # Configure X-axis
    ax2.set_xlabel("Case Number")
    ax2.set_xlim(0)
    x_max = len(caseno)
    ax2.xaxis.set_ticks([0, x_max//4, x_max//2, 3*x_max//4, x_max])
    # Configure Y-axis
    ax2.set_ylabel("Fitness function score")

    # Plot!
    ax2.plot(caseno, database["fitness_score"], '-')

    # Reset
    plt.tight_layout()
    fig.savefig("mem_usage_fitness_func_sample.pdf", format="pdf",
                bbox_inches="tight")
    plt.clf()
    plt.close()



if __name__ == "__main__":
    main()
