import pandas as pd
import chromadb
from chromadb.config import Settings
import uuid


class Portfolio:
    def __init__(self, file_path="app/resources/portfolio_links.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

        self.chroma_client = chromadb.PersistentClient(
            path="vectorstore",
            settings=Settings(anonymized_telemetry=False)
        )
        self.collection = self.chroma_client.get_or_create_collection(
            name="portfolio"
        )

    def load_portfolio(self):
        if self.collection.count() == 0 and not self.data.empty:
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[str(row["Techstack"])],
                    metadatas=[{"links": row["Links"]}],
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills, n_results=3):

        if isinstance(skills, dict):
            skills = (
                skills.get("Must-Have Skills", [])
                + skills.get("Good-to-Have Skills", [])
            )

        if isinstance(skills, list):
            skills = " ".join(skills)

        if not skills:
            return []

        result = self.collection.query(
            query_texts=[skills],
            n_results=n_results
        )

        metadatas = result.get("metadatas", [])

        links = []

        for group in metadatas:
            for item in group:
                if isinstance(item, dict) and "links" in item:
                    links.append(item["links"])

        return list(dict.fromkeys(links))