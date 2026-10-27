import chatbot as st

from main import process_pdf, ask_question


# Page configuration
st.set_page_config(
    page_title="Chat with Your PDF",
    page_icon="📚",
    layout="centered"
)


# Page heading
st.title("📚 Chat with Your PDF")

st.write(
    "Upload a PDF and ask questions about its content."
)


# Initialize session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "pdf_id" not in st.session_state:
    st.session_state.pdf_id = None

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None

if "messages" not in st.session_state:
    st.session_state.messages = []




# PDF upload section
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)


# Process a newly uploaded PDF
if uploaded_file is not None:

    current_pdf_id = (
        uploaded_file.name,
        len(uploaded_file.getvalue())
    )

    if current_pdf_id != st.session_state.pdf_id:

        # Clear the previous document's state
        st.session_state.vector_store = None
        st.session_state.pdf_id = None
        st.session_state.pdf_name = None
        st.session_state.messages = []

        with st.spinner(
            "Reading PDF and creating embeddings..."
        ):

            try:
                vector_store = process_pdf(uploaded_file)

                st.session_state.vector_store = vector_store
                st.session_state.pdf_id = current_pdf_id
                st.session_state.pdf_name = uploaded_file.name

                st.success("PDF processed successfully!")

            except Exception as e:
                st.error(f"Unable to process the PDF: {e}")


# Display the chat interface after successful processing
if st.session_state.vector_store is not None:

    st.info(
        f"Currently loaded PDF: {st.session_state.pdf_name}"
    )

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    # Download chat history
    chat_text = ""

    for message in st.session_state.messages:

        role = message["role"].capitalize()
        content = message["content"]

        chat_text += f"{role}: {content}\n\n"

        # Include source pages if available
        if message.get("sources"):
            pages = ", ".join(
                str(page)
                for page in message["sources"]
            )

            chat_text += f"Source pages: {pages}\n\n"

    st.download_button( label="📥 Download Chat History",
                            data=chat_text, 
                            file_name="pdf_chat_history.txt",
                            mime="text/plain",
                            disabled=not st.session_state.messages, 
                            key="download_chat_history" )


    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

            if message.get("sources"):
                pages = ", ".join(
                    str(page)
                    for page in message["sources"]
                )

                st.caption(f"Source pages: {pages}")

    # Question input
    question = st.chat_input(
        "Ask a question about your PDF..."
    )

    if question:

        # Save the user's question
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)

        # Generate the answer
        with st.chat_message("assistant"):

            with st.spinner(
                "Searching the PDF and generating an answer..."
            ):

                try:
                    result = ask_question(
                        st.session_state.vector_store,
                        question
                    )

                    answer = result["answer"]
                    sources = result["sources"]

                    st.write(answer)

                    if sources:
                        pages = ", ".join(
                            str(page)
                            for page in sources
                        )

                        st.caption(f"Source pages: {pages}")

                    # Save the answer and its source pages
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    })

                except Exception as e:
                    st.error(
                        f"Unable to generate an answer: {e}"
                    )
