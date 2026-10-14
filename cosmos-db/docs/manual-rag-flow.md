# Manual RAG flow

```mermaid
flowchart TD
    A[User question] --> B[Generate embedding]
    B --> C[Cosmos DB vector search]
    C --> D[Get top matching product docs]
    D --> E[Build prompt with product context]
    E --> F[Azure OpenAI chat completion]
    F --> G[Return answer]
```

This is the flow implemented in the direct, no-LangChain notebook.

It is explicit and easy to understand:
- embed the query
- search the vector index
- fetch relevant product records
- inject them into a prompt
- ask the model to answer
