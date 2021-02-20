# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120

def good_level_cholostrol(total_cholostrol, ldl, triglyceride):
    return total_cholostrol < 200 and ldl < 100 and triglyceride < 150
def high_level_cholostrol(total_cholostrol, ldl, triglyceride):
    return 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200
def need_tlc_diet(total_cholostrol, ldl, triglyceride):
    return 200 <total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200

if good_level_cholostrol(total_cholostrol, ldl, triglyceride):
    # good level
    print('*** Good level of cholestrol ***')
elif high_level_cholostrol(total_cholostrol, ldl, triglyceride):
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
elif need_tlc_diet(total_cholostrol, ldl, triglyceride):
    #TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
else:
    print('Error: unhandled case.')