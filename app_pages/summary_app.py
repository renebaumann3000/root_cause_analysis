import streamlit as st

def summary_page():
    st.title("Project Summary: AI-Powered Root Cause Analysis for Enhanced Customer Service")

    st.header("Background")
    st.write("""
    In the fast-paced business environment, effective communication and data exchange between the customer service department and other departments are often lacking. Despite being the company's mouthpiece, customer service often struggles with siloed information, hindering their ability to provide quick and comprehensive solutions.
    """)

    st.header("Objective")
    st.write("""
    The primary goal of this project is to leverage AI in performing root cause analysis to not just answer customer queries but to preemptively identify and resolve underlying issues. This proactive approach aims at reducing the incidence of customer complaints and improving the overall service experience.
    """)

    st.header("Challenge")
    st.write("""
    One of the most formidable challenges in this endeavor is the highly specific nature of root causes that vary significantly across companies. The task of automatically detecting these root causes, particularly with minimal data input, is close to a “Mission Impossible”. Each company's unique problems, processes, and customer interactions create a complex web that traditional analysis methods struggle to navigate effectively.

    Traditional root cause analysis methods, including AI-based ones, demand substantial data input from various departments and systems. This extensive data requirement poses a challenge for many companies that either lack such data or find the process of data entry cumbersome.
    """)

    st.header("Solution")
    st.write("""
    This pre-alpha version of the AI-powered root cause analysis tool is envisioned to demonstrate the potential of big data in overcoming these challenges. By integrating limited yet crucial data inputs, such as customer service contact drivers and process flow charts, the AI aims to intelligently predict potential root causes. This approach not only simplifies the data input process but also harnesses the latent power of big data, opening new horizons in predictive analytics.
    """)

    st.header("Impact")
    st.write("""
    A successful prediction of even a single root cause can significantly benefit a company by:
    - Eliminating Contact Drivers: Directly addressing the reasons why customers reach out, thereby reducing repetitive queries.
    - Reducing Costs: Lowering operational costs by streamlining the customer service process.
    - Improving Products: Gaining insights into product-related issues and enhancing product quality.
    - Boosting Sales: Happy customers are more likely to return, leading to increased sales and brand loyalty.
    """)

    st.header("Conclusion")
    st.write("""
    This AI-powered root cause analysis project is not just a tool for problem-solving; it's a strategic asset for enhancing customer satisfaction and loyalty. By simplifying the data input process and providing accurate predictions, it promises to be a game-changer in the realm of customer service.
    """)