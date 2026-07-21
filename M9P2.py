def compute_batting_average(hits, at_bats):
    batting_average = hits / at_bats
    return batting_average

player_count = 0

response = input("Do you want to enter player information? Enter Yes to continue: ")

while response == "Yes" or response == "yes" or response == "Y" or response == "y":
    last_name = input("Enter the player's last name: ")
    hits = float(input("Enter the number of hits: "))
    at_bats = float(input("Enter the number of at-bats: "))

    batting_average = compute_batting_average(hits, at_bats)

    player_count = player_count + 1

    print("Last Name:", last_name)
    print("Batting Average:", format(batting_average, ".3f"))
    print()

    response = input("Do you want to enter player information? Enter Yes to continue: ")

print("Number of players entered:", player_count)