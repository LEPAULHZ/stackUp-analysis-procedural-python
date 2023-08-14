# Monte Carlo Simulation method for random distribution
import numpy as np

# math for internal stack up
# sum all the individual random samples for each body together


def in_body_measure(in_samp_val):
    internal_body_stack = round(sum(in_samp_val), 3)
    return internal_body_stack

# math for external stack up
# not as straight forward and require understanding the ME design
# calculate the difference on the top and bottom bodies to get the thickness
# then sum all the individual random samples for each body together


def ex_body_measure(ex_samp_val):
    n = len(ex_samp_val)
    if n >= 5:
        ex_bot_layer = np.absolute(ex_samp_val[0]-ex_samp_val[1])
        ex_top_layer = np.absolute(ex_samp_val[-1]-ex_samp_val[-2])
        ex_mid_layer = sum(ex_samp_val[2:-2])
        external_body_stack = round(
            sum([ex_bot_layer, ex_top_layer, ex_mid_layer]), 3)
        return external_body_stack
    else:
        return print('ArgumentError: This particular case require atleast 5 argument')


def main():
    print('Running monte_carlo_stack_up module directly')


if __name__ == '__main__':
    main()
