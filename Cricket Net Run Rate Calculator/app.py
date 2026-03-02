print("Hi, Welcome to Net Run Rate Calculator")
team1 = input("Enter Team 1 Name: ")
team2 = input("Enter Team 2 Name: ")
overs = float(input("Total Overs in the Match: "))
#Taking Team 1 Info
team1_run = int(input(f"Run scored by {team1}: "))
team1_overs = float(input(f"Total Overs Faced by {team1}, if all out then {overs}: "))
team1_val = (team1_run/team1_overs)
#Taking Team 2 Info
team2_run = int(input(f"Run scored by {team2}: "))
team2_overs = float(input(f"Total Overs Faced by {team2}, if all out then {overs}: "))
team2_val = (team2_run/team2_overs)
#Final Nrr for Both Team
team1_nrr = (team1_val-team2_val)
team2_nrr = -(team1_nrr)
#Final Output of Net Run Rate Each Team
print(f"Net Run Rate of {team1} will be: {team1_nrr:.2f}")
print(f"Net Run Rate of {team2} will be: {team2_nrr:.2f}")