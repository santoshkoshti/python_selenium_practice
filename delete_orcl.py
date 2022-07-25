from oracle_database import cur, con

def delete_data_like(del_type):
    query = "delete from pynew where urls like :del_type"
    # query = "delete from pynew where urls like '%Python%' "
    try:
        cur.execute(query, [del_type])
        con.commit()
        print("data deleted")
    except:
        print("something went wrong..")
delete_data_like('%Python%')

def delete_data_id(del_type):
    query = "delete from pynew where urls = :del_type"
    #query = "delete from pynew where urls = 'Python' "
    try:
        cur.execute(query, [del_type])
        con.commit()
        print("data deleted")

    except:
        print("something went wrong..")
delete_data_id('Python')

cur.close()
