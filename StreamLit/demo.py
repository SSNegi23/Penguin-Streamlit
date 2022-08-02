import streamlit as st

st.title("Hello World")

st.header("Header")

st.subheader("Sub header")

st.text("This is the Text Function.")

st.markdown(""" # H1 tag
## h2 tag
### h3 tag

$Emoji$ - 
:moon: <br>
:sunglasses:

** Bold **
_italics_
 """,True) 
#  with true here, emoji came to new line

st.latex(r'''  a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')

d = {
    "name":"Shivang",
    "Language":"Python",
    "Topic":"StreamLit"
}

st.write("Shivang","Python","StreamLit")
# if you put a function in st.write() it will show details of function 
st.write(print)
# Dictionary
st.write(d)