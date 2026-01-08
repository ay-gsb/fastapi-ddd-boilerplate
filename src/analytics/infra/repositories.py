from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import analytics.domain.models as domain_models
import analytics.infra.orm as orm_models


class SportTableRepo:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self) -> List[domain_models.Sport]:
        result = await self.session.execute(select(orm_models.SportTable))
        return [row.to_domain() for row in result.scalars()]
