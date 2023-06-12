def solution(players, callings):
    player_indices = {player : index for index, player in enumerate(players)}
    
    for i in callings:
        current_index = player_indices[i]
        desired_index = current_index - 1
        
        players[current_index], players[desired_index] = players[desired_index], players[current_index]
        player_indices[players[current_index]] = current_index
        player_indices[players[desired_index]] = desired_index
    
    return players