import streamlit as st
from root_cause_app import root_cause_page
from flow_chart_app import flow_chart_page

st.set_page_config(page_title="AI powered Root Cause Analysis")

class MultiPage:
    def __init__(self, app_name) -> None:
        self.pages = {}
        self.app_name = app_name

    def add_page(self, title, func) -> None:
        self.pages[title] = func

    def run(self):
        st.title(self.app_name)
        page_title = st.sidebar.radio('Menu', list(self.pages.keys()))

        # State management
        if 'state' not in st.session_state:
            st.session_state['state'] = {}

        try:
            # Dynamic Page Loading
            page_function = self.pages[page_title]
            page_function()
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.error("Please contact the admin if the problem persists.")

# Create an instance of the MultiPage class
app = MultiPage("AI powered Root Cause Analysis")

# Add pages to the app
app.add_page("Root Cause Predictor", root_cause_page)
app.add_page("Flow Chart Predictor", flow_chart_page)

# Run the app
app.run()
