# Worst Case method utilize simple arithmetic
# This method assumed the extreme limits
# Recommend this method for low production volumes
import numpy as np

# math for internal stack up
# sum all the nominal measurement
# sum all the upper tolerance
# sum all the lower tolerance
# upper limit is calculated by nominal + upper
# lower limit is calculated by nominal - lower


def in_nominal_measure(data_frame):
    nominal_values = data_frame.loc[i, 'Nominal']

    internal_body_stack = round(sum(nominal_values), 3)
    return internal_body_stack


def ex_nominal_measure(ex_samp_val):
    external_body_stack = round(sum(ex_samp_val), 3)
    return external_body_stack


def main():
    print('Running worst_case_stack_up module directly')


if __name__ == '__main__':
    main()
