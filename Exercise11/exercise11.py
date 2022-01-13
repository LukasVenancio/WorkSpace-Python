height = int(input('What is the height of the wall?'))
width = int(input('What is the width of the wall?'))
area = height * width
necessaryPaint = area / 2

print('-'*20)
print('Total wall area: {}m²'.format(area))
print('Necessary paint: {}l'.format(necessaryPaint))
