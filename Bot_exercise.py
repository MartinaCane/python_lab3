from sys import argv
'''External functions for the list - STARTING'''
# add a new task
def new_task(tasks_list):

    string = input("Type the new task:\n>")
    tasks_list.append(string)
    print("New task successfully added")


# remove a task - given the entire string
def remove_task(tasks_list):
    string = input("Type the entire content of the task you want to delete:\n>")
    if (string in tasks_list):
        tasks_list.remove(string)
        print("The element was successfully deleted")
    else:
        print("The element you specified is not in the list!")


# remove a task - given an element of the string
def remove_multiple_tasks(tasks_list):
    remove_list = []
    substring = input("Type the substring you want to use to remove all tasks that contain it:\n>")

    #mark tasks that contains the specified substring
    for single_task in tasks_list:
        #if the substring is contained in the task we save it in the remove_list
        if (substring in single_task):
            remove_list.append(single_task)
    if (len(remove_list)>0):
        for task_to_remove in remove_list:
            if (task_to_remove in tasks_list):
                tasks_list.remove(task_to_remove)
                print("The element "+task_to_remove+" was successfully removed")
    else:
        print("We did not find any tasks to delete!")


# print the entire list sorted in alphabetical order
def print_sorted_list(tasks_list):

    if (len(tasks_list) == 0):
        print("The list is empty")
    else:
        print(sorted(tasks_list))

'''External functions for the list - FINISHED'''

#-------------------------------------------------------------------------------

'''External functions for the bot - STARTING'''

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction


# define a command handler. Command handlers usually take two arguments:
# bot and update
def start(bot, update):
    update.message.reply_text("Here I am")

def show(bot, update):
    update.message.reply_text(print_sorted_list(tasks_list)))

def new(bot, update):
    update.message.reply_text(new_task(tasks_list))

def remove(bot, update):
    update.message.reply_text(remove_task(tasks_list)))

def removeAll(bot, update):
    update.message.reply_text(remove_multiple_tasks(tasks_list))


# the non-command handler
def echo(bot, update):
    # simulate typing from the bot
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)

    # get the message from the user
    repeat_text = update.message.text
    # send the message back
    update.message.reply_text(repeat_text)
    # alternative way: bot.sendMessage(update.message.chat_id, repeat_text)


def bot():

    # create the EventHandler and pass it your bot's token
    updater = Updater("513703656:AAFIV1vBhHuXLz9f9XXT_AwuxVKi5aEaXfI")

    # get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))            # add the command handler for the "/start" command
    dp.add_handler(CommandHandler("showTasks", show))
    dp.add_handler(CommandHandler("newTask", new))
    dp.add_handler(CommandHandler("removeTask", remove))
    dp.add_handler(CommandHandler("removeAllTasks", removeAll))


    dp.add_handler(MessageHandler(Filters.text, echo))       # on non-command textual messages - echo the original message

    # start the bot
    updater.start_polling()


    updater.idle()

'''External functions for the bot - FINISHED'''
#--------------------------------------------------------------------------------------

if __name__ == '__main__':

    tasks_list = []

    ended = False

    # if the user did not insert a filename we start from an empty list
    filename = ""
    if (len(argv) > 1):
        filename = argv[1]
        try:
            txt = open(filename)

            tasks_list = txt.read().splitlines()  # read the file row by row without "/n"

            txt.close()

        except IOError:
            print("File not found! We will start with an empty list")

    # keep asking strings until the user types 4 to exit
    while not ended:
        print("Insert the number corresponding to the action you want to perform")
        print("1: insert a new task")
        print("2: remove a task (by typing all its content)")
        print("3: remove all the existing tasks that contain a provided string")
        print("4: show all existing tasks sorted in alphabetic order")
        print("5: close the program")

        string = input("Your choice:\n>")

        # check the input
        while string.isdigit() != True:
            # if the string is not a number we will ask a new input
            string = input("Wrong input! Your choice:\n>")

            # convert the string to int (integer number)
        choice = int(string)

        if (choice == 1):  # insert a new task
            new_task(tasks_list)
        elif (choice == 2):  # remove a task
            remove_task(tasks_list)
        elif (choice == 3):  # remove tasks containing a provided string
            remove_multiple_tasks(tasks_list)
        elif (choice == 4):  # show the list of tasks
            print_sorted_list(tasks_list)
        elif (choice == 5):  # exit
            ended = True
        else:
            print("Not supported: insert a number between 1 and 4\n")



        # before closing the program, we save results on file
    if (ended and filename != ""):
        try:
             txt = open(filename, "w")

             for single_task in tasks_list:
                 txt.write(single_task + "\n")

             txt.close()

        except IOError:
            print("Problems in saving todo list to file")

if __name__ == "__bot__":
    bot()
