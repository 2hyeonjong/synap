#money.py

def solution(n):
    units = ['']+list('십백천')
    won = list('조억만원')
    nums = '일이삼사오육칠팔구'
    n = n.replace(',','')[:-1]
    result = []
    #단위별 금액
    if int(n) > 999999999999:
        result += (n[0:-12], n[-12:-8],n[-8:-4], n[-4:])
    elif int(n) > 99999999:
        result += (n[0:-8], n[-8:-4], n[-4:])
    elif int(n) > 9999:
        result += (n[-8:-4], n[-4:])
    else:
        result += (n[-4:])
    table = []
    #금액뒤 단위 붙이기
    for i in result:
        i = int(i)
        u_index= 0
        answer = []
        while i>0:
            i,r =divmod(i, 10)
            if r > 0:
                answer.append(nums[r-1]+ units[u_index])
            u_index += 1
        table.append(''.join(answer[::-1]))
    answer = []
    won_index =-1
    #최종 금액 + 단위(십백천) + 단위(만억조) + 원
    for i in table[::-1]:
        if i == '' : won_index -= 1
        else :
            if len(table) > 1:
                if i[0] =='일' and len(i) >=2 : i = i.replace('일', '')
            answer.append(i+won[won_index]+ ' ') 
            won_index -= 1
    answer = ''.join(answer[::-1]) 
    return answer[:-1] if answer[-2] == '원' else answer[:-1] +'원'

print(solution('1원'))
print(solution('80,270원'))
print(solution('1,234,567,890원'))
print(solution('111,111원'))
print(solution('100,000,000,000,000원'))