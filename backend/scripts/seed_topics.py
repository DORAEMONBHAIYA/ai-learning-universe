"""Seed topics and prerequisite relationships."""

import asyncio
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from core.config import settings
from models.topic import Topic, TopicPrerequisite

engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

TOPICS = [
    {
        "title": "Python Basics",
        "description": "Variables, data types, control flow, functions, and basic I/O.",
        "difficulty": 1,
        "estimated_hours": 8.0,
        "icon": "python",
        "prerequisites": [],
    },
    {
        "title": "Data Structures",
        "description": "Lists, stacks, queues, trees, graphs, hash tables, and their implementations.",
        "difficulty": 2,
        "estimated_hours": 15.0,
        "icon": "layers",
        "prerequisites": ["Python Basics"],
    },
    {
        "title": "Algorithms",
        "description": "Sorting, searching, dynamic programming, greedy algorithms, and complexity analysis.",
        "difficulty": 3,
        "estimated_hours": 20.0,
        "icon": "code",
        "prerequisites": ["Data Structures"],
    },
    {
        "title": "SQL & Databases",
        "description": "Relational database design, SQL queries, indexing, and normalization.",
        "difficulty": 2,
        "estimated_hours": 10.0,
        "icon": "database",
        "prerequisites": ["Python Basics"],
    },
    {
        "title": "Probability & Statistics",
        "description": "Descriptive statistics, probability distributions, hypothesis testing, and Bayesian inference.",
        "difficulty": 3,
        "estimated_hours": 15.0,
        "icon": "sigma",
        "prerequisites": ["Python Basics"],
    },
    {
        "title": "Linear Algebra",
        "description": "Vectors, matrices, eigenvalues, SVD, and their applications in ML.",
        "difficulty": 3,
        "estimated_hours": 12.0,
        "icon": "matrix",
        "prerequisites": ["Python Basics"],
    },
    {
        "title": "Calculus for ML",
        "description": "Derivatives, gradients, optimization, and backpropagation fundamentals.",
        "difficulty": 3,
        "estimated_hours": 10.0,
        "icon": "sigma",
        "prerequisites": ["Linear Algebra"],
    },
    {
        "title": "Machine Learning Fundamentals",
        "description": "Supervised and unsupervised learning, train/test splits, cross-validation, bias-variance tradeoff.",
        "difficulty": 3,
        "estimated_hours": 20.0,
        "icon": "brain",
        "prerequisites": ["Python Basics", "Probability & Statistics"],
    },
    {
        "title": "Data Wrangling & Visualization",
        "description": "Pandas, NumPy, Matplotlib, Seaborn for data cleaning and exploration.",
        "difficulty": 2,
        "estimated_hours": 10.0,
        "icon": "bar-chart",
        "prerequisites": ["Python Basics"],
    },
    {
        "title": "Deep Learning",
        "description": "Neural networks, CNNs, RNNs, transformers, and training techniques.",
        "difficulty": 4,
        "estimated_hours": 25.0,
        "icon": "network",
        "prerequisites": ["Machine Learning Fundamentals", "Calculus for ML"],
    },
    {
        "title": "Natural Language Processing",
        "description": "Tokenization, embeddings, transformers, BERT, GPT, and text classification.",
        "difficulty": 4,
        "estimated_hours": 20.0,
        "icon": "message-square",
        "prerequisites": ["Deep Learning", "Probability & Statistics"],
    },
    {
        "title": "Computer Vision",
        "description": "Image processing, CNNs, object detection, segmentation, and generative models.",
        "difficulty": 4,
        "estimated_hours": 20.0,
        "icon": "camera",
        "prerequisites": ["Deep Learning", "Linear Algebra"],
    },
    {
        "title": "Reinforcement Learning",
        "description": "Markov decision processes, Q-learning, policy gradients, and PPO.",
        "difficulty": 5,
        "estimated_hours": 18.0,
        "icon": "zap",
        "prerequisites": ["Deep Learning", "Algorithms"],
    },
    {
        "title": "LLMs & AI Agents",
        "description": "Prompt engineering, RAG, tool use, agent architectures, and LangChain patterns.",
        "difficulty": 4,
        "estimated_hours": 15.0,
        "icon": "bot",
        "prerequisites": ["Natural Language Processing", "Deep Learning"],
    },
    {
        "title": "MLOps & Deployment",
        "description": "Model serving, Docker, CI/CD, monitoring, and ML pipeline orchestration.",
        "difficulty": 4,
        "estimated_hours": 15.0,
        "icon": "container",
        "prerequisites": ["Machine Learning Fundamentals", "SQL & Databases"],
    },
    {
        "title": "Knowledge Graphs",
        "description": "RDF, SPARQL, graph databases, entity resolution, and graph neural networks.",
        "difficulty": 4,
        "estimated_hours": 12.0,
        "icon": "git-branch",
        "prerequisites": ["Data Structures", "Machine Learning Fundamentals"],
    },
    {
        "title": "System Design",
        "description": "Distributed systems, API design, caching, load balancing, and scalability patterns.",
        "difficulty": 4,
        "estimated_hours": 20.0,
        "icon": "server",
        "prerequisites": ["Data Structures", "SQL & Databases"],
    },
    {
        "title": "Placement Preparation",
        "description": "Resume building, DSA practice, mock interviews, and company-specific prep.",
        "difficulty": 3,
        "estimated_hours": 25.0,
        "icon": "target",
        "prerequisites": ["Algorithms", "System Design", "Machine Learning Fundamentals"],
    },
]


async def seed():
    async with async_session() as session:
        result = await session.execute(select(Topic))
        existing = result.scalars().all()

        if existing:
            print(f"Found {len(existing)} existing topics. Skipping seed.")
            return

        topic_map: dict[str, uuid.UUID] = {}

        for topic_data in TOPICS:
            prereq_titles = topic_data.pop("prerequisites")
            topic = Topic(**topic_data)
            session.add(topic)
            await session.flush()
            topic_map[topic_data["title"]] = topic.id

            for prereq_title in prereq_titles:
                prereq_id = topic_map.get(prereq_title)
                if prereq_id:
                    session.add(TopicPrerequisite(topic_id=topic.id, prerequisite_id=prereq_id))
                else:
                    print(f"  Warning: prerequisite '{prereq_title}' not found for '{topic_data['title']}'")

        await session.commit()
        print(f"Seeded {len(TOPICS)} topics with prerequisite relationships.")


async def main():
    try:
        await seed()
    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
