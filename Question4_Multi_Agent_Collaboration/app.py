# ============================================================
# Question 4 - Multi-Agent Collaboration System
# ============================================================

from datetime import datetime


# ============================================================
# AGENT 1: RESEARCH AGENT
# ============================================================

class ResearchAgent:

    def research(self, topic):
        print("\n[Research Agent] Starting research...")
        print(f"[Research Agent] Researching topic: {topic}")

        information = [
            f"{topic} is an important area of modern technology.",
            f"{topic} is used to solve complex real-world problems.",
            f"{topic} can improve efficiency, productivity, and decision-making.",
            f"{topic} is being adopted across different industries.",
            f"Future developments in {topic} are expected to provide new opportunities."
        ]

        print("[Research Agent] Research completed.")

        return information


# ============================================================
# AGENT 2: ANALYST AGENT
# ============================================================

class AnalystAgent:

    def analyze(self, topic, information):
        print("\n[Analyst Agent] Analyzing research findings...")

        analysis = {
            "topic": topic,
            "key_points": [
                "The technology has significant practical applications.",
                "It can improve operational efficiency.",
                "It supports better decision-making.",
                "Organizations can use it to solve complex problems.",
                "Future improvements may increase its impact."
            ],
            "advantages": [
                "Improved efficiency",
                "Automation of repetitive tasks",
                "Better decision-making",
                "Cost and time savings"
            ],
            "challenges": [
                "Implementation cost",
                "Data security and privacy",
                "Need for skilled professionals",
                "Integration with existing systems"
            ]
        }

        print("[Analyst Agent] Analysis completed.")

        return analysis


# ============================================================
# AGENT 3: REPORT AGENT
# ============================================================

class ReportAgent:

    def generate_report(self, topic, information, analysis):

        print("\n[Report Agent] Generating final report...")

        report = []

        report.append("=" * 70)
        report.append("          MULTI-AGENT COLLABORATION REPORT")
        report.append("=" * 70)

        report.append(f"\nTopic: {topic}")
        report.append(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        report.append("\n\n1. RESEARCH FINDINGS")
        report.append("-" * 70)

        for i, item in enumerate(information, 1):
            report.append(f"{i}. {item}")

        report.append("\n\n2. ANALYSIS")
        report.append("-" * 70)

        report.append("\nKey Points:")
        for point in analysis["key_points"]:
            report.append(f"- {point}")

        report.append("\nAdvantages:")
        for advantage in analysis["advantages"]:
            report.append(f"- {advantage}")

        report.append("\nChallenges:")
        for challenge in analysis["challenges"]:
            report.append(f"- {challenge}")

        report.append("\n\n3. CONCLUSION")
        report.append("-" * 70)
        report.append(
            f"{topic} has significant potential to improve efficiency, "
            "automation, and decision-making. Successful implementation "
            "requires addressing security, cost, and skill-related challenges."
        )

        report.append("\n\n4. AGENT COLLABORATION FLOW")
        report.append("-" * 70)
        report.append(
            "Research Agent -> Analyst Agent -> Report Agent"
        )

        report.append("\n" + "=" * 70)
        report.append("             REPORT GENERATED SUCCESSFULLY")
        report.append("=" * 70)

        return "\n".join(report)


# ============================================================
# MAIN MULTI-AGENT SYSTEM
# ============================================================

def main():

    print("=" * 70)
    print("       AGENTIC AI - MULTI-AGENT COLLABORATION SYSTEM")
    print("=" * 70)

    topic = input("\nEnter a topic for the agents: ")

    # Create agents
    research_agent = ResearchAgent()
    analyst_agent = AnalystAgent()
    report_agent = ReportAgent()

    # Agent 1: Research
    research_results = research_agent.research(topic)

    # Agent 2: Analysis
    analysis_results = analyst_agent.analyze(
        topic,
        research_results
    )

    # Agent 3: Report generation
    final_report = report_agent.generate_report(
        topic,
        research_results,
        analysis_results
    )

    # Display final report
    print("\n")
    print(final_report)

    # Save report
    with open("final_report.txt", "w", encoding="utf-8") as file:
        file.write(final_report)

    print("\nFinal report saved as: final_report.txt")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
