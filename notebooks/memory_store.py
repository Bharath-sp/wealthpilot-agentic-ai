import os
from typing import Any


DEFAULT_MEMORY_NAMESPACE = "loan_applicants"


def get_memory_namespace() -> str:
    namespace = os.getenv("SUPERMEMORY_NAMESPACE", DEFAULT_MEMORY_NAMESPACE).strip()
    if not namespace:
        raise ValueError("SUPERMEMORY_NAMESPACE must not be empty")
    return namespace


def remember_memory(
    client: Any,
    namespace: str,
    content: str,
    applicant_id: str,
    **metadata: Any,
) -> Any:
    if not namespace.strip():
        raise ValueError("Memory namespace must not be empty")
    if not applicant_id.strip():
        raise ValueError("Applicant ID must not be empty")
    return client.add(
        content=content,
        container_tag=namespace,
        metadata={**metadata, "Applicant ID": applicant_id},
    )


def recall_memories(
    client: Any,
    namespace: str,
    query: str,
    applicant_id: str,
    k: int = 1,
) -> list[tuple[str, str, float]]:
    if not namespace.strip():
        raise ValueError("Memory namespace must not be empty")
    if not applicant_id.strip():
        raise ValueError("Applicant ID must not be empty")
    if k < 1:
        raise ValueError("k must be at least 1")

    filters = {"key": "Applicant ID", "value": applicant_id}
    results: list[tuple[str, str, float]] = []

    memories = client.search.memories(
        q=query,
        container_tag=namespace,
        filters=filters,
        limit=k,
    ).results
    for result in memories:
        metadata = getattr(result, "metadata", None) or {}
        content = getattr(result, "memory", None)
        if content and metadata.get("Applicant ID") == applicant_id:
            results.append(
                (applicant_id, content, float(getattr(result, "similarity", 0.0) or 0.0))
            )

    if results:
        return results

    documents = client.search.documents(
        q=query,
        container_tags=[namespace],
        filters=filters,
        limit=k,
    ).results
    for result in documents:
        metadata = getattr(result, "metadata", None) or {}
        if metadata.get("Applicant ID") != applicant_id:
            continue
        content = " ".join(
            chunk.content
            for chunk in (getattr(result, "chunks", None) or [])
            if chunk and getattr(chunk, "content", None)
        ).strip()
        if content:
            results.append(
                (applicant_id, content, float(getattr(result, "score", 0.0) or 0.0))
            )

    return results
