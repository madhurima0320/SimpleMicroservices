from __future__ import annotations

from typing import Optional, Annotated
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field, StringConstraints

from .person import UNIType

# Course ID format: Department prefix + 4 digits (e.g., CS1234, MATH1001)
CourseIDType = Annotated[str, StringConstraints(pattern=r"^[A-Z]{2,4}\d{4}$")]


class CourseBase(BaseModel):
    course_id: CourseIDType = Field(
        ...,
        description="Course identifier (2-4 uppercase letters + 4 digits).",
        json_schema_extra={"example": "CS1234"},
    )
    name: str = Field(
        ...,
        description="Course name.",
        json_schema_extra={"example": "Introduction to Computer Science"},
    )
    department: str = Field(
        ...,
        description="Academic department offering the course.",
        json_schema_extra={"example": "Computer Science"},
    )
    credits: int = Field(
        ...,
        ge=1,
        le=6,
        description="Number of credit hours (1-6).",
        json_schema_extra={"example": 3},
    )
    description: Optional[str] = Field(
        None,
        description="Course description and learning objectives.",
        json_schema_extra={"example": "An introduction to fundamental concepts in computer science including algorithms, data structures, and programming."},
    )
    instructor_uni: UNIType = Field(
        ...,
        description="UNI of the instructor teaching this course.",
        json_schema_extra={"example": "pr123"},
    )
    semester: str = Field(
        ...,
        description="Academic semester (e.g., Fall 2024, Spring 2025).",
        json_schema_extra={"example": "Fall 2024"},
    )
    max_enrollment: Optional[int] = Field(
        None,
        ge=1,
        description="Maximum number of students that can enroll.",
        json_schema_extra={"example": 30},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "course_id": "CS1234",
                    "name": "Introduction to Computer Science",
                    "department": "Computer Science",
                    "credits": 3,
                    "description": "An introduction to fundamental concepts in computer science including algorithms, data structures, and programming.",
                    "instructor_uni": "pr123",
                    "semester": "Fall 2024",
                    "max_enrollment": 30,
                }
            ]
        }
    }


class CourseCreate(CourseBase):
    """Creation payload for a Course."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "course_id": "MATH1001",
                    "name": "Calculus I",
                    "department": "Mathematics",
                    "credits": 4,
                    "description": "Differential and integral calculus of functions of one variable.",
                    "instructor_uni": "mat456",
                    "semester": "Spring 2025",
                    "max_enrollment": 25,
                }
            ]
        }
    }


class CourseUpdate(BaseModel):
    """Partial update for a Course; supply only fields to change."""
    course_id: Optional[CourseIDType] = Field(
        None, description="Course identifier.", json_schema_extra={"example": "CS1235"}
    )
    name: Optional[str] = Field(None, json_schema_extra={"example": "Advanced Computer Science"})
    department: Optional[str] = Field(None, json_schema_extra={"example": "Computer Science"})
    credits: Optional[int] = Field(None, ge=1, le=6, json_schema_extra={"example": 4})
    description: Optional[str] = Field(None, json_schema_extra={"example": "Advanced topics in computer science."})
    instructor_uni: Optional[UNIType] = Field(None, json_schema_extra={"example": "pr456"})
    semester: Optional[str] = Field(None, json_schema_extra={"example": "Spring 2025"})
    max_enrollment: Optional[int] = Field(None, ge=1, json_schema_extra={"example": 35})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Advanced Computer Science"},
                {"credits": 4},
                {"max_enrollment": 35},
            ]
        }
    }


class CourseRead(CourseBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Course ID.",
        json_schema_extra={"example": "88888888-8888-4888-8888-888888888888"},
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
                    "id": "88888888-8888-4888-8888-888888888888",
                    "course_id": "CS1234",
                    "name": "Introduction to Computer Science",
                    "department": "Computer Science",
                    "credits": 3,
                    "description": "An introduction to fundamental concepts in computer science including algorithms, data structures, and programming.",
                    "instructor_uni": "pr123",
                    "semester": "Fall 2024",
                    "max_enrollment": 30,
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }

