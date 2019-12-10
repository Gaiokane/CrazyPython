'''
    **
 *      *
*        *
*        *
 *      *
    **
'''

R = 7
for i in range(2 * R + 1):
    ban = (R ** 2 - (R - i) ** 2) ** 0.5
    start = round(R - ban)
    midnum = round(2 * ban)
    #开始打印start个空格，然后打印*，中间打印midnum个空格，然后打印*
    print('  ' * start + '*' + '  ' * midnum + '*')