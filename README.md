 **Defined Goal:**
1.	Clone Professor Ferguson’s Simple Microservices Repository.
2.	Create a project that is my version using two different resources.
   
a.	Copy the structure of Professor Ferguson’s repository

b.	Define two models.

c.	Implement “API first” definition by implementing placeholder routes for each resource:

    i.	GET /<resource>
    ii.	POST /<resource>
    iii.GET /<resource>/{id}
    iv.	PUT /<resource>/{id}
    v.	DELETE /<resource>/{id}

d.	Annotate models and paths to autogenerate OpenAPI document.

e.	Tested OpenAPI document dispatching to methods.
  Outcome: Achieved


**Notes:**

1) Created Two New Models
Course Model: University courses with fields like course_id, name, department, credits, instructor_uni
Enrollment Model: Student enrollments linking student_uni to course_id with status, grades, and dates

2) Built Complete REST API
Full CRUD Operations: POST, GET, PATCH, PUT, DELETE for both resources
Advanced Filtering: Query parameters for searching/filtering data
Proper Validation: Pydantic models with field constraints and patterns
Error Handling: 404, 422 responses with meaningful messages

3) Tested & Working
All endpoints tested with curl commands
Complete CRUD lifecycle verified
Result: A fully functional University Management API with Course and Enrollment resources!
