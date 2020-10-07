# Individual challenge

## Matrix Challenge

As part of our training in BeCode, each student received a challenge to accomplish in order to demonstrate their Python skills

My challenge, was the Matrix challenge. 

## Instructions

The instructions for the challenge were the following :

Given a string with embedded newlines, we had to develop a code that would give as a result two different lists :
- A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
- A list of the columns, reading each column top-to-bottom while moving from left-to-right.

## How

To solve the challenge, I decided to created a file "challenge.py" with all the relevant code.
Once the code was established, I was using the test file provided and linking it to my "challenge.py" file.

The code of "challenge.py" was composed of a class composed itself by a functionn.

The class itself would already split the string each time there is a newline.

The function would do the two tasks required :
- Give a list of rows : By splitting one more time the original string.
- Give a list of columns : By rearranging the result obtained with rows (using a zip())

## Difficulties 

As it was my first attempt to officially use Classes in a project, this was really challenging for me and not as easy as presented by the coaches.

I directly had what (and how) was to be achieved in mind but to translate this in the adequate code with Classes was an other story.

## Process

As I had the solution in mind from the very beginning, I tried to create a really simple code in order to accomplish this.
The simple code only containing a function.

Once it was working, I tried "change" this code using Classes

As I met many difficulties in order to make the Classes work, I had to ask some clarifications to my colleague Davy.
