from fastapi import APIRouter, HTTPException
from app.models.request_models import AdditionRequest
from app.models.response_models import AdditionResponse
from app.controllers.addition_controller import process_addition_request

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    try:
        response, status, started_at, completed_at = process_addition_request(request.payload)
        return AdditionResponse(
            batchid=request.batchid,
            response=response,
            status=status,
            started_at=started_at,
            completed_at=completed_at
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
