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
    in_nominal_val = data_frame.loc[i, 'Nominal']
    in_upper_tol = data_frame.loc[i, 'Tolerance']
    in_lower_tol = data_frame.loc[i, 'Tolerance']
    in_sum_nom_val = sum(in_nominal_val)
    in_sum_up_tol = sum(in_upper_tol)
    in_sum_low_tol = sum(in_lower_tol)
    in_upper_lim = round(in_sum_nom_val - in_sum_up_tol, 3)
    in_lower_lim = round(in_sum_nom_val - in_sum_low_tol, 3)

    return [in_upper_lim, in_lower_lim]

# math for external stack up
# not as straight forward and require understanding the ME design
# calculate the difference on the top and bottom bodies to get the thickness


def ex_nominal_measure(data_frame):
    # extracting all the values in nomminal col
    # first arithmitic operation is to determine the material thickness between top and bottom bodies
    n = len(data_frame.idex)
    if n >= 5:
        ex_nominal_val = data_frame.loc[i, 'Nominal']
        ex_nom_bot_layer = np.absolute(ex_nominal_val[0]-ex_nominal_val[1])
        ex_nom_top_layer = np.absolute(ex_nominal_val[-1]-ex_nominal_val[-2])
        ex_upper_tol = data_frame.loc[i, 'Tolerance']
        ex_lower_tol = data_frame.loc[i, 'Tolerance']
        external_body_stack = round(sum(ex_samp_val), 3)
        return external_body_stack
    else:
        return print('ArgumentError: This particular case require atleast 5 argument')


def main():
    print('Running worst_case_stack_up module directly')


if __name__ == '__main__':
    main()
