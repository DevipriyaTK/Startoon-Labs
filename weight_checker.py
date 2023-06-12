def can_form_weight(W, weights):
    if W == 0:
        return True
    if len(weights) == 0:
        return False

    current_weight = weights[0]

    # Check if the current weight is equal to W
    if current_weight == W:
        return True

    # Check if we can form W using the remaining weights
    if can_form_weight(W - current_weight, weights[1:]):
        return True

    # Check if we can form W without using the current weight
    if can_form_weight(W, weights[1:]):
        return True

    return False
W = 15
list = [4, 3, 5, 6, 4]
print(can_form_weight(W, lists))
W = 9
list = [4, 1, 3, 7]
print(can_form_weight(W, lists))

