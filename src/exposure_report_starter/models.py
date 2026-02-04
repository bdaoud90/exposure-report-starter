from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Finding(BaseModel):
    title: str
    description: str
    impact: Optional[str] = None
    likelihood: Optional[str] = None


class RiskRating(BaseModel):
    label: str
    score: str
    rationale: Optional[str] = None


class Recommendation(BaseModel):
    title: str
    description: str
    owner: Optional[str] = None
    target_date: Optional[str] = Field(default=None, description="Target completion date")


class ReportInput(BaseModel):
    report_title: str = Field(default="Exposure Report")
    organization: str = Field(default="Organization")
    prepared_for: Optional[str] = None
    prepared_by: Optional[str] = None
    report_date: Optional[str] = None
    executive_summary: str
    scope: str
    methodology: str
    findings: List[Finding] = Field(default_factory=list)
    risk_ratings: List[RiskRating] = Field(default_factory=list)
    recommendations: List[Recommendation] = Field(default_factory=list)
    appendix: Optional[str] = None
    data_sources: List[str] = Field(default_factory=list)
