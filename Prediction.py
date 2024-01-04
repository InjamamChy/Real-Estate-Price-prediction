import os
import streamlit as st
import pandas as pd
x = []
y1 = False
y2 = False
y3 = False
expense_date  = "" 
category = "" 
amount = "" 
notes= ""
notesx= ""
amountx = "" 
document_upload = "" 
created_at = "" 
updated_at = "" 
notid = "" 
categoryx = ""

from src.db_ops import show_data, edit_data, delete_data

def insert_parameter(cursor,db):
    if 'flag' not in st.session_state:
        st.session_state.flag = 0
    

    global x
    st.sidebar.header('add or delete column')
    task = st.sidebar.selectbox('--------',
                                    ('Add column', 
                                     'Delete column'))

    if(task == "Add column"):
        # Streamlit Form
        st.title('Add Column to Database')

        # Form to get new column details
        new_column_name = st.text_input('Enter the new column name:')
        new_column_type = st.text_input('Enter the data type for the new column :')
        # x.append(new_column_name)
        # for i, element in enumerate(x, start=1):
        #     st.write(f" {element}")

        if st.button('Add Column'):
            # x = (new_column_name)
            # x.append(new_column_name)
            # for i, element in enumerate(x, start=1):
            #     st.write(f" {element}")
            
            
            # Use the ALTER TABLE statement to add the new column
            alter_query = f'''ALTER TABLE expense ADD COLUMN {new_column_name} {new_column_type}'''
                            ##AFTER document"
            # ALTER TABLE student_information ADD COLUMN new_column_name longtext;

            try:
                cursor.execute(alter_query)
                db.commit()
                st.success(f"Column '{new_column_name}' added successfully.")
                st.balloons()
            except:
                st.error("Error adding column")
                
    if(task == "Delete column"):
        st.title('Delete Column to Database')
        st.header('button for columns')
        cursor.execute('''SHOW COLUMNS FROM expense FROM ExpenseDB''')
        
        columns = [column[0] for column in cursor.fetchall()]
        
        if st.button('show Columns'):
            try:
                st.title('Columns for Table: expense')
                for column in columns:
                    st.write(column)
                    #st.success(f"Column '{new_column_name}' added successfully.")
                    st.balloons()
            except:
                st.error("Error adding column")

        # Streamlit Form
        st.title('Delete Column from Database')

        # Form to get the column name to be deleted
        column_to_delete = st.text_input('Enter the column name to be deleted:')

        if st.button('Delete Column'):
            # Use the ALTER TABLE statement to delete the column
            alter_query = f"ALTER TABLE expense DROP COLUMN {column_to_delete};"

            try:
                cursor.execute(alter_query)
                db.commit()
                st.success(f"Column '{column_to_delete}' deleted successfully.")
            except:
                st.error("Error deleting column: ")

