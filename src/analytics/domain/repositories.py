from typing import List, Protocol

from analytics.domain.models import Sport


class ISportRepository(Protocol):
    async def get_all(self) -> List[Sport]: ...
