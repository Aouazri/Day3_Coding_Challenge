# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#we lower case both names before starting
lower_case_name1= name1.lower()
lower_case_name2= name2.lower()

#variables for true 
true_count1= 0 
true_count2=0
true_sum=0
#variables for love
love_count1= 0 
love_count2=0
love_sum=0
#counting for true:
true_count1= lower_case_name1.count('t')+lower_case_name1.count('r')+lower_case_name1.count('u')+lower_case_name1.count('e')
true_count2= lower_case_name2.count('t')+lower_case_name2.count('r')+lower_case_name2.count('u')+lower_case_name2.count('e')
#true_sum for both names:
true_sum = str(true_count1+true_count2)

#counting for love:
love_count1 = lower_case_name1.count('l')+lower_case_name1.count('o')+lower_case_name1.count('v')+lower_case_name1.count('e')
love_count2 = lower_case_name2.count('l')+lower_case_name2.count('o')+lower_case_name2.count('v')+lower_case_name2.count('e')
#love_sum for both names:
love_sum = str(love_count1+love_count2)

score = int(true_sum + love_sum)

if score<=10 or score >=90: 
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>= 40 and score <=50: 
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")





