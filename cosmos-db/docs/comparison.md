# Manual vs LangChain comparison

```mermaid
flowchart LR
    subgraph Manual
        M1[Embed query]
        M2[Cosmos vector search]
        M3[Build prompt manually]
        M4[Call Azure OpenAI]
        M1 --> M2 --> M3 --> M4
    end

    subgraph LangChain
        L1[Retriever]
        L2[Prompt template]
        L3[LLM]
        L4[Agent / tools]
        L1 --> L2 --> L3
        L4 --> L3
    end
```

## Summary

- Manual RAG is straightforward and explicit.
- LangChain adds structure for more complex workflows and tool orchestration.
- You do not need LangChain for a basic vector retrieval app.
- LangChain becomes valuable when you want reusable orchestration, memory, tool use, and multi-step agents.
