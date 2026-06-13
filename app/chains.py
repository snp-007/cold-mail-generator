import os
import json
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}

            ### INSTRUCTION:
            The scraped text is from a careers page.

            Extract all job postings and return them as a JSON array.

            For each job posting return:

            {{
                "role": "job title",
                "experience": "required experience",
                "skills": [
                    "skill1",
                    "skill2",
                    "skill3"
                ],
                "description": "complete job description"
            }}

            IMPORTANT:
            - skills MUST always be a list of strings.
            - Do NOT create nested skill categories.
            - Do NOT use objects for skills.
            - Do NOT use keys such as Must-Have Skills or Good-to-Have Skills.
            - Return valid JSON only.
            - Do not return any explanation or preamble.

            ### VALID JSON ONLY:
            """
        )

        chain_extract = prompt_extract | self.llm

        res = chain_extract.invoke(
            input={"page_data": cleaned_text}
        )

        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)

            jobs = res if isinstance(res, list) else [res]

            # Normalize skills format
            for job in jobs:

                if "skills" not in job:
                    job["skills"] = []

                # Handle nested skill dictionaries
                if isinstance(job["skills"], dict):
                    job["skills"] = (
                        job["skills"].get("Must-Have Skills", [])
                        + job["skills"].get("Good-to-Have Skills", [])
                    )

                # Handle comma-separated string
                elif isinstance(job["skills"], str):
                    job["skills"] = [
                        skill.strip()
                        for skill in job["skills"].split(",")
                        if skill.strip()
                    ]

                # Ensure list format
                elif not isinstance(job["skills"], list):
                    job["skills"] = []

            return jobs

        except Exception as e:
            raise OutputParserException(
                f"Unable to parse jobs. Details: {str(e)}"
            )

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are XYZ, a Business Development Executive at A-company.

            A-company is an AI and Software Consulting company specializing in:
            - AI Solutions
            - Machine Learning Applications
            - Data Engineering
            - Web Development
            - Cloud Solutions
            - Business Process Automation

            Your task is to write a personalized cold email to the hiring team.

            The email should:
            - Show understanding of the role requirements.
            - Briefly explain how A-company can help.
            - Highlight relevant expertise.
            - Include the most relevant portfolio links from:
              {link_list}
            - Be concise and professional.
            - End with a clear call to action.

            Do not write any preamble.

            ### EMAIL:
            """
        )

        chain_email = prompt_email | self.llm

        res = chain_email.invoke(
            {
                "job_description": json.dumps(job, indent=2),
                "link_list": links
            }
        )

        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))