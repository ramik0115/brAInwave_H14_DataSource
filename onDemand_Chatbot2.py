import streamlit as st
import requests

def create_chat_session(api_key, external_user_id):
    create_session_url = 'https://api.on-demand.io/chat/v1/sessions'
    create_session_headers = {
        'apikey': api_key
    }
    create_session_body = {
        'pluginIds': [],
        'externalUserId': external_user_id
    }
    response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)
    response_data = response.json()
    return response_data['data']['id']

def submit_query(api_key, session_id, query):
    submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
    submit_query_headers = {
        'apikey': api_key
    }
    submit_query_body = {
        'endpointId': 'predefined-openai-gpt4o',
        'query': query,
        'pluginIds': ["plugin-1712327325", "plugin-1713962163", "plugin-1717464304"],
        'responseMode': 'sync'
    }
    query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)
    return query_response.json()

def main():
    st.title("OnDemand Chat Assistant")
    
    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Sidebar configuration
    st.sidebar.header("API Configuration")
    
    # Pre-fill with your API key and user ID but allow changes
    default_api_key = "465vS5VxzwKjQB0KiYfZUIxPrtJzDFHx"
    default_user_id = "671bd9cf7700a32e7c463ba3"
    
    api_key = st.sidebar.text_input("Enter API Key", 
                                   value=default_api_key, 
                                   type="password")
    external_user_id = st.sidebar.text_input("Enter External User ID", 
                                           value=default_user_id, 
                                           type="password")

    if not api_key or not external_user_id:
        st.warning("Please enter your API key and external user ID in the sidebar.")
        return

    # Create session button
    if 'session_id' not in st.session_state and st.button("Create Chat Session"):
        with st.spinner("Creating chat session..."):
            try:
                session_id = create_chat_session(api_key, external_user_id)
                st.session_state['session_id'] = session_id
                st.success("Chat session created successfully!")
            except Exception as e:
                st.error(f"Error creating chat session: {str(e)}")

    # Display chat interface if session exists
    if 'session_id' in st.session_state:
        # Display chat history
        for message in st.session_state['chat_history']:
            if message['type'] == 'user':
                st.write(f"You: {message['content']}")
            else:
                st.write(f"Assistant: {message['content']}")

        # Query input
        query = st.text_input("Type your message here")
        
        if st.button("Send") and query:
            with st.spinner("Getting response..."):
                try:
                    # Add user message to chat history
                    st.session_state['chat_history'].append({
                        'type': 'user',
                        'content': query
                    })

                    # Get response
                    response = submit_query(api_key, st.session_state['session_id'], query)
                    
                    # Extract and display the response
                    if 'data' in response and 'response' in response['data']:
                        assistant_response = response['data']['response']
                        
                        # Add assistant response to chat history
                        st.session_state['chat_history'].append({
                            'type': 'assistant',
                            'content': assistant_response
                        })
                        
                        # Rerun to update the display
                        st.rerun()
                    else:
                        st.error("Unexpected response format")
                        st.json(response)  # Display full response for debugging
                except Exception as e:
                    st.error(f"Error submitting query: {str(e)}")
    else:
        st.info("Click 'Create Chat Session' to start chatting.")

    # Add a clear chat button
    if st.sidebar.button("Clear Chat History"):
        st.session_state['chat_history'] = []
        st.rerun()

if __name__ == "__main__":
    main()