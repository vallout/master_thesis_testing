from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

# connect to edu database and localhost
client = MongoClient("127.0.0.1:27017")
db = client.edu
client.drop_database('edu')

# create ids for reference
# user/avatar ids:
nicks_id = ObjectId('60312e4c8709edadf5dfa0c0')
nicoles_id = ObjectId('60312e4c8709edadf5dfa0c1')
jamals_id = ObjectId('60312e4c8709edadf5dfa0c2')

# project ids:
dogs_project_id = ObjectId('60312e4c8709edadf5dfa0c3')
green_project_id = ObjectId('60312e4c8709edadf5dfa0c4')

# item ids:

nice_trousers_id = ObjectId('60312e4c8709edadf5dfa0c5')
super_shoes_id = ObjectId('60312e4c8709edadf5dfa0c6')
sweet_shirt_id = ObjectId('60312e4c8709edadf5dfa0c7')
unique_shirt_id = ObjectId('60312e4c8709edadf5dfa0c8')
dirty_trousers_id = ObjectId('60312e4c8709edadf5dfa0c9')
high_end_shoes_id = ObjectId('60312e4c8709edadf5dfa0ca')


user_class = 'de.valentin.master.core.user.UserProjection'
projects_class = 'de.valentin.master.core.project.ProjectProjection'
avatar_class = 'de.valentin.master.core.avatar.AvatarProjection'
item_class = "de.valentin.master.core.item.ItemProjection"
task_class = "de.valentin.master.core.task.TaskProjection"
user_challenge_class = 'de.valentin.master.core.userchallenge.UserChallengeProjection'
group_challenge_class = 'de.valentin.master.core.groupchallenge.GroupChallengeProjection'

# create users
initialCollections = {}

initialCollections["users"] = [
        {
            "_id": nicks_id,
            "title": 'Mr.',
            "firstname": 'Nick',
            "lastname": 'Nickolson',
            "primaryMail": 'nick.nickolson@mail.com',
            "projects": [
                str(green_project_id)
            ],
            "_class": user_class
        },
        {
            "_id": nicoles_id,
            "title": 'Mrs.',
            "firstname": 'Nicole',
            "lastname": 'Nicoleson',
            "primaryMail": 'nicole.nicoleson@mail.com',
            "projects": [
                str(dogs_project_id)
            ],
            "_class": user_class
        },
        {
            "_id": jamals_id,
            "title": 'Mrs.',
            "firstname": 'Jamal',
            "lastname": 'Abara',
            "primaryMail": 'jamal.abara@mail.com',
            "projects": [
                str(green_project_id)
            ],
            "_class": user_class
        }
    ]

#create avatars of users
initialCollections["avatars"] = [
        {
            "_id": nicks_id,
            "face": 'MASKULIN',
            "hairColor": 'BLACK',
            "skinColor": '123,231,13',
            "facialExpression": 'HAPPY',
            "points": 1472,
            "avatarItems": {},
            "userItems": [],
            "version": 1,
            "_class": avatar_class
        },
        {
            "_id": nicoles_id,
            "face": 'FEMALE',
            "hairColor": 'BLOND',
            "skinColor": '244,67,54',
            "facialExpression": 'NEUTRAL',
            "points": 200,
            "avatarItems": {},
            "userItems": [],
            "version": 1,
            "_class": avatar_class
        },
        {
            "_id": jamals_id,
            "face": 'NEUTRAL',
            "hairColor": 'BRUNETTE',
            "skinColor": '24,145,80',
            "facialExpression": 'COOL',
            "points": 334,
            "avatarItems": {},
            "userItems": [],
            "version": 1,
            "_class": avatar_class
        },
    ]
#create projects
initialCollections["projects"] = [
        {
            "_id": green_project_id,
            "name": 'Keep Planting',
            "description": 'Join this project to fight climate change',
            "members": [
                nicks_id,
                jamals_id
            ],
            "_class": projects_class
        },
        {
            "_id": dogs_project_id,
            "name": 'Hope for Dogs',
            "description": 'This project is about helping strayed dogs '+
                            'to find a good place and way to live.',
            "members": [
                nicoles_id
            ],
            "_class": projects_class
        }
    ]
# create items

initialCollections["items"] = [
        {
            "_id": nice_trousers_id,
            "itemType":"TROUSERS",
            "name":"Nice trousers",
            "description":"Just nice trousers",
            "modelId":'FB3AUUAXVND4',
            "price":50,
            "_class":item_class
        },
        {
            "_id": super_shoes_id,
            "itemType":"SHOES",
            "name":"Super shoes",
            "description":"These are great shoes",
            "modelId":'W2R1I204PZF4',
            "price":0,
            "_class":item_class
        },
        {
            "_id": sweet_shirt_id,
            "itemType":"SHIRT",
            "name":"Sweet shirt",
            "description":"This shirt is really sweet",
            "modelId":'90UH9K9IKRXZ',
            "price":200,
            "_class":item_class
        },
        {
            "_id":unique_shirt_id,
            "itemType":"SHIRT",
            "name":"Unique shirt",
            "description":"This shirt is unique",
            "modelId":'14SH3Z5RX02I',
            "price":0,
            "_class":item_class
        },
        {
            "_id":high_end_shoes_id,
            "itemType":"SHOES",
            "name":"High-end shoes",
            "description":"Super duper mega shoes",
            "modelId":'BVNVJNQH5MH7',
            "price":5000,
            "_class":item_class
        },
        {
            "_id":dirty_trousers_id,
            "itemType":"TROUSERS",
            "name":"Dirty trousers",
            "description":"These are sprinkled",
            "modelId":'D8MUPMWFE7PK',
            "price":10,
            "_class":item_class
        }
    ]

initialCollections["tasks"] = [
        {
            "_id":ObjectId(),
            "projectId":green_project_id,
            "userId":nicks_id,
            "state":"DOING",
            "name": 'masstige',
            "description": 'Neque modi amet ut aliquam magnam.',
            "deadline": datetime.datetime(2018, 6, 1),
            "likers":[],
            "_class":task_class
        },
        {
            "_id":ObjectId(),
            "projectId":green_project_id,
            "userId":nicks_id,
            "state":"DO",
            "name": 'appropriates',
            "description": 'Amet ut ut amet ut.',
            "deadline":datetime.datetime(2018, 6, 1),
            "likers":[],
            "_class":task_class
        },
        {
            "_id":ObjectId(),
            "projectId":green_project_id,
            "userId":nicks_id,
            "state":"DO",
            "name": 'desloratadine',
            "description": 'Modi quiquia neque labore est etincidunt numquam.',
            "deadline":datetime.datetime(2018, 6, 1),
            "likers":[
                jamals_id
            ],
            "_class":task_class
        },
        {
            "_id":ObjectId(),
            "projectId":green_project_id,
            "userId":jamals_id,
            "state":"FINISHED",
            "name": 'manstress',
            "description": 'Dolore labore dolor dolore quiquia modi sit.',
            "deadline":datetime.datetime(2018, 6, 1),
            "likers":[],
            "_class":task_class
        },
        {
            "_id":ObjectId('6032316c688becd0f8adf9bf'),
            "projectId":green_project_id,
            "userId":nicks_id,
            "state":"FINISHED",
            "name": 'wheatear',
            "description": 'Aliquam ipsum est sed velit.',
            "deadline":datetime.datetime(2018, 6, 1),
            "likers":[
                jamals_id
            ],
            "_class":task_class
        },
    ]

initialCollections["userChallenges"] = [
        {
            "_id": ObjectId("6032316c688becd0f8adf9c0"),
            "event": 'ProjectJoined',
            "queryKeyword": 'byUser',
            "occurencesAsCondition": 1,
            "rewardItem": unique_shirt_id,
            "active": True,
            "_class": user_challenge_class
        },
        {
            "_id": ObjectId("6032316c688becd0f8adf9c1"),
            "event": 'TaskCreated',
            "queryKeyword": 'byUser',
            "occurencesAsCondition": 1,
            "rewardPoints": 20,
            "active": True,
            "_class": user_challenge_class
        },
        {
            "_id": ObjectId("6032316c688becd0f8adf9c2"),
            "event": 'TaskLiked',
            "queryKeyword": 'byCreator',
            "occurencesAsCondition": 3,
            "rewardPoints": 20,
            "active": True,
            "_class": user_challenge_class
        }
    ]

initialCollections["groupChallenges"] = {
        "_id": ObjectId(),
        "isRunning": True,
        "type": 'PLATFORM',
        "eventName": 'TaskFinished',
        "description": 'We need help from all of you! We got an offering, that if ' + 
                        'we finish 100 tasks on this platform until the end of the week, '+
                        'every participant will be richly rewarded.',
        "beginning": datetime.datetime(2021,2,20),
        "end": datetime.datetime(2021,2,27),
        "condition": 100,
        "rewardPoints": 200,
        "_class": group_challenge_class
    }

initialCollections["tasksLiked"] = [
    {
        "_id": ObjectId(),
        "projectId": green_project_id,
        "creatorId": nicks_id,
        "likerId": ObjectId(),
        "timestamp": 1613833993249,
        "_class": 'de.valentin.master.core.events.todoliked.TaskLikedProjection'
    },
    {
        "_id": ObjectId(),
        "projectId": green_project_id,
        "creatorId": nicks_id,
        "likerId": ObjectId(),
        "timestamp": 1613833993248,
        "_class": 'de.valentin.master.core.events.todoliked.TaskLikedProjection'
    }
]

db.userProjection.insert_many(initialCollections["users"])
db.avatarProjection.insert_many(initialCollections["avatars"])
db.projectProjection.insert_many(initialCollections["projects"])
db.itemProjection.insert_many(initialCollections["items"])
db.taskProjection.insert_many(initialCollections["tasks"])
db.userChallengeProjection.insert_many(initialCollections["userChallenges"])
db.groupChallengeProjection.insert_one(initialCollections["groupChallenges"])

db.taskLikedProjection.insert_many(initialCollections["tasksLiked"])
