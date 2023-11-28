import re, itertools
nvi = '38L16L3L38L3R48R16R22R5L8R46L32R38R41L29L9R23R44L19R2R50R18R50L44L28L12R31R44R19R42R7R47L45L37L5R6L36R33L4R20R14L38L8L3L31R46R36R40L45R15L4L44R19L16L3R11R35L48R5R32L13R1L35L42R3L40R27R36R42L30L8R24R30L12R48R43L40L47L36L40R36R13R9R1R40L42L7L7L25L15L13R36R48L23R8L11R38L42L5L42R4L13R40L12R17R31R10L29R43L42R41L50R13L34R30R28R29L30L41L6R48L49L1R44L50R32R1R21L1R7R46L39R28L49R19L6L48L26R49R15L45L1R43R27R45L42L47R46L30L45L1R7L24L42R4R5L25L14R46L10L3L44L34R16R39L23L19L37L10R21L17R48L9L1L48R11R47L37L41L4R26L22R5R4L14R15L41L48R37R14R17L14R11L33R3R7R42R43R31L22L32R1R15R1L40R28L10R6R26L25R21R18R3L16L11L23L50R40L23L24L9L37L24R6L4L5L20L34R48R43R38L6L21R1L3R13L40L39R34L26L3L10L12L15L26R23R45R19R25L40R17R50R25L21L20R42R50R39R36L5L2L9R46L19R9L4L27R45R19R33R39L1L37L47R14R41R35R1L46R33R4R36L32R23L2L14R25L31R32R16R39R33R36R10L38L35R20R50L7L49R19L45R39L45L13L50L13L32L46L16R17L20L35R17R10R45R18R21L3L2L3L42R31L11R31R45R30R6R39L11L34L46R7R39R26R42R47R24L10L46R18R41R45L27R37R20R33L4L14R7L13R49R35R31L11L1R33L4R50R2R2R24R37R20R22R23L25R33L3L2R13L13L33R25L30R47R37L23R43L31L46R17R13L29L47L46R22L37R44L38L20L14L41R43R2R24L40L23R9R29L13L43L39R37L37L17R29L23L29L43R21R4R2L7R34L24R38R10L9R38L16R41L4R19L4L44R16L43R49L23L22L27L27R1L30R21R43R7R6R24L40R11R33L26L42L35L8R16L30R26R44R36L16L2R23R11R19R5R15R30L37L10L24R44L6R48R33L50R48L32R3R28L14R46L36L9R35L21L19L28R29R6R7R17R42L8R24R40R40L36R42L47L47L38R35R7R42R12L37R35L12R36L22R21L49R49R45R26L20R13L4R21R45L21R35L21R13R19R19L17L39L30R29R17L32L6L4R16R34R32L29L24L2L4R9L6R8R7L16L20L27L16L32R11R27R4R30L6R17L2R32R29R24R21R31R44L39L39L38R5L31L16R7L18L40R47R18R23L35L8R39R27L3L39R29L38L8R24L35R28R18L27L12L18R6R10R25R45R44R44L33L34R27R23R13R9R25L7L23L39L34R25L45R15R14R1L28R11L13R13L10L26L31L24L3L23R44R49L24R38L2R15R33R23R34L49L18R24R10L22L47R39R16R2R23L32R45R44R24R5R34R16R39R28L7L8R32L30R39R41L3L2R11R17R42R14L4L28R31R33R43L4L10R42L50L13R6L15L27L21L46R22R6L48R33R14L29R11R8R43R45L46R36L42L38L13R49R42L22R46R7R21L20L29R27R19R33L26L8R17R11L36L42R21R13L11R2R43L25R30L34R10L49L11L43R17L9R21R18L11R6R17R33R17R6L40R28R29R22L34L35R43R21R47R20L2L38R29L42R43R38R33L27R13L50L47L9L38L7L24R41R42R24L22R15L47R7L14L39R16R25R46L4R49R3R42L7L10R39R42L32L11L14R33R6R25R16R37L1R20L36L43L50R31L20R13R30L37L18R34R22R22L6L42L20L48L50R11R22R44L32R12R41R31L45R23R40R22R39R37L13L49L48L27L45R13L5L20R45R32L24L36L33R3R7L38L26L43R34L46R6L36L35R47R1R47R37R20R11R14R14L7L11L12L32L49L33L50R7L35R42R37L14L9R35L21L23R18R3R8R47R46L19L36L28R30R43L7R24R25L35R36L24L41L47R43L10R22L28R18R39L43L10L4R16R11R30L35R48R25L43L35L11R31L47L14L27R16R41L10R9R45R48L50R39L17L37R24R9R23R19R23R25R31L50R46R32L42L1L14L30L14L31L1R45R28R22L24L12R36L24L25L10L26L6L15R28R9L43R5R26R26R40L10L40R47L37R8R48L44R17R11L42L21L33R36R3L13R8R27L26R22R47R16R20R3R46L9L34L10R27L34R27L8L17L3R12R24L1R43R46L45L1L43L6L39R9R16R9L13L41R31L37L36R25L29R29L1L9L26R9L13R13R47R40L5L14L43L37L26R16L18L32R27L7L43R42R14L29L5L24L32R40R39R1L16L29R49R11L17L23L27R16R16L11R29R23L44R49R50R6R44R5R16L35R7L15R18R20R46L2R21R8L26R30L15L4L34R48L12L21R47R7L6L39R27L5R24L35L20L21L38L47R9L3L6R1R21R35R18R30L9L24R7L8R46L19R7R4L13L11L32L4R32L29R21R6R41L3R22L31L6R47R49R24R21R38R29L17R32L22L28R12L27L33R21R46R48L46R38L39R14L18L39R19R23L29R29L28L22R2L46L6L9L17R46R7L39L20R46R37R46R10R10L49R17L24R30R34R10R42R1L2R30L38R34L25R47L6R49L48R5R7R13L15L45L6R22L42L25L45L39R22R32R1R12R21L46L38R26R35L11R46R27R17R38L23R3R26L43L16L17R2R4R25R45L42L31R50L15R48L19R10L38R47R23L21R45L25R42L48L48L4L26R38R10R47R28R22L40R33R9L33R24L44R34L12R5L44L27R37R43L15R3R41R3L17R11L35R14L5L31R18L17L23R32R39R40L40L27L24L42L38R11L24L4L31L1L34L36R47L4R7R48R21L49R34R17R42R13R31R17L46L21R26R36L18R24R12L12L8R50R47L9R46L3L31R33R25R45R47L17L15L18L17R1L9L16L11R49L35R5R10L5R27L14L38L3R20R1L39R30L10R5R2L6L25R11R26L3R2L4R29L32L20R44R16L24L25R15L28L19R10L3L37R2R39R14R7L33L4R4L49L38L46R11R17L43R17R34R14R43L29R36R34L48R35L30L39L17R25L34R13R37R2L23R17R42L21L17L28R44L27R26L15L6R15R34R13R15L6L47R15L17L49L5R2R10R32L3L1R7R33L28L49L44L44R45R16L17R45R42L7L7R40L27L15R32R38R32R12R50R10L26L41R22R29R29L36R43R44R3L19L2R26R20R31L22L11R37R7L35L28R44L40R7R7R17R46L1R42R9R37R28R23R31L2R6L26R39L39L23L48R10R31L13R17R14L30L18L20R49L25R43L46L26R10R18R34R50R12L17R6L37R38R5R28R4R14L49L7L4L12R5L43L50L41L29L14R22L23R21L1R16L36R10L17L20L42R36L18R27L16L35R18R40L28R4L20R23R22R49L39R17L21L15L9R6L19L21R28R2R30L13L22R21R11R29R43R27L21L32L50L18L23L12R45L36R26R18L40R33L36R30R34R40R17L9L18R41R13L40R6L9R24L24L33L22L23L21R14R25R25R11R37R40R23L26R23R47L20R20R22R19R31L6R15L21R26R34L7R39R30R42L18L11L38L5L18R47L2R14R29R33R17R38R33R3R21R42L46L17R37L46L6R12L7R11L41L7R1L16R21L48R18R15R11R12R49L11R15L42R49R19R25L42R4L19R34R12L26R8L28L46L28R30R6R41L12R39R38L40R31R47R9R49R27R28L21L44L19L42R39L38R18L37R19R2L1R7L35R40R14R2R24R34L13R8L2L9R28L45R3L48R17L41R43R27L14L33L6R16L45L11L30R32R7R10R18R36R16R9L2L7R45R45R13R39R44L32R31L25L22R17L15R11L11L3L37R8L25R38R29L25L25L6L2R19R14L2L28L47R46R11L47R21L50R27L45L46L24R48R2L1L3L50R8R27L15R10L42R11L34R36R14L41L38L25L13R4R5L26R45R3R28L14L32L39R20L42L49L1R44R34R14L12L48R38R11R4L43L50R42L9R43L3L13L36L35R26R40R12L40R44R42L27L8R34R19L30R20L46L4R5L28L1R48L14L37R29R41L8R49R30L19L2R45L48R28L40L40L31L26L16L19L30R23R1R29R11R41R10R5R11L23R23R41R11L8R35R4L38R22L19R9L45L31L6L3R39R7L7L16R47R27L31R35R39R47R35R17R37L38R34L5L7R48L50L14R3R33R12R44L31L4L5R26R2R46L2R39R31R41R34R47R2L36R12L41R41R5R43L42L36R47R50R21R35L11R47L28R29L24R8L38L9L2R14L43R20R46R50L34R11L32L6R21R38R5L21R33R21L10R38L35R21L9L21L31L32L5R37L10R11L22L32L42R17R45R13R11L31L39L11L44R6L19R48L42R20L41L6R36L38L10L36R19R49R44R2R12R32L13R9L41L50R13R19L29R7R39L5L36R48R37R34R23R49R19R31L39L9L9L42L15L46R48R18R5L45L27L39L21R38R10L40R31R11R32R31R8R21L38L49L22R46R40R9L19L14L29'
# nvi = '10R5L5R10L4R5L5' # example input
nv = [a for a in re.split('(R)|(L)',nvi) if a] # no idea why re outputs None
mp = open('2022_22.txt').read().splitlines() # map input
rows, cols = len(mp), max([len(y) for y in mp])
mp = [list(y+(cols - len(y))*' ') for y in mp] # adding space to empty lines
# mpt = 
xr = [(min(r:=[i for i,a in enumerate(y) if a!=' ']),max(r)) for y in mp] # range per row and column. assuming no intersections in between
yr = [(min(r:=[i for i,a in enumerate(x) if a!=' ']),max(r)) for x in [[row[j] for row  in mp] for j in range(cols)]]

def ts(t):
    return '>' if t==0 else 'v' if t==1 else '<' if t==2 else '^'

x,y,t = mp[0].index('.'), 0, 0 # row, column and facing at start position
mp[y][x] = ts(t)

while True:
    s, d = int(nv.pop(0)), 1 if t in [0,1] else -1 # steps and dir
    if t in [0,2]:
        xl,xu = xr[y]; yp = y
        for i in range(s):
            xp = x + d
            if xp < xl: xp = xu
            elif xp > xu: xp = xl
            if mp[yp][xp] == '#': break
            elif mp[yp][xp] == ' ': print('error: space is not avoided now')
            else:
                x = xp
                mp[y][x] = ts(t)
    else:
        yl,yu = yr[x]; xp = x
        for i in range(s):
            yp = y + d
            if yp < yl: yp = yu
            elif yp > yu: yp = yl
            if mp[yp][xp] == '#': break
            elif mp[yp][xp] == ' ': print('error: space is not avoided now')
            else:
                y = yp
                mp[y][x] = ts(t)
    if nv:
        t = (t + (1 if nv.pop(0) =='R' else 3)) % 4 # rotate
        mp[y][x] = ts(t)
    else: break

[print("".join(y)) for y in mp]
print(1000*(y+1) + 4 * (x+1) + t) # 117102