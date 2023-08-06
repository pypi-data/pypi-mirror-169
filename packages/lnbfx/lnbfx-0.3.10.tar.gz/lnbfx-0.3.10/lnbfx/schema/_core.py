from typing import Optional

# import lnschema_core  # noqa
from sqlmodel import Field, ForeignKeyConstraint, SQLModel

from . import id as idg


class bfx_pipeline(SQLModel, table=True):  # type: ignore
    """Bioinformatics pipeline metadata."""

    __table_args__ = (
        ForeignKeyConstraint(
            ["id", "v"],
            ["pipeline.id", "pipeline.v"],
            name="bfx_pipeline_pipeline",
        ),
    )
    id: str = Field(primary_key=True, index=True)
    v: str = Field(primary_key=True, index=True)


class bfx_run(SQLModel, table=True):  # type: ignore
    """Bioinformatics pipeline run metadata."""

    __table_args__ = (
        ForeignKeyConstraint(
            ["bfx_pipeline_id", "bfx_pipeline_v"],
            ["bfx_pipeline.id", "bfx_pipeline.v"],
            name="bfx_run_bfx_pipeline",
        ),
    )
    id: str = Field(primary_key=True, foreign_key="pipeline_run.id", index=True)
    dir: Optional[str] = None
    bfx_pipeline_id: str = Field(index=True)
    bfx_pipeline_v: str = Field(index=True)


class bfxmeta(SQLModel, table=True):  # type: ignore
    """Metadata for files associated with bioinformatics pipelines."""

    id: Optional[str] = Field(default_factory=idg.bfxmeta, primary_key=True)
    file_type: Optional[str] = None
    dir: Optional[str] = None


class dobject_bfxmeta(SQLModel, table=True):  # type: ignore
    """Link table between dobject and bfxmeta tables."""

    __table_args__ = (
        ForeignKeyConstraint(
            ["dobject_id", "dobject_v"],
            ["dobject.id", "dobject.v"],
            name="dobject_bfxmeta_dobject",
        ),
    )
    dobject_id: str = Field(primary_key=True, index=True)
    dobject_v: str = Field(primary_key=True, index=True)
    bfxmeta_id: str = Field(primary_key=True, foreign_key="bfxmeta.id", index=True)
