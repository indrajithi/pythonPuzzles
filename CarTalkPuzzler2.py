"""
Copyright 2015 Indrajith Indraprastham.
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

Question:
"I was driving on the highway the other day and I happened to notice my odometer.
Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
miles, for example, I'd see 3-0-0-0-0-0.

Now, what I saw that day was very interesting. I noticed that the last 4 digits were
palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
palindrome, so my odometer could have read 3-1-5-4-4-5.
"One mile later, the last 5 numbers were palindromic. For example, it could have read
3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
you ready for this? One mile later, all 6 were palindromic!"

"The question is, what was on the odometer when I first looked?"

"""

def puzzle(word):
     """Returns True if the following conditions are True.
     1: Last four digits are palindrome.
     2: Last five digits are palindrome after word + 1
     3: Middle four digit are palindrome after word + 2
     4: All six letters are plindrome after word + 3
               
     """
     if str(word[2:]) == str(word[:1:-1]): #checks last four for palindrome
          word = int(word) + 1
          word = str(word)
          if str(word[1:]) == str(word[:0:-1]): #checks last five for palindrome
               word = int(word) + 1
               word = str(word)
               if str(word[1:5]) == str(word[4:0:-1]): #check middle four for pamindrome
                    word = int(word) + 1
                    word = str(word)
                    if str(word[:]) == str(word[::-1]): #checks whole string for palindrome
                         return True

print "Solution:\nPossibl Odometer reading(s)"
for word in range(100000, 1000000): 
    od_read = str(word)    
    if puzzle(od_read):     
        print od_read
          
