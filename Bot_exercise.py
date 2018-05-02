from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction


def start(bot, update):
    update.message.reply_text("""Hi, here you have the actions you can perform:
    1. /showTasks
    2. /newTask
    3. /removeTask
    4. /removeAllTasks""")


def show(bot, update):

    if len(tasks)!=0:
        taskToPrint = ["List of the tasks:"] + tasks
        taskToPrint = '\n- '.join(taskToPrint)
        update.message.reply_text(taskToPrint)
    else:
        taskToPrint = "The list of the tasks is empty"
        update.message.reply_text(taskToPrint)


def new(bot, update, args):

    input_new = " ".join(args)

    if input_new != '':
            update.message.reply_text('''Creating updated list of tasks, you add: 
            '''+ input_new)
            tasks.append(input_new)
    else:
            update.message.reply_text("Error, type task after the command")

def remove(bot, update, args):

    input_delete = " ".join(args)

    if input_delete != '':
            update.message.reply_text('''Creating updated list of tasks, you deleted: 
            '''+ input_delete)
            tasks.remove(input_delete)
    else:
            update.message.reply_text("Error, type task after the command")


def removeAll(bot, update,args):
    tasks.clear()
    print(tasks)
    update.message.reply_text("All Tasks have been successfully deleted")


def main():
    # create the EventHandler and pass it your bot's token
    updater = Updater("513703656:AAFIV1vBhHuXLz9f9XXT_AwuxVKi5aEaXfI")

    # Open the file in reading mode
    savedTasks = open("task_list.txt", "r+")
    for line in savedTasks:
        line = line[0:len(line) - 1]  # -1 used to eliminate the end of raw character
        tasks.append(line)

   # message.text("To start the bot please selct: /start")

    # get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))  # add the command handler for the "/start" command
    dp.add_handler(CommandHandler("showTasks", show))
    dp.add_handler(CommandHandler("newTask", new, pass_args=True))  # pass_args=True To write
    dp.add_handler(CommandHandler("removeTask", remove, pass_args=True))
    dp.add_handler(CommandHandler("removeAllTasks", removeAll, pass_args=True))


    # start the bot
    updater.start_polling()
    updater.idle()


tasks = []

if __name__ == "__main__":
    main()
