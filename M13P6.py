players = {}

file = open("M13P6.txt", "r")

last_name = file.readline().strip()

while last_name != "":
    batting_average = float(file.readline())
    players[last_name] = batting_average
    last_name = file.readline().strip()

file.close()

print(f"{'Player Name':<20}{'Batting Average':>20}")
print("-" * 40)

for name, average in players.items():
    print(f"{name:<20}{average:>20.3f}")