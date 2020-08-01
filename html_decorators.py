def div(func):
    # You have to code here!
    def func_wrapper(*args, **kwargs):
        return '<div>{}</div>'.format(func(*args, **kwargs))

    return func_wrapper


def article(func):
    # You have to code here!
    def func_wrapper(*args, **kwargs):
        return '<article>{}</article>'.format(func(*args, **kwargs))

    return func_wrapper


def p(func):
    # You have to code here!
    def func_wrapper(*args, **kwargs):
        return '<p>{}</p>'.format(func(*args, **kwargs))

    return func_wrapper


# Here you must apply the decorators, uncomment this later
@div
#@article
#@p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
