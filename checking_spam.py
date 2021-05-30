
from typing import Text
text= input("Enter a text : ")

if("money" in text):
    spam = True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True

elif("subscribe this" in text):
    spam=True

else:
    spam=False


#checking
if(spam):
    print("This is SPAM")
else:
    print("This is not SPAM")