# Worst Case method utilize simple arithmetic
# This method assumed the extreme limits
# Recommend this method for low production volumes
import numpy as np

# Math for internal stack up
# Upper limit determines by Max Material Conditions (MMC)
# Lower limit determines by Least Material Conditions (LMC)
# Straight forrward logic and airthmetic


def in_nominal_measure(data_frame):
    # Extract 'Nominal', 'Tolerance' columns as NumPy arrays
    in_nominal_val = data_frame['Nominal'].to_numpy()
    in_lower_tol = data_frame['Tolerance'].to_numpy()
    in_upper_tol = data_frame['Tolerance'].to_numpy()

    # Calculate sum of 'Nominal', 'Tolerance' values
    in_sum_nom_val = sum(in_nominal_val)
    in_sum_low_tol = sum(in_lower_tol)
    in_sum_up_tol = sum(in_upper_tol)

    # Calculate upper and lower limits
    in_lower_lim = round(in_sum_nom_val - in_sum_low_tol, 3)
    in_upper_lim = round(in_sum_nom_val + in_sum_up_tol, 3)
    return [in_lower_lim, in_upper_lim]

# Math for external stack up
# Not as straight forward and require understanding the ME design
# Understand subject like Material Conditions (MC) for CAD designs
# Upper limit determines by Max Material Conditions (MMC)
# Lower limit determines by Least Material Conditions (LMC)


def ex_nominal_measure(data_frame):
    n = len(data_frame.index)
    if n >= 5:
        # Extract 'Nominal', 'Tolerance' columns as NumPy arrays
        ex_nominal_val = data_frame['Nominal'].to_numpy()
        ex_lower_tol = data_frame['Tolerance'].to_numpy()
        ex_upper_tol = data_frame['Tolerance'].to_numpy()

        # Calculate lower and upper values of the array using vectorized operations
        ex_lower_val = ex_nominal_val - ex_lower_tol
        ex_upper_val = ex_nominal_val + ex_upper_tol

        # Adjust the first and last row limits
        # The lower limit for the first and last row is when we have MMC
        # The upper limit for the first and last row is when we have LMC
        # This logic is opposite for all the other parts
        ex_lower_val[0] = ex_nominal_val[0] + ex_lower_tol[0]
        ex_lower_val[-1] = ex_nominal_val[-1] + ex_lower_tol[-1]
        ex_upper_val[0] = ex_nominal_val[0] - ex_upper_tol[0]
        ex_upper_val[-1] = ex_nominal_val[-1] - ex_upper_tol[-1]

        # Calculate upper and lower limits
        ex_lower_lim = round(((ex_lower_val[1]-ex_lower_val[0]) + (
            sum(ex_lower_val[2:-2])) + (ex_lower_val[-2]-ex_lower_val[-1])), 3)
        ex_upper_lim = round(((ex_upper_val[1]-ex_upper_val[0]) + (
            sum(ex_upper_val[2:-2])) + (ex_upper_val[-2]-ex_upper_val[-1])), 3)
        return [ex_lower_lim, ex_upper_lim]

    else:
        return print('ArgumentError: This particular case require atleast 5 argument')
