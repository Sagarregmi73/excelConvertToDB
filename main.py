from fastapi import FastAPI
from controllers import data_controller

app = FastAPI(title="Excel/CSV to MongoDB API")
app.include_router(data_controller.router)
