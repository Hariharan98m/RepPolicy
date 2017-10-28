def print_list(list, n):
    for i in range(n):
        if list[i]==-1:
            print('-', end=' ')
        else:
            print(list[i], end=' ')
    print('\n')

def set_n_pages(ref_string, freq, tick, n):
    j=0
    fault=0
    for i in range(n):
        print_list(stack,n)
        k=input('At Clock Cycle '+str(i+1)+'\nEnter the page num')
        print('Insert ',k)
        ref_string.append(k)
        tick.append(False)
        if j==n:
            break
        print('Insert ',k)
        stack[j]=k
        if k not in freq:
            freq[k]=0
        freq[k]=freq[k]+1
        j=j+1
        fault=fault+1
    return fault

n=(int)(input('Enter num of page slots'))
stack=[-1 for x in range(n)]
m=(int)(input('Enter the size of the address stream'))
ref_string= []

tick=[]
freq={}
j=0
fault=set_n_pages(ref_string, freq,tick,n)

def print_stack_freq(dic):
    print('Frequencies of pages in the Stack\nPages\tFreq')
    for i in dic:
        print(i,'\t',dic[i])
    print('\nLeast freq=',min(dic.values()))

def print_pages(lfu):
    print('Pages ',end='')
    for i in lfu:
        print(i,end=', ')
    print('have the same value of min freq\nGoing by FIFO,')
    
for i in range(n,m):
    print_list(stack,n)
    k=input('At Clock Cycle '+str(i+1)+'\nEnter the page num')
    print('Insert ',k)
    ref_string.append(k)
    tick.append(False)
    if ref_string[i] in stack:
        freq[ref_string[i]]=freq[ref_string[i]]+1    
        continue
    dic={x:freq[x] for x in freq if x in stack}
    print_stack_freq(dic)
    lfu=[x for x in stack if (freq[x]==min(dic.values()))]
    memory=0
    index=i
    ind=0
    if(len(lfu)!=1):
        print_pages(lfu)
        
        for j in ref_string[i::-1]:
            if j in lfu and (not tick[index]):
                memory=j
                ind=index
            index=index-1
    else:
        for j in ref_string[i::-1]:
            if j==lfu[0] and (not tick[index]):
                ind=index
                break
            index=index-1
        memory=lfu[0]

    print('Replacing, ',memory)
    for j in range(n):
        if stack[j]==memory:
            stack[j]=ref_string[i]
    freq[memory]=0
    tick[ind]=True
    if k not in freq:
            freq[k]=0

    freq[ref_string[i]]=freq[ref_string[i]]+1    
    fault=fault+1
else:
    print_list(stack,n)
    
print('Faults :',fault)
exit=input('Press to continue...')
