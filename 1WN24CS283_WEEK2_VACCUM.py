rooms = {
    "A": "Dirty",
    "B": "Dirty"
}
battery=100
current_room = "A"
print("Initial State:", rooms)
while True:
    if rooms[current_room] == "Dirty":
        print("Room", current_room, "is Dirty")
        battery=battery-40
        print("Action: SUCK")
        rooms[current_room] = "Clean"
    else:
        print("Room", current_room, "is Clean")
        if current_room == "A":
            current_room = "B"
            print("Action: MOVE RIGHT")
        else:
            current_room = "A"
            print("Action: MOVE LEFT")
    if all(status == "Clean" for status in rooms.values()):
        print("\nGoal Achieved!")
        print("percentage=",battery)
        print("Final State:", rooms)
        break
