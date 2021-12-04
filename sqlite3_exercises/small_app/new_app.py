import database

# add record to the database
# database.add_one("janusz", 70)


# delete one record
# need to use quotes
# database.delete_one("3")

# create list
score_list = [
    ("wiola", 100),
    ("adam", 50),
]
# add list into database
# database.add_many(score_list)

# search for score with where
database.look_up("adam")

# print all records from db
# database.show_all()
