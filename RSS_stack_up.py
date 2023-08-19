# RSS method assume a normal statistical distribution
import numpy as np
sigma = 3


def in_RSS(data_frame):
    # Extract 'Nominal', 'SD' columns as NumPy arrays
    in_nominal_val = data_frame['Nominal'].to_numpy()
    in_SD_val = data_frame['SD'].to_numpy()

    # Calculate squares of standard deviations
    in_SD_square = in_SD_val ** 2

    # Calculate Root Sum Square (RSS) & 'Nominal' sum
    in_rss = np.sqrt(np.sum(in_SD_square))
    in_nominal_sum = sum(in_nominal_val)

    # Calculate 3 sigma tolerance zone
    in_tol = in_rss * sigma

    # Calculate upper and lower limits
    in_lower_lim = round(in_nominal_sum - in_tol, 3)
    in_upper_lim = round(in_nominal_sum + in_tol, 3)
    return [in_lower_lim, in_upper_lim]


def ex_RSS(data_frame):
    n = len(data_frame.index)
    if n >= 5:
        # Extract 'Nominal', 'SD' columns as NumPy arrays
        ex_nominal_val = data_frame['Nominal'].to_numpy()
        ex_SD_val = data_frame['SD'].to_numpy()

        # Calculate squares of standard deviations
        ex_SD_square = ex_SD_val ** 2

        # Calculate Root Sum Square (RSS) & 'Nominal' sum
        ex_rss = np.sqrt(np.sum(ex_SD_square))
        ex_nominal_sum = (ex_nominal_val[1] - ex_nominal_val[0]) + sum(
            ex_nominal_val[2:-2]) + (ex_nominal_val[-2] - ex_nominal_val[-1])

        # Calculate 3 sigma tolerance zone
        ex_tol = ex_rss * sigma

        # Calculate upper and lower limits
        ex_lower_lim = round(ex_nominal_sum - ex_tol, 3)
        ex_upper_lim = round(ex_nominal_sum + ex_tol, 3)
        return [ex_lower_lim, ex_upper_lim]

    else:
        return print('ArgumentError: This particular case require atleast 5 argument')
