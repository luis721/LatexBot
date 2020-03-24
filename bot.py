import logging

from PIL import Image
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


def image_resize(file, output='equation.png'):
    image = Image.open(file)
    width, height = image.size
    white = Image.new('RGB', (width+64, int(3*width/4)), (255, 255, 255))
    white.paste(image, (32, 3*width//8-height//2))
    white.save(output)


def latex(update, context):
    chat_id = update.message.chat.id
    texto = update.message.text
    if len(texto) < len('/latex '):
        update.message.reply_text("Escribe una ecuación junto al comando.")
        return

    texto = texto[texto.find(' '):]
    try:
        equation = r'$${}$$'.format(texto)
        preview(equation, viewer='file', filename='test.png', euler=False)
        image_resize('test.png')
        context.bot.send_photo(chat_id=chat_id, photo=open('equation.png', 'rb'))
    except Exception as e:
        update.message.reply_text("Disculpa, no he logrado procesar esta ecuación.")


def inline(update, context):
    chat_id = update.message.chat.id
    texto = update.message.text
    if len(texto) < len('/inline '):
        update.message.reply_text("Escribe una ecuación junto al comando.")
        return

    texto = texto[texto.find(' '):]
    equation = r'${}$'.format(texto)
    try:
        preview(equation, viewer='file', filename='test.png', euler=False)
        image_resize('test.png')
        context.bot.send_photo(chat_id=chat_id, photo=open('equation.png', 'rb'))
    except Exception as e:
        print(e)
        update.message.reply_text("Disculpa, no he logrado procesar esta ecuación.")


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)