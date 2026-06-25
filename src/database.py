import sqlite3
print("DATABASE FILE LOADED")
def get_filename_by_id(file_id):
    print("DB:", file_id)
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT filename FROM uploads
        WHERE id = ?
        """,
        (file_id,) #notice the comma in line 11
    ) #execute has two parameters seperated by ,
    row = cursor.fetchone()
    conn.close()
    return row