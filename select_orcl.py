from oracle_database import cur, con

def get_all_data():
    query = "select * from pynew"
    # query = "insert into pynew values ('python')"
    try:
        cur.execute(query)
        # for i in cur.fetchall():
        #     print(i)

        for i in cur.fetchmany(numRows = 10):  #give some number
            print(i)

        # for i in cur.fetchmany(4):  #give some number
        #     print(i)

        # for i in cur.fetchone():
        #     print(i)

        print("fetched all data..")
    except:
        print("something went wrong..")

get_all_data()
cur.close()