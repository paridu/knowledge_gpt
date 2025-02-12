answer_col, sources_col = st.columns(2)

# Initialize LLM with OpenRouter's settings
llm = ChatOpenAI(
    model=model,
    openai_api_key=openrouter_api_key,
    temperature=0,
    openai_api_base="https://openrouter.ai/api/v1",
    headers={
        "HTTP-Referer": "https://your-site.com",  # Update this
        "X-Title": "KnowledgeGPT",
    }
)

result = query_folder(
    folder_index=folder_index,
    query=query,
    return_all=return_all_chunks,
    llm=llm,
)

with answer_col:
    st.markdown("#### Answer")
    st.markdown(result.answer)

with sources_col:
    st.markdown("#### Sources")
    for source in result.sources:
        st.markdown(source.page_content)
        st.markdown(source.metadata["source"])
        st.markdown("---")