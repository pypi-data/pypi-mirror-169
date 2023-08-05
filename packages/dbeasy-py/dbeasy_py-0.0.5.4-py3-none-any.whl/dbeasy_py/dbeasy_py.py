import sqlite3

def teste(n):
    return True



def createTable(conn):
    name = input("Insira o nome da tabela: ")
    pk = 0
    sql = "CREATE TABLE "+name+" ( "

    while True:
        lineName = input("Insira o nome do dado: ")
        lineType = int(input("Insira o tipo do dado: [1] INTEGER, [2] REAL, [3] TEXT, [4] BLOB "))
        if lineType == 1:
            lineType = " INTEGER "
        
        elif lineType == 2:
            lineType = " REAL "
        
        elif lineType == 3:
            lineType = " TEXT "
        
        elif lineType == 4:
            lineType = " BLOB "
        
        else:
            print("ERROR")
            break

        if pk == 0:
            linePk = int(input("Esse dado é uma chave primaria: [1] SIM, [2] NÃO? "))
            newLines = int(input("Deseja inserir outra linha: [1] SIM, [2] NÃO? "))
            if linePk == 1:
                pk = 1
                linePk = "PRIMARY KEY,"
            else:
                linePk = ", "

            if newLines == 2:
                linePk = " "
        
        
        sql = sql+lineName+lineType+"NOT NULL"+linePk

        if linePk == "":
            break
    

    return(sql)