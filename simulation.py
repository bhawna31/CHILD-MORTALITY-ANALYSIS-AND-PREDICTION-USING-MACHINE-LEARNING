# def simulate_policy(prediction, healthcare, nutrition):

#     reduction = (healthcare * 0.05) + (nutrition * 0.04)
#     new_value = prediction * (1 - reduction)

#     return int(new_value)


def simulate_policy(prediction, healthcare, nutrition):

    reduction = (healthcare * 0.05) + (nutrition * 0.04)
    new_value = prediction * (1 - reduction)

    return int(new_value)