from __future__ import annotations

from functools import total_ordering

from pydantic import BaseModel

from migrate_code.__about__ import __version__
from migrate_code.types import OriginalMigrationFunc, StageId


@total_ordering
class MigrationRecord(BaseModel):
    """The metadata for a migration stage."""

    migration_name: str
    stage_id: StageId
    migrate_code_version: str = __version__

    def __lt__(self, other):
        if not isinstance(other, MigrationRecord):
            raise TypeError(f"Cannot compare MigrationRecord with {type(other)}")
        if self.migration_name != other.migration_name:
            raise RuntimeError("Cannot compare stages from different migrations")
        return self.stage_id < other.stage_id

    def __eq__(self, other):
        if not isinstance(other, MigrationRecord):
            raise TypeError(f"Cannot compare MigrationRecord with {type(other)}")
        if self.migration_name != other.migration_name:
            raise RuntimeError("Cannot compare stages from different migrations")
        return self.stage_id == other.stage_id

    class Config:
        frozen = True


@total_ordering
class MigrationStage(BaseModel):
    description: str
    action: OriginalMigrationFunc
    record: MigrationRecord

    @property
    def id(self) -> StageId:
        return self.record.stage_id

    def __call__(self):
        self.action()

    def __lt__(self, other):
        if not isinstance(other, MigrationStage):
            raise TypeError(f"Cannot compare MigrationStage with {type(other)}")
        return self.record < other.record

    def __eq__(self, other):
        if not isinstance(other, MigrationStage):
            raise TypeError(f"Cannot compare MigrationStage with {type(other)}")
        return self.record == other.record

    class Config:
        fields = {"action": {"exclude": True}}


class LogEntry(BaseModel):
    """The metadata for a log entry."""

    sha: str | None
    is_current_sha: bool
    stage: MigrationStage
    applied: bool

    class Config:
        frozen = True
