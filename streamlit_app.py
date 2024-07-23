import streamlit as st
import subprocess


def execute_rscript(file):
    process = subprocess.Popen(
        ["Rscript", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    result = process.communicate()
    return result


def render_r_code(file):
    with st.expander("Code", expanded=True):
        code = open(file, "r").read()
        # Remove every line that starts with load() function
        code = "\n".join(
            [line for line in code.split("\n") if not line.startswith("load(")]
        )
        st.code(code, language="r")


def render_r_output(file):
    result = execute_rscript(file)
    stdout, stderr = result
    if stdout:
        st.write("Output:")
        st.code(stdout)


def render_rscript(file):
    render_r_code(file)
    render_r_output(file)


st.header("🧰 dplyr - A Grammar of Data Manipulation")
st.markdown("""dplyr is a grammar of data manipulation, providing a consistent set of verbs that help you solve the most common data manipulation challenges:

- `mutate()` adds new variables that are functions of existing variables
- `select()` picks variables based on their names.
- `filter()` picks cases based on their values.
- `summarise()` reduces multiple values down to a single summary.
- `arrange()` changes the ordering of the rows.
""")

st.sidebar.markdown("""
# About
This demo shows the use of R in a Streamlit App by showcasing 5 example use cases.

The R code for all 5 examples are rendered on-the-fly in this app.

R packages used:
- `dplyr`
""")

st.subheader("Example 1")
st.markdown("""
- Select the year, month, day, departure time, origin, destination, carrier, air time, and distance columns from the flights data frame.
- Randomly sample 10 rows from the resulting data frame.
""")
render_rscript("src/dplyr/example-01.R")

st.subheader("Example 2")
st.markdown("""
- Select all flights that have an origin starting with the letter "J"
""")
render_rscript("src/dplyr/example-02.R")

st.subheader("Example 3")
st.markdown("""
- Select the first 10 flights that depart on January 1st
""")
render_rscript("src/dplyr/example-03.R")

st.subheader("Example 4")
st.markdown("""
- Show all the airlines in the dataset
- Order them by name
""")
render_rscript("src/dplyr/example-04.R")

st.subheader("Example 5")
st.markdown("""
- Top 10 carriers with the lowest average departure delay
""")
render_rscript("src/dplyr/example-05.R")
