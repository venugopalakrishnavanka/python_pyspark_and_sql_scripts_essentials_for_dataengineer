""" Find Employees without department - Create dataframe, department and employee """
from pyspark.sql import function as F
merged = employee_df.join(department_df,"dept_id","left")
employee_without_dept = merged.filter(F.col("dept_id").isNull())
employee_without_dept.show()
