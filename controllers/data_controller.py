from fastapi import APIRouter, UploadFile, File, Query
from fastapi.responses import JSONResponse
from typing import Optional, List
from schemas import RecordSchema
from services import data_service

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    count = await data_service.process_file_upload(file)
    return {"message": f"{count} records inserted successfully."}

@router.get("/records/", response_model=List[RecordSchema])
async def get_all():
    return await data_service.fetch_all_records()

@router.get("/search/", response_model=List[RecordSchema])
async def search(
    part_number: Optional[str] = None,
    year: Optional[int] = None,
    category: Optional[str] = None,
    model: Optional[str] = None,
    vehicle_type: Optional[str] = None,
    color: Optional[str] = None,
    stock: Optional[int] = None
):
    filters = {}
    if part_number: filters["part_number"] = part_number
    if year: filters["year"] = year
    if category: filters["category"] = category
    if model: filters["model"] = model
    if vehicle_type: filters["vehicle_type"] = vehicle_type
    if color: filters["color"] = color
    if stock: filters["stock"] = stock

    return await data_service.search_records(filters)
