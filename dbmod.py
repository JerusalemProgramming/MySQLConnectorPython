## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES

import csv
import mysql.connector
from mysql.connector import Error

## END IMPORT MODULES
## END IMPORT MODULES
## END IMPORT MODULES

## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTIONS

## BEGIN DEFINE FUNCTION
def fn_OpenFileCSV():
    
    ## WHILE CSV FILE IS OPEN...
    with open('TEST_DB_EMAILS.csv') as csv_file:
    
        ## READ FILE INTO CSV_READER OBJECT
        csv_reader = csv.reader(csv_file, delimiter=';')
    
        ## DECLARE VARIABLE FOR COUNTER
        LineCount = 0
    
        ## DECLARE VARIABLE FOR EMPTY LIST
        ListOfTuples = []
    
        ## BEGIN FOR LOOP:  FOR EACH ROW IN CSV_READER OBJECT
        for row in csv_reader:
            
            if LineCount == 0:
                
                #print(row, type(row)) ## LIST OF STRINGS
                StringOfHeaders = f'{", ".join(row)}'
                ## print(StringOfHeaders)
                
                ## LIST OF STRINGS (HEADERS)
                ListOfStrings = row
            
                ## INCREMENT COUNTER
                LineCount += 1
                
            else:
                
                ## print(row)
                
                ## DECLARE VARIABLE FOR EMPTY LIST
                values = []
    
                ## BEGIN FOR LOOP
                for each in row:
    
                    values.append(each)
                
                ## END FOR LOOP
                
                ## CONVERT LIST TO IMMUTABLE TUPLE
                t = tuple(values)
                
                ## APPEND TUPLE TO LIST OF TUPLES
                ListOfTuples.append(t)
    
                ## INCREMENT COUNTER    
                LineCount += 1
                  
        ## END FOR LOOP:  FOR EACH ROW IN CSV_READER OBJECT
                     
        print(f'Processed {LineCount} lines in CSV File.')

        ## RETURN()
        return(StringOfHeaders, ListOfStrings, ListOfTuples) ## StringOfHeaders = 1 (one) string of headers; ListOfStrings = ListOfHeaders; ListOfTuples = DATA OF EACH ROW
           
## END DEFINE FUNCTION
        

## BEGIN DEFINE FUNCTION
def fn_CreateDBServerConnection(NameHost, NameUser, PasswordUser):

    ## CONNECTION
    cnx = None

    ## TRY:
    try:
        
        cnx = mysql.connector.connect(
        host=NameHost,
        user=NameUser,
        password=PasswordUser)

        DBServerInfo = cnx.get_server_info()
            
        print("Connection to MySQL DB SERVER successful")
        print("Connected to MySQL Server version", DBServerInfo)

    ## EXCEPT:
    except Error as e:
        print(f"The error '{e}' occurred")

    ## RETURN()
    return(cnx)

## END DEFINE FUNCTION
    

## BEGIN DEFINE FUNCTION
def fn_QueryDB(cnx, query, values=None):

    ## CURSOR
    cur = cnx.cursor()

    ## TRY:
    try:
        cur.execute(query, values)
        print("Query", query, "with values =", values, "executed successfully")

    ## EXCEPT:
    except Error as e:
        print(f"The error '{e}' occurred")

    ## RETURN()
    return(cur)

## END DEFINE FUNCTION
    

## BEGIN DEFINE FUNCTION
def fn_LoopQuery_InsertIntoDBTable(cnx, NameDBTable, StringOfHeaders, ListOfHeaders, ListOfTuples):
    
#    # DECLARE SQL-QUERY VARIABLE FOR SQL QUERY - INSERT DATA INTO DATABASE (DB) TABLE
#    QueryInsertIntoDB = """
#    INSERT INTO """ + NameDBTable + """(Z, Y, X) VALUES (%s, %s, %s)"""
#    
#    QueryInsertIntoDB = """
#    INSERT INTO """ + NameDBTable + """(Z, Y, X""" + """) VALUES (%s, %s, %s)"""
#    
#    QueryInsertIntoDB = """
#    INSERT INTO """ + NameDBTable + """(""" + StringOfHeaders + """) VALUES (%s, %s, %s)"""
#    
#    # ValuesInsertIntoDB = (007, -007)
    
    ValuesCounter = len(ListOfHeaders)
    
    for i, each in enumerate(ListOfTuples):  ## FOR EACH ROW IN CSV FILE
        
            print("i = ", i) ## TEST PRINT COUNTER
    
            ## CREATES SQL-QUERY ACCORDING TO NUMBER IN VALUES COUNTER VARIABLE
            QueryInsertIntoDB = """
            INSERT INTO """ + NameDBTable + """(""" + StringOfHeaders + """) VALUES (
            %s""" + f"{', %s' * (ValuesCounter - 1)}" + """)"""
            
            ValuesInsertIntoDB = each  ## ...i.e. EACH TUPLE = NUMBER IN VALUES COUNTER VARIABLE
     
            ## BEGIN CALL FUNCTION - QUERY DB:  INSERT DATA INTO DATABASE (DB) TABLE
            cur = fn_QueryDB(cnx, QueryInsertIntoDB, ValuesInsertIntoDB)

    ## RETURN ()
    return(cur)

## END DEFINE FUNCTION


## END DEFINE FUNCTIONS
## END DEFINE FUNCTIONS
## END DEFINE FUNCTIONS
