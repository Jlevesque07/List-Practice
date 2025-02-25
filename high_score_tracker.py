# TASK: Create a high score tracker that keeps the top 5 scores.

def score_adder(score: int) -> list:
    high_scores.append(score)
    high_scores.sort()
    high_scores.reverse()
    return high_scores[:5]
# Sort the list in descending order
# Keep only the top 5 scores
# Return the updated list
# Start with an empty high scores list
# Use a loop to let the user enter scores until they type -1
# Call the function with each new score and display the updated top 5 scores
high_scores = []
while True:
    question = input("Would you like to input a new high score? [y/n] ").strip().lower()
    if question == "y":
        score = int(input("What is your score? "))
        print(score_adder(score))
    else:
        break