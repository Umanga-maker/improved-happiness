name = "Umanga"
count = 1

def another():
    color = "blue"
    global count
    count += 2
    print (count)
    
    def greeting(name):
        nonlocal color 
        color = "red"
        print(color)
        print(name)
        
    greeting("Umanga")


another()
