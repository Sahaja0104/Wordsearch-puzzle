#    '''
#     A board is a list of str. For example, the board
#        ANTT
#        XSOB
#    is represented as the list
#        [['A','N','T','T'],['X','S','O','B']]
#    A word list is alist of str. For exmaple, the list of words
#        ANT
#        BOX
#        SOB
#        TO
#    is represented as the list
#        ['ANT','BOX','SOB','TO']
#    '''

def is_valid_word(wordlist,word):
    ''' (list of str,str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT','BOX','SOB','TO'],'TO')
    True
    '''
    
    found = False
    for i in range(len(wordlist)):
        if((wordlist[i] == word) and not(found)):
            found = True

    return found
            
def make_str_from_row(board,row_index):
    ''' (list of list of str,int) -> str

    Return the characters from the row of the board with
    index row_index as a single string.

    >>> make_str_from_row([['A','N','T','T'],['X','S','O','B']],0)
    'ANTT'
    '''

    row = ''
    for i in range(len(board[row_index])):
        row = row + board[row_index][i] 

    return row

def make_str_from_column(board,column_index):
    ''' (list of list of str, int) -> str

    Return the characters from the column of the board with
    index_column as a single string.

    >>> make_str_from_column([['A','N','T','T'],['X','S','O','B']],1)
    'NS'
    '''
    s = ''
    for i in range(len(board)):
        s = s + board[i][column_index]

    return s

def board_contains_word_in_row(board,word):
    ''' (list of list of str,str) -> bool

    Return True if and only if one or more of the rows of the board
    contains word.

    Precondition: board has atleast one row and one column, and
    word is a valid word.

    >>> board_contains_word_in_row([['A','N','T','T'],['X','S','O','B']],'SOB')
    True
    '''
    for row_index in range(len(board)):
         if word in make_str_from_row(board,row_index):
             return True

    return False

def board_contains_word_in_column(board,word):
    ''' (list of list of str,str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A','N','T','T'],['X','S','O','B']],'NO')
    False
    '''

    for column_index in range(len(board[1])):
        if word in make_str_from_column(board,column_index):
            return True

    return False


def board_contains_word(board,word):
    ''' (list of list of str,str) -> bool

    Return True if and only if word appears in board

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A','N','T','T'],['X','S','O','B']],'ANT')
    True
    '''

    if (board_contains_word_in_row(board,word) or board_contains_word_in_column(board,word)):
        return True

    return False

def word_score(word):
    ''' (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per charcater for all characters in word
                 10+: 3 points per charcater foa all characters in word
    >>> word_score('DRUDGERY')
    16
    '''
    points = 0
    if(len(word) < 3):
        points = points + 0*len(word)
    elif(len(word) >= 3 and len(word) <= 6):
        points = points + 1*len(word)
    elif(len(word) >= 7 and len(word) <= 9):
        points = points + 2*len(word)
    elif(len(word) >= 10):
        points = points + 3*len(word)
            
    return points
        
def update_score(player_info,word):
    ''' ([str,int]list,str) -> NoneType

    Player info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan',4],'ANT')
    '''
    player_info[1] = player_info[1] + word_score(word)


def num_words_on_board(board,words):
    ''' (list of list of str,list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A','N','T','T'],['X','S','O','B']],['ANT','BOX','SOB','TO'])
    3
    '''
    count = 0
    for i in range(len(words)):
        if board_contains_word(board,words[i]):
            count = count + 1
           
    return count


def read_words(words_file):
    ''' (file open for reading) -> list of str 

    Return how many words appear on board.

    Return a list of all words (with newlines removed) from open file words_file.

    Precondition: Each line of the file contains a wprd in ippercase characters
    from the standard English alphabet.
    '''
    
    s = words_file.readlines()
    last = s[-1]
    newlist = []
    for line in s:
        sublist = ''
        for i in range(len(line)-1):
            sublist = sublist + line[i]
        newlist.append(sublist)
    newlist[-1] = last
    
    return newlist
                
def read_board(board_file):
    ''' (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line.New lines are not included in the board.
    '''
    s = board_file.readlines()
    last = s[-1][-1]
    newlist = []
    for line in s:
        sublist = []
        for i in range(len(line)-1):
            sublist.append(line[i])
        newlist.append(sublist)

    new = newlist[-1]+[last]
    newlist[-1] = new
    
    return newlist

import tkinter.filedialog


def print_board(board):
    ''' (list of str) -> NoneType

    Display the contents of board.
    
    '''

    for row_index in range(len(board)):
        print(make_str_from_row(board,row_index))
        
def get_players_list():
    '''() -> list of [str,int] list

    Prompt the player(s) to enter their names and return a list of player info
    as a two-item list with name and score , respectively.

    '''
    players = []
    player = input('Enter player 1 name:')
    while player.strip() or not(players):
        player = player.strip()
        for i in range(len(players)):
            if player in players[i][0]:
                print("A player by that name is already playing.")
        if player:
            players.append([player,0])
        if players:
            print('Leave a blank player name to begin playing.')

        player = input('Enter player {num} name :'.format(num=len(players)+1))

    return players


def play_game(players,board,words):
    ''' (list of [str,int] list, list of list of str,list of str) -> NoneType

    Play the game with players,board,words.

    '''
    num_remaining = num_words_on_board(board,words) - len(found_words)
    player_num = 0
    while num_remaining > 0:
        print_headers(players,board,found_words,num_remaining)

        guess = input("[{player}]Enter a word (or blank to pass):".format(
            player = players[player_num % len(players)][0]))

        guess = guess.strip().upper()

        if is_valid_word(words,guess) and board_contains_word(board,guess) and \
           not guess in found_words:
            update_score(players[player_num % len(players)],guess)
            found_words.append(guess)

        num_remaining = num_words_on_board(board,words) - len(found_words)
        player_num += 1
    print("\t\t\tGAME OVER!\t\t\t\n")

def print_headers(players,board,found_words,num_remaining):
    ''' (list of [str,int] list,list of list of str,list of str,int) -> NoneTYpe

    Play the score, board, and some other details.

    '''
    print('\n')
    print_score(players)
    print_board(board)
    print("\n")
    print('Words remaining: {num} words left'.format(num = num_remaining))
    print('Words found: ' + (' '.join(found_words) or 'No words found,yet.'))

def print_score(players):
    ''' (list of [str,int] list) -> NoneType

    Print the scores for each of the players.

    '''
    print("Score" + "   " + "Player Name")
    for name,score in players:
        print(' ' + str(score).rjust(3) + '\t' + name )
    print('\n')

#Load the words list.
word_filename = tkinter.filedialog.askopenfilename()
word_file = open(word_filename,'r')
words = read_words(word_file)
word_file.close()

board_filename = tkinter.filedialog.askopenfilename()
board_file = open(board_filename,'r')
board = read_board(board_file)
board_file.close()

found_words = []

players = get_players_list()

play_game(players,board,words)

print_score(players)

