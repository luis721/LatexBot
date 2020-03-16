from sympy import preview


def start(update, context):
    update.message.reply_text('Bienvenido a este bot.')


def saludo(update, context):
    nombre = update.message.forward_from.first_name
    mensaje = 'Hola, {}. ¿Cómo estás? :-)'.format(nombre)
    update.message.reply_text(mensaje)


def latex(update, context):
    try:
        chat_id = update.message.chat.id
        texto = update.message.text[7:]
        equation = r'$${}$$'.format(texto)
        preview(equation, viewer='file', filename='test.png', euler=False)
        context.bot.send_photo(chat_id=chat_id, photo=open('test.png', 'rb'))
    except Exception as e:
        update.message.reply_text("Disculpa, no he logrado procesar esta ecuación.")


def inline(update, context):
    chat_id = update.message.chat.id
    texto = update.message.text[8:]
    equation = r'${}$'.format(texto)
    try:
        preview(equation, viewer='file', filename='test.png', euler=False)
        context.bot.send_photo(chat_id=chat_id, photo=open('test.png', 'rb'))
    except Exception as e:
        print(e)
        update.message.reply_text("Disculpa, no he logrado procesar esta ecuación.")
