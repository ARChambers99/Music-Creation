import random
uniform= []
uniform.append ([.143,.143,.143,.143,.143,.143,.142])
uniform.append ([.143,.143,.143,.143,.143,.143,.142])
uniform.append ([.143,.143,.143,.143,.143,.143,.142])
uniform.append ([.143,.143,.143,.143,.143,.143,.142])
uniform.append ([.143,.143,.143,.143,.143,.143,.142])
uniform.append ([.143,.143,.143,.143,.143,.143,.142])
uniform.append ([.143,.143,.143,.143,.143,.143,.142])

blues= [] #for blues we will apply this to both rock and blues due to similarities
blues.append ([0,.1,.1,.4,.15,.1,.15])
blues.append ([0,0,0,.1,.3,.4,.2])
blues.append ([.1,0,0,.1,.3,.2,.3])
blues.append ([0,.1,.1,0,.4,.25,.15])
blues.append ([.15,.3,.3,0,0,0,.25])
blues.append ([.1,.4,.2,.15,.15,0,0])
blues.append ([.05,.2,.3,.05,.25,.15,0])

jazz= []
jazz.append ([.0,.6,.1,.1,.15,.05,0])
jazz.append ([.2,0,.1,.05,.5,.05,.1])
jazz.append ([.2,.05,0,.05,.2,.3,.2])
jazz.append ([.2,.1,.05,0,.3,.2,.15])
jazz.append ([.4,.2,.05,.05,0,.1,.2])
jazz.append ([.2,.3,.05,.15,.1,0,.2])
jazz.append ([.2,.1,.2,.1,.2,.2,0])

start = 0

def next_chord(start, genre):
    total=0
    r = random.random()
    for i in range (len(genre[start])):
        total += genre[start][i]
        if r<total:
            return i #This works so far. In case of emergency delete up to here
        
def repeat(start, num, genre):
    current_chord = start
    print(current_chord,end="  ")
    for i in range (num):
        current_chord=next_chord(current_chord, genre)
        print(current_chord,end="  ")
        
        
