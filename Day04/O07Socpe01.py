
glbX = 100

def fun(x):             # local variable - scope is lexical
    global glbX         # do not assign a value in this line
    print(f"x :{x}")
    glbX = 500      # local variable glbX same name as global variable
    print(f"glbX :{glbX}")

print(f"Before the function call :{glbX}")

fun(20)

print(f"After the function call :{glbX}")