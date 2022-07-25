from oracle_database import cur, con

def insert_data(ins_data):
    query = "insert into pynew values (:ins_data)"
    # query = "insert into pynew values ('python')"
    try:
        cur.execute(query, [ins_data])
        con.commit()
        print("data inserted..")
    except:
        print("something went wrong..")

insert_data('Python')
cur.close()