from typing import List

from fastapi import APIRouter, Depends

import analytics.api.dependencies as deps
import analytics.api.schemas as schemas
import analytics.domain.services as domain_services

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Analytics API is running."}


@router.get("/health")
async def health_check():
    return {"status": "healthy"}


@router.get("/sports", response_model=List[schemas.Sport])
async def get_sports(
    srv: domain_services.SportService = Depends(deps.get_sport_service),
):
    return await srv.get_all()
