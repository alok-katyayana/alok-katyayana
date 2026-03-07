import os
from crewai import Agent, Task, Crew

def linkdin_blog(task_description, nrefine=5):
    output = []
    
    linkdin_guy = Agent(
        role="Linkdin Media Manager",
        goal="Create a post which in line with the regular usages on Linkdin platform",
        backstory="""You are an awesome Social Media Manager who is known for creating Catchy posts for Linkdin.
                  You are awesome in using English Language and can play with words to create massive 
                  effects.
                    """
    )

    linkdin_refine_guy = Agent(
        role="Senior Linkdin Media Manager",
        goal="""Create a post which is line with the regular usages on Linkdin platform,
                you don't start from scratch, you are given a ready post, you think hard to refine it.""",
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
        verbose=True,
        planning=True,  # Enable planning feature
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
            verbose=True,
            planning=True,  # Enable planning feature
        )

        begin = crew.kickoff()

        output.append(begin.raw)

    return output
