# (n)vim.

Since late May 2024 I decided I'd take another go at learning VIM motions and shortcuts while working on one of my new personal projects. It's been going pretty well! But I still need my cheatsheet a lot of the time.

I can't say that these types of shortcuts make me feel more productive than a traditional IDE or text editor at this stage, but it brings its own type of fun to use a tool like this which is good enough for now.

## NVIM- A Cheatsheet

### **Navigation**

hjkl - move cursor

w - next word

b - back a word

e - end of next word

$ - end of line

0 or ^ - move to start of line

_ - move to first character of line

G - moves to end of file

#G - moves to line #

gg - moves to start of file

\<C-o\> - moves back to previous positions

\<C-i\> - moves forward to newer positions

/string - searches for string forward

?string - searches for string backwards

n - next occurrence forward

N - next backwards

% - over a bracket jumps to matching bracket

fx - find in line

\<C-]\> - jump to function definition

### **Modes**

esc - normal mode

i - insert at cursor

I - insert at beginning of line

a - append at cursor

A - append at end of line

v - visual highlight

\<C-v\> - visual block (vertical)

### **Motions**

press twice = do this to the whole line

x - delete character under cursor

d - delete

D - delete from cursor to end of line (also d$)

dd - delete whole line

u - undo

U - undo changes on line

\<C-r\> - redo

c - change

cc - change whole line

y - yank (copy)

yy - yank whole line

p - put/paste

r - replace

R - replace multiple

o - new line below cursor

O - new line above cursor

V - select whole line

### **Files**

nvim * - open all files in current folder

:[w]n(ext) - [write and] go to next file

:[w]N - [write and] go to previous file

:! - unix command

:w - save

:q! - quit without saving

:wq or ZZ - save and quit

\<C-g\> - displays cursor location and file status

F1 - new window

\<C-w\> - change window

\<C-d\> or Tab - autocomplete command

:tabnew [filename] - open file in new tab

:e [filename] - edit or create file by filename

### **Formatting**

gg=G - autoformat/indent whole file

\<C-y\> - accept autocomplete suggestion

### **Substitute**

:s/old/new - substitutes new for first old in line

:s/old/new/g - subs for all olds in line

:#,#s/old/new/g - subs all olds between two line #s

:%s/old/new/g - subs all in file

:%s/old/new/gc - same but asks for confirmation for each one

### **Help**

:help - opens help text, use help \<something\> to search for docs on a particular thing

