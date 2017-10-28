def print_list(list, n):
    for i in range(n):
        if list[i]==-1:
            print('-', end=' ')
        else:
            print(list[i], end=' ')
    print('\n')

n=(int)(input('Enter num of page slots'))
m=(int)(input('Enter the size of the page reference string'))
stack=[-1 for x in range(n)]

ref_string= []
j=0
fault=0
for i in range(m):
    print_list(stack,n)
    k=input('At Clock Cycle '+str(i+1)+'\nEnter the page num')
    print('Insert ',k)
    ref_string.append(k)
    if k in stack:
        continue
    stack[j]=k
    j=(j+1) % n
    fault=fault+1
else:
    print_list(stack,n)
print('Faults :',fault)
exit=input('Press to continue...')
#7 0 1 2 0 3 0 4 2 3 0 3 2 1 2
