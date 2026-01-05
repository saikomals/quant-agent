import typer
from rich.console import Console
from src.audit.schemas import EvidenceBundle
from src.agent.graph import build_graph # <--- IMPORT THIS

app = typer.Typer()
console = Console()

@app.command()
def run(
    ticket: str = typer.Option(..., help="Jira Ticket ID"),
    goal: str = typer.Option(..., help="High-level research goal"),
):
    console.print(f"[bold green]Starting Run for {ticket}[/bold green]")

    # 1. Initialize State
    initial_bundle = EvidenceBundle(ticket_id=ticket, agent_version="v0.1")
    initial_state = {
        "ticket_id": ticket,
        "goal": goal,
        "evidence": initial_bundle,
        "plan": None,
        "code": None,
        "execution_result": None
    }

    # 2. Load the Brain
    graph = build_graph()

    # 3. Run the Brain
    # The graph will print its own logs from the nodes we defined
    final_state = graph.invoke(initial_state)

    # 4. Report Results
    console.print("\n[bold blue]Run Complete. Final State:[/bold blue]")
    console.print(f"Plan: {final_state['plan']}")
    console.print(f"Result: {final_state['execution_result']}")
    console.print(f"Audit Log Count: {len(final_state['evidence'].replay_log)}")

if __name__ == "__main__":
    app()