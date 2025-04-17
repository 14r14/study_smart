from google.adk.agents import LlmAgent, Agent
from google.adk.tools import FunctionTool


async def get_user_preferences_input() -> str:
    """
    Function to get user preferences for study goals, subjects of interest, available time, and preferred resource types.
    This function will prompt the user for their study goals, subjects of interest, and available time for studying.
    The user may also provide additional information such as their preferred study methods (e.g., reading, practice problems, group study) and any specific resources they would like to use (e.g., textbooks, online courses).
    The function will return the user's preferences as a string.

    :return: User preferences as a string.
    :rtype: str
    """
    preferences = str(input())
    return preferences


MODEL = "gemini-2.0-flash"

get_user_preferences = LlmAgent(
    name="get_user_preferences",
    description="Prompts the user for their study goals, subjects of interest, available time, and preferred resource types.",
    instruction="You are a study assistant. Your task is to ask the user about their study goals, subjects of interest, and available time for studying. "
                "Please ask the user for their study goals, subjects of interest, and available time before generating the plan."
                "The user may also provide additional information such as their preferred study methods (e.g., reading, practice problems, group study) and any specific resources they would like to use (e.g., textbooks, online courses)."
                "Use the get_user_preferences tool to collect this information."
                "Once you have the user's preferences, store them in the state key 'user_preferences' in a structured format.",
    output_key="user_preferences",
    model=MODEL,
    tools=[
        FunctionTool(func=get_user_preferences_input)
    ]
)

study_plan_generator = LlmAgent(
    name="study_plan_generator",
    description="Generates a personalized study plan based on the user's goals and available time.",
    instruction="""You are a study plan generator. Your task is to create a personalized study plan for the user based on their goals, available time, and preferred study methods. 
                    Use the user's preferences provided in the state key 'user_preferences' to generate the plan.
                    You will then generate a detailed study plan that includes specific topics to cover, recommended resources, and a timeline for completion.
                    The study plan should be realistic and achievable, taking into account the user's schedule and learning style.
                    Your response should be clear and organized, with a focus on helping the user stay motivated and on track with their studies.
                    Please ensure that the study plan is tailored to the user's needs and preferences, and provide any additional tips or resources that may be helpful for their study journey.
                    The user may also ask for specific study tips or techniques to improve their study habits, and you should be prepared to provide those as well.
                    Remember to keep the user engaged and motivated throughout the process, and encourage them to reach out for help or support if they need it.""",
    output_key="study_plan",
    model=MODEL,
)

resource_recommender = LlmAgent(
    name="resource_recommender",
    description="Recommends study resources such as books, articles, and videos based on the user's interests.",
    instruction="""You are a resource recommender. Your task is to suggest study resources such as books, articles, and videos based on the user's interests and study goals. 
                    The user will provide you with their preferred subjects and any specific topics they want to focus on. 
                    You will then generate a list of recommended resources that are relevant to their interests and study needs.
                    Please ask the user for their preferred subjects and any specific topics they want to focus on before generating the recommendations.
                    Your response should include a variety of resource types (e.g., books, articles, videos) and should be tailored to the user's learning style and preferences.
                    Make sure to provide a brief description of each resource and explain why it would be helpful for the user.
                    Encourage the user to explore different types of resources and find what works best for them.
                    Use the study plan in state key 'study_plan' to generate the recommendations.""",
    output_key="resources",
    model=MODEL,
)

further_assistance = LlmAgent(
    name="further_assistance",
    description="Provides further assistance to the user if they have more questions or need additional resources.",
    instruction="If the user has more questions or needs further assistance, provide them with the necessary information or resources using the appropriate tools. "
                "If the user has no more questions, use the farewell tool to thank them for using the study assistant and wish them success in their studies.",
    output_key="further_assistance",
    model=MODEL,
)

farewell_exit = LlmAgent(
    name="farewell",
    description="A farewell message to the user.",
    instruction="Thank the user for using the study assistant and wish them success in their studies.",
    model=MODEL,
)

root_agent = Agent(
    name="study_smart",
    description="A comprehensive study assistant that helps users create personalized study plans and recommends resources.",
    instruction="You are an expert study assistant. Your task is to help users create personalized study plans and recommend resources based on their goals and preferences. "
                "You will use the get_user_preferences tool to collect information about the user's study goals, subjects of interest, and available time. "
                "You will generate a personalized study plan using the study_plan_generator tool. "
                "Once the study plan is generated, you will provide the user with a detailed outline of their study plan, including specific topics to cover, recommended resources, and a timeline for completion. "
                "If the user would like specific resources, you will recommend study resources using the resource_recommender tool. "
                "Ask the user if they have any more questions or if they need further assistance using the further_assistance tool. "
                "If they do, provide them with the necessary information or resources using the appropriate tools. "
                "If the user has no more questions, use the farewell_exit tool to thank them for using the study assistant and wish them success in their studies.",
    sub_agents=[
        get_user_preferences,
        study_plan_generator,
        further_assistance,
        resource_recommender,
        farewell_exit,],
    model=MODEL,
)