import formatter

if __name__ == "__main__":
    text = """
# comment
-- comment
// comment
/* comment */
/*
comment
*/
/*

comment

*/

DEFINE TABLE user SCHEMAFULL;
DEFINE TABLE user SCHEMALESS PERMISSIONS FOR select, create, update, delete NONE; 
DEFINE TABLE user SCHEMALESS PERMISSIONS NONE;
DEFINE TABLE user SCHEMALESS PERMISSIONS FOR select WHERE id = $auth.id OR admin = true, FOR create, update, delete NONE;
# fields
DEFINE FIELD creditors ON user TYPE array;
SELECT * FROM user;
SELECT * FROM account;
"""
    formatter.parse(text)
