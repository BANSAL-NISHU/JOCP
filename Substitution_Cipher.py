"""
The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of
substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the
alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on.

The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.

Thus to cipher a given text we need an integer value, known as shift which indicates the number of position each letter
of the text has been moved down.
"""
import string
d = {}
data = ""
file = open("output_file", "w")

for i in range(len(string.ascii_letters)):
    d[string.ascii_letters[i]] = string.ascii_letters[i-1]
# print(d)

with open("input_file") as f:
    while True:
        # Read at most n characters from stream.
        #
        # Read from underlying buffer until we have n characters or we hit EOF.
        # If n is negative or omitted, read until EOF.
        c = f.read(1)
        if not c:
            print("End of the file")
            break

        if c in d:
            data = d[c]

        else:
            data = c
        file.write(data)
        # print(data)
file.close()
