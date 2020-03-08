from flask_table import Table, Col, NestedTableCol, LinkCol


# class NestedGradeTable(Table):
#     value = Col("")


class CourseTable(Table):
    id = Col("Student id")
    last_name = Col("Last Name")
    first_name = Col("First Name")
    view = LinkCol(
        "View",
        "student_detail",
        url_kwargs=dict(student_id="id"),
        anchor_attrs={"class": "btn btn-dark"},
    )
    # grades = NestedTableCol("Grades", NestedGradeTable)
    classes = ["table table-hover"]
    thead_classes = ["thead-dark"]
    table_id = "course-table"


class StudentTable(Table):
    # value = Col(assignment.assignment_name)
    classes = ["table table-hover"]
    thead_classes = ["thead-dark"]
    table_id = "student-table"
