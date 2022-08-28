import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon=":tada:", layout="wide")

with st.container():
	st.subheader("Hi, I am Peter Kure :wave:")
	st.title("A Computer Scientist from Uganda")
	st.write("I am passionate about open source software and coding")
	st.write("[Learn More >](https://pythonandvba.com)")

with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("What i do")
		st.write("##")
		st.write(
		   """
			On my Github i crossed 1.1k commits in the last year

		  """
		)
		st.write("[Github Profile >](https://www.github.com/peterkure3)")
