playing_field = [[' - ' for j in range(3)] for i in range(3)]

res = ''
step = 0
char = 'x'

def field():
    print('   0  1  2')
    for i, row in enumerate(playing_field):
        print(i, end=' ')
        print(''.join(row))
    return row

def win_check():
    row_temp = []
    count = [0, 0, 0]
    
    if (((playing_field[0][0] == playing_field[1][1] == playing_field[2][2]) or \
       (playing_field[2][0] == playing_field[1][1] == playing_field[0][2])) and playing_field[1][1] != ' - '):
            return True
    
    for row in playing_field:
        if len(set(row)) == 1 and ' - ' not in row:
            return True
            
        if not row_temp:
                row_temp = row
        else: 
            column_index = 0       
            while column_index < len(row):
                if row_temp[column_index] == row[column_index] and row_temp[column_index] != ' - ':
                    count[column_index] += 1
                column_index += 1                
                    
    for col_sum in count:        
        if col_sum == 2:
            return True
            
    return False
    
while ' - ' in field():
    row_input = input(f'Введите номер строки для игрока {char} (от 0 до 2): ') 
    column_input = input(f'Введите номер колонки для игрока {char} (от 0 до 2): ')
    
    if row_input in ['0', '1', '2'] and column_input in ['0', '1', '2']:
        if playing_field[int(row_input)][int(column_input)] != ' - ':
            print('Занято!')
        else:
            playing_field[int(row_input)][int(column_input)] = f' {char} ' 
            
            if win_check():
                field()
                print(f'Выиграл {char}!')
                break 
            else:
                print('Ничья!')
            
            step += 1
            char = 'o'
                       
    else:
        print('Ошибка ввода. Повторите попытку.')
    
    if step > 1:
        step = 0
        char = 'x'
        
        
    

