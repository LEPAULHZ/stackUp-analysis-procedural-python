import os
import pandas as pd
import numpy as np
from matplotlib import pyplot
import get_sample
import limit_combinations
import monte_carlo_stack_up
import worst_case_stack_up
import RSS_stack_up

# Function to load data from Excel sheets into DataFrames


def load_data(file_path):
    sheet_title1 = 'internal_stack_up_data'
    df1 = pd.read_excel(file_path, sheet_name=sheet_title1)
    df_mod1 = df1.copy()    # Create a copy to work with

    sheet_title2 = 'external_stack_up_data'
    df2 = pd.read_excel(file_path, sheet_name=sheet_title2)
    df_mod2 = df2.copy()    # Create a copy to work with

    return df_mod1, df_mod2

# Function to generate sample data using RandomSampleGenerator class


def generate_sample_data(sample_generator, sample_size):
    v_stack = sample_generator.vertical_stack(sample_size)
    random_sample = np.apply_along_axis(
        sample_generator.normal_dist, axis=1, arr=v_stack)
    return np.apply_along_axis(
        np.random.choice, axis=1, arr=random_sample)

# Function to plot a normal distribution


def plot_normal_distribution(some_array, sample_size):
    pyplot.hist(some_array, bins=20)
    pyplot.title('%d Samples' % sample_size)
    pyplot.show()

# Function to perform Monte Carlo analysis


def perform_monte_carlo(df_mod1, df_mod2, sample_size):
    # Load data and create instances of the RandomSampleGenerator class
    sample_generator_internal = get_sample.RandomSampleGenerator(df_mod1)
    sample_generator_external = get_sample.RandomSampleGenerator(df_mod2)

    # Generate random samples for internal and external dimensions
    in_samp_rand = generate_sample_data(sample_generator_internal, sample_size)
    ex_samp_rand = generate_sample_data(sample_generator_external, sample_size)

    # Perform Monte Carlo analysis
    monte_carlo_stack_up.analyze_monte_carlo(
        in_samp_rand, ex_samp_rand, sample_size)

# Function to perform Worst Case Method analysis


def perform_worst_case(df_mod1, df_mod2):
    # Perform Worst Case Method analysis
    worst_case_stack_up.analyze_worst_case(df_mod1, df_mod2)

# Function to perform Root Sum Square analysis


def perform_root_sum_square(df_mod1, df_mod2):
    # Perform Root Sum Square analysis
    RSS_stack_up.analyze_root_sum_square(df_mod1, df_mod2)

# Main function


def main():
    # Creating original file path of the data
    cwd = os.getcwd()
    file_title = 'stack_up_analysis.xlsx'
    file_path = os.path.join(cwd, file_title)

    # Load data
    df_mod1, df_mod2 = load_data(file_path)

    # Set the sample size
    sample_size = 1000

    # Perform different analysis methods
    perform_monte_carlo(df_mod1, df_mod2, sample_size)
    perform_worst_case(df_mod1, df_mod2)
    perform_root_sum_square(df_mod1, df_mod2)


if __name__ == '__main__':
    main()
