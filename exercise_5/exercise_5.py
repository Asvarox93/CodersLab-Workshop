import re
from random import randint

# Change string to RPG dice roll
def dice(stype):
    if stype not in re.findall(r"(\d{0,1}[D]\d{1,3}[\+-]{0,1}\d*)",stype):
        return f"Your string is not valid"

    dice_roll = ''.join(re.findall(r"(\d+)D", stype))
    dice_type = ''.join(re.findall(r"D(\d+)", stype))
    modifier = ''.join(re.findall(r"([\+-]\d+)", stype))

    allowed_dice_type = ['3','4','6','8','10','12','20','100']

    if dice_roll == '':
        dice_roll = 1
    if modifier == '':
        modifier = 0
    if dice_type not in allowed_dice_type:
        return f"Your dice type is not valid"

    return sum([randint(1,int(dice_type)) for _ in range(int(dice_roll))])+int(modifier)



print(dice('2D10+10'))
print(dice('2D3'))
print(dice('D12-1'))
print(dice('SD12-1'))
print(dice('D11'))
print(dice('D+1'))
print(dice('D100*4'))