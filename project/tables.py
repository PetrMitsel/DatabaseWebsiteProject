from flask_table import Table, Col, NestedTableCol


class NestedGradeTable(Table):
    value = Col("")


class CourseTable(Table):
    id = Col("Student id")
    last_name = Col("Last Name")
    first_name = Col("First Name")
    grades = NestedTableCol("Grades", NestedGradeTable)
    classes = ["table table-hover"]
    thead_classes = ["thead-dark"]
    table_id = "course-table"

