# %% [markdown]
# #  Numbers

# %% [markdown]
# Compute the number of bytes in one Gigabyte (1kb = 1024 bytes, 1mb = 1024 kb, 1gb = 1024 mb)

# %%
#Write your code here
gb = 1024 * (mb)
mb = 1024 * (kb)
kb = 1024 * (b)
b = 1

gb

# %% [markdown]
# You bought 500 shares of stock A at $\$$600 on day 0 and you sold it at  $\$$1000 on day 700.
# The daily discount rate is 0.0001%. How much profit did you make in terms of net present value.
# 

# %%
#Write your code here
Shares = 500
Purchased_Price = 600
Sale_Price = 1000
Purchased_Date = 0 
Sale_Date = 700
DDR = 0.000001
# Converted it 

x = (Shares * Sale_Price)
y = (Shares * Purchased_Price)

z = x - y 

profit = z / (1+DDR) ** Sale_Date

profit



# %% [markdown]
# For any value of x, create a variable called even_check that is True if x is even and False if x is odd. 

# %%
#Write your code here
x = 1020020
even_check = x % 2 == 0 
even_check

# %% [markdown]
# You have num_shirts t-shirts, num_shorts pairs of shorts and num_shoes pairs of shoes.  Create a variable called num_outfits that stores the total number of different outfits you can make.

# %%
#Write your code here
n_shirts = 5
n_shorts = 5
n_shoes = 3

num_outfits = (n_shirts * n_shorts * n_shoes)
num_outfits


# %% [markdown]
# # String Practice
# 
# Create variable called "name" that stores your full name. Find whether your name has an even or odd number of letters.

# %%
#Write your code here
name = ("Xander Bienne Manrique Caraig")
name_length = len(name)

if name_length % 2==0:
   print("True")
else:
    print("False")


# %% [markdown]
# Correct the following variable so it is equal to "spammy"

# %%
#Write your code here
s = "spaxxy"
x = s.replace("x","m")

x



# %% [markdown]
# Figure out a way to slice and combine the strings s1, s2, and s3 so that the variable consec_ints = "123456789".

# %%
s1 = "12345"
s2 = "34567"
s3 = "789"

#Write your code here
X = ( s1 + s2[3:] + s3[1:])
X

# %% [markdown]
# #  List Practice
# 
# 

# %% [markdown]
# Add the first and last elements of the list L. Store the result in a variable called sum_first_last. Your code should work if I change L.

# %%
L = [5,1,43,2,4,56,7,90, 67]

#Write your code here
sum_first_last = L[0] + L[-1]

print(sum_first_last)


# %% [markdown]
# Slice and combine the elements of the list L in a way to print out "spam".

# %%
L = [1,"s", 2, 3, "p", "a", 34,1,"m"]


#Write your code here
spam = L[1] + L[4] + L[5] + L[8]

spam





# %% [markdown]
# Create a variable called num_L which store the number represented by the list of strings in L.  For the example num_L should be 145. You may assume 3 digit numbers.

# %%
L = ["1","4","5" ]

#Write you code here
num_L = int("".join(L))
num_L


# %% [markdown]
# Create a list L of numbers of odd length.  Complete the following tasks:
# 
#  - Find the median element
#  - Slice out all element indexed lower than the median element

# %%
L= [4,5,3,2,6,6,9]

#Write your code here
X = len(L) // 2
X = sorted(L)[X]

Y = L[:X]

X 
Y


