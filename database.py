from azure.cosmos import CosmosClient,PartitionKey
import os
from dotenv import load_dotenv
from models import Record

load_dotenv()
class Database:
    def __init__(self):
        self.endpoint = os.environ.get("AZURE_ENDPOINT")
        self.key = os.environ.get("AZURE_KEY")

    def container(self,database_name,container_name):
        client = CosmosClient(self.endpoint,self.key)
        database = client.create_database_if_not_exists(id=database_name)
        container = database.create_container_if_not_exists(id=container_name,partition_key=PartitionKey(path="/id"))
        return container

    def create_record(self,container,record):
        container.create_item(record)
        print(f"Record created: {record}")

    def get_all_records(self,container):
        records = container.query_items(
            query="SELECT * FROM c",
            enable_cross_partition_query=True
        )
        return records

    def get_record(self,container,id):
        record = container.read_item(item=id, partition_key=id)
        print(f"Record retrieved: {record}")

    def update_record(self,container,record):
        container.upsert_item(record)
        print(f"Record updated: {record}")

    def delete_record(self,container,id):
        container.delete_item(item=id, partition_key=id)
        print(f"Record deleted: {id}")

def main():
    db = Database()
    container = db.container("budget_db","records")
    data = db.delete_record(
        container,
        "c13e20a8-0edc-4821-857e-f406028e5853",)
    print(data)

if __name__ == "__main__":
    main()
