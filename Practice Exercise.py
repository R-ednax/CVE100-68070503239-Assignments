# %% [markdown]
# Exercise 1
# 
# Write a function to report the weather condition. 
# Input ==> Temperature ('C)
# 
# IF the temperature is below 0, print "Freezing Cold"
# IF the temperature is 0-20, print "Cold Weather"
# IF the temperature is 21-30, print " Warm Weather"
# Otherwise, print "Hot Weather"

# %%
def weather_report(temp: float):
    if temp < 0:
        print("Freezing Cold")
    elif temp <= 20:
        print("Cold Weather")
    elif temp <= 30:
        print("Warm Weather")
    else:
        print("Hot Weather")

weather_report(30)




# %% [markdown]
# 

# %% [markdown]
# Exercise 2
# 
# Write a function that takes an integer as an input score
# 
# If the score is greater than or equal to 50, print "Pass"
# If the score is greater than or equal to 75, print "Good"
# If the score is exactly 100, print "Perfect"
# 
# Since these are multiple independent conditions, more than one message print

# %%
def get_score(score: float):
    if score >= 100:
        print("Perfect")
    elif score >= 75:
        print("Good")
    elif score >=50:
        print("Pass")
    else:
        print("Fail")

get_score(60)

# %% [markdown]
# Exercise 3
# 
# Write a program that returns the count of vowels in the string. Use a for loop to go through each character in the string.
# 
# Input ==> apple, Output ==> 2
# 
# Input ==> Hello World, Output => 3
# 
# Input ==> balloon, Output ==> 3

# %%
def count_vowels(st: str):
    count = 0
    #TO DO
    vowels = "aeiouAEIOU"
    for char in st:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Python"))


