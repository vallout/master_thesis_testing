from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta

db = MongoClient("localhost:27017").edu

functions = []

boots_id = ""

def print_with_time(input_text):
    now = datetime.now()
    formated_date = "{}:{}:{}:{}".format(now.hour, now.minute, now.second, now.microsecond)
    print("{}: {}".format(formated_date, input_text))

def user_logged_in(output):
    if (output["operationType"] == "insert" and 
        output["fullDocument"]["userId"] == ObjectId('60312e4c8709edadf5dfa0c2') and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.events.userloggedin.UserLoggedInProjection'):
        print_with_time("Jamals logged in event: {}".format('worked'))
    else:
        print_with_time("Jamals logged in event: {}".format('failed'))

functions.append(user_logged_in)

def item_created(output):
    global boots_id
    if (output["operationType"] == "insert" and 
        output["fullDocument"]["itemType"] == "SHOES" and
        output["fullDocument"]["name"] == "Mysterious boots" and
        output["fullDocument"]["description"] == "A mystery" and
        output["fullDocument"]["modelId"] == "some_item_model" and
        output["fullDocument"]["price"] == 0 and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.item.ItemProjection'):
        boots_id=output["fullDocument"]["_id"]
        print_with_time("Mysterious boots created: {}".format('worked'))
    else:
        print_with_time("Mysterious boots created: {}".format('failed'))

functions.append(item_created)

def group_challenge_created(output):
    global boots_id
    if (output["operationType"] == "insert" and 
        output["fullDocument"]["isRunning"] == False and
        output["fullDocument"]["eventName"] == "taskFinished" and
        output["fullDocument"]["description"] == "Finish'em" and
        output["fullDocument"]["end"].day == (datetime.today() + timedelta(6)).day and
        output["fullDocument"]["end"].month == (datetime.today() + timedelta(6)).month and
        output["fullDocument"]["end"].year == (datetime.today() + timedelta(6)).year and
        output["fullDocument"]["condition"] == 100 and
        output["fullDocument"]["rewardPoints"] == 0 and
        output["fullDocument"]["rewardItem"] == str(boots_id) and
        output["fullDocument"]["isFinished"] == False and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.groupchallenge.GroupChallengeProjection'):
        print_with_time("Group challenge created: {}".format('worked'))
    else:
        print_with_time("Group challenge created: {}".format('failed'))

functions.append(group_challenge_created)

def group_challenge_activated(output):
    global boots_id
    if (output["operationType"] == "replace" and 
        output["fullDocument"]["isRunning"] == True and
        output["fullDocument"]["eventName"] == "taskFinished" and
        output["fullDocument"]["description"] == "Finish'em" and
        output["fullDocument"]["beginning"].day == datetime.today().day and
        output["fullDocument"]["beginning"].month == datetime.today().month and
        output["fullDocument"]["beginning"].year == datetime.today().year and
        output["fullDocument"]["end"].day == (datetime.today() + timedelta(6)).day and
        output["fullDocument"]["end"].month == (datetime.today() + timedelta(6)).month and
        output["fullDocument"]["end"].year == (datetime.today() + timedelta(6)).year and
        output["fullDocument"]["condition"] == 100 and
        output["fullDocument"]["rewardPoints"] == 0 and
        output["fullDocument"]["rewardItem"] == str(boots_id) and
        output["fullDocument"]["isFinished"] == False and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.groupchallenge.GroupChallengeProjection'):
        print_with_time("Group challenge activated: {}".format('worked'))
    else:
        print_with_time("Group challenge activated: {}".format('failed'))

functions.append(group_challenge_activated)

for count, change in enumerate(db.watch()):
    try:
        functions[count](change)
    except IndexError:
        break