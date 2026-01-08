from sqlalchemy.orm import Mapped, declarative_base, mapped_column

import analytics.domain.models as domain_models

Base = declarative_base()


class SportTable(Base):
    __tablename__ = "sports"
    name: Mapped[str] = mapped_column(primary_key=True)

    def to_domain(self) -> domain_models.Sport:
        return domain_models.Sport(name=self.name)

    @staticmethod
    def from_domain(sport: domain_models.Sport) -> "SportTable":
        return SportTable(name=sport.name)
