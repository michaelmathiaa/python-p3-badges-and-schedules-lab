def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    return [f'Hello, my name is {name}.' for name in names]

def assign_rooms(names):
    index = 1
    greeting_list = []
    for name in names:
        greeting_list.append(f"Hello, {name}! You'll be assigned to room {index}!")
        index += 1
    return greeting_list

def printer(names):
    for badge_creator in batch_badge_creator(names):
        print(badge_creator)
    for greeting in assign_rooms(names):
        print(greeting)    
