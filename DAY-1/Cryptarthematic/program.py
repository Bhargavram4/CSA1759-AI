from itertools import permutations
def cryptarthematic(letters):
    #UL=UNIQUE LETTERS
    UL=''.join(set(letters))
    if len(UL)>10:
        print("Too Many Unique Letters")
        return
    for p in permutations(range(10),len(UL)):
        ans=dict(zip(UL,p))
        A1=1000*ans['S']+100*ans['E']+10*ans['N']+ans['D']
        A2 = 1000 * ans['M'] + 100 * ans['O'] + 10 * ans['R'] + ans['E']
        B1 =10000*ans['M']+ 1000 * ans['O'] + 100 * ans['N'] + 10 * ans['E'] + ans['Y']
        if A1+A2==B1:
            if ans['S']!=0 and ans['M']!=0:
                print(f"SEND={A1}\n+MORE={A2}\nMONEY={B1}")
                for x,y in ans.items():
                    print(f"{x}={y}")
                return
    print("Solution Not Found")








letters="SENDMOREMONEY"
cryptarthematic(letters)
