import streamlit as st
import csv
import io

st.title("CSV Summarizer")
st.write("Upload a CSV file and get a quck statistical summary of its numeric columnns.")

#File Uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    #Read the uploaded file
    content = io.StringIO(uploaded_file.read().decode("utf-8"))
    reader = csv.reader(content)
    headers = next(reader)
    rows = list(reader)

    st.subheader("Overview")
    st.write(f"**Column names:** {headers}")
    st.write(f"**Total rows:** {len(rows)}")

    #Find numeric columns
    numeric_cols = []
    if rows:
        first_row = rows[0]
        for i, value in enumerate(first_row):
            try:
                float(value)
                numeric_cols.append(i)
            except ValueError:
                pass
    
    #Show stats for each numeric column
    if numeric_cols:
        st.subheader("Numeric Column Stats")
        for col_index in numeric_cols:
            col_name =  headers[col_index]
            values = []
            for row in rows:
                try:
                    values.append(float(row[col_index]))
                except (ValueError, IndexError):
                    pass


            if values:
                total = sum(values)
                average = total / len(values)
                maximum = max(values)
                minimum = min(values)

                st.write(f"### {col_name}")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Sum", f"{total:,.2f}")
                col2.metric("Average", f"{average:,.2f}")
                col3.metric("Min", f"{minimum:,.2f}")
                col4.metric("Max", f"{maximum:,.2f}")
    else:
        st.info("No numeric columns found in this file.")
else:
    st.info("Upload a CSV file to get started.")
