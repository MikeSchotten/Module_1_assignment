player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = player_0 + ' ' + str(goal_0) + ', ' + player_1 + ' ' + str(goal_1)
print(scorers)

report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)

player = 'Berry van Aerle'
first_name = player[ : player.find(' ')]
print(first_name)
last_name_len = len(player[player.find(' ') + 1 : ])
print(last_name_len)
name_short = first_name[:1] + '. ' + player[player.find(' ') + 1 : ]
print(name_short)

chant = (first_name + '! ') * (len(first_name) - 1) + first_name + '!'
chant_2 = ((first_name + '! ') * len(first_name))[ : -1]   # This is another method to achieve the same result (no space as last character)
print(chant)
good_chant = print(chant[-1] != ' ')
print(chant_2)
good_chant_2 = print(chant_2[-1] != ' ')  # Both methods show "True", i.e. the last character is not a space.