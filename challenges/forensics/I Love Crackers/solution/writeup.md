# i love crackers
You are given a excel file and we can see that it is password protected.
Thus, use office2john to get the hash, and then use johntheripper to crack the file.
![alt text](./images/image.png)
![alt text](./images/image2.png)
There will be a lot of fake flags in the file, however the real flag can be found at the final cell, XFD1048576
Use the formula, =CONCAT(XEC1048576:XFD1048576), to get the flag, `YCEP25{DO_YOU_WANT_SOME_TEA}`