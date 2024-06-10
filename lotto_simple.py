# Simple PowerBall lottery number generator
# Made by SuperMcFamous 
 
from collections import Counter

def predict_next_numbers(data):
    # Flatten the list of past winning numbers
    all_numbers = [number for draw in data for number in draw]

    # Count the frequency of each number
    number_counts = Counter(all_numbers)

    # Find the most common numbers
    most_common_numbers = number_counts.most_common(5)
    predicted_main_numbers = [number for number, _ in most_common_numbers]

    # Predict the Powerball number based on frequency
    powerball_numbers = [draw[-1] for draw in data]
    powerball_number_counts = Counter(powerball_numbers)
    predicted_powerball_number = powerball_number_counts.most_common(1)[0][0]

    return predicted_main_numbers, predicted_powerball_number

# Example usage:
historical_data = [
    (8, 44, 45, 51, 69, 12),
    (19, 29, 35, 36, 45, 16),
    (28, 38, 52, 54, 68, 8),
    (17, 34, 56, 60, 61, 9),
    (9, 30, 39, 49, 59, 21),
    (6, 33, 35, 36, 64, 24),
    (5, 16, 18, 26, 67, 4),
    (1, 7, 48, 64, 68, 5),
    (19, 36, 37, 42, 59, 19),
    (19, 42, 45, 55, 69, 6),
    (5, 14, 29, 38, 66, 1),
    (3, 6, 39, 49, 67, 21),
    (7, 41, 43, 44, 51, 5),
    (14, 20, 23, 53, 69, 4),
    (1, 11, 19, 21, 68, 15),
    (11, 38, 47, 67, 69, 14),
    (9, 30, 53, 55, 62, 23),
    (2, 20, 22, 26, 47, 21),
    (12, 16, 33, 39, 52, 1),
    (4, 35, 41, 44, 58, 25),
    (24, 29, 44, 47, 54, 2),
    (7, 16, 41, 56, 61, 23),
    (7, 33, 40, 43, 69, 10),
    (6, 7, 12, 24, 36, 15),
    (6, 21, 23, 39, 54, 23),
    (22, 27, 44, 52, 69, 9),
    (11, 38, 41, 62, 65, 15),
    (19, 24, 40, 42, 56, 23),
    (12, 13, 33, 50, 52, 23),
    (37, 46, 57, 60, 66, 8),
    (7, 11, 19, 53, 68, 23),
    (6, 23, 25, 34, 51, 3),
    (13, 22, 27, 54, 66, 9),
    (10, 17, 20, 39, 44, 16),
    (12, 23, 44, 57, 61, 5),
    (21, 29, 54, 59, 62, 4),
    (1, 3, 7, 16, 66, 5),
    (30, 36, 49, 52, 63, 16),
    (6, 19, 28, 44, 60, 10),
    (36, 42, 50, 52, 67, 26),
    (3, 18, 27, 36, 53, 12),
    (16, 26, 29, 38, 50, 6),
    (24, 29, 42, 51, 54, 16),
    (3, 8, 40, 53, 58, 3),
    (4, 27, 33, 41, 42, 14),
    (4, 23, 45, 50, 53, 17),
    (6, 28, 59, 62, 69, 21),
    (1, 4, 45, 47, 67, 18),
    (17, 36, 43, 53, 67, 14),
    (27, 28, 34, 37, 44, 8),
    (12, 21, 62, 67, 69, 17),
    # Add more historical data here...
]

predicted_main_numbers, predicted_powerball_number = predict_next_numbers(historical_data)

print("Predicted next main numbers:", predicted_main_numbers)
print("Predicted next Powerball number:", predicted_powerball_number)
