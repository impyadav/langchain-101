"""
# -*- coding: utf-8 -*-

Created on Oct 2023
@author: Prateek Yadav

"""
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate


def cl_maker(job_description, projects):
    system_template = "You're an AI CoverLetter Maker"
    system_message_template = SystemMessagePromptTemplate.from_template(system_template)

    human_template = "I want to make cover letter for a job application. I will provide you Job description and my " \
                     "skill set and projects, based on those you have to design a cover letter." \
                     f"Here is the Job description {job_description} and Here is the about my porjects {projects}"

    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_template, human_message_prompt])

    request = chat_prompt.format_prompt(job_description=job_description, projects=projects).to_messages()

    chat = ChatOpenAI()
    res = chat(request)

    return res.content


if __name__ == '__main__':
    with open('./examples/my_projects.txt', 'r') as f:
        project_data = f.read()

    with open('./examples/job_description.txt', 'r') as f:
        job_desc_data = f.read()

    result = cl_maker(job_desc_data, project_data)

    with open('./output/output_CL.txt', 'w') as f:
        f.write(result)
