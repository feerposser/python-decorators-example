
def decorator(func):
    print("função decorator")

    def teste(*args, **kwargs):
        print("Chamando funcao: %s()" % func.__name__)
        print("args", args)
        print("kwargs", kwargs)
        return func(*args, **kwargs)

    print("executar função teste")

    return teste


@decorator
def hello_world(x):
    print("função hello world")
    print("Hello,", x)


hello_world("fernando")