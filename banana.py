import re


def get_count(sub_string, full_string):
    # count = full_string.count(sub_string)
    count = len(re.findall('(?=' + sub_string +')', full_string))
    return count


vowels = ['A', 'E', 'O', 'U', 'I']
list_uniq = {}
player1_Points = 0
player2_Points = 0
string = ("banana")
string = string.upper()
for i in range(len(string)):
    for y in range(len(string)):
        if y >= i:
            x = string[i:y + 1]
            list_uniq[x] = get_count(x, string)
            # print(string[i:y + 1] + str(get_count(x, string)))

            # print(string[i:y + 1]+str(i)+str(y) )
            # print(string[i:y + 1] + str(counter))
# print(list_uniq)
for el in list_uniq:
    if el[0] in vowels:
        player1_Points = player1_Points + list_uniq[el]
    else:
        player2_Points = player2_Points + list_uniq[el]

# print(list_uniq)
if(player1_Points>player2_Points):
 print(str('Stuart'+" "+str(player1_Points)))
else:
 print(str('Kevin'+" "+str(player2_Points)))


































