def display_high_low(last_names, scores):
    high_var = 0
    high_index = 0

    low_var = 999
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i

        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i


    print("Highest Score:")
    print("Last Name:", last_names[high_index])
    print("Score:", scores[high_index])
    print()

    print("Lowest Score:")
    print("Last Name:", last_names[low_index])
    print("Score:", scores[low_index])

last_names = []
scores = []

file = open("M13P3.txt", "r")
last_name = file.readline().strip()

while last_name != "":
    score = float(file.readline())

    last_names.append(last_name)
    scores.append(score)

    last_name = file.readline().strip()

file.close()

display_high_low(last_names, scores)