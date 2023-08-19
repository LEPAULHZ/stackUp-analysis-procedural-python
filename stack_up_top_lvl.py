import os
import pandas as pd
import numpy as np
from matplotlib import pyplot
import get_sample
import limit_combinations
import monte_carlo_stack_up
import worst_case_stack_up
import RSS_stack_up

# --------------------------
# Data Loading and Settings
# --------------------------

# Creating original file path of the data
cwd = os.getcwd()
file_title = 'stack_up_analysis.xlsx'
file_path = os.path.join(cwd, file_title)

# Load data from Excel sheets into DataFrames
sheet_title1 = 'internal_stack_up_data'
df1 = pd.read_excel(file_path, sheet_name=sheet_title1)
df_mod1 = df1.copy()    # Create a copy to work with

sheet_title2 = 'external_stack_up_data'
df2 = pd.read_excel(file_path, sheet_name=sheet_title2)
df_mod2 = df2.copy()    # Create a copy to work with

# Set the sample size
sample_size = 1000

# ----------------------
# Generate Sample Data
# ----------------------

# Create instances of the RandomSampleGenerator class
sample_generator_internal = get_sample.RandomSampleGenerator(df_mod1)
sample_generator_external = get_sample.RandomSampleGenerator(df_mod2)

# Use the methods of the instance
# Create a vertical stack of 'ave', 'SD', and 'sample size' array
# Vectorize each row to create a normal distribution for each bodies
# Select a random value from each normal distribution
v_stack_internal = sample_generator_internal.vertical_stack(sample_size)
random_sample_internal = np.apply_along_axis(
    sample_generator_internal.normal_dist, axis=1, arr=v_stack_internal)
in_samp_rand = np.apply_along_axis(
    np.random.choice, axis=1, arr=random_sample_internal)

v_stack_external = sample_generator_external.vertical_stack(sample_size)
random_sample_external = np.apply_along_axis(
    sample_generator_external.normal_dist, axis=1, arr=v_stack_external)
ex_samp_rand = np.apply_along_axis(
    np.random.choice, axis=1, arr=random_sample_external)

# ----------------------
# Visualization Function
# ----------------------

# Function normal_dist_plot plot normal distribution for each bodies


def normal_dist_plot(some_array):
    pyplot.hist(some_array, bins=20)
    pyplot.title('%d Samples' % sample_size)
    return pyplot.show()


# Plotting all rows normal distribution
"""
in_samp_rand_plot = np.apply_along_axis(
    normal_dist_plot, axis=1, arr=random_sample_internal)
"""
# Plotting specific row(s) normal distribution
"""
normal_dist_plot(random_sample_external[0])
"""


# -------------------------------------
# Analysis Using Different Methods
# -------------------------------------

print('___________________________________')

# Monte Carlo Method (MCM)
try:
    internal_dim_MCM = monte_carlo_stack_up.in_body_measure(in_samp_rand)
    external_dim_MCM = monte_carlo_stack_up.ex_body_measure(ex_samp_rand)
    MCM_gap_dim = round(external_dim_MCM - internal_dim_MCM, 3)
    print('Monte Carlo Method')
    print('Internal Dimensions:', '|', internal_dim_MCM, 'in. |')
    print('External Dimensions:', '|', external_dim_MCM, 'in. |')
    print('Gap:', '|', MCM_gap_dim, 'in. |')
except Exception as NotEnoughExternalBodies:
    print('NotEnoughExternalBodies')

print('___________________________________')

# Worst Case Method (WCM)
try:
    [internal_Ldim_WCM, internal_Udim_WCM] = worst_case_stack_up.in_nominal_measure(
        df_mod1)
    [external_Ldim_WCM, external_Udim_WCM] = worst_case_stack_up.ex_nominal_measure(
        df_mod2)
    [min_diff_WCM, max_diff_WCM, min_label_WCM, max_label_WCM, print_results_WCM] = limit_combinations.calculate_limit_combinations(
        internal_Ldim_WCM, internal_Udim_WCM, external_Ldim_WCM, external_Udim_WCM)

    print('Worst Case Method')
    print('Internal Dimensions: |Lower Limit:', internal_Ldim_WCM, 'in.|',
          '|Upper Limit:', internal_Udim_WCM, 'in.|')
    print('External Dimensions: |Lower Limit:', external_Ldim_WCM, 'in.|',
          '|Upper Limit:', external_Udim_WCM, 'in.|')
    print("Minimum Gap:", min_label_WCM, '|', min_diff_WCM, 'in.|')
    print("Maximum Gap:", max_label_WCM, '|', max_diff_WCM, 'in.|')
    print(print_results_WCM)


except Exception as NotEnoughExternalBodies:
    print('NotEnoughExternalBodies')

print('___________________________________')

# Root Sum Square (RSS)
try:
    [internal_Ldim_RSS, internal_Udim_RSS] = RSS_stack_up.in_RSS(df_mod1)
    [external_Ldim_RSS, external_Udim_RSS] = RSS_stack_up.ex_RSS(df_mod2)
    [min_diff_RSS, max_diff_RSS, min_label_RSS, max_label_RSS, print_results_RSS] = limit_combinations.calculate_limit_combinations(
        internal_Ldim_RSS, internal_Udim_RSS, external_Ldim_RSS, external_Udim_RSS)
    print('Root Sum Square Method')
    print('Internal Dimensions: |Lower Limit:', internal_Ldim_RSS, 'in.|',
          '|Upper Limit:', internal_Udim_RSS, 'in.|')
    print('External Dimensions: |Lower Limit:', external_Ldim_RSS, 'in.|',
          '|Upper Limit:', external_Udim_RSS, 'in.|')
    print("Minimum Gap:", min_label_RSS, '|', min_diff_RSS, 'in.|')
    print("Maximum Gap:", max_label_RSS, '|', max_diff_RSS, 'in.|')
    print(print_results_RSS)

except Exception as NotEnoughExternalBodies:
    print('NotEnoughExternalBodies')


def main():
    pass


if __name__ == '__main__':
    main()
