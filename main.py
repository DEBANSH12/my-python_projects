import random


MAX_LINES=4
MAX_BET=100
MIN_BET=1

symbol_count={"A":2,"B":4,"C":6.,"D":8}
symbol_value={"A":10,"B":20,"C":30,"D":40}



def check_wins(columns, lines, bet, values):
    # Placeholder implementation
    winnings=0
    win_lines=[]
    for lines in range(lines):
        symbol=columns[0][lines]
        for column in columns:
            symbol_to_check=column[lines]
            if symbol != symbol_to_check:
                break
            else:
                winnings+=values[symbol]*bet
                win_lines.append(lines+1)
            
        return win_lines,winnings
    
    


def get_slot_machine_spins(rows, cols, symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        column.append(column)
    return columns



def print_slot_machine(columns):
    for row in range (len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end="|")
            else:
                print(column[row],end="")
               
        print()        
            
  
        
        
 


def deposit():
    while True:
          
        money = input("Please enter the amount you want to deposit!!--> INR ")
        if money.isdigit():
             money= int(money)
             if money >0:
                 break
             else:
                 print("please enter a valid amount")
        else:
                print("PLEASE ENTER AMOUNT IN NUMBERS")
                
    return money
def slot():
    while True:
        slot=input("enter the number of slots you want to bet on (1-" +  str(MAX_LINES)+")?")
        if slot.isdigit():
            slot=int(slot)
            if 1<= slot <= MAX_LINES:
                break
            else:
                print("enter the number of lines in the  range")
        else:
            print("enter a valid set of slots for the bets")
            

    return slot
def get_bet():
    while True:
        money=input("enter the amount of bets you want to place ?: INR  ")
        if money.isdigit():
            money=int(money)
            if MIN_BET<=money<=MAX_BET:
                break
            else:
                print(f"amount should be between {MIN_BET} and {MAX_BET}")
        else:
            print("enter a valid set of bets")
    return money


def your_spins(balance):
    lines=slot()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        
        if total_bet>balance:
            print(f"you can only bet the amount you have in balance.The balance amount is.:${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. The total bet is ${total_bet}")

    rows = 3  # Define the number of rows
    cols = 3  # Define the number of columns
    slots = get_slot_machine_spins(rows, cols, symbol_count)





def main():
    balance=deposit()
    lines=slot()
    while True:
        print(f"Your Curent balance is ${balance}")
        answer=input("Please consent to play(q to quit).")
        if answer=="q":
            break
        balance+=your_spins(balance)
        
    print(f"FINALLY YOUR BALANCE IS ${balance}")
    
    
main()
            
   
        
       
          
