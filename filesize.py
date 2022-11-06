f = open("sample.txt", "w")
f.write("hello welcome to the sample file!")
f.close()

import os
file_size = os.path.getsize("sample.txt")
print("size of file is :",file_size, "bytes")
