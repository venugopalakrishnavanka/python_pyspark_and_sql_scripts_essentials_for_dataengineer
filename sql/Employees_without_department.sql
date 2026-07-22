-- This is a single-line comment
SELECT e.*
FROM employee e
LEFT JOIN department d
      ON e.dept_id = d.dept_id
	  WHERE d.dept_id IS NULL;