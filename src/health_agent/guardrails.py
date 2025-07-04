from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
    output_guardrail,
)
from utils.model_config import model
from context import UserSessionContext
from utils.model_config import model, config

class MessageOutput(BaseModel):
    response: str

class ValidatetGoalOutput(BaseModel):
    is_valid: bool
    reasoning: str


Input_Guardrail_agent = Agent(
    name="Input guardrail agent",
    instructions= """
    Please review the user's goal input and validate the following:

    1: Goal format: Check if the goal includes a valid quantity (e.g., 5), metric (e.g., kg, pounds), and duration (e.g., 2 months).

    2: Dietary or injury input: If the user mentions any dietary preferences or injuries, check if they are clearly stated and valid.

    3: Unsupported or incomplete input: If the input is missing key parts or contains unsupported content, mark it as invalid.
    """,
    output_type=ValidatetGoalOutput,
    model=model

)   

@input_guardrail
async def health_input_guardrail(
        context: RunContextWrapper[UserSessionContext],
        agent: Agent,
        Input: str | list[TResponseInputItem]
    ) -> GuardrailFunctionOutput:

    result = await Runner.run(Input_Guardrail_agent, Input , context=context.context, run_config=config)


    return GuardrailFunctionOutput(
        output_info = result.final_output,
        tripwire_triggered=result.final_output.is_valid
    )






class validateJsonFormate(BaseModel):
    is_valid: bool
    reasoning: str
    



Output_Guardrail_agent = Agent(
    name= "output guardials agent",
    instructions= """
    Please analyze the agent's final response and perform the following checks:

    1: Ensure that the output is in a structured JSON format or matches the defined Pydantic model schema.

    2: Verify that all required fields are present and their data types are correct.

    3: If the response is invalid, incomplete, or poorly structured, mark it as invalid.
    """,
    output_type=validateJsonFormate,
    model=model
)


@output_guardrail
async def health_output_guardrail(
    context: RunContextWrapper[UserSessionContext],
    agent: Agent,
    output: MessageOutput

    ) -> GuardrailFunctionOutput:

    result = await Runner.run(Output_Guardrail_agent, output.response, context=context.context, run_config=config)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_valid
    )





