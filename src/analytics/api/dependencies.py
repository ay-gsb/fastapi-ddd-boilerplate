from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

import analytics.domain.services as domain_services
import analytics.infra.repositories as infra_repos
from analytics.infra.db import get_db


async def get_sport_service(session: AsyncSession = Depends(get_db)):
    repo = infra_repos.SportTableRepo(session)

    return domain_services.SportService(repo)
