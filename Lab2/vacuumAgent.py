def test_case():
    possible_states = ['Clean', 'Dirty']    #used for building room states
    test_results = []                       #keeps track of individual case results
    expected = [0, 0, 2, 1, 1, 2, 3, 3]
    for left_state in range(2):
        for right_state in range(2):
            for vacuum_start in range(2):
                # build new room state and initialize empty action list
                room_state = [possible_states[left_state], possible_states[right_state], vacuum_start]
                action_list = []

                print("Starting state: ", room_state)
                cost = vacuum_agent(room_state, action_list)    #vacuum_agent updates room_state, action list
                print("Ending state:   ", room_state)           #  and returns cost (1 point per action taken)
                print("Action cost:    ", cost)
                print("Actions taken:  ", action_list)

                if room_state[0:2] == ['Clean', 'Clean']:       #Tests if vacuum successfully cleaned room
                    print("PASSED :)")
                    test_results.append(cost)
                else:
                    print("FAILED :(")
                    test_results.append(-1)
                print("")

    return list(zip(test_results,expected))

def vacuum_agent(state, actions):
    action_count = 0    #counts actions taken
    while state[0] == 'Dirty' or state[1] == 'Dirty':   #Loop continues while either square is dirty
        perform_action(state, actions)                  #Performs an action based on room state and updates
        action_count+=1                                 #  the room and the action list
    return action_count

def perform_action(state, actions):
    if state[2] == 0:               # If agent is in left square
        if state[0] == 'Dirty':     # If left square is dirty, suck and mark clean
            actions.append('Suck')
            state[0] = 'Clean'
        else:                       # else, left square is clean, move right
            actions.append('Right')
            state[2] = 1
    elif state[1] == 'Dirty':       #if agent is in right square and right square dirty
        actions.append('Suck')
        state[1] = 'Clean'
    else:                           #else agent is in right square, right square clean, move left
        actions.append('Left')
        state[2] = 0


if __name__ == '__main__':
    results = test_case()
    i = 1;
    for result, expected in results:
        if result == expected:
            print("Test #", i," passed")
        else:
            print("Test #", i," failed")
        i += 1