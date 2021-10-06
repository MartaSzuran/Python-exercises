# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# # exam_st_date = (11, 12, 2014)
# # Exercise 9

# my solution
exam_st_date = (11, 12, 2014)
print("The examination will start:", exam_st_date[0], "/", exam_st_date[1], "/", exam_st_date[2])

# page solution
print("The examination will start: %i / %i / %i" % exam_st_date)
