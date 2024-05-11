x = 10

def function():
    global x # rewrites outside x
    x = 20
    y = 10
    def inner_function():
        nonlocal y # rewrites function() scope
        y = 30
        print(f'inner: {y}')

    inner_function()
    print(f'outer: {x=}{y=}')

function()
print(f'global: {x}')
