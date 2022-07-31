# Напишите программу, удаляющую из текста все слова, содержащие "абв"

# 1-й вариант

def delet_words_with(text_in: str, comb_lettr: str) -> str:
    list = text_in.split()
    text_out = ''
    for i in range(len(list)):
        if comb_lettr not in list[i]:
            text_out +=  list[i] + ' '
    return text_out

my_text_in = input('Enter your text:\n ')
my_comb_lettr = input('Enter your combination of letters:\n ')
my_text_out = delet_words_with(my_text_in, my_comb_lettr)
print('Your text without this combination:\n', my_text_out)

#-------------------------------------------------------------------------------#
 
# 2-й вариант

text_in = input('Enter your text:\n ').split()
comb_lettr = input('Enter your combination of letters:\n ')
text_out = ' '.join([i for i in text_in if comb_lettr not in i])
print('Your text without this combination:\n', text_out)

#-------------------------------------------------------------------------------#

# 3-й вариант

text_in = input('Enter your text:\n ').split()
comb_lettr = input('Enter your combination of letters:\n ')
text_out = ' '.join(filter(lambda x: comb_lettr not in x, text_in))
print('Your text without this combination:\n', text_out)
