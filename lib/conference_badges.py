def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # all_badges = []
    # for name in names:
    #     all_badges.append(f"Hello, my name is {name}.")
    # return all_badges
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    # room_assignments = []
    # for name in names:
    #     room_assignments.append(f"Hello, {name}! You'll be assigned to room {names.index(name)+1}!")
    # return room_assignments
    return [f"Hello, {name}! You'll be assigned to room {names.index(name)+1}!" for name in names]

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for assignment in assign_rooms(names):
        print(assignment)
