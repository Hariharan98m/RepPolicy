def print_list(list, n):
    for i in range(n):
        if list[i]==-1:
            print('-', end=' ')
        else:
            print(list[i], end=' ')
    print('\n')

def set_n_pages(ref_string, n):
    j=0
    fault=0
    for i in range(n):
        print_list(stack,n)
        k=input('At Clock Cycle '+str(i+1)+'\nEnter the page num')
        print('Insert ',k)
        ref_string.append(k)
        if j==n:
            break
        stack[j]=k
        j=j+1
        fault=fault+1
    return fault

n=(int)(input('Enter num of page slots'))
stack=[-1 for x in range(n)]
m=(int)(input('Enter the size of the address stream'))
ref_string= []
j=0
fault=set_n_pages(ref_string, n)

for i in range(n,m):
    print_list(stack,n)
    k=input('At Clock Cycle '+str(i+1)+'\nEnter the page num')
    print('Insert ',k)
    ref_string.append(k)
    if ref_string[i] in stack:
        continue
    memory=0
    count=n
    save=set()
    for j in ref_string[i::-1]:
        if count==0:
            break
        if j in stack and j not in save:
            memory=j
            save=save | {j}
            count=count-1
    print("Least Recently Used ",memory)
    for x in range(n):
        if stack[x]==memory:
            stack[x]=ref_string[i]
    fault=fault+1
else:
    print_list(stack,n)
print('Faults :',fault)
exit=input('Press to continue...')
