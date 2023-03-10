import os
import re
from os.path import exists
import glob


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


class Color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


total_mark = 0

mark = 0
current_dir = os.getcwd().split('/')

try:
    with open("part1.txt", "r") as f:
        part1 = f.readlines()
    if re.match(r"\/home\/.*", part1[0]):
        mark += 1
        print("Part 1,1: OK")
    if re.match(r"\/home\/.*\/CS1XC3\/L06", part1[1]):
        mark += 1
        print("Part 1,2: OK")
    homefound = False
    for i in part1:
        if i.split("=")[0] == "HOME":
            homefound = True
            if part1[2] == i.split("=")[1].split("/")[-1]:
                mark += 1
                print("Part 1,3: OK")
    if not homefound:
        mark += 1
        print("Part 1,3: Mark given cause no other way to check")
    if "command not found" in part1[4]:
        mark += 1
        print("Part 1,4: OK")
    if len(part1) - 4 > 20:
        counter = 0
        for i in part1:
            if i.split("=")[0] == "PATH" or i.split("=")[0] == "HOME" or i.split("=")[0] == "PWD" or i.split("=")[0] == "SHELL":
                counter += 1
        if counter == 4:
            mark += 1
            print("Part 1,5: OK")
except FileNotFoundError:
    pass
print(f"\n{Color.GREEN}Part 1: {mark}/5{Color.END}")
print("-------------------------------\n")
total_mark += mark

mark = 0

try:
    with open("part2.txt", "r") as f:
        part2 = f.read()
    if "profile" in part2 and ("load average" in part2 or "load averages" in part2):
        mark += 1
        print("Part 2,1: OK")
except FileNotFoundError:
    pass

counter = 0
if exists(".bash_profile"):
    with open(".bash_profile", "r") as f:
        bash_profile = f.readlines()
elif exists(".bashrc"):
    with open(".bashrc", "r") as f:
        bash_profile = f.readlines()
else:
    bash_profile = []
bash_profile = [i.strip("\n") for i in bash_profile]
for i in bash_profile:
    if re.match(r'PS1=".*\\u.*\\W.* "', i) or re.match(r'cd .*', i) or i == "git pull" or i == "cd":
        counter += 1
       
if counter == 4:
    mark += 2
    print("Part 2,2: OK")
try:
    with open(".bash_logout", "r") as f:
        bash_logout = f.readlines()
except FileNotFoundError:
    bash_logout = []

bash_logout = [i.strip("\n").rstrip() for i in bash_logout]
counter = 0

for i in bash_logout:
    i = i.strip()
    if re.match(r'cd .*\/CS1XC3', i) or i == "git add ." or re.match(r'git commit -m ".*"', i) or re.match(r'git push.*', i) or i == "[ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q":
        counter += 1
if counter == 5:
    mark += 2
    print("Part 2,3: OK")

print(f"\n{Color.GREEN}Part 2: {mark}/5{Color.END}")
print("-------------------------------\n")
total_mark += mark

mark = 0

if find("solitaire.c", "part3"):
    mark += 5
    print("Part 3,1: OK")

print(f"\n{Color.GREEN}Part 3: {mark}/5{Color.END}")
print("-------------------------------\n")
total_mark += mark

mark = 0

correct_strings = [
    "2 + 2 = %d",
    "2 * 2 = %d",
    "<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>",
    "         Barrett's Privateers by Stan Rogers        ",
    "Oh, the year was 1778",
    "(How I wish I was in sherbrooke now!)",
    "A letter of marque came from the king",
    "To the scummiest vessel I'd ever seen",
    "God damn them all!",
    "I was told we'd cruise the seas for American gold",
    "We'd fire no guns-shed no tears",
    "Now I'm a broken man on a Halifax pier",
    "The last of Barrett's Privateers",
    "Oh, Elcid Barrett cried the town",
    "For twenty brave men all fishermen who",
    "Would make for him the Antelope's crew",
    "The Antelope sloop was a sickening sight,",
    "She'd a list to the port and her sails in rags",
    "And the cook in scuppers with the staggers and the jags",
    "On the King's birthday we put to sea,",
    "We were 91 days to Montego Bay",
    "Pumping like madmen all the way",
    "On the 96th day we sailed again",
    "When a bloody great Yankee hove in sight",
    "With our cracked four pounders we made to fight",
    "The Yankee lay low down with gold",
    "She was broad and fat and loose in the stays",
    "But to catch her took the Antelope two whole days",
    "Then at length we stood two cables away",
    "Our cracked four pounders made an awful din",
    "But with one fat ball the Yank stove us in",
    "God damn them all!",
    "The Antelope shook and pitched on her side",
    "Barrett was smashed like a bowl of eggs",
    "And the Maintruck carried off both me legs",
    "So here I lay in my 23rd year",
    "It's been 6 years since we sailed away",
    "And I just made Halifax yesterday",
    "<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>"]
correct_archive_files = "C_Shanties.oproducts.osums.o"

if glob.glob("part4/*.a") != []:
    top_strings = os.popen("strings part4/top").read().split("\n")
    archive_content = os.popen(
        "ar -t part4/*.a").read().replace("\n", "").replace("/", "")
    if set(correct_strings).issubset(set(top_strings)) and archive_content == correct_archive_files:
        print("Part 4,1: OK")
        mark += 5
print(f"\n{Color.GREEN}Part 4: {mark}/5{Color.END}")
print("-------------------------------\n")
total_mark += mark

mark = 0

try:
    with open("dynamic/part5.txt") as file:
        part5 = file.read()
    if "/usr/bin/ld: cannot find -lLab6Part5" in part5 and "collect2: error: ld returned 1 exit status" in part5 and "./top: error while loading shared libraries: libLab6Part5.so: cannot open shared object file: No such file or directory" in part5:
        mark += 1
        print("Part 5,1: OK")
except FileNotFoundError:
    pass

try:
    with open("dynamic/runtop.sh") as file:
        runtop = file.read()
    if 'export LD_LIBRARY_PATH' in runtop and 'LD_LIBRARY_PATH="$LD_LIBRARY_PATH:' in runtop and "./top" in runtop and "unset LD_LIBRARY_PATH" in runtop:
        mark += 2
        print("Part 5,2: OK")
except FileNotFoundError:
    pass

try:
    with open("dynamic/compiletop.sh", "r") as file:
        compiletop = file.readlines()
    for i in compiletop:
        i = i.strip()
        if re.match(r"gcc -L.* -Wl,-rpath=.* -Wall -o test top.c -lLab6Part5", i):
            mark += 2
            print("Part 5,3: OK")
except FileNotFoundError:
    pass
print(f"\n{Color.GREEN}Part 5: {mark}/5{Color.END}")
print("-------------------------------\n")
total_mark += mark

print(f"{Color.CYAN}Total mark is {total_mark}/25{Color.END}")
