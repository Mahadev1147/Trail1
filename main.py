import streamlit as st
import webbrowser
import random

# Define a function to generate a response from the chatbot
def generate_response(user_input):
    # For this example, we'll just return a random response
    responses = ["Hello!", "How can I help you?", "I'm not sure I understand.", "Goodbye!"]
    return random.choice(responses)


#To open meeting page
def open_html_file(file_path):
    url=f"file://{file_path}"
    webbrowser.open_new_tab(url)


if "counter" not in st.session_state:
    st.session_state["counter"]=0


count=st.session_state["counter"]

if count%3==0:
    st.title("Login")

    col1,col2=st.columns([2,1])

    with col1:
        st.text_input("Username:")
        st.text_input("Password:")
        if st.button("Login"):
            count+=1
            st.session_state["counter"]=count
    with col2:
        st.image("login.png",use_column_width="True")

elif count%3==1:

    option=st.sidebar.selectbox("",("Alice","Meeting","Upload files","Exit"))

    if option=="Alice":

        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

        user_input=st.text_input("You: ")

        if st.button("Send"):

            response=generate_response(user_input)
            
            st.session_state.chat_history.append({"user":user_input,"bot":response})

            
            st.session_state.user_input=""

        st.markdown("Previous prompts ")
        for i,message in enumerate(st.session_state.chat_history):
            st.markdown(f"**You**: {message['user']}")
            st.markdown(f"**Bot**: {message['bot']}")
            st.markdown("---")
            if i < len(st.session_state.chat_history) - 1:
                st.markdown("")  # Add a blank line between messages       

    elif option=="Meeting":

        st.header("Join meeting:")

        st.text_input("Enter meeting URL:")

        st.markdown("")
        st.markdown("---")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.header("Start meeting:")

        html_file_path="meeting.html"

        if st.button("Launch"):
            file_path = "C:/Users/mahad/OneDrive/Delete needed/StreamlitPrac/meeting.html"
            open_html_file(file_path)

    elif option=="Upload files":
        uploaded_file=st.file_uploader("Upload PDF file",type="pdf")

        levelTitles=st.selectbox("Choose threshold level",["Executive","Senior Management","Middle Management","Supervisory","Operational"])

        titleLevelDict={"Executive":5,"Senior Management": 4,"Middle Management":3,"Supervisory":2,"Operational":1}

        titleLevel=titleLevelDict[levelTitles]

        department=st.multiselect("Select Department",["Sales","Human Resources","Marketing","FInance","Law","IT support"])
        st.write("The level is: "+str(titleLevel))

        st.write("Chosen dept:")
        st.write(department)




        st.write(uploaded_file.name)
    elif option=="Exit":
        if st.button("Logout"):
            count+=1
            st.session_state["counter"]=count

elif count%3==2:
    st.title("Logout Success!!")
    if st.button("Login"):
        count+=1
        st.session_state["counter"]=count



