import streamlit as st
from PIL import Image
from utility import login
from src.db_connection import get_database_connection
from src.expense_op import save_expense
from src.parameter_ins import insert_parameter

# Load images
logo_image = Image.open("img/company_logo.png")
ai_image = Image.open("img/company_banner.png")

st.set_page_config(page_title=" Real Estate Price Prediction", page_icon=logo_image, layout="wide")

# Display the logo and the main title of the page
# st.image(logo_image, width=100)
# st.title("Welcome to Grow with Data :seedling:")

# Create columns for the logo and the title
col1, col2 = st.columns([1, 3])

# Display the logo in the first column
with col1:
    st.image(logo_image, width=100)

# Display the main title of the page in the second column
with col2:
    st.markdown("# Welcome to Real Estate Price Prediction:seedling:")

# Introduction about "Grow with Data"
st.header("Price Prediction For Real Estates")

st.markdown('''
            ### Project Features
            - User Authentication: Secure login system for personal use.
            - Price prediction: Ability to predict prices of real estates.
            - Data Persistence: Save and retrieve predicted data using files and databases.
            - Categorization: Organize prices into categories.
            - Reporting: Visualize expenses with charts and summaries.
            - Interactive GUI: A user-friendly web interface using Streamlit.
            ''')



def menu():
        st.sidebar.header("What's you choice?")
        task = st.sidebar.selectbox('--------',
                                    ('Price Authentications', 
                                     'Prediction of real estate prices',
                                     'Records'))

        if task == 'Price Authentications':
            cursor, db = get_database_connection()
            save_expense(cursor, db)
        elif task == 'Records':
             pass
            # reporting()
        elif task == 'Prediction of real estate prices':
             cursor, db = get_database_connection()
             insert_parameter(cursor, db)
             pass
            # parameter_listing()



@login
def main():
    cols1, cols2, cols3 = st.columns((1, 4, 1))
    # cols1.image('smart-group-logo-r.png')
    cols2.markdown("<h1 style='text-align: left;margin-top:-2rem; margin-left:1rem; color: #E12D06;'>Personal Expense Tracker</h1>", unsafe_allow_html=True)
    st.write('\n')

    if st.session_state["authentication_status"]:

        # URL of the GIF
        # col1, col2, col3 = st.columns(3)
        # for i in range(1, 30, 3):
        #     gif_url = 'https://darebee.com/images/exercise/2022/december{}.gif'
        #     # st.write(gif_url.format(1))
        #     # Display the GIF in Streamlit
        #     col1.image(gif_url.format(i), caption=f'Exercise {i}', width=300)
        #     col2.image(gif_url.format(i+1), caption=f'Exercise {i+1}', width=300)
        #     col3.image(gif_url.format(i+2), caption=f'Exercise {i+2}', width=300)

        menu()
        


if __name__ == '__main__':
    main()