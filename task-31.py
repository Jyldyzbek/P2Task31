a = input('Enter your word:').split()
print('Kolichestvo slov: ', len(a))
b = ''
for f in a:
    b += f
print('Kolichestvo bukv: ', len(b))