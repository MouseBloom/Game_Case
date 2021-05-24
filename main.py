# Case-study
# Developers:
# Marinkin O. (65%),
# Seledtsov A. (50%),
# Evdischenko M. (35%)

import tkinter as tk
import random


window = tk.Tk()
window.title('The Kng Game')
lbl = tk.Label()


d = {'Church': 50, 'People': 50, 'Army': 50, 'Treasury': 50}
b = -1
def destroy():
    for widget in window.winfo_children():
        widget.destroy()
def main(d):
    ch = 'Church', d.get('Church')
    peop = 'People', d.get('People')
    arm = 'Army', d.get('Army')
    treas = 'Treasury', d.get('Treasury')
    lb1 = tk.Label(window,text = ch, fg = 'white', bg = 'black', width ='10', font=("Comic Sans MS", 35))
    lb2 = tk.Label(window,text=peop, fg='white', bg='black',width ='10', font=("Comic Sans MS", 35))
    lb3 = tk.Label(window,text=arm, fg='white', bg='black', width ='10',font=("Comic Sans MS", 35))
    lb4 = tk.Label(window,text=treas, fg='white', bg='black',width ='10', font=("Comic Sans MS", 35))
    lb1.place( relx = 0.15)
    lb2.place(relx = 0.3)
    lb3.place(relx=0.45)
    lb4.place(relx=0.60)
    if d.get('Church') < 0:
        church0()
    elif d.get('Church') > 100:
        church100()
    elif d.get('People') < 0:
        people0()
    elif d.get('People') > 100:
        people100()
    elif d.get('Army') > 100:
        army100()
    elif d.get('Army') < 0:
        army0()
    elif d.get('Treasury') < 0:
        treasury0()
    elif d.get('Treasury') > 100:
        treasury100()
    else:
        event_choice(d)



def event_choice(d):
    global b
    a = random.randint(1,20)
    while b == a:
        a = random.randint(1,20)
    b = a
    if a == 1:
        event1(d)
    if a == 2:
        event2(d)
    if a == 3:
        event3(d)
    if a == 4:
        event4(d)
    if a == 5:
        event5(d)
    if a == 5:
        event5(d)
    if a == 6:
        event6(d)
    if a == 7:
        event7(d)
    if a == 8:
        event8(d)
    if a == 9:
        event9(d)
    if a == 10:
        event10(d)
    if a == 11:
        event11(d)
    if a == 12:
        event12(d)
    if a == 13:
        event13(d)
    if a == 14:
        event14(d)
    if a == 15:
        event15(d)
    if a == 16:
        event16(d)
    if a == 17:
        event17(d)
    if a == 18:
        event18(d)
    if a == 19:
        event19(d)
    if a == 20:
        event20(d)


def church0():

    def click():

        end.destroy()
        btn.destroy()
        d = {'Church': 50, 'People': 50, 'Army': 50, 'Treasury': 50}
        first_step(d)
    end = tk.Label(text='Your country has been taken by pagans\r the burnt you alive', bg = 'black', fg = 'white',font=("Comic Sans MS", 20))
    end.place(anchor='center', relx=.5, rely=.3)
    btn = tk.Button(text = 'TRY AGAIN', width = '10', height = '5',  fg = 'black',  command = click)
    btn.place(anchor = 'center', relx = .5, rely = .4)


def church100():

    def click():

        end.destroy()
        btn.destroy()
        d = {'Church': 50, 'People': 50, 'Army': 50, 'Treasury': 50}
        first_step(d)
    end = tk.Label(text='Your bishop overthrown you\r you died in prison', bg = 'black', fg = 'white',font=("Comic Sans MS", 20))
    end.place(anchor='center', relx=.5, rely=.3)
    btn = tk.Button(text = 'TRY AGAIN', width = '10', height = '5',  fg = 'black',  command = click)
    btn.place(anchor = 'center', relx = .5, rely = .4)


def people0():

    def click():

        end.destroy()
        btn.destroy()
        d = {'Church': 50, 'People': 50, 'Army': 50, 'Treasury': 50}
        first_step(d)
    end = tk.Label(text='People of your kingdom made a revolution\r you were killed by crowd', bg = 'black', fg = 'white',font=("Comic Sans MS", 20))
    end.place(anchor='center', relx=.5, rely=.3)
    btn = tk.Button(text = 'TRY AGAIN', width = '10', height = '5',  fg = 'black',  command = click)
    btn.place(anchor = 'center', relx = .5, rely = .4)


def people100():

    def click():
        end.destroy()
        btn.destroy()
        d = {'Church': 50, 'People': 50, 'Army': 50, 'Treasury': 50}
        first_step(d)
    end = tk.Label(text='People of you kingdom made democracy\r you are no longer in rule but your name will be remembered for ages', bg = 'black', fg = 'white',font=("Comic Sans MS", 20))
    end.place(anchor='center', relx=.5, rely=.3)
    btn = tk.Button(text = 'TRY AGAIN', width = '10', height = '5',  fg = 'black',  command = click)
    btn.place(anchor = 'center', relx = .5, rely = .4)


def army100():
    def click():

        end.destroy()
        btn.destroy()
        d = {'Church': 50, 'People': 50, 'Army': 50, 'Treasury': 50}
        first_step(d)
    end = tk.Label(window,text='Your army is to strong, they made general their new king\r you were executed ', bg = 'black', fg = 'white',font=("Comic Sans MS", 20))
    end.place(anchor='center', relx=.5, rely=.3)
    btn = tk.Button(text = 'TRY AGAIN', width = '10', height = '5',  fg = 'black',  command = click)
    btn.place(anchor = 'center', relx = .5, rely = .4)


def army0():
    def click():

        end.destroy()
        btn.destroy()
        d = {'Church': 50, 'People': 50, 'Army': 50, 'Treasury': 50}
        first_step(d)
    end = tk.Label(text='Your kingdom was taken by invaders\r you were slaved and died in the mines', bg = 'black', fg = 'white',font=("Comic Sans MS", 20))
    end.place(anchor='center', relx=.5, rely=.3)
    btn = tk.Button(text = 'TRY AGAIN', width = '10', height = '5',  fg = 'black',  command = click)
    btn.place(anchor = 'center', relx = .5, rely = .4)


def treasury100():
    def click():

        end.destroy()
        btn.destroy()
        d = {'Church': 50, 'People': 50, 'Army': 50, 'Treasury': 50}
        first_step(d)
    end = tk.Label(text='People united against you to make communism\r you and your family was shot', bg = 'black', fg = 'white',font=("Comic Sans MS", 20))
    end.place(anchor='center', relx=.5, rely=.3)
    btn = tk.Button(text = 'TRY AGAIN', width = '10', height = '5',  fg = 'black',  command = click)
    btn.place(anchor = 'center', relx = .5, rely = .4)


def treasury0():
    def click():

        end.destroy()
        btn.destroy()
        d = {'Church': 50, 'People': 50, 'Army': 50, 'Treasury': 50}
        first_step(d)
    end = tk.Label(text='All the authority was taken by rich men, you lost any power\r you were exiled', bg = 'black', fg = 'white',font=("Comic Sans MS", 20))
    end.place(anchor='center', relx=.5, rely=.3)
    btn = tk.Button(text = 'TRY AGAIN', width = '10', height = '5',  fg = 'black',  command = click)
    btn.place(anchor = 'center', relx = .5, rely = .4)


def event1(d):
    def yes():
        d['Army'] += 20
        d['Treasury'] -= 20
        destroy()
        main(d)
    def no():
        d['Army'] -= 20
        d['Treasury'] += 20
        destroy()
        main(d)

    tex = tk.Label(window,text = "Our army is weak, Should we hire more wariors?",  bg = 'yellow', fg = 'black', width = '100', font = ("Comic Sans MS", 30))

    btn1 = tk.Button(window,text = 'YES',width = '10', height = '5',  fg = 'black', command = yes)
    btn2 = tk.Button(window,text = 'NO',width = '10', height = '5',  fg = 'black', command = no)
    tex.place(anchor = 'center',relx = 0.5, rely = 0.2)
    btn1.place(relx = 0.1, rely = 0.3)
    btn2.place(relx = 0.75, rely = 0.3)


def event2(d):
    def yes():
        d['People'] += 10
        d['Church'] += 10
        d['Treasury'] += 10
        destroy()
        main(d)
    def no():
        d['People'] -= 20
        d['Church'] -= 10
        destroy()
        main(d)
    tex = tk.Label(window,text = "You adviser suggest marrying princess from the other kingdom ",  bg = 'yellow',width = '100', fg = 'black', font = ("Comic Sans MS", 30))
    btn1 = tk.Button(window,text = 'YES',width = '10', height = '5',  fg = 'black', command = yes)
    btn2 = tk.Button(window,text = 'NO',width = '10', height = '5',  fg = 'black', command = no)
    tex.place(anchor = 'center',relx = 0.5, rely = 0.2)
    btn1.place(relx = 0.1, rely = 0.3)
    btn2.place(relx = 0.75, rely = 0.3)

def event3(d):
    def yes():
        d['People'] += 10
        d['Treasury'] -= 25
        d['Church'] += 10
        destroy()
        main(d)
    def no():
        d['People'] -= 10
        d['Treasury'] += 20
        d['Church'] -= 10
        destroy()
        main(d)
    tex = tk.Label(window,text="Should we build a new school", bg='yellow', fg='black',width = '100', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text = 'YES',width = '10', height = '5',  fg = 'black', command = yes)
    btn2 = tk.Button(window,text = 'NO',width = '10', height = '5',  fg = 'black', command = no)
    tex.place(anchor = 'center',relx = 0.5, rely = 0.2)
    btn1.place(relx = 0.1, rely = 0.3)
    btn2.place(relx = 0.75, rely = 0.3)



def event4(d):
    def yes():
        d['People'] += 10
        d['Army'] -= 10
        destroy()
        main(d)
    def no():
        d['People'] -= 10
        d['Church'] += 10
        destroy()
        main(d)
    tex = tk.Label(window,text="People are afraid of goblins, who will take care of it?",width = '100', bg='yellow', fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text = 'Army',width = '10', height = '5',  fg = 'black', command = yes)
    btn2 = tk.Button(window,text = 'Church',width = '10', height = '5',  fg = 'black', command = no)
    tex.place(anchor = 'center',relx = 0.5, rely = 0.2)
    btn1.place(relx = 0.1, rely = 0.3)
    btn2.place(relx = 0.75, rely = 0.3)


def event5(d):
    def yes():
        d['People'] += 10
        d['Army'] += 10
        d['Treasury'] -= 20
        destroy()
        main(d)
    def no():
        d['People'] -= 10
        d['Church'] += 10
        destroy()
        main(d)
    tex = tk.Label(window,text = "Other king gifted us book collection. Should we built a library",width = '100', bg='yellow', fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text = 'YES',width = '10', height = '5',  fg = 'black', command = yes)
    btn2 = tk.Button(text = 'NO',width = '10', height = '5',  fg = 'black', command = no)
    tex.place(anchor = 'center',relx = 0.5, rely = 0.2)
    btn1.place(relx = 0.1, rely = 0.3)
    btn2.place(relx = 0.75, rely = 0.3)



def event6(d):
    def yes():
        d['People'] += 5
        d['Treasury'] -= 10
        destroy()
        main(d)
    def no():
        d['People'] -= 20
        d['Treasury'] += 10
        destroy()
        main(d)
    tex = tk.Label(window,text="Local river dried out. Should we dig new ?",width = '100', bg='yellow', fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text = 'YES',width = '10', height = '5',  fg = 'black', command = yes)
    btn2 = tk.Button(window,text = 'NO',width = '10', height = '5',  fg = 'black', command = no)
    tex.place(anchor = 'center',relx = 0.5, rely = 0.2)
    btn1.place(relx = 0.1, rely = 0.3)
    btn2.place(relx = 0.75, rely = 0.3)

def event7(d):
    def yes():
        d['People'] += 5
        d['Army'] += 5
        d['Church'] += 5
        destroy()
        main(d)
    def no():
        d['Treasury'] += 15
        destroy()
        main(d)
    tex = tk.Label(window,text="We found lots of gold in the mine. What we do?", width = '100',bg='yellow', fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text = 'Share',width = '10', height = '5',  fg = 'black', command = yes)
    btn2 = tk.Button(window,text = 'It all my!',width = '10', height = '5',  fg = 'black', command = no)
    tex.place(anchor = 'center',relx = 0.5, rely = 0.2)
    btn1.place(relx = 0.1, rely = 0.3)
    btn2.place(relx = 0.75, rely = 0.3)

def event8(d):
    def yes():
        d['Church'] += 5
        d['Army'] -= 10

        destroy()
        main(d)
    def no():
        d['Church'] -= 20
        d['Army'] += 5
        destroy()
        main(d)
    tex = tk.Label(window,text="Soldiers stole money from church. Should we punish them?",width = '100', bg='yellow', fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text = 'YES',width = '10', height = '5',  fg = 'black', command = yes)
    btn2 = tk.Button(window,text = 'NO',width = '10', height = '5',  fg = 'black', command = no)
    tex.place(anchor = 'center',relx = 0.5, rely = 0.2)
    btn1.place(relx = 0.1, rely = 0.3)
    btn2.place(relx = 0.75, rely = 0.3)


def event9(d):
    def yes():
        d['Treasury'] -= 20
        d['People'] += 15

        destroy()
        main(d)
    def no():
        d['People'] -= 10
        destroy()
        main(d)
    tex = tk.Label(window,text="Our capital stinks. Built sewerage?", bg='yellow',width = '100', fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text = 'YES',width = '10', height = '5',  fg = 'black', command = yes)
    btn2 = tk.Button(window,text = 'NO',width = '10', height = '5',  fg = 'black', command = no)
    tex.place(anchor = 'center',relx = 0.5, rely = 0.2)
    btn1.place(relx = 0.1, rely = 0.3)
    btn2.place(relx = 0.75, rely = 0.3)

def poisoned():
    def click():

        end.destroy()
        btn.destroy()
        d = {'Church': 50, 'People': 50, 'Army': 50, 'Treasury': 50}
        first_step(d)
    end = tk.Label(text='Wine was poisoned\r you died the next day', bg = 'black',width = '100', fg = 'white',font=("Comic Sans MS", 20))
    end.place(anchor='center', relx=.5, rely=.3)
    btn = tk.Button(text = 'TRY AGAIN', width = '10', height = '5',  fg = 'black',  command = click)
    btn.place(anchor = 'center', relx = .5, rely = .4)

def event10(d):
    def yes():
        destroy()
        b = random.randint(1,2)
        if b == 1:
            d['Church'] += 2
            destroy()
            main(d)
        if b == 2:
            destroy()
            poisoned()
    def no():
        destroy()
        main(d)

    tex = tk.Label(window,text="Bottle of wine?", bg='yellow', fg='black',width = '100', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text = 'YES',width = '10', height = '5',  fg = 'black', command = yes)
    btn2 = tk.Button(window,text = 'NO',width = '10', height = '5',  fg = 'black', command = no)
    tex.place(anchor = 'center',relx = 0.5, rely = 0.2)
    btn1.place(relx = 0.1, rely = 0.3)
    btn2.place(relx = 0.75, rely = 0.3)


def event11(d):
    def yes():
        d['Treasury'] += 10
        d['Church'] += 10
        d['People'] -= 5
        destroy()
        main()
    def no():
        d['Church'] -= 10
        destroy()
        main(d)
    tex = tk.Label(window,text="The church wants to introduce a new tax. The church is ready to share. Allow them?",bg='yellow',width = '100', fg='black',font=("Comic Sans MS", 30))
    btn1 = tk.Button(window, text='YES', width='10', height='5', fg='black', command=yes)
    btn2 = tk.Button(window,text='NO', width='10', height='5', fg='black', command=no)
    tex.place(anchor='center', relx=0.5, rely=0.2)
    btn1.place(relx=0.1, rely=0.3)
    btn2.place(relx=0.75, rely=0.3)


def event12(d):
    def yes():
        d['Treasury'] -= 10
        d['People'] -= 5
        d['Army'] -= 10
        destroy()
        main(d)
    def no():
        d['People'] -= 10
        destroy()
        main(d)

    tex = tk.Label(window,text="The Eastern baronies are gathering on our border. Send an army?",width = '100',bg='yellow', fg='black',font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text='YES', width='10', height='5', fg='black', command=yes)
    btn2 = tk.Button(window,text='NO', width='10', height='5', fg='black', command=no)
    tex.place(anchor='center', relx=0.5, rely=0.2)
    btn1.place(relx=0.1, rely=0.3)
    btn2.place(relx=0.75, rely=0.3)


def event13(d):
    def yes():
        d['Treasury'] += 10
        d['Army'] += 10
        destroy()
        main(d)
    def no():
        d['People'] -= 10
        d['Army'] -= 10
        destroy()
        main(d)

    tex = tk.Label(window,text="Our enemies want a peace agreement. Conclude?",width = '100',bg='yellow', fg='black',font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text='YES', width='10', height='5', fg='black', command=yes)
    btn2 = tk.Button(window,text='NO', width='10', height='5', fg='black', command=no)
    tex.place(anchor='center', relx=0.5, rely=0.2)
    btn1.place(relx=0.1, rely=0.3)
    btn2.place(relx=0.75, rely=0.3)


def event14(d):
    def yes():
        d['Army'] -= 10
        destroy()
        main(d)
    def no():
        d['People'] -= 10
        d['Treasury'] -= 10
        destroy()
        main(d)

    tex = tk.Label(window,text="The public barn is on fire. Send troops?",width = '100',bg='yellow', fg='black',font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text='YES', width='10', height='5', fg='black', command=yes)
    btn2 = tk.Button(window,text='NO', width='10', height='5', fg='black', command=no)
    tex.place(anchor='center', relx=0.5, rely=0.2)
    btn1.place(relx=0.1, rely=0.3)
    btn2.place(relx=0.75, rely=0.3)


def event15(d):
    def yes():
        d['Treasury'] -= 10
        d['Church'] -= 10
        d['People'] += 10
        destroy()
        main(d)
    def no():
        d['Church'] += 10
        main(d)
        main(d)
    tex = tk.Label(window, text="Scientists want to conduct a study. Allocate money?",width = '100',bg='yellow', fg='black',font=("Comic Sans MS", 30))
    btn1 = tk.Button(window,text='YES', width='10', height='5', fg='black', command=yes)
    btn2 = tk.Button(window, text='NO', width='10', height='5', fg='black', command=no)
    tex.place(anchor='center', relx=0.5, rely=0.2)
    btn1.place(relx=0.1, rely=0.3)
    btn2.place(relx=0.75, rely=0.3)


def event16(d):
    def yes():
        d['Church'] += 10
        d['Treasury'] -= 10

        destroy()
        main(d)
    def no():
        d['Church'] -= 10
        d['Army'] += 5
        destroy()
        main(d)

    tex = tk.Label(window, text="Should we build a new church?", width='100', bg='yellow',fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window, text='YES', width='10', height='5', fg='black', command=yes)
    btn2 = tk.Button(window, text='NO', width='10', height='5', fg='black', command=no)
    tex.place(anchor='center', relx=0.5, rely=0.2)
    btn1.place(relx=0.1, rely=0.3)
    btn2.place(relx=0.75, rely=0.3)


def event17(d):
    def yes():
        d['People'] += 10
        d['Treasury'] -= 10

        destroy()
        main(d)

    def no():
        d['People'] -= 10
        destroy()
        main(d)

    tex = tk.Label(window, text="The people are starving. Should we distribute food?", width='100', bg='yellow',fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window, text='YES', width='10', height='5', fg='black', command=yes)
    btn2 = tk.Button(window, text='NO', width='10', height='5', fg='black', command=no)
    tex.place(anchor='center', relx=0.5, rely=0.2)
    btn1.place(relx=0.1, rely=0.3)
    btn2.place(relx=0.75, rely=0.3)

def event18(d):
    def yes():
        d['People'] += 10
        d['Treasury'] -= 10
        d['Church'] -= 10
        d['Army'] += 15
        destroy()
        main(d)
    def no():
        d['People'] -= 10
        d['Church'] += 5
        d['Army'] -= 10
        destroy()
        main(d)
    tex = tk.Label(window, text="Woman claims that her child is yours", width='100', bg='yellow',fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window, text='ACCEPT', width='10', height='5', fg='black', command=yes)
    btn2 = tk.Button(window, text='DENIE', width='10', height='5', fg='black', command=no)
    tex.place(anchor='center', relx=0.5, rely=0.2)
    btn1.place(relx=0.1, rely=0.3)
    btn2.place(relx=0.75, rely=0.3)


def event19(d):
    def yes():
        d['People'] -= 10
        d['Army'] += 10

        destroy()
        main(d)

    def no():
        d['Army'] -= 10
        destroy()
        main(d)

    tex = tk.Label(window, text="The catapults are damaged. Find the traitors??", width='100', bg='yellow',fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window, text='YES', width='10', height='5', fg='black', command=yes)
    btn2 = tk.Button(window, text='NO', width='10', height='5', fg='black', command=no)
    tex.place(anchor='center', relx=0.5, rely=0.2)
    btn1.place(relx=0.1, rely=0.3)
    btn2.place(relx=0.75, rely=0.3)


def event20(d):
    def yes():
        d['Treasury'] -= 10
        d['Army'] += 10

        destroy()
        main(d)

    def no():
        d['People'] -= 10
        destroy()
        main(d)

    tex = tk.Label(window, text="The ship is in quarantine. Maybe it's the plague. Close the entire port?", width='100', bg='yellow',fg='black', font=("Comic Sans MS", 30))
    btn1 = tk.Button(window, text='YES', width='10', height='5', fg='black', command=yes)
    btn2 = tk.Button(window, text='NO', width='10', height='5', fg='black', command=no)
    tex.place(anchor='center', relx=0.5, rely=0.2)
    btn1.place(relx=0.1, rely=0.3)
    btn2.place(relx=0.75, rely=0.3)


def first_step(d):
    destroy()
    def clicked():
        lbl.destroy()
        btn.destroy()
        main(d)
    lbl = tk.Label(text = 'All yor decisions will affect your kingdom and you future, choose wisely', fg = 'white', bg= 'black', font=("Comic Sans MS", 20))
    lbl.pack()
    btn = tk.Button(text = 'I understand', command = clicked, font = ("Comic Sans MS",20))
    btn.place(in_= lbl, anchor="center", relx=.5, rely=5)






def game_start(d):
    def clicked():
        lbl.configure(text = 'Game starts')
        btn1.destroy()
        lbl.destroy()
        first_step(d)
    window.title('The Kng Game')
    window.configure(bg = "black")
    window.geometry('1000x1000')
    lbl.configure(text="Start the Game?", fg = 'white', bg= 'black', font=("Comic Sans MS", 20))
    btn1 = tk.Button(window,text="Start",  command = clicked, font = ("Comic Sans MS", 20))
    lbl.pack()
    btn1.place(in_= lbl, anchor="center", relx=.5, rely=5)





game_start(d)
window.mainloop()