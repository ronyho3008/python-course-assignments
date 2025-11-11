# Home Assignment 🏠
===

## Coment on friends Day02 assignment 
I enjoyed looking and comenting on Adib's DNA sequences transformer and on Shelly's PCR Calculator :)

---

## Improving my dilution calculator
I created a new folder inside Day03 of homework and copied the code I wrote last week "from_day02" into it. 
Inside the folder I add two new files:
1. dilution_logic - the calculation of my dilution calculator
2. Gui_logic - the UI part of the code

For the tests, I asked ChatGPT to help me test my code in two ways using the pytest library. I also tested myself by manually calculating the tests that the chat gave and when I saw that they were correct, I made sure that I was indeed able to run them properly (I also used the chat to install pytest along the way).

uv add pytest

uv run pytest

I focused on testing the dilution_logic file only to make sure that the calculation I used in the code works correctly and returns the correct result and I got the expected result 


====================== 2 passed in 0.02s =======================
(in green of course)

Then I consulted the chat if he knew of a 3rd-party library that I could use to replace part of the code.

After he complimented me that I was exactly at the stage where I was learning to “breathe like a real programmer 👑,” he suggested the NumPy library. I read a little about it and discovered that it is a well-known library that is used for mathematical calculations and allows efficient work with arrays and advanced calculations - sounds great! 

So I asked the chat to write me a code that would replace mine with the numpy library and of course also explain to me how to install it

uv pip install numpy

As a heads-up, I also added an additional test file that would test the new code with the numpy upgrade because why not?

uv run pytest

and that's it for today 👏🏻🎉🎊
