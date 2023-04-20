#Написати fizzbuzz для 20 комплектів по три числа, які записані в файл.
#Читайте із файлу перший рядок з трьома числами, беріть із нього числа,
#рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.
#Переробити другу задачу так, щоб результат писався в інший файл.

import sys
filename_r = sys.argv[1]
filename_w = sys.argv[2]
#filename_r='dat.txt'
#filename_w='1,txt'
f = open(filename_r, 'r')
g = open(filename_w, 'w')
for line in f:
    fizz, buzz, thizz = map(int, line.split())

    if buzz<fizz:
        print('Error')
    else:
        rez=''
        for d in range(1,thizz+1):
            if not(d%fizz):
                rez+='F'
                if not(d%buzz):
                    rez+='B'
                elif not(d%buzz):
                    rez+='B'
            else:
                rez+=str(d)
            rez+=' '
    
    
        g.write(rez+'\n')
f.close()
g.close()
    