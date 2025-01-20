import random

# List of names
names = [
    "faissel",
    "saif",
    "kareem",
    "kerllos",
    "Moaz Nasser",
    "Moaz Kamal",
    "Adham",
    "Mohamed Assem",
    "Michel",
    "Mostafa E.",
    "Mostafa S.",
    "Yahia",
    "Abdelrahman H.",
    "Ahmed Anwar",
    "Ahmed Hany",
    "Mazen Megahd",
    "Yousef",
    "Nour",
    "Desoky",
    "Mohamed Hany",
    "Ahmed Ramadan",
    "Adelrahman R.",
]

# Shuffle the list of names to randomize it
for _ in range(0, 10):
    random.shuffle(names)

# Split into 3 teams of 4 members and 2 teams of 5 members
teams = {
    "Team 1": names[:4],
    "Team 2": names[4:8],
    "Team 3": names[8:12],
    "Team 4": names[12:17],
    "Team 5": names[17:],
}

# Print the teams
for team, members in teams.items():
    print(f"{team}: {', '.join(members)}")
