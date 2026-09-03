import requests
from bs4 import BeautifulSoup
from datetime import datetime


def search_web(query):
    results = []

    # Wikipedia API
    try:
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "srlimit": 5
        }

        headers = {
            "User-Agent": "ResearchReportAgent/1.0"
        }

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=15
        )

        data = response.json()

        for item in data["query"]["search"]:
            title = item["title"]
            snippet = BeautifulSoup(
                item["snippet"],
                "html.parser"
            ).get_text()

            page_url = (
                "https://en.wikipedia.org/wiki/"
                + title.replace(" ", "_")
            )

            results.append({
                "title": title,
                "url": page_url,
                "snippet": snippet
            })

    except Exception as e:
        print("Search error:", e)

    return results


def generate_summary(results):

    if not results:
        return "No information found."

    summary = ""

    for result in results:
        summary += result["snippet"] + " "

    return summary


def generate_report(topic, results, summary):

    report = ""

    report += "=" * 70 + "\n"
    report += "RESEARCH REPORT\n"
    report += "=" * 70 + "\n\n"

    report += "Research Topic: " + topic + "\n"
    report += "Generated On: " + datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    ) + "\n\n"

    report += "1. INTRODUCTION\n"
    report += "-" * 70 + "\n"

    report += (
        "This report provides an overview of "
        + topic
        + ". Information was collected from "
          "online sources and summarized below.\n\n"
    )

    report += "2. KEY FINDINGS\n"
    report += "-" * 70 + "\n"

    for i, result in enumerate(results, 1):

        report += f"\n{i}. {result['title']}\n"
        report += f"   {result['snippet']}\n"

    report += "\n3. SUMMARY\n"
    report += "-" * 70 + "\n"
    report += summary + "\n\n"

    report += "4. REFERENCES\n"
    report += "-" * 70 + "\n"

    for i, result in enumerate(results, 1):

        report += f"{i}. {result['title']}\n"
        report += f"   {result['url']}\n"

    report += "\n" + "=" * 70 + "\n"
    report += "END OF REPORT\n"
    report += "=" * 70 + "\n"

    return report


# MAIN PROGRAM

print("=" * 70)
print("AGENTIC AI - RESEARCH REPORT AGENT")
print("=" * 70)

topic = input("\nEnter your research topic: ")

print("\nSearching for information...")

results = search_web(topic)

if results:

    print(f"\nFound {len(results)} sources.")

    print("\n--- Search Results ---")

    for i, result in enumerate(results, 1):

        print(f"\n{i}. {result['title']}")
        print(f"   {result['url']}")
        print(f"   {result['snippet']}")

    print("\nGenerating research report...")

    summary = generate_summary(results)

    report = generate_report(
        topic,
        results,
        summary
    )

    with open(
        "research_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print("\n" + "=" * 70)
    print("RESEARCH REPORT GENERATED SUCCESSFULLY!")
    print("=" * 70)

    print("\nFile created:")
    print("research_report.txt")

else:

    print("\nNo search results found.")
    print("Please check your internet connection.")
