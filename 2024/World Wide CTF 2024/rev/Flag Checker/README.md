
## x64dbg + IDA
---

We are trying to run the application.

[](1.png)

The application is asking for 4 characters to be entered.

We are trying with 4 characters; let's see what happens.

[](2.png)

Nothing happens.

We will check in IDA what the program is doing.

The program creates an MD5 hash from the provided argument and XORs the memory using this hash.

[](3.png)

This array is used in this function; let's check what it does.

[](4.png)

It creates some process; I assume it will run a program that has been encoded using the generated hash.

[](5.png)


