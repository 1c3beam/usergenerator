import random as r
vowels=['a','e','i','o','u']
nums=[x for x in range(97,123)]
cons=[chr(x) for x in nums if x not in [ord(y) for y in vowels]]
num_suff=[x for x in range(11)]
un=['admin','user','rand','sys']

ans=input('how many users to create: ')
print('processing . . .')
for i in range(int(ans)):
    pw=''
    pick_un=''
    pick_un=r.choice(un)
    for i in range(5):
        pick_pmv=r.choice(vowels)
        pick_pmc=r.choice(cons)
        pw+=r.choice([pick_pmc,pick_pmv])
    for i in range(5):
        pick_num=r.choice(num_suff)
        pick_un+=str(pick_num)

    print(pick_un,pw,sep='-',file=open('cred.txt','a'))