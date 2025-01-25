# bash.

My old disorganized cheatsheet for bash scripting.

## Bash - A Cheatsheet

i=0
cat file.txt | while read line;
do
    i=$i+1
    if [[ $i -eq 10 ]]; then
        echo $line
        break
    fi
done

grep - search for specific terms in a file
awk - text processor extracts data
sed - text processor for stream editing
sort - sort command
uniq -c: uniq is used to filter out the repeated lines which are successive, -c means counting

CHEATSHEET
Line 1 - #!/bin/sh
Line 2 - any arguments from terminal that should be committed to var
system var ALL CAPS, user var all lower case
one command per line or seperated by semicolon
# for single line comment, ' ' comments multiple lines
user var definition like this with no spaces!! and double quotes for strings if wanted, no single: a=1
var declaration string by default, add declare -i first to make number\
unset <var> converts var number to string
$ = get value
echo does simple print of string in quotes
single quotes ' ' does not evaluate variables, double quotes " " does
printf controls: \" double quote, \\ backslash, \b backspace, \c produce no further output, \e escape, \n new line, \r carriage return, \t horizonal tab, \v vertical tab
echo ${<var>} - curly brackets allow modification of string when printing
echo ${<var>/<string1>/<string2>} - replaces first instance of string1 with string2
echo ${<var>:x:y} - returns string from character number x onward to y
echo ${#<var>} - returns string length
if/elif/else [condition]; then
        [result]
for loop: >for var in [[condition]]  >do  ><something>  >done
while loop: >while [[condition]]  >do  ><something>  >done
until loop: >until [[condition]]  >do ><something>  >done
case/switch statements: case $<var> in
<case 1>)
        [result]
*)
        [result for any other case not defined]
exit 0;;
esac
break - escapes out of a loop
continue - exists only present interation of loop
done - end script/loop
function declaration syntax, using "function" before funct name is optional:
function <functname> () {
echo "Hello Learner"
}
<functname> <argument> <argument>
prefix local to create local var within function
Logical symbols: && and, || or, == or -eq equals to, != or -ne not equal, < -lt, > -gt, <= -le, >= -ge
read <var> takes user input and turns it into a var
declare array: array=(ITEM1 ITEM2 ITEM3)
access array: echo ${array[2]} prints ITEM2. there's also slice operators
echo {1..10} or echo {a..z} - prints range

COMMAND LINE
cd - change directory. ~ is home, .. goes up one dir
~ = /home/user/
ls - list files in current folder
makedir - makes new dir in location, makedir -p creates intermediate directories if needed
cat <filename> - open file in command line
Contents=$(cat file.txt); echo -e "START OF FILE\n$Contents\nEND OF FILE" - assigns contents of file to var and then prints it. -e interprets newline escape characters as escape characters idk what that means
cp <file to copy> <new file name> - copy files or dir to one place or another
mv <file to move> <destination file> - moves files
head -n x file.txt - prints x number of lines from start of text file
tail -n x file.txt - same from end
sort file.txt - sorts text file's lines (?)
there are others
trap "<commands>" <signal1> <signal2> <signal3> - runs commands if any of the signals recieved
help - lists commands

OTHER NOTES
extension .shs
start script with #!/bin/sh - defines the location of engine used to execute the script
user var definition: a=1
print user var a: echo $a
Bourne-Again SHell - BASH
#! called shebang, ! just called bang
sudio chmod +x demo.sh to grant execute permissions to given script
File test operators test whether: -d if dir exists, -e if file exits, -r if read access, -w if write access, -x if execute access, -s if file size > 0
System variables: BASH - shell name, BASH_VERSION - shell version, HOME - home directory path, USERNAME - username
Learn VI/M at some point bc it's available on ever Linux system
pwd (Print Working Directory) prints path of current directory. pwd -L prints symbolic path, pwd -P prints acttual path. $PWD stores path of current dir.
find . -type f\( -name ".c" -o -name "*.sh"\) finds multiple file name extensions, just add an -o for each filename type
Find all directories with the name 'build': find . -type d -name build
There are commands for the above to delete when using the find command but I won't list them
Zombie process: process that has died but has not exited which leaves the process still in the process table
add & to end of script to run in background
&& makes script execute only if previous one was sucessful
control instructions specify the order instructions in a script are executed
show how long system has been running: uptime
cmp compares two files until it finds a mismatch
diff finds all mismatches between two files
grep/egrep: searches file for string of characters, has many commands
pass an argument (first argument) to a scripts: cat $1
cat does a bunch of other things too. short for concatenation
tar stands for tape archive, backups up data
