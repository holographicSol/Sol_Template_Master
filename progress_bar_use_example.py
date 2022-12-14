import pyprogress

print('\n\n')
# print('Example:')
# whole = 10000
# part = 0
# multiplier = pyprogress.multiplier_from_inverse_factor(factor=5)
# while part < whole:
#     part += 1
#     pyprogress.progress_bar(part=part,
#                             whole=whole,
#                             factor=5,
#                             multiplier=multiplier)
# print('\n\n')

# print('\nExample:')
# whole = 1000
# part = 0
# multiplier = pyprogress.multiplier_from_inverse_factor(factor=5)
# while part < whole:
#     part += 1
#     pyprogress.progress_bar(part=part,
#                             whole=whole,
#                             percent=True,
#                             color='BLACK',
#                             pre_append='[DOWNLOADING] ',
#                             encapsulate_l='▲',
#                             encapsulate_r='▲',
#                             encapsulate_l_color='BLUE',
#                             encapsulate_r_color='BLUE',
#                             progress_char='_',
#                             factor=5,
#                             multiplier=multiplier
#                             )
# print('\n\n')
#
# print('\nExample:')
# whole = 1000
# part = 0
# multiplier = pyprogress.multiplier_from_inverse_factor(factor=10)
# while part < whole:
#     part += 1
#     pyprogress.progress_bar(part=part,
#                             whole=whole,
#                             percent=True,
#                             color='MAGENTA',
#                             pre_append='[REPLICATING] ',
#                             encapsulate_l='[',
#                             encapsulate_r=']',
#                             progress_char='_',
#                             factor=10,
#                             multiplier=multiplier
#                             )
# print('\n\n')
#
# print('Example:')
# whole = 10000
# part = 0
# multiplier = pyprogress.multiplier_from_inverse_factor(factor=20)
# while part < whole:
#     part += 1
#     pyprogress.progress_bar(part=part,
#                             whole=whole,
#                             percent=False,
#                             bg_color='WHITE',
#                             pre_append='[SEARCHING] ',
#                             progress_char=' ',
#                             factor=20,
#                             multiplier=multiplier
#                             )
# print('\n\n')
#
# print('Example:')
# whole = 100
# part = 0
# multiplier = pyprogress.multiplier_from_inverse_factor(factor=25)
# while part < whole:
#     part += 1
#     pyprogress.progress_bar(part=part,
#                             whole=whole,
#                             percent=True,
#                             color='CYAN',
#                             pre_append='[CLONING] ',
#                             progress_char='|',
#                             factor=25,
#                             multiplier=multiplier
#                             )
# print('\n\n')
#
# print('Example:')
# whole = 100
# part = 0
# multiplier = pyprogress.multiplier_from_inverse_factor(factor=50)
# while part < whole:
#     part += 1
#     pyprogress.progress_bar(part=part,
#                             whole=whole,
#                             percent=True,
#                             bg_color='GREEN',
#                             pre_append='[PROGRESS] ',
#                             progress_char=' ',
#                             encapsulate_l='|',
#                             encapsulate_r='|',
#                             encapsulate_l_color='LIGHTMAGENTA_EX',
#                             encapsulate_r_color='LIGHTMAGENTA_EX',
#                             factor=50,
#                             multiplier=multiplier
#                             )
# print('\n\n')
#
# print('Example:')
# whole = 100
# part = 0
# multiplier = pyprogress.multiplier_from_inverse_factor(factor=50)
# while part < whole:
#     part += 1
#     pyprogress.progress_bar(part=part,
#                             whole=whole,
#                             percent=True,
#                             bg_color='LIGHTMAGENTA_EX',
#                             pre_append='[EXTRACTING] ',
#                             progress_char=' ',
#                             encapsulate_l='|',
#                             encapsulate_r='|',
#                             encapsulate_l_color='LIGHTBLUE_EX',
#                             encapsulate_r_color='LIGHTBLUE_EX',
#                             factor=50,
#                             multiplier=multiplier
#                             )
# print('\n\n')
#
# print('Example:')
# whole = 100
# part = 0
# multiplier = pyprogress.multiplier_from_inverse_factor(factor=50)
# while part < whole:
#     part += 1
#     pyprogress.progress_bar(part=part,
#                             whole=whole,
#                             percent=True,
#                             bg_color='RED',
#                             pre_append='[SELF DESTRUCT SEQUENCE] ',
#                             progress_char=' ',
#                             encapsulate_l='|',
#                             encapsulate_r='|',
#                             encapsulate_l_color='LIGHTCYAN_EX',
#                             encapsulate_r_color='LIGHTCYAN_EX',
#                             factor=50,
#                             multiplier=multiplier)
# print('\n\n')
#
# print('Example:')
# whole = 100
# part = 0
# multiplier = pyprogress.multiplier_from_inverse_factor(factor=50)
# while part < whole:
#     part += 1
#     pyprogress.progress_bar(part=part,
#                             whole=whole,
#                             percent=True,
#                             bg_color='RED',
#                             pre_append='[SELF DESTRUCT SEQUENCE] ',
#                             progress_char=' ',
#                             encapsulate_l='|',
#                             encapsulate_r='|',
#                             encapsulate_l_color='LIGHTCYAN_EX',
#                             encapsulate_r_color='LIGHTCYAN_EX',
#                             factor=50,
#                             multiplier=multiplier)
print('\n\n')
#
print('Example :')
whole = 100000
part = 0
bg_i = 0
multiplier = pyprogress.multiplier_from_inverse_factor(factor=50)
multiplier_2 = pyprogress.multiplier_from_inverse_factor(factor=20)
while part < whole:
    part += 1

    if bg_i < len(pyprogress.bg_color_):
        for index, key in enumerate(pyprogress.bg_color_):
            if index == bg_i:
                if 'WHITE' not in key:
                    bg = key
    else:
        bg_i = 0
    pyprogress.progress_bar(n_progress_bar=2,
                            n_progress_space_char='  |  ',
                            part=part,
                            whole=whole,
                            percent=True,
                            bg_color=bg,
                            encapsulate_l='|',
                            encapsulate_r='|',
                            pre_append='[INITIATING WARP DRIVE] ',
                            append=str(' ' + str(part)),
                            progress_char=' ',
                            factor=50,
                            multiplier=multiplier,
                            part_2=part,
                            whole_2=whole,
                            percent_2=True,
                            bg_color_2=bg,
                            encapsulate_l_2='|',
                            encapsulate_r_2='|',
                            pre_append_2='[DEPARTURE TIME] ',
                            append_2=str(' ' + str(part) + ' / ' + str(whole)),
                            progress_char_2=' ',
                            factor_2=20,
                            multiplier_2=multiplier_2
                            )
    bg_i += 1
print('\n\n')
