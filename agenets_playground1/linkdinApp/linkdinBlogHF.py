import os
from crewai import Agent, Task, Crew, LLM


def linkdin_blog_free(task_description, nrefine=5):
    output = []
    llm = LLM(
    model="huggingface/meta-llama/Llama-3.1-8B-Instruct",
    temperature=0.7
    )
    
    linkdin_guy = Agent(
        llm=llm,
        role="Linkdin Media Manager",
        goal="""Create a post which in line with the regular usages on Linkdin platform.
                 The tone of the post should be serious and mildly inspirational.""",
        backstory="""You are an awesome Social Media Manager who is known for creating Catchy posts for Linkdin.
                  You are awesome in using English Language and can play with words to create massive 
                  effects.
                    """
    )

    linkdin_refine_guy = Agent(
        llm=llm,
        role="Senior Linkdin Media Manager",
        goal="""Create a post which is line with the regular usages on Linkdin platform,
                you don't start from scratch, you are given a ready post, you think hard to refine it.
                 The tone of the post should be serious and mildly inspirational.
                """,
        backstory="""You are an awesome Social Media Manager who is known for creating Catchy posts for Linkdin.
                  You are awesome in using English Language and can play with words to create massive 
                  effects. You are good at taking someone's idea and take it to the next level.
                    """
    )

    task_description = task_description

    post = Task(
            description= task_description,
            expected_output='A 100-200 word post suitable for linkdin, which may include emojee if required.',
            agent=linkdin_guy
        )

    crew = Crew(
        tasks=[post],
        verbose=False,
        planning=False,
        memory=False
    )

    begin = crew.kickoff()

    output.append(begin.raw)

    for _ in range(nrefine):
        refineapost = Task(
            description= f"Refine the following LinkdIn Post \n {begin.raw} ",
            expected_output='A 100-200 word post suitable for linkdin, which may include emojee if required.',
            agent=linkdin_refine_guy
        )

        crew = Crew(
            tasks=[refineapost],
            verbose=False,
            planning=False,
            memory=False
        )

        begin = crew.kickoff()

        output.append(begin.raw)

    return output
