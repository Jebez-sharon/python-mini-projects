from scores import get_scoreboard
from stats import get_stats

while True:
    print("\nNBA menu")
    print("1.Todays Games")
    print("2.League Leaders")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        get_scoreboard()

    elif choice == "2":
        get_stats()

    elif choice == "3":
        break

    else:
        print("Invalid choice")