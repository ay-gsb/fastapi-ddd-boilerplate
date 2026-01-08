from datetime import datetime, timezone
from typing import Optional

from attrs import define, field


@define
class TimestampMixin:
    created_at: datetime = field(factory=lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = field(default=None, kw_only=True)
