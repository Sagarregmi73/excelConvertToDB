from database import db
from typing import List, Dict

collection = db["records"]

async def insert_many_records(records: List[Dict]):
    return await collection.insert_many(records)

async def get_all_records() -> List[Dict]:
    docs = []
    async for doc in collection.find():
        doc["_id"] = str(doc["_id"])
        docs.append(doc)
    return docs

async def find_records_by_filter(filters: Dict) -> List[Dict]:
    docs = []
    async for doc in collection.find(filters):
        doc["_id"] = str(doc["_id"])
        docs.append(doc)
    return docs
