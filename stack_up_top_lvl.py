# Libraries
import os
import pandas as pd

import get_sample
import monte_carlo_stack_up


# creating orginal file Path of the data
cwd = os.getcwd()
file_title = 'stack_up_analysis.xlsx'
file_path = os.path.join(cwd, file_title)

# assigning both sheets to its own dataframe
sheet_title1 = 'internal_stack_up_data'
df1 = pd.read_excel(file_path, sheet_name=sheet_title1)
df_mod1 = df1.copy()
sheet_title2 = 'external_stack_up_data'
df2 = pd.read_excel(file_path, sheet_name=sheet_title2)
df_mod2 = df2.copy()

# normal_dist function takes each row and create a normal distribution
# output the average, standard dev and a random value from the normal dist
[in_samp_ave, in_samp_stdev, in_samp_rand] = get_sample.normal_dist(df_mod1)
[ex_samp_ave, ex_samp_stdev, ex_samp_rand] = get_sample.normal_dist(df_mod2)

# Monte Carlo Method (MCM)
internal_dim = monte_carlo_stack_up.in_body_measure(in_samp_rand)
external_dim = monte_carlo_stack_up.ex_body_measure(ex_samp_rand)
MCM_gap_dim = round(external_dim - internal_dim, 3)
print('Monte Carlo Method')
print('Internal Dimensions:', internal_dim, 'in.')
print('External Dimensions:', external_dim, 'in.')
print('Gap:', MCM_gap_dim, 'in.')


def main():
    pass


if __name__ == '__main__':
    main()
