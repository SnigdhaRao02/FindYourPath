from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
import pprint

class DB:

    def __init__(self) -> None:
        self.uri = "mongodb+srv://atharvakale1234:ArJxyOTStetAa4PU@cluster0.6oj8h6f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client =  MongoClient(self.uri,tlsCAFile=certifi.where())
        self.db=None
        self.ping()

    def ping(self):
        try:
            self.client.admin.command('ping')
            self.db=self.client["Cluster0"]
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)


    def add_data(self, document):
        for _,i in document.items():
            if isinstance(document[_],str):
                document[_] = i.lower()
            elif isinstance(document[_],list):
                for j in range(len(document[_])):
                    document[_][j] = document[_][j].lower()
        post_id=self.db["test_collection"].insert_one(document).inserted_id
        print("Document inserted with id: ", post_id)
        return post_id

    # data={'author': author_FN + author_LN, 'title': post_title, 'subtitle': post_subtitle,   }
    # post_id=add_data()
    def add_data2(self):
        document={
            'author':'Challa Sai Charitha',
            'title': 'Blog Post 1',
            'content':'First post',
            'date_posted':'May 22,2024',
            'tags': ['python']
        }
        post_id=self.db["test_collection"].insert_one(document).inserted_id
        print("Document inserted with id: ", post_id)
        return post_id

    def read_data(self):
        data=self.db["test_collection"].find()
        posts=[]
        for post in data:
            pprint.pprint(post)
            posts.append(post)
        return posts
    
    def find_data(self, find):
        for i in range(len(find)):
            find[i] = find[i].lower()
        data=self.db["test_collection"].find({"Category" : {"$in": find}})
        posts=[]
        for post in data:
            # pprint.pprint(post)
            posts.append(post)
        return posts