# ~/.bash_logout

if [ "$SHLV" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
cd /home/pandea23/CS1XC3
git add .
git commit -m "Shell Logout Commit"
git push
