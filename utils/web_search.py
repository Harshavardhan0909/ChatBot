from duckduckgo_search import DDGS
from config.config import MAX_WEB_RESULTS


def search_web(query):

    results = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=MAX_WEB_RESULTS):
                results.append(r["body"])

        return "\n".join(results)

    except Exception as e:
        return f"Web search error: {str(e)}"