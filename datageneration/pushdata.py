from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import generatedata
import time

uri = "mongodb+srv://siddhu2502:best1234@bigdataproj.ooixpnk.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# show all databases
print(client.list_database_names())

# create new database named networkmetrics
db = client["networkmetrics"]

# creating collection
siddhu = db["siddhu"]


def push_data():
    cpu, memory, disk, network, time_now = generatedata.get_system_metrics()
    data = {"cpu": cpu, "memory": memory, "disk": disk, "network": network, "timestamp":time_now}
    siddhu.insert_one(data)
    print("Data inserted successfully")

# Run the push_data function every second for 10 minutes
end_time = time.time() + 40
while time.time() < end_time:
    push_data()