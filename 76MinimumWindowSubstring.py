
def t2lst(t):
    lst=[]
    for i in t:
        if i not in lst:
            lst.append(i)
    return lst

def notshortest(test,t):
    # lst=t2lst(t)
    for i in range(len(test)):  
        if test[i] in t:
            if test[i] in test[i+1:]:
                i+=1
            else:
                break
        else:
            i+=1
    return i

def shortest(record,maxlen):
    short=maxlen
    for i in record:
        if i[1]-i[0]<short:
            short=i[1]-i[0]
            index=i
    return index

def minWindow(s, t):
    t=t2lst(t)
    start,end=0,0
    already=[]
    record=[]
    #cover=[]#跟start end保持一致
    # for i in range(len(s)):
    while end<len(s):##
        if s[end] in t:#下一个字符是ABC
            if s[end] not in already:#第一种情况 新字符还没出现过/第一次出现
                already.append(s[end])
                    
                if len(already)==len(t):
                    record.append((start,end))

                end+=1
            elif len(already)<len(t):
                #第二种情况 新字符出现过  但加入后依然未满 
                #ABB ABA 处理方式相同 
                end+=1
            else:#第三种情况 新字符出现过 且此时already已满
                if s[end]==s[start]:#重复出现的恰好是首字符
                    start+=1
                    while s[start] not in t:
                        start+=1   
                    start+=notshortest(s[start:end+1],t) 
                    record.append((start,end))
                else:#其他重复
                    end+=1
        else:
            if len(already)==0:#为空
                start+=1
            end+=1
    index=shortest(record,len(s))
    return s[index[0]:index[1]+1]

s="a"
t="aa"
print(minWindow(s, t))


