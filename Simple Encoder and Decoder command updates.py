# -*- coding: utf-8 -*-
"""
@author: Joshua Mirôn
Caesar Cipher: 
encode msg with rotation number or decode msg with keyword 
"""

# setup empty string for while loop
userCommand = ''

# string of possible commands
availableCommands = 'edqEDQ'

## create string of lower alpha characters
alpha = "abcdefghijklmnopqrstuvwxyz"
        
## prompt user for input
print('\nWelcome to my Caesar cipher!', end='')
print('\nWhat would you like to do?')

## while loop that continues until user quits with 'q'
while userCommand != 'q':
    userCommand = input(
    '''    - type 'e' to encode a string
    - type 'd' to decode a string
    - type 'q' to quit
Enter your command here: ''')

    ## confirm user input is a valid command, print error and loop if not
    if userCommand not in availableCommands:
        print('\nInvalid Response. Please choose from the available commands')
        
    if userCommand == 'e':
        print('\nRunning Encode function')
        
        # Encode function
        
        ## from user: collect msg to be encoded and desired shift
        message = input('What message would you like to encode? ')
        rotation = int(input('What rotation would you like? '))
        
        # put msg in lowercase
        message = message.lower()
        
        ## create empty string for encoded msg
        encodedMsg = ""
        
        ## create for loop to iterate through each character of the msg
        for char in message:
            ## check if character is alphabetic
            if char in alpha:
                ## convert character to Unicode numeric
                charAsOrd = ord(char)
                ## add rotation
                encodedCharAsOrd = charAsOrd + rotation 
                ## for chars past z (ords over 122) subtract 26
                if encodedCharAsOrd > 122:
                    encodedCharAsOrd -= 26
                ## convert Unicode numeric back to character
                newChar = chr(encodedCharAsOrd)
                ## add encoded character to encoded message
                encodedMsg += newChar
                
            ## if char is not alphabetic, pass char through to encodedMsg
            else:
                encodedMsg += char
        
        ## print output
        print('\nYour encoded message is: ', encodedMsg)
        
        ## prompt user for next action, loop back to top
        print('\nWould you like to complete another operation?')
        
    if userCommand == 'd':
        print('\nRunning Decode function')
        
        # Decode function

        ## from user: collect msg to be decoded and keyword
        message = input("What message would you like to decode? ")
        keyword = input("Please provide an already decoded string from the above message: ").lower()

        # identify rotation with the next ~35 lines of code
        ## set starter rotation
        rotation = 1

        ## identify already encoded keyword to decode
        encodedKeyword = keyword
        
        ## create while loop, check for keyword in message
        while encodedKeyword not in message:

            ## create empty string for encoded keyword
            encodedKeyword = ""
            
            ## create for loop to iterate through each character of the message
            for char in keyword:
                ## check if character is alphabetic
                if char in alpha:
                    ## convert character to Unicode numeric
                    charAsOrd = ord(char)
                    ## add rotation
                    encodedCharAsOrd = charAsOrd + rotation 
                    ## for chars past z (ords over 122) subtract 26
                    if encodedCharAsOrd > 122:
                        encodedCharAsOrd -= 26
                    ## convert Unicode numeric to character
                    newChar = chr(encodedCharAsOrd)
                    ## add encoded character to encoded message
                    encodedKeyword += newChar
                ## if char is not alphabetic, pass through to encodedMsg
                else:
                    encodedKeyword += char
            rotation +=1
            
            if rotation == 26: 
                print('\nDecoding your message is not possible with this cipher')
                break

        # set rotation, removing latest rotation addition
        rotation -=1

        # using discovered rotation, decode message
        ## create empty string for encoded message
        decodedMsg = ""

        ## create for loop to iterate through each character of the message
        for char in message:
            ## check if character is alphabetic
            if char in alpha:
                ## convert character to Unicode numeric
                charAsOrd = ord(char)
                ## subtract rotation
                decodedCharAsOrd = charAsOrd - rotation 
                ## for chars prior to a (ords under 97) add 26
                if decodedCharAsOrd < 97:
                    decodedCharAsOrd += 26
                ## convert Unicode numeric to character
                newChar = chr(decodedCharAsOrd)
                ## add encoded character to encoded message
                decodedMsg += newChar
            ## if char is not alphabetic, pass char through to encodedMsg
            else:
                decodedMsg += char

        ## print output
        print('\nThe rotation needed was: ', rotation)
        print('Your decoded message is: ', decodedMsg)
        
        ## prompt user for next action, loop back to top
        print('\nWould you like to complete another operation?')
        
 # sign-off message      
print("\nThank you for trying out my cipher")



