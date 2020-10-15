import os
import getpass
import pyttsx3
from colorama import init 
from termcolor import colored 
init() 

x='  Welcome Sir , I am Atom , how can I help You'
x=x.center(210)
print(colored( x , 'grey', 'on_yellow')) 
pyttsx3.speak("Welcome Sir , I am Atom , how can I help You")
print(colored(' \t\t\t\t\t\t\t\t\t\t  ________________________________________________', 'green', 'on_grey'))
pyttsx3.speak("Please enter your password to login")
passwd= getpass.getpass('Enter the password')
apass='Pal942'
if apass!=passwd:
    e=" Wrong password Try Again Later!!!!!!"
    e.center(210)
    print(colored(e,'red','on_grey'))
    pyttsx3.speak("wrong password try again later")
    exit()
pyttsx3.speak("How are you sir")
r='How are you Sir'
r=r.center(210)
print(colored(r, 'grey', 'on_yellow'),end='\n')

p=input()
if (("fine in p") or ("good" in p)):
    pyttsx3.speak("You are doing good")
    s='You are doing good'
    s=s.center(210)
    print(colored(s,'grey','on_yellow'))
else:
    pyttsx3.speak("Sir you should consult a doctor")
    print("Sir you should consult a doctor").center(210)
t='What do you want to run'
t=t.center(210)
print(colored(t,'green','on_grey'))
pyttsx3.speak("What do you want to run")
print("Please Enter your choice")


while True:
     
      x=input().lower()
      
      
      if (("run" in x) or ("execute" in x) or ("open" in x)) and (("notepad" in x) or ("text" in x)):
        pyttsx3.speak('Launching Notepad')
        y="Launching Notepad"
        y=y.center(210)
        print(colored(y,'green','on_grey'))
        os.system('notepad')
    

      elif (("run" in x) or ("execute" in x) or ("play" in x) or ("open" in x)) and (("media" in x) or ("player" in x) or ("music" in x)):
        pyttsx3.speak('Launching Windows Media Player')
        u="Launching Windows Media Player"
        u=u.center(210)
        print(colored(u,'green','on_grey'))
        os.system('wmplayer')   
      
      elif (("run" in x) or ("execute" in x) or ("open" in x)) and ( ("virtual" in x) or ("box" in x)):
        pyttsx3.speak('Launching Virtual Box')
        v="Launching Virtual Box"
        v=v.center(210)
        print(colored(v,'green','on_grey'))
        os.system('VirtualBox') 
     
      elif (("run" in x) or ("execute" in x) or ("open" in x)) and (("microsoft" in x) or ("edge" in x)):
         pyttsx3.speak('Launching Microsoft edge')
         w="Launching Microsoft Edge"
         w=w.center(210)
         print(colored(w,'green','on_grey'))
         os.system('msedge')
     
      elif (("run" in x) or ("execute" in x) or ("open" in x)) and ( ("git" in x) or ("bash" in x)):
         pyttsx3.speak('Launching git bash')
         a="Launching Git Bash"
         a=a.center(210)
         print(colored(a,'green','on_grey'))
         os.system('git-bash') 
     
      elif (("open" in x) or ("run" in x)) and ( ("file" in x) or ("explorer" in x)):
         pyttsx3.speak('Opening file explorer')
         b="Opening file explorer"
         b=b.center(210)
         print(colored(b,'green','on_grey'))
         os.system('explorer') 
      elif (("open" in x) or ("run" in x)) and ( ("Microsoft" in x) or ("Teams" in x) or ("meeting")):
         pyttsx3.speak('Launching Microsoft Teams')
         c="Launching  Microsoft Teams"
         c=c.center(210)
         print(colored(c,'green','on_grey'))
         os.system('ptoneclk') 
     
      
      else:
         pyttsx3.speak('Thanks You Sir have a nice day')
         d="Thnak You Sir have a nice day !!!"
         d=d.center(210)
         print(colored(d,'green','on_grey'))
         exit()
