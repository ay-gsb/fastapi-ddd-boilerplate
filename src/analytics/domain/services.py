from typing import List

import analytics.domain.models as domain_models
import analytics.domain.repositories as domain_repos


class SportService:
    def __init__(self, repo: domain_repos.ISportRepository) -> None:
        self.repo = repo

    async def get_all(self) -> List[domain_models.Sport]:
        return await self.repo.get_all()
