from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

client = MongoClient("127.0.0.1:27017")
db = client.edu
client.drop_database('edu')

initialCollections = {}

projectId = ObjectId("60224f1aa5d8b00b85c1fc41")
userId_1 = ObjectId("601bfef20104521f0f59e7c7")
jamals_id = ObjectId('60312e4c8709edadf5dfa0c2')

challengeId_1 = ObjectId("602267b6a5d8b00b85c1fc5a")
challengeId_2 = ObjectId("6022c3bb6dbc4429e5f04bbb")
challengeId_3 = ObjectId("6022c60531d93477de434681")

unique_shirt_id = ObjectId("60312e4c8709edadf5dfa0c8")

user_class = 'de.valentin.master.core.user.UserProjection'
avatar_class = 'de.valentin.master.core.avatar.AvatarProjection'
task_liked_class = "de.valentin.master.core.events.taskliked.TaskLikedProjection"
task_finished_class = "de.valentin.master.core.events.taskfinished.TaskFinishedProjection"
task_created_class = "de.valentin.master.core.events.taskcreated.TaskCreatedProjection"
project_joined_class = "de.valentin.master.core.events.projectjoined.ProjectJoinedProjection"
project_created_class = "de.valentin.master.core.events.projectcreated.ProjectCreatedProjection"
user_loggedin_class = "de.valentin.master.core.events.userloggedin.UserLoggedInProjection"
user_registered_class = "de.valentin.master.core.events.userregistered.UserRegisteredProjection"
item_class = "de.valentin.master.core.item.ItemProjection"
user_challenge_class = 'de.valentin.master.core.userchallenge.UserChallengeProjection'
group_challenge_class = 'de.valentin.master.core.groupchallenge.GroupChallengeProjection'


initialCollections["users"] = {
    "_id": jamals_id,
    "title": 'Mrs.',
    "firstname": 'Jamal',
    "lastname": 'Abara',
    "primaryMail": 'jamal.abara@mail.com',
    "projects": [],
    "_class": user_class
}
initialCollections["avatars"] = {
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
}

initialCollections["taskLiked"] = [
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1612257756000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1612257756000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1612257756000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1612257756000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1611652956000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1611652956000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1611652956000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1611652956000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1611652956000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1611652956000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1611048156000,
      "_class":task_liked_class
   },
   {
      "_id": ObjectId(),
      "projectId": projectId,
      "creatorId": userId_1,
      "likerId": userId_1,
      "timestamp":1611048156000,
      "_class":task_liked_class
   }
]

initialCollections["taskFinished"] = [
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": task_finished_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": task_finished_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": task_finished_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611652956000,
      "_class": task_finished_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611652956000,
      "_class": task_finished_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611048156000,
      "_class": task_finished_class
   }
]

initialCollections["taskCreated"] = [
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611652956000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611652956000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611652956000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611048156000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611048156000,
      "_class": task_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611048156000,
      "_class": task_created_class
   }
]

initialCollections["rewardGained"] = [
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId": challengeId_1,
      "type":"UserChallenge",
      "timestamp":1612257756000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId": challengeId_2,
      "type":"UserChallenge",
      "timestamp":1611651730000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId": challengeId_3,
      "type":"UserChallenge",
      "timestamp":1612257756000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId": challengeId_1,
      "type":"UserChallenge",
      "timestamp":1612257756000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId": challengeId_1,
      "type":"UserChallenge",
      "timestamp":1611045055000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId": challengeId_1,
      "type":"UserChallenge",
      "timestamp":1611045055000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId": challengeId_1,
      "type":"UserChallenge",
      "timestamp":1611649855000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId": challengeId_1,
      "type":"UserChallenge",
      "timestamp":1611649855000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId":challengeId_1,
      "type":"UserChallenge",
      "timestamp":1611649855000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId": challengeId_3,
      "type":"UserChallenge",
      "timestamp":1611651730000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId": challengeId_3,
      "type":"UserChallenge",
      "timestamp":1611651730000
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "challengeId":challengeId_3,
      "type":"UserChallenge",
      "timestamp":1611651730000
   }
]

initialCollections["projectJoined"] = [
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": project_joined_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": project_joined_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class": project_joined_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "projectId": projectId,
      "timestamp":1611652956000,
      "_class": project_joined_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "projectId": projectId,
      "timestamp":1611652956000,
      "_class": project_joined_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "projectId": projectId,
      "timestamp":1611652956000,
      "_class": project_joined_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "projectId": projectId,
      "timestamp":1611048156000,
      "_class": project_joined_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "projectId": projectId,
      "timestamp":1611048156000,
      "_class": project_joined_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "projectId": projectId,
      "timestamp":1612888744528,
      "_class": project_joined_class
   }
]

initialCollections["projectCreated"] = [
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611048156000,
      "_class":project_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611652956000,
      "_class":project_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611048156000,
      "_class":project_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1611048156000,
      "_class":project_created_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "projectId": projectId,
      "timestamp":1612257756000,
      "_class":project_created_class
   }
]

initialCollections["userRegistered"] = [
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "timestamp":1612257756000,
      "_class": user_registered_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "timestamp":1611652956000,
      "_class": user_registered_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "timestamp":1611652956000,
      "_class": user_registered_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "timestamp":1611048156000,
      "_class": user_registered_class
   },
   {
      "_id": ObjectId(),
      "userId": ObjectId(),
      "timestamp":1611048156000,
      "_class": user_registered_class
   }
]

initialCollections["userLoggedIn"] = [
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1612257756000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1612257756000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1612257756000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1612257756000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1612257756000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1612257756000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1612257756000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1611652956000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1611652956000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1611652956000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1611652956000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1611652956000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1611048156000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1611048156000,
      "_class": user_loggedin_class
   },
   {
      "_id": ObjectId(),
      "userId": userId_1,
      "timestamp":1611048156000,
      "_class": user_loggedin_class
   }
]

initialCollections["items"] = [
    {
        "_id":unique_shirt_id,
        "itemType":"SHIRT",
        "name":"Unique shirt",
        "description":"This shirt is unique",
        "modelId":'14SH3Z5RX02I',
        "price":0,
        "_class":item_class
    }
]


initialCollections["userChallenges"] = [
    {
        "_id": challengeId_1,
        "event": 'ProjectJoined',
        "queryKeyword": 'byUser',
        "occurencesAsCondition": 1,
        "rewardItem": unique_shirt_id,
        "active": True,
        "_class": user_challenge_class
    },
    {
        "_id": challengeId_3,
        "event": 'TaskCreated',
        "queryKeyword": 'byUser',
        "occurencesAsCondition": 1,
        "rewardPoints": 20,
        "active": True,
        "_class": user_challenge_class
    },
    {
        "_id": challengeId_2,
        "event": 'TaskFinished',
        "queryKeyword": 'byUserAndTime',
        "beginning": datetime.datetime(2021,1,20),
        "end": datetime.datetime(2021,1,27),
        "occurencesAsCondition": 5,
        "rewardPoints": 20,
        "active": True,
        "_class": user_challenge_class
    }
]

initialCollections["groupChallenges"] = [
    {
        "_id": ObjectId(),
        "isRunning": False,
        "type": 'PLATFORM',
        "eventName": 'UserLoggedIn',
        "description": 'Login, come on',
        "end": datetime.datetime(2021,2,3),
        "condition": 3,
        "rewardPoints": 200,
        "isFinished": True,
        "_class": group_challenge_class
    }
]

db.userProjection.insert_one(initialCollections["users"])
db.avatarProjection.insert_one(initialCollections["avatars"])
db.taskLikedProjection.insert_many(initialCollections["taskLiked"])
db.taskFinishedProjection.insert_many(initialCollections["taskFinished"])
db.taskCreatedProjection.insert_many(initialCollections["taskCreated"])
db.projectJoinedProjection.insert_many(initialCollections["projectJoined"])
db.projectCreatedProjection.insert_many(initialCollections["projectCreated"])
db.userRegisteredProjection.insert_many(initialCollections["userRegistered"])
db.userLoggedInProjection.insert_many(initialCollections["userLoggedIn"])
db.rewardGainedProjection.insert_many(initialCollections["rewardGained"])

db.itemProjection.insert_many(initialCollections["items"])

db.userChallengeProjection.insert_many(initialCollections["userChallenges"])
db.groupChallengeProjection.insert_many(initialCollections["groupChallenges"])