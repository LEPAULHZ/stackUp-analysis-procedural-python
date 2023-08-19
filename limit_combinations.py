def calculate_limit_combinations(internal_lower_limit, internal_upper_limit, external_lower_limit, external_upper_limit):
    # Calculate the differences between upper and lower limits for the possible combinations
    combinations = [
        external_upper_limit - internal_upper_limit,
        external_upper_limit - internal_lower_limit,
        external_lower_limit - internal_upper_limit,
        external_lower_limit - internal_lower_limit
    ]

    # Labels for the combinations
    labels = [
        '(external upper - internal upper)',
        '(external upper - internal lower)',
        '(external lower - internal upper)',
        '(external lower - internal lower)'
    ]

    # Find indices of minimum and maximum differences
    min_diff_index = combinations.index(min(combinations))
    max_diff_index = combinations.index(max(combinations))

    # Retrieve minimum and maximum differences
    min_difference = round(combinations[min_diff_index], 3)
    max_difference = round(combinations[max_diff_index], 3)

    # Retrieve corresponding labels
    min_label = labels[min_diff_index]
    max_label = labels[max_diff_index]

    # Check for interference and populate the result list
    if min_difference < 0 or max_difference < 0:
        # If either the minimum or maximum difference is negative, interference exists
        result_message = 'There exists an interference: '

        # Determine which label corresponds to the interference
        if min_difference < max_difference:
            result_message += f'{min_label} is negative'
        else:
            result_message += f'{max_label} is negative'

    else:
        result_message = 'There are positive spacing'

    return [min_difference, max_difference, min_label, max_label, result_message]
