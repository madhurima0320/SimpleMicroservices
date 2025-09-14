from __future__ import annotations

from typing import Optional, Annotated
from uuid import UUID, uuid4
from datetime import datetime, date
from pydantic import BaseModel, Field, StringConstraints
from enum import Enum

from .person import UNIType
from .course import CourseIDType


class EnrollmentStatus(str, Enum):
    """Enrollment status enumeration."""
    ACTIVE = "active"
    DROPPED = "dropped"
    COMPLETED = "completed"
    WITHDRAWN = "withdrawn"


class EnrollmentBase(BaseModel):
    student_uni: UNIType = Field(
        ...,
        description="UNI of the student enrolling in the course.",
        json_schema_extra={"example": "abc1234"},
    )
    course_id: CourseIDType = Field(
        ...,
        description="Course identifier the student is enrolling in.",
        json_schema_extra={"example": "CS1234"},
    )
    enrollment_date: date = Field(
        ...,
        description="Date when the student enrolled in the course.",
        json_schema_extra={"example": "2024-08-15"},
    )
    status: EnrollmentStatus = Field(
        default=EnrollmentStatus.ACTIVE,
        description="Current enrollment status.",
        json_schema_extra={"example": "active"},
    )
    grade: Optional[str] = Field(
        None,
        description="Final grade received (A+, A, A-, B+, B, B-, C+, C, C-, D+, D, F, P, NP).",
        json_schema_extra={"example": "A"},
    )
    credits_earned: Optional[int] = Field(
        None,
        ge=0,
        description="Number of credits earned for this enrollment.",
        json_schema_extra={"example": 3},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "student_uni": "abc1234",
                    "course_id": "CS1234",
                    "enrollment_date": "2024-08-15",
                    "status": "active",
                    "grade": None,
                    "credits_earned": None,
                }
            ]
        }
    }


class EnrollmentCreate(EnrollmentBase):
    """Creation payload for an Enrollment."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "student_uni": "xyz789",
                    "course_id": "MATH1001",
                    "enrollment_date": "2024-08-20",
                    "status": "active",
                    "grade": None,
                    "credits_earned": None,
                }
            ]
        }
    }


class EnrollmentUpdate(BaseModel):
    """Partial update for an Enrollment; supply only fields to change."""
    student_uni: Optional[UNIType] = Field(
        None, description="UNI of the student.", json_schema_extra={"example": "abc1235"}
    )
    course_id: Optional[CourseIDType] = Field(
        None, description="Course identifier.", json_schema_extra={"example": "CS1235"}
    )
    enrollment_date: Optional[date] = Field(None, json_schema_extra={"example": "2024-08-16"})
    status: Optional[EnrollmentStatus] = Field(None, json_schema_extra={"example": "completed"})
    grade: Optional[str] = Field(None, json_schema_extra={"example": "A-"})
    credits_earned: Optional[int] = Field(None, ge=0, json_schema_extra={"example": 3})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"status": "completed", "grade": "A"},
                {"status": "dropped"},
                {"grade": "B+", "credits_earned": 3},
            ]
        }
    }


class EnrollmentRead(EnrollmentBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Enrollment ID.",
        json_schema_extra={"example": "77777777-7777-4777-7777-777777777777"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "77777777-7777-4777-7777-777777777777",
                    "student_uni": "abc1234",
                    "course_id": "CS1234",
                    "enrollment_date": "2024-08-15",
                    "status": "active",
                    "grade": None,
                    "credits_earned": None,
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }

