my_hist = []

init_play = prev_play = 'S'
opponent_list = [False,False,False,False]
ideal_response = {'P':'R','R':'S','S':'P'}
opponent_quincy_counter = -1
play_order = [{
  "RR":0,
  "RP":0,
  "RS":0,
  "PR":0,
  "PP":0,
  "PS":0,
  "SR":0,
  "SP":0,
  "SS":0,
}]

def player(prev_opponent_play, opponent_hist=[]):
  global my_hist, prev_play,opponent_list,ideal_response,opponent_quincy_counter,play_order
  opponent_hist.append(prev_opponent_play)
  my_hist.append(prev_play)

  #quincy
  if(len(set(opponent_list))== 1 and opponent_hist[-5:] == ['R','P','P','S','R']):
    opponent_list[0] = True

  if(opponent_list[0]):
    if(len(opponent_hist) % 1000 == 0):
      opponent_list = [False,False,False,False]
      opponent_hist.clear()

    opponent_quincy_list = ['P','S','S','R','P']
    opponent_quincy_counter = (opponent_quincy_counter + 1) % 5
    return opponent_quincy_list[opponent_quincy_counter]

  #pynshai
  if(len(set(opponent_list)) == 1 and opponent_hist[-5:] == ['P', 'P', 'R', 'R', 'R']):
    opponent_list[1] = True

  if(opponent_list[1]):
    last_two = ''.join(my_hist[-2:])
    if(len(last_two) == 2):
      play_order[0][last_two] += 1
      potential_plays = [
        prev_play + 'R', 
        prev_play + 'P', 
        prev_play + 'S', 
      ]
      sub_order = {
        k : play_order[0][k]
        for k in potential_plays if k in play_order[0]
      }
      prediction = max(sub_order, key = sub_order.get)[-1:]
        
      if(len(opponent_hist) % 1000 == 0):
        opponent_list = [False, False, False, False]
        opponent_hist.clear()
        play_order = [{
          "RR" : 0, 
          "RP" : 0, 
          "RS" : 0, 
          "PR" : 0, 
          "PP" : 0, 
          "PS" : 0, 
          "SR" : 0, 
          "SP" : 0, 
          "SS" : 0, 
        }]

      prev_play = ideal_response[prediction]
      return prev_play

  #dari
  if(len(set(opponent_list)) == 1 and opponent_hist[-5:] == ['P', 'R', 'R', 'R', 'R']):
    opponent_list[2] = True
    if(opponent_list[2]):
      if(len(opponent_hist) % 1000 == 0):
          opponent_list = [False, False, False, False]
          opponent_hist.clear()
      prev_play = ideal_response[prev_play]
      return prev_play


  #mei2
  if(len(set(opponent_list)) == 1 and opponent_hist[-5:] == ['R', 'R', 'R', 'R', 'R']):
    opponent_list[3] = True
    if(opponent_list[3]):
      if(len(opponent_hist) == 1000):
        opponent_list = [False, False, False, False]
        opponent_hist.clear()
            
      last_ten = my_hist[-10:]
      most_frequent = max(set(last_ten), key = last_ten.count)
      prev_play = ideal_response[most_frequent]
      return prev_play
    
  prev_play = init_play
  return prev_play


