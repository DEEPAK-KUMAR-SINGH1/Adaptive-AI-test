from langgraph.graph import StateGraph, END

class State(dict):
    pass


def analyze_results(state):

    responses = state["responses"]

    weak_topics = []

    for r in responses:
        if not r["is_correct"]:
            weak_topics.append(r["topic"])

    state["weak_topics"] = list(set(weak_topics))

    return state


graph = StateGraph(State)

graph.add_node("analyze", analyze_results)

graph.set_entry_point("analyze")

graph.add_edge("analyze", END)

adaptive_graph = graph.compile()