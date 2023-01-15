# Embedded Programming in C

I love the [[c programming]] language and [[embedded]] systems. As it turns out C has a lot of features that are especially relevant to targeting embedded hardware and these are a few.

## Important Keywords For Embedded In C - A Cheatsheet

**extern** - storage classifier keyword to tell compiler variable or function is defined outside scope of this file. Sometimes optional when assumed by compiler.

**static** - tells compiler that local variable in function's value persists each time it is called from whatever value it held the time before i.e. memory is not released after function ends. When used globally it prevents other files from accessing or modifying that variable. Can also go in front of function declaration to prevent it being called from outside function.

**const** - enforces a read-only attribute on variables. preferred syntax is [data type] const [var declaration]; though data type and const can be in either order. Const throws error if you try and modify the variable by its name BUT you CAN still change the value by its address. On stm32, global const variables live in flash memory, so if trying to modify the variable by its address it will not work because flash is write-protected. When using const on a pointer (const \*pData), the pointer can still be modified but the data it points to can not. If written (\*const pData) with the asterisk outside const, it means the pointer is unmodifiable but the data it points to is. const is essentially a safeguard for data that should not be changed, not that it always can't be changed. also can help compiler generate more optimized code and improve readability. Use generously especially in function prototypes.

**volatile** - tells compiler that data may unexpectedly change at any time and not to do any optimization on it. Use with memory-mapped peripheral registers of the microcontroller, multiple tasks accessing global read/write variables in an RTOS multithread application, or when a global variable is used to share data between the main code and an ISR code. ISRs are global flags/variables or interrupt requests coming from multiple external I/O sources which may occur simultaneously. For registers, use non-volatile pointer to volatile data ex: uint8_t volatile \*pStatusReg;. Also use for intentional delays/empty 'for' loops such as for debouncing, otherwise compiler will remove it because it slows the application down.

**const** and **volatile** can be used together, especially for data that should not be modified by the programmer (const) but will have unexpected changes from external world (volatile)

## Bitwise Operators For Embedded In C - A Cheatsheet

**Testing of bits (&[and])** - Bits are tested against a masked value, which is a number chosen for a test that uses all zeros except for the bits that are being tested. Good for on/off and switches.

**Setting of bits(|[or])** - Bits are adjusted to specific values. Masked value uses | to set 0s to 1s.

**Clearing of bits(~[not] and &)** - & can be used with 0s to clear bits and 1s to leave those bits alone, ~ can be used as a nice shortcut involving left shifts.

**Toggling of bits(^[XOR])** - a 1 will toggle the bit at that position

**Bitwise shift operators are << and >>**. Bits of the 1st operant will be shifted right(>>) or left (<<) by the amount decided by the second operand. Shifting right/left in binary format moves all bit positions right/left and leftmost/rightmost positions are filled with empty 0s. Right shift decreases value, left shift increases. A value is multiplied by 2 for each left shift, divided by 2 for each right shift.

**One shortcut to creating mask values**: create mask value of 1 and << left shift by the bit position you are wanting to set. ex: data = data | (1<<4); to set 4th bit. Can also clear by using the same method to shift a 1 to the bit you want to clear and use ~. ex: data & ~(1<<4); to clear 4th bit

**Bit extraction** - extract a range of bits by right shifting (>>) the identified portion to until it touches the 0th bit (least significant bit), then mask the value to extract only 6 bits and save to another variable. ex: output = (uint8_t) ((data >> 9) & 0x003F); where data is 16 bits being typecasted to 8 bit output

*Related*: [Embedded](embedded.html)