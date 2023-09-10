#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # calculate average score
    total = 0
    for score in scores:
        total += score
    average = round(total / len(scores))
    low_score = min(scores)
    high_score = max(scores)   
    median = len(scores) // 2
    if len(scores) % 2 == 1:  
        median_score = scores[median]
    else:                     
        middle1 = scores[median]
        middle2 = scores[median-1]
        median_score = (middle1 + middle2)/2
    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)
    print("Low Score:       ", low_score)
    print("High Score:      ", high_score)
    print("Median Score:    ", median_score)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


