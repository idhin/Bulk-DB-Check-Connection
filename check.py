import mysql.connector
from mysql.connector import Error
import colorama
from colorama import Fore

outF = open("hasil.txt", "w")

with open('list.txt') as f:
    for line in f:
        s = line.rstrip()
        rest = s.rsplit('|', 3)
        hostname = rest[0]
        username = rest[1]
        passnya = rest[2]
        dbName = rest[3]

        # print(hostname + " : " + username + " : " + passnya + " : " + dbName)
        # s.rsplit('|', 1)

        conn = None
        try:
            conn = mysql.connector.connect(host=hostname,
                                           database=dbName,
                                           user=username,
                                           password=passnya)
            if conn.is_connected():
                print(Fore.GREEN + hostname + " : " + username +
                      " : " + passnya + " : " + dbName + " Connected BosQ")
                outF.write(line)
                outF.write("\n")
                outF.close()

        except Error as e:
            print(e)

        finally:
            if conn is not None and conn.is_connected():
                conn.close()
