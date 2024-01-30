from main import Stack

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the Game
num_disks = int(input('\nHow many disks do you want to play with?\n'))
while num_disks < 3:
    num_disks = input('Enter a number greater than or equal to 3\n')

for i in reversed(range(num_disks)):
    left_stack.push(i)

num_optimal_moves = ((2 ** num_disks) - 1)

print('\nThe fastest you can solve this game is in {} moves'.format(str(num_optimal_moves)))


# Get User Input
def get_input():
    choices = [i.get_name()[0] for i in stacks]  # gets the first letter of the choices available
    while True:  # ask for an input till its valid
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print('enter {0} for {1}'.format(letter, name))  # presents the valid choices
        user_input = input('')
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


# Play the Game
# win if right stack is full and others empty
num_user_moves = 0
while right_stack.get_size() != num_disks:  # while the right is not full yet, ie while game is not finished yet
    print('\n\n\n...Current Stacks...')
    for i in stacks:  # prints out the state of each stack
        i.print_items()
    while True:
        # keeps asking what move user wants to make till valid
        print('\nWhich stack do you want to move from?\n')
        from_stack = get_input()
        print('\nWhich satck do you want to move to?\n')
        to_stack = get_input()
        # to check if user has made a vaid move
        if from_stack.get_size() == 0:  # if from stack is empty
            print('\n\nInvalid Move. Try Again')
        elif to_stack.get_size() == 0 or (from_stack.peek() < to_stack.peek()):
            # checks that the to stack is empty or the from node is smaller than to stacks top node
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves = + 1
            break  # only breaks loop (ie. stops asking for user choices) when valid inputs have been chosen
        else:
            print('\n\n Invalid Move. Try Again')

    print('\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}'.format(num_user_moves,
                                                                                                   num_optimal_moves))



