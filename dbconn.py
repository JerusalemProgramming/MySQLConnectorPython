## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES

import dbmod

## END IMPORT MODULES
## END IMPORT MODULES
## END IMPORT MODULES

## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM

## DECLARE PYTHON VARIABLES
NameHost = "localhost"
NameUser = "root"
PasswordUser = ""
NameDB = "test15"
NameDBTable = "emails"

## BEGIN CALL FUNCTION - OPEN CSV FILE
StringOfHeaders, ListOfHeaders, ListOfTuples = dbmod.fn_OpenFileCSV()

## BEGIN CALL FUNCTION - CREATE DB SERVER CONNECTION
cnx = dbmod.fn_CreateDBServerConnection(NameHost, NameUser, PasswordUser)

## DECLARE SQL-QUERY VARIABLE FOR SQL QUERY - CREATE DATABASE (DB)
QueryCreateDB = "CREATE DATABASE " + NameDB + ";"

## BEGIN CALL FUNCTION - QUERY DB:  CREATE DATABASE (DB)
cur = dbmod.fn_QueryDB(cnx, QueryCreateDB)

## DECLARE SQL-QUERY VARIABLE FOR SQL QUERY - CHOOSE DATABASE (DB) TO USE
QueryUseDB = "USE " + NameDB + ";"

## BEGIN CALL FUNCTION - QUERY DB:  USE DATABASE (DB)
cur = dbmod.fn_QueryDB(cnx, QueryUseDB)

## DECLARE SQL-QUERY VARIABLE FOR SQL QUERY - CREATE DATABASE (DB) TABLE
QueryCreateDBTable = """
CREATE TABLE """ + NameDBTable + """(id INT AUTO_INCREMENT PRIMARY KEY,
EmailAddress VARCHAR(255),
NameLast VARCHAR(255),
NameFirst VARCHAR(255)
);
"""
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																							
## BEGIN CALL FUNCTION - QUERY DB:  CREATE DATABASE (DB) TABLE
cur = dbmod.fn_QueryDB(cnx, QueryCreateDBTable)

## BEGIN CALL FUNCTION - LOOP QUERY DB:  LOOP MULTIPLE INSERTS OF SINGLE VALUES INTO DATABASE (DB) TABLE
cur = dbmod.fn_LoopQuery_InsertIntoDBTable(cnx, NameDBTable, StringOfHeaders, ListOfHeaders, ListOfTuples)

## DECLARE SQL-QUERY VARIABLE FOR SQL QUERY - TRUNCATE DATABASE (DB) TABLE
QueryTruncateDBTable = "TRUNCATE TABLE " + NameDBTable + ";"
## cur = dbmod.fn_QueryDB(cnx, QueryTruncateDBTable) ## COMMAND REQUIRED TO TRUNCATE DB TABLE FROM CLI

## DECLARE SQL-QUERY VARIABLE FOR SQL QUERY - DROP DATABASE (DB) TABLE
QueryDropDBTable = "DROP TABLE " + NameDBTable + ";"
## cur = dbmod.fn_QueryDB(cnx, QueryDropDBTable) ## COMMAND REQUIRED TO DROP DB TABLE FROM CLI

## DECLARE SQL-QUERY VARIABLE FOR SQL QUERY - DROP DATABASE (DB)
QueryDropDB = "DROP DATABASE " + NameDB + ";"
## cur = dbmod.fn_QueryDB(cnx, QueryDropDB) ## COMMAND REQUIRED TO DROP DB FROM CLI

## END MAIN PROGRAM
## END MAIN PROGRAM
## END MAIN PROGRAM

## GAME OVER
## GAME OVER
## GAME OVER
