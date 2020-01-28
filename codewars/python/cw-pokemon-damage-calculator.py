def calculate_damage(your_type, opponent_type, attack, defense):
    multiplier = 1
    
    if ((your_type == 'fire') & (opponent_type == 'grass')) or ((your_type == 'water') & (opponent_type == 'fire')) or ((your_type == 'grass') & (opponent_type == 'water')) or ((your_type == 'electric') & (opponent_type == 'water')):
        multiplier = 2
    elif  ((opponent_type == 'fire') & (your_type == 'grass')) or ((opponent_type == 'water') & (your_type == 'fire')) or ((opponent_type == 'grass') & (your_type == 'water')) or ((opponent_type == 'electric') & (your_type == 'water')) or (your_type == opponent_type):
        multiplier = 0.5
        
    return 50*(attack/defense)*multiplier