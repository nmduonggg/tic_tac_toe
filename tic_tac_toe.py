from IPython.display import clear_output

# Display game
def display_game(game_list):
    
    sublists = []
    
    for i in range(0,len(game_list), 3):
        sublist = game_list[i: i+3]
        sublists.append(sublist)
    
    for i, sl in enumerate(sublists):
        print(' | '.join(sl))
        if i != 2:
            print('---'*3)
        
# Choice of character: X or O
def character_choice():
    
    char = ''
    
    while char not in ['X','O']:
        char = input('Do you want to be X or O ?')
        
    return char
    
#Position choice 1-9
def position_choice():
    
    pos = 0
    
    acceptable_range = range(1,10)
    
    while pos not in acceptable_range:
        pos = int(input('Choose your postion in the board (1-9): '))
        
    return pos

# Function to fill a character in a postion 
def replace_character(character, game_list):
    
    pos = position_choice()
    while game_list[pos - 1] != ' ':
        
        pos = position_choice()
    
    game_list[pos - 1] = character

# Function to decide whether player wanna play or not
def game_choice():
    
    keep_playing = 0
    
    choice = input('Do you want to keep playing? Yes or No')
    
    while choice not in ['Yes', 'No']:
        
        choice = input('Do you want to keep playing? Yes or No')
        
    if choice == 'Yes':
        keep_playing = True
    else:
        keep_playing = False

# Winning condition
def win(game_list):
    
    # Some initial assignment
    sublists = []
    winning = ''
    
    for i in range(0,len(game_list), 3):
        sublist = game_list[i: i+3]
        sublists.append(sublist)
    
    a,b,c = sublists
    check_list = a + b + c    
    
    # Check for winning condition on ROW
    win_row = list(filter((lambda x: len(set(x)) == 1),sublists))
    if len(win_row) != 0 and (' ' not in win_row[0]):
        winning = 1
    
    # Check for winning condition on COLUMN
    for i in range(3):
        if a[i] ==  b[i] == c[i] != ' ':
            winning = 1
    
    # Check for winning condition on DIAGONAL
    if (a[0] == b[1] == c[-1] != ' ') or (a[-1] == b[1] == c[0] != ' '):
        winning = 1
       
    # Check for TIE condition
    if (' ' not in check_list) and (winning != 1):
        winning = 0
        
    return winning


# Play game
def play():
    
    game_on = True
    game_list = [' ' for i in range(9)]
    character_choices = ['X', 'O']
    winning = ''
    
    #First choice
    character = character_choice()
    replace_character(character, game_list)
    display_game(game_list)
        
    while game_on:
        
        # Automatically choose the opposite charcter
        character = character_choices[character_choices.index(character)-1]
        replace_character(character, game_list)
        
        # After our choice we need to clear the output for the new board
        clear_output()
        display_game(game_list)
        
        # Winning condition
        winning = win(game_list)
        
        if winning == 1:
            game_on = False
            print('Congratulations! You have won the game!')
        elif winning == 0:
            game_on = False
            print('Tie')
        

# Play
play()