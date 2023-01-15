# the c programming language.

C wasn't my first programming language, but it was my second and easily my favorite. Managing memory manually isn't strictly necessary for every task, but as someone who  loves [[embedded]] and small, efficient software tools that [[do less]], it just makes the most sense. Computing resources are always finite even if they seem large and in a world where inefficient and power-hungry software has become the norm, most applications could benefit from a healthy distrust of dynamic memory allocation.

## Pointers In C - A Cheatsheet

**pointers/addresses** are always unsigned data

& = gets the address of a data/var ("**pass by reference**")

\* = gets the data/var located at address (**dereference**)

int *p = &n; **stores the address** of n in variable p

calling *p "**dereferences**" address of data

-> is **used in place of dot notation** to access the members of the structure or the unions using pointers

**Address of an array in C** is actually the address of the first byte of the array, which is fine because data in an array is stored consecutively

**Assigning a &[variable] to pointer variable** needs to be typecast as such. ex. char \*pAddress = (char*)&data;

**Declaring a pointer variable** needs a * after the data type declaration. ex. char* address1 = (char*) 0x0007FFF8E3C3824; needs to be typecasted to fit into char data type. The compiler will always reserve same # of bytes regardless of the data type but the data type instead determines the behavior of operations(read, write, increment, decrement, etc) carried out on the pointer variable and how many bytes of information the result will yield. (So seems like generally you want to choose a pointer type that uses the same size as the data that it is pointing to)

**What data is read from a pointer** depends on data type used, for ex. char data = *address1; will fetch only 1 byte because char is being used

**Conventional** to write pointers for variable locations with p[variablename]

&[variable]'s data type will be [data type]* by **default**
