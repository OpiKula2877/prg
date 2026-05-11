def generate_warps():
    warps = []
    for c1 in 'abcdefghijklmnopqrstuvwxyz':
        warps.append(f'aa{c1}')
    for c1 in 'abcdefghijklmnopqrstuvw':
        warps.append(f'ab{c1}')
    return warps

warps = generate_warps()

for warp in warps:
    print(f'Hotovo: /warp {warp}')

print("Všechny warpy dokončeny!")