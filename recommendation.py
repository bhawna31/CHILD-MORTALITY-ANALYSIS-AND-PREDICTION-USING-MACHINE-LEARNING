# # def detect_trend(data):
# #     if len(data) < 2:
# #         return "stable"
# #     return "increasing" if data[-1] > data[0] else "decreasing"


# # def generate_recommendation(pred, trend):

# #     if pred > 10000:
# #         risk = "HIGH"
# #         actions = [
# #             "Increase healthcare funding",
# #             "Improve child nutrition",
# #             "Expand vaccination programs"
# #         ]
# #     elif pred > 5000:
# #         risk = "MEDIUM"
# #         actions = [
# #             "Improve sanitation",
# #             "Strengthen monitoring"
# #         ]
# #     else:
# #         risk = "LOW"
# #         actions = ["Situation stable"]

# #     if trend == "increasing":
# #         actions.append("Mortality rising → Immediate action required")

# #     return risk, actions


def detect_trend(data):
    if len(data) < 2:
        return "stable"
    return "increasing" if data[-1] > data[0] else "decreasing"


def generate_recommendation(pred, trend):

    if pred > 10000:
        risk = "HIGH"
        actions = [
            "Increase healthcare funding",
            "Improve child nutrition",
            "Expand vaccination programs"
        ]
    elif pred > 5000:
        risk = "MEDIUM"
        actions = [
            "Improve sanitation",
            "Strengthen healthcare monitoring"
        ]
    else:
        risk = "LOW"
        actions = ["Situation stable"]

    if trend == "increasing":
        actions.append("Mortality rising → Immediate action required")

    return risk, actions


# def detect_trend(values):
#     if len(values) < 2:
#         return "Stable"
#     if values[-1] > values[0]:
#         return "Increasing"
#     elif values[-1] < values[0]:
#         return "Decreasing"
#     return "Stable"


# def generate_recommendation(prediction, trend):
#     if prediction > 8000:
#         risk = "High"
#         actions = [
#             "Increase healthcare funding",
#             "Strengthen child health programs",
#             "Expand vaccination coverage"
#         ]
#     elif prediction > 4000:
#         risk = "Medium"
#         actions = [
#             "Monitor regional healthcare performance",
#             "Improve nutrition programs"
#         ]
#     else:
#         risk = "Low"
#         actions = [
#             "Maintain healthcare policies",
#             "Continue preventive care"
#         ]

#     if trend == "Increasing":
#         actions.append("Immediate intervention recommended")

#     return risk, actions