# Импортируем необходимые классы.
import asyncio
import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

BOT_TOKEN = "7816645205:AAGEbU-3X9HW96lQEIw2tyoULDb3Ev11654"

reply_keyboard = [['/set', '/unset']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

# !!! username bot: @YLyceumPoliteEcho_bot


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def remove_job_if_exists(name, context):
    """Удаляем задачу по имени.
    Возвращаем True если задача была успешно удалена."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


async def set_timer(update, context):
    if context.args:
        try:
            seconds = int(context.args[0])

            chat_id = update.effective_message.chat_id
            job_removed = remove_job_if_exists(str(chat_id), context)
            context.job_queue.run_once(task, seconds, chat_id=chat_id, name=str(chat_id), data=seconds)

            text = f'Вернусь через {seconds} с.!'
            if job_removed:
                text += ' Старая задача удалена.'
            await update.effective_message.reply_text(text)
        except (ValueError, IndexError):
            await update.message.reply_text("Пожалуйста, укажите время в секундах. /set sec")
    else:
        await update.message.reply_text("Пожалуйста, укажите время в секундах. /set sec")


async def task(context):
    """Выводит сообщение"""
    seconds = context.job.data  # Получаем переданные данные
    await context.bot.send_message(context.job.chat_id, text=f'КУКУ! {seconds} прошли!')


async def unset(update, context):
    """Удаляет задачу, если пользователь передумал"""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Таймер отменен!' if job_removed else 'У вас нет активных таймеров'
    await update.message.reply_text(text)


async def start(update, context):
    await update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
        reply_markup=markup
    )


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник.")


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("set", set_timer))
    application.add_handler(CommandHandler("unset", unset))
    application.run_polling()


if __name__ == '__main__':
    main()
