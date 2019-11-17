
vertical = ' ---'
horizontal = '|   '

x = int(input("Tic Tic Toe's 1st dimension? : "))
y = int(input("2nd dimension? : "))

def draw(x,y):
    for i in range(x):
        print((x*vertical))
        print((y+1) * horizontal)
    print(x*vertical)
    
print("Here is your Tic Toc Toe")
draw(x,y)