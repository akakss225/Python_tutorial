Ld=745e-6
Lq=2360e-6
vs_max = 250
phi_a=0.06424

# 반지름
def fwcontrol(x, y, r):
    global Ld
    global Lq
    global vs_max
    global phi_a
    
    answer = ((vs_max-10) ** 2 - r ** 2 * (Ld*x+phi_a) ** 2) / r ** 2 / (Lq * y) / Lq
    
    return answer

def solution(idsr, iqsr, wrm, y):
    limit = fwcontrol(idsr, iqsr, wrm)
    answer = 0
    if y >= limit:
        answer = limit - 1
    else:
        answer = y
    return answer
    

print(solution(-100, 160, 785.4, 150))