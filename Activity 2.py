def pal(t):
    end=len(t)-1
    start=0
    while (start<end):
        if t[start]!=t[end]:
            return False
        start=start+1
        end=end-1
    return True
t=("start")
if (pal(t)):
    print("Its a palindrome")
else:
    print("Its not a palindrome")