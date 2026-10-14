# LangChain RAG flow

```mermaid
flowchart TD
    A[User question] --> B[Retriever]
    B --> C[Cosmos DB vector store]
    C --> D[Relevant documents]
    D --> E[Prompt template]
    E --> F[LLM]
    F --> G[Answer]

    H[Tool 1: product search] --> I[Agent]
    J[Tool 2: filter by price] --> I
    K[Tool 3: compare features] --> I
    I --> F
```

This is the higher-level orchestration pattern used by LangChain.

It gives you reusable components such as:
- retrievers
- prompt templates
- LLM wrappers
- tool calling and orchestration

This is useful when the workflow becomes more complex than a single retrieval + answer cycle.
