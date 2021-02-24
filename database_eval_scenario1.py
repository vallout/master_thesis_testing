from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

db = MongoClient("localhost:27017").edu

functions = []

jamirs_ip = ""
jamirs_id = ""

def print_with_time(input_text):
    now = datetime.now()
    formated_date = "{}:{}:{}:{}".format(now.hour, now.minute, now.second, now.microsecond)
    print("{}: {}".format(formated_date, input_text))

# trigger "Video watched"
def video_watched(output):
    print(output)
    global jamirs_ip
    if (output["operationType"] == "insert" and 
        output["fullDocument"]["points"] == 30 and
        output["fullDocument"]["triggeredEvents"] == ["VideoWatched"] and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.temppoints.TemporaryPointsProjection'):
        jamirs_ip = output["fullDocument"]["_id"]
        print_with_time("Video watched: {}".format('worked'))
    else:
        print_with_time("Video watched: {}".format('failed'))

functions.append(video_watched)

# trigger "StayedOnPage"
def stayed_on_page(output):
    print(output)
    if (output["operationType"] == "replace" and
        output["fullDocument"]["points"] == 50 and
        output["fullDocument"]["triggeredEvents"] == 
            ["VideoWatched", "StayedOnPage"] and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.temppoints.TemporaryPointsProjection'):
        print_with_time("Stayed on page: {}".format('worked'))
    else:
        print_with_time("Stayed on page: {}".format('failed'))

functions.append(stayed_on_page)
# trigger "SpecialRegistration"
def special_registration(output):
    print(output)
    if (output["operationType"] == "replace" and
        output["fullDocument"]["points"] == 100 and
        output["fullDocument"]["triggeredEvents"] == 
            ["VideoWatched", "StayedOnPage", "SpecialRegistration"] and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.temppoints.TemporaryPointsProjection'):
        print_with_time("Special registration button: {}".format('worked'))
    else:
        print_with_time("Special registration button: {}".format('failed'))

functions.append(special_registration)
# create user for Jamir
def create_user_for_jamir(output):
    print(output)
    global jamirs_id
    if (output["operationType"] == "insert" and
        output["fullDocument"]["title"] == "Mr." and
        output["fullDocument"]["firstname"] == "Jamir" and
        output["fullDocument"]["lastname"] == "Gupta" and
        output["fullDocument"]["primaryMail"] == "jamir.gupta@mail.com" and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.user.UserProjection'):
        jamirs_id = output["fullDocument"]["_id"]
        print_with_time("Create user for Jamir: {}".format('worked'))
    else:
        print_with_time("Create user for Jamir: {}".format('failed'))

functions.append(create_user_for_jamir)
# save userRegistered event
def user_registered_event(output):
    print(output)
    global jamirs_id
    if (output["operationType"] == "insert" and
        output["fullDocument"]["userId"] == jamirs_id and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.events.userregistered.UserRegisteredProjection'):
        print_with_time("save userRegistered event: {}".format('worked'))
    else:
        print_with_time("save userRegistered event: {}".format('failed'))

functions.append(user_registered_event)

def init_avatar_of_jamir(output):
    print(output)
    global jamirs_id
    if (output["operationType"] == "insert" and
        output["fullDocument"]["_id"] == jamirs_id and
        output["fullDocument"]["face"] == "NEUTRAL" and
        output["fullDocument"]["hairColor"] == "BRUNETTE" and
        output["fullDocument"]["skinColor"] == "120,120,120" and
        output["fullDocument"]["facialExpression"] == "NEUTRAL" and
        output["fullDocument"]["points"] == 0 and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.avatar.AvatarProjection'):
        print_with_time("init avatar of Jamir: {}".format('worked'))
    else:
        print_with_time("init avatar of Jamir: {}".format('failed'))

functions.append(init_avatar_of_jamir)

def add_tmp_points_to_avatar(output):
    print(output)
    global jamirs_id
    if (output["operationType"] == "replace" and
        output["fullDocument"]["_id"] == jamirs_id and
        output["fullDocument"]["face"] == "NEUTRAL" and
        output["fullDocument"]["hairColor"] == "BRUNETTE" and
        output["fullDocument"]["skinColor"] == "120,120,120" and
        output["fullDocument"]["facialExpression"] == "NEUTRAL" and
        output["fullDocument"]["points"] == 100 and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.avatar.AvatarProjection'):
        print_with_time("add points to avatar from tmpPoints: {}".format('worked'))
    else:
        print_with_time("add points to avatar from tmpPoints: {}".format('failed'))

functions.append(add_tmp_points_to_avatar)

def clear_tmp_points(output):
    print(output)
    global jamirs_ip
    if (output["operationType"] == "delete" and
        output["documentKey"]["_id"] == jamirs_ip):
        print_with_time("delete tmpPoints: {}".format('worked'))
    else:
        print_with_time("delete tmpPoints: {}".format('failed'))

functions.append(clear_tmp_points)

def save_user_logged_in_event(output):
    global jamirs_id
    if (output["operationType"] == "insert" and
        output["fullDocument"]["userId"] == jamirs_id and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.events.userloggedin.UserLoggedInProjection'):
        print_with_time("save userLoggedIn event: {}".format('worked'))
    else:
        print_with_time("save userLoggedIn event: {}".format('failed'))

functions.append(save_user_logged_in_event)

def change_profile_of_jamir(output):
    print(output)
    global jamirs_id
    if (output["operationType"] == "replace" and
        output["fullDocument"]["_id"] == jamirs_id and
        output["fullDocument"]["title"] == "Mr." and
        output["fullDocument"]["firstname"] == "Jamir" and
        output["fullDocument"]["lastname"] == "Gupta" and
        output["fullDocument"]["primaryMail"] == "jamir.gupta@mail.com" and
        output["fullDocument"]["phone"] == "0123456789" and
        output["fullDocument"]["pictureId"] == "some_picture_id" and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.user.UserProjection'):
        print_with_time("Change Jamir's profile: {}".format('worked'))
    else:
        print_with_time("Change Jamir's profile: {}".format('failed'))

functions.append(change_profile_of_jamir)

def change_look_of_avatar(output):
    print(output)
    global jamirs_id
    if (output["operationType"] == "replace" and
        output["fullDocument"]["_id"] == jamirs_id and
        output["fullDocument"]["face"] == "MASKULIN" and
        output["fullDocument"]["hairColor"] == "BLACK" and
        output["fullDocument"]["skinColor"] == "244,67,54" and
        output["fullDocument"]["facialExpression"] == "COOL" and
        output["fullDocument"]["points"] == 100 and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.avatar.AvatarProjection'):
        print_with_time("change look of avatar: {}".format('worked'))
    else:
        print_with_time("change look of avatar: {}".format('failed'))

functions.append(change_look_of_avatar)

def after_bought_item(output):
    print(output)
    global jamirs_id
    if (output["operationType"] == "replace" and
        output["fullDocument"]["_id"] == jamirs_id and
        output["fullDocument"]["face"] == "MASKULIN" and
        output["fullDocument"]["hairColor"] == "BLACK" and
        output["fullDocument"]["skinColor"] == "244,67,54" and
        output["fullDocument"]["facialExpression"] == "COOL" and
        output["fullDocument"]["points"] == 50 and
        output["fullDocument"]["userItems"] == [
            ObjectId('60312e4c8709edadf5dfa0c5')
        ] and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.avatar.AvatarProjection'):
        print_with_time("change avatar after buying item: {}".format('worked'))
    else:
        print_with_time("change avatar after buying item: {}".format('failed'))

functions.append(after_bought_item)

# for some reason handle second update of avatar without changes
def skip(output):
    pass

functions.append(skip)

def after_equipped_trousers(output):
    print(output)
    if (output["operationType"] == "replace" and
        output["fullDocument"]["_id"] == jamirs_id and
        output["fullDocument"]["face"] == "MASKULIN" and
        output["fullDocument"]["hairColor"] == "BLACK" and
        output["fullDocument"]["skinColor"] == "244,67,54" and
        output["fullDocument"]["facialExpression"] == "COOL" and
        output["fullDocument"]["points"] == 50 and
        output["fullDocument"]["userItems"] == 
            [ObjectId('60312e4c8709edadf5dfa0c5')] and
        output["fullDocument"]["avatarItems"] == {
            "TROUSERS": ObjectId('60312e4c8709edadf5dfa0c5')
        } and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.avatar.AvatarProjection'):
        print_with_time("equip trousers: {}".format('worked'))
    else:
        print_with_time("equip trousers: {}".format('failed'))

functions.append(after_equipped_trousers)

def add_jamir_to_project_members(output):
    print(output)
    global jamirs_id
    if (output["operationType"] == "replace" and
        output["fullDocument"]["_id"] == ObjectId('60312e4c8709edadf5dfa0c4') and
        output["fullDocument"]["name"] == "Keep Planting" and
        output["fullDocument"]["description"] == "Join this project to fight climate change" and
        output["fullDocument"]["members"] == [
            ObjectId('60312e4c8709edadf5dfa0c0'), 
            ObjectId('60312e4c8709edadf5dfa0c2'), 
            jamirs_id
        ] and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.project.ProjectProjection'):
        print_with_time("add Jamir to project members: {}".format('worked'))
    else:
        print_with_time("add Jamir to project members: {}".format('failed'))

functions.append(add_jamir_to_project_members)

def add_project_to_jamir(output):
    print(output)
    if (output["operationType"] == "replace" and
        output["fullDocument"]["title"] == "Mr." and
        output["fullDocument"]["firstname"] == "Jamir" and
        output["fullDocument"]["lastname"] == "Gupta" and
        output["fullDocument"]["primaryMail"] == "jamir.gupta@mail.com" and
        output["fullDocument"]["phone"] == "0123456789" and
        output["fullDocument"]["pictureId"] == "some_picture_id" and
        output["fullDocument"]["projects"] == [
            "60312e4c8709edadf5dfa0c4"
        ] and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.user.UserProjection'):
        print_with_time("add project to Jamir: {}".format('worked'))
    else:
        print_with_time("add project to Jamir: {}".format('failed'))

functions.append(add_project_to_jamir)

def save_project_joined_event(output):
    print(output)
    if (output["operationType"] == "insert" and
        output["fullDocument"]["userId"] == jamirs_id and
        output["fullDocument"]["projectId"] == ObjectId('60312e4c8709edadf5dfa0c4') and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.events.projectjoined.ProjectJoinedProjection'):
        print_with_time("save projectJoined event: {}".format('worked'))
    else:
        print_with_time("save projectJoined event: {}".format('failed'))

functions.append(save_project_joined_event)

def reward_item_to_jamirs_avatar(output):
    print(output)
    if (output["operationType"] == "replace" and
        output["fullDocument"]["_id"] == jamirs_id and
        output["fullDocument"]["face"] == "MASKULIN" and
        output["fullDocument"]["hairColor"] == "BLACK" and
        output["fullDocument"]["skinColor"] == "244,67,54" and
        output["fullDocument"]["facialExpression"] == "COOL" and
        output["fullDocument"]["points"] == 50 and
        output["fullDocument"]["userItems"] == [
            ObjectId('60312e4c8709edadf5dfa0c5'),
            ObjectId('60312e4c8709edadf5dfa0c8')
        ] and
        output["fullDocument"]["avatarItems"] == {
            "TROUSERS": ObjectId('60312e4c8709edadf5dfa0c5')
        } and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.avatar.AvatarProjection'):
        print_with_time("reward item to Jamirs avatar: {}".format('worked'))
    else:
        print_with_time("reward item to Jamirs avatar: {}".format('failed'))

functions.append(reward_item_to_jamirs_avatar)

def save_reward_gained_event1(output):
    print(output)
    if (output["operationType"] == "insert" and
        output["fullDocument"]["userId"] == jamirs_id and
        output["fullDocument"]["challengeId"] == ObjectId('6032316c688becd0f8adf9c0') and
        output["fullDocument"]["_class"] ==
            'de.valentin.master.core.events.rewardgained.RewardGainedProjection'):
        print_with_time("save rewardGained event 1: {}".format('worked'))
    else:
        print_with_time("save rewardGained event 1: {}".format('failed'))

functions.append(save_reward_gained_event1)

def add_like_to_task(output):
    print(output)
    if (output["operationType"] == "replace" and
        output["fullDocument"]["userId"] == ObjectId('60312e4c8709edadf5dfa0c0') and
        output["fullDocument"]["projectId"] == ObjectId('60312e4c8709edadf5dfa0c4') and
        output["fullDocument"]["state"] == "FINISHED" and
        output["fullDocument"]["name"] == "wheatear" and
        output["fullDocument"]["description"] == "Aliquam ipsum est sed velit." and
        output["fullDocument"]["likers"] == [
            ObjectId('60312e4c8709edadf5dfa0c2'), 
            jamirs_id
        ] and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.task.TaskProjection'):
        print_with_time("add like to task: {}".format('worked'))
    else:
        print_with_time("add like to task: {}".format('failed'))

functions.append(add_like_to_task)

def save_task_liked_event(output):
    print(output)
    if (output["operationType"] == "insert" and
        output["fullDocument"]["creatorId"] == ObjectId('60312e4c8709edadf5dfa0c0') and
        output["fullDocument"]["projectId"] == ObjectId('60312e4c8709edadf5dfa0c4') and
        output["fullDocument"]["likerId"] == jamirs_id and
        output["fullDocument"] ["_class"] == 
            'de.valentin.master.core.events.taskliked.TaskLikedProjection'):
        print_with_time("save taskLiked event: {}".format('worked'))
    else:
        print_with_time("save taskLiked event: {}".format('failed'))

functions.append(save_task_liked_event)

def reward_points_to_nicks_avatar(output):
    print(output)
    if (output["operationType"] == "replace" and
        output["fullDocument"]["_id"] == ObjectId('60312e4c8709edadf5dfa0c0') and
        output["fullDocument"]["face"] == "MASKULIN" and
        output["fullDocument"]["hairColor"] == "BLACK" and
        output["fullDocument"]["skinColor"] == "123,231,13" and
        output["fullDocument"]["facialExpression"] == "HAPPY" and
        output["fullDocument"]["points"] == 1492 and
        output["fullDocument"]["userItems"] == [] and
        output["fullDocument"]["avatarItems"] == {} and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.avatar.AvatarProjection'):
        print_with_time("reward points to nicks avatar: {}".format('worked'))
    else:
        print_with_time("reward points to nicks avatar: {}".format('failed'))

functions.append(reward_points_to_nicks_avatar)

def save_reward_gained_event2(output):
    print(output)
    if (output["operationType"] == "insert" and
        output["fullDocument"]["challengeId"] == ObjectId('6032316c688becd0f8adf9c2') and
        output["fullDocument"]["userId"] == ObjectId('60312e4c8709edadf5dfa0c0') and
        output["fullDocument"] ["_class"] == 
            'de.valentin.master.core.events.rewardgained.RewardGainedProjection'):
        print_with_time("save rewardGained event 2: {}".format('worked'))
    else:
        print_with_time("save rewardGained event 2: {}".format('failed'))

functions.append(save_reward_gained_event2)

def create_jamirs_task(output):
    print(output)
    if (output["operationType"] == "insert" and
        output["fullDocument"]["userId"] == jamirs_id and
        output["fullDocument"]["projectId"] == ObjectId('60312e4c8709edadf5dfa0c4') and
        output["fullDocument"]["state"] == "DO" and
        output["fullDocument"]["name"] == "Jamir's task" and
        output["fullDocument"]["description"] == "My first task" and
        output["fullDocument"]["deadline"] == datetime(2021, 2, 21, 23, 0) and
        output["fullDocument"]["likers"] == [] and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.task.TaskProjection'):
        print_with_time("create jamirs task: {}".format('worked'))
    else:
        print_with_time("create jamirs task: {}".format('failed'))

functions.append(create_jamirs_task)

def save_task_created_event(output):
    print(output)
    if (output["operationType"] == "insert" and
        output["fullDocument"]["userId"] == jamirs_id and
        output["fullDocument"]["projectId"] == ObjectId('60312e4c8709edadf5dfa0c4') and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.events.taskcreated.TaskCreatedProjection'):
        print_with_time("save taskCreated event: {}".format('worked'))
    else:
        print_with_time("save taskCreated event: {}".format('failed'))

functions.append(save_task_created_event)

def reward_points_to_jamirs_avatar(output):
    print(output)
    if (output["operationType"] == "replace" and
        output["fullDocument"]["_id"] == jamirs_id and
        output["fullDocument"]["face"] == "MASKULIN" and
        output["fullDocument"]["hairColor"] == "BLACK" and
        output["fullDocument"]["skinColor"] == "244,67,54" and
        output["fullDocument"]["facialExpression"] == "COOL" and
        output["fullDocument"]["points"] == 70 and
        output["fullDocument"]["userItems"] == [
            ObjectId('60312e4c8709edadf5dfa0c5'),
            ObjectId('60312e4c8709edadf5dfa0c8')
        ] and
        output["fullDocument"]["avatarItems"] == {
            "TROUSERS": ObjectId('60312e4c8709edadf5dfa0c5')
        } and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.avatar.AvatarProjection'):
        print_with_time("reward points to Jamirs avatar: {}".format('worked'))
    else:
        print_with_time("reward points to Jamirs avatar: {}".format('failed'))

functions.append(reward_points_to_jamirs_avatar)

def save_reward_gained_event3(output):
    print(output)
    if (output["operationType"] == "insert" and
        output["fullDocument"]["userId"] == jamirs_id and
        output["fullDocument"]["challengeId"] == ObjectId('6032316c688becd0f8adf9c1') and
        output["fullDocument"]["_class"] == 
            'de.valentin.master.core.events.rewardgained.RewardGainedProjection'):
        print_with_time("save rewardGained event 3: {}".format('worked'))
    else:
        print_with_time("save rewardGained event 3: {}".format('failed'))

functions.append(save_reward_gained_event3)

for count, change in enumerate(db.watch()):
    try:
        functions[count](change)
    except IndexError:
        break