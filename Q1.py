# If the numbers to are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100 : 'onehundred',
    200 : 'twohundred',
    300 : 'threehundred',
    400 : 'fourhundred',
    500 : 'fivehundred',
    600 : 'sixhundred',
    700 : 'sevenhundred',
    800 : 'eighthundred',
    900 : 'ninehundred',
    1000 : 'onethousand'
}

ans = ""
num = ""
for i in range(100,132):
    if(i >= 20 and i <= 99 and i not in dict):
        temp = str(i)
        tens = int(temp[0])*10
        ones = int(temp[1])
        num = dict[tens] + dict[ones]
        ans += num
    elif(i >= 100 and i <= 999 and i not in dict):
        temp = str(i)
        hundreds = int(temp[0])*100
        tens = int(temp[1])*10
        ones = int(temp[2])
        if(int(temp[1]+temp[2]) in dict):
            num += dict[hundreds] + 'and' + dict[int(temp[1]+temp[2])]
        elif(ones == 0):
            num = dict[hundreds] + 'and' + dict[tens]
        elif(tens == 0):
            num = dict[hundreds] + 'and' + dict[ones]
        else:
            num = dict[hundreds] + 'and' + dict[tens] + dict[ones]
        ans += num
    elif(i in dict):
        ans += dict[i]
    # ans += dict[i]
print(ans)