from typing import List, Dict
from fastapi import UploadFile
from utils.file_parser import parse_file
from repositories import data_repository

async def process_file_upload(file: UploadFile) -> int:
    records = await parse_file(file)
    await data_repository.insert_many_records(records)
    return len(records)

async def fetch_all_records() -> List[Dict]:
    return await data_repository.get_all_records()

async def search_records(filters: Dict) -> List[Dict]:
    return await data_repository.find_records_by_filter(filters)
