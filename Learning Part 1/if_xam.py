 # typing = input("Please Type an integer number: ")
# typing = int(typing)
# jor = typing % 2


# if (jor == 0):
#     jor = 'jor'
# else:
#     jor = 'bejor'
    
# print(jor) 


user_input = input( 'Please enter a number : ' )
user_input = int( user_input )

# is_even = True if (user_input % 2 == 0) else False
# messeage = "You entered a even number" if is_even else "You entered a odd number"

if ( user_input % 2 == 0 ) :
    messeage = "You entered a even number"
else:
    messeage = "You entered a odd number"

print( messeage )

