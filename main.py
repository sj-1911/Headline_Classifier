import sys

from parser import ParserFactory
from strategies import AlphabeticalSort, LengthSort, ReverseSort
from decorators import BaseHeadline, TimestampDecorator, TruncateDecorator, KeywordDecorator


def choose_parser(url: str):
    """Attempt to get a parser for the given URL, or exit with an error."""
    try:
        return ParserFactory.get_parser(url)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def fetch_headlines(parser, url: str):
    """Attempt to fetch headlines using the given parser, or exit with an error."""
    try:
        return parser.get_headlines(url)
    except Exception as e:
        print(f"Failed to retrieve headlines: {e}")
        sys.exit(1)


def select_sort_strategy() -> object:
    """Prompt the user to choose a sorting strategy, default to alphabetical on invalid input."""
    print("\nChoose a sorting method:")
    print("1. Alphabetical (A-Z)")
    print("2. Reverse Alphabetical (Z-A)")
    print("3. By Length (Longest First)")

    choice = input("Enter 1, 2, or 3: ")
    if choice == '1':
        return AlphabeticalSort()
    elif choice == '2':
        return ReverseSort()
    elif choice == '3':
        return LengthSort()
    else:
        print("Invalid choice. Defaulting to alphabetical.")
        return AlphabeticalSort()


def main():
    # Step 1: Grab headlines from site
    url = input("Enter the URL of a news site (CNN or BBC): ")
    parser = choose_parser(url)
    headlines = fetch_headlines(parser, url)

    # Step 2: Sort according to user choice
    sorter = select_sort_strategy()
    sorted_headlines = sorter.sort(headlines)

    # Step 3: Decorate each headline
    decorated_headlines = []
    for h in sorted_headlines:
        # Wrap the base headline
        headline_obj = BaseHeadline(h)
        # Apply decorators in sequence
        headline_obj = TimestampDecorator(headline_obj)
        headline_obj = TruncateDecorator(headline_obj, max_length=80)
        headline_obj = KeywordDecorator(headline_obj, keyword="AI")

        final_text = headline_obj.get_text()
        if final_text:
            decorated_headlines.append(final_text)

    # Step 4: Display final headlines
    print("\nFinal Headlines:\n")
    for idx, h in enumerate(decorated_headlines, 1):
        print(f"{idx}. {h}")


if __name__ == "__main__":
    main()
