import asyncio
import streamlit as st
from agents import Runner, ItemHelpers,  InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from context import UserSessionContext
from multi_agent import health_wellness_agent
from utils.model_config import config

st.set_page_config(page_title="Health Agent", page_icon="💪")

st.title("💪 Health & Wellness Planner Agent")
st.subheader("Your AI Assistant for Diet, Fitness, and Injury Support")
st.markdown("Talk to your personal AI trainer about your fitness, diet, or health concerns.")
menu = ["Health Agent", "Dashboard"]




if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.context = UserSessionContext(name="User", uid=1)

user_input = st.chat_input("Ask your health planner...")

if user_input:
  
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

 
    st.session_state.response_text = ""
    response_area = st.empty()

    async def get_streamed_response():
        try:
          
            result = Runner.run_streamed(
                starting_agent=health_wellness_agent,
                input=user_input,
                context=st.session_state.get("context", {}),
                run_config=config
            )

          
            async for step in result.stream_events():

                if step.type == "raw_response_event":
                    token = getattr(step.data, "delta", "")
                    st.session_state.response_text += token
                    response_area.markdown(st.session_state.response_text)

                elif step.type == "run_item_stream_event":
                    if step.item.type == "tool_call_output_item":
                        tool_output = step.item.output
                        st.session_state.response_text += f"\n Tool Result: {tool_output}\n"
                        response_area.markdown(st.session_state.response_text)

                

        except InputGuardrailTripwireTriggered:
            st.error("❌ Your input is invalid. Please rephrase your goal.")
            return

        except OutputGuardrailTripwireTriggered:
            st.error("⚠️ Agent's response was blocked due to policy violation.")
            return

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(get_streamed_response())


    st.session_state.messages.append({
        "role": "agent",
        "content": st.session_state.response_text
    })
