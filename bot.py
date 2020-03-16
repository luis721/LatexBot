import logging
from sympy import preview


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# TODO usar objeto de buffer en lugar de guardar el archivo


def start(update, context):
    update.message.reply_text('Bienvenido a este bot.')


def saludo(update, context):
    nombre = update.message.from_user.first_name
    mensaje = 'Hola, {}. ¿Cómo estás? :-)'.format(nombre)
    update.message.reply_text(mensaje)


def latex(update, context):
    chat_id = update.message.chat.id
    texto = update.message.text
    texto = texto[texto.find(' '):]
    try:
        equation = r'$${}$$'.format(texto)
        preview(equation, viewer='file', filename='test.png', euler=False)
        context.bot.send_photo(chat_id=chat_id, photo=open('test.png', 'rb'))
    except Exception as e:
        update.message.reply_text("Disculpa, no he logrado procesar esta ecuación.")


def inline(update, context):
    chat_id = update.message.chat.id
    texto = update.message.text
    texto = texto[texto.find(' '):]
    equation = r'${}$'.format(texto)
    try:
        preview(equation, viewer='file', filename='test.png', euler=False)
        context.bot.send_photo(chat_id=chat_id, photo=open('test.png', 'rb'))
    except Exception as e:
        print(e)
        update.message.reply_text("Disculpa, no he logrado procesar esta ecuación.")


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)