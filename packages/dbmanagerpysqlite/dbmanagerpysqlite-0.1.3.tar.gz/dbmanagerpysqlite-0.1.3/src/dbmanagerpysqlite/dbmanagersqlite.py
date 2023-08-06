import sqlite3
import datetime


class Db_manager:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_db(self):
        connection = sqlite3.connect(self.db_name)
        connection.close()

    def create_table(self, table_dict: dict):

        header_string = f"CREATE TABLE IF NOT EXISTS {table_dict.get('table_name')} ("
        for index, fild in enumerate(table_dict.get("filds")):
            fild_name = fild.get("name")
            fild_type = fild.get("type")
            if index != (len(table_dict.get("filds")) - 1):
                header_string += f"{fild_name} {fild_type}, "
            else:
                header_string += f"{fild_name} {fild_type} "

        header_string += ");"

        print(header_string)
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(header_string)
        connection.commit()
        connection.close()
        print("TABLE CREATED SUCCESSFULLY!")

    def add_data(self, insert_dict: dict):
        header_string = f"INSERT INTO {insert_dict.get('table_name')} VALUES ("
        for index, value in enumerate(insert_dict.get("values")):
            if isinstance(value, str):
                value = f"'{value}'"
            if index != (len(insert_dict.get("values")) - 1):
                header_string += f"{value}, "
            else:
                header_string += f"{value}"
        header_string += f")"
        print(header_string)
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(header_string)
        connection.commit()
        connection.close()
        print("DATA INSERTED SUCCESSFULLY!")

    def delete_data(self, remove_dict):
        if isinstance(remove_dict.get('to_check_value'), str):
            remove_dict["to_check_value"] = f"""'{remove_dict["to_check_value"]}'"""
        header_string = f"DELETE FROM {remove_dict.get('table_name')} WHERE {remove_dict.get('fild')} {remove_dict.get('operator')} {remove_dict.get('to_check_value')}"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(header_string)
        connection.commit()
        connection.close()
        print("DATA REMOVED SUCCESSFULLY!")

    def query(self, query_dict):
        header = "SELECT "
        for index, fild in enumerate(query_dict.get("filds")):
            if index != len(query_dict.get("filds")) - 1:
                header += f"{ fild} , "
            else:
                header += f" {fild} "
        header += f"FROM {query_dict.get('table_name')} "
        if (conditions := query_dict.get("conditions")) != None:
            header += " WHERE "
            for counter, condition in enumerate(conditions):
                header += condition + " "
                try:
                    header += query_dict.get("connections")[counter] + " "
                except:
                    continue
        if (order := query_dict.get("order")) != None:
            header += f" ORDER BY {order} "
            if order[0] == "-":
                header += " DESC "
        # print(header)
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(header)
        query = cursor.fetchall()
        connection.close()
        print("QUERY TAKEN SUCCESSFULLY!")
        return query
