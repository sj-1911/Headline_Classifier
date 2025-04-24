from parser import ParserFactory
from stratagies import AlphabeticalSort, LegnthSort, ReverseSort
from decorators import BaseHeadline, TimestampDecorator, TruncateDecorator, KeywordDecorator

# Step 1: Grab headlines from site
url = input("Enter the URL of a news site (CNN or BBC): ")
parser = ParserFactory.get_parser(url)
headlines = parser.get_headlines(url)

# Step 2: Let user pick sorting method
print("\nChoose a sorting method:")
print("1. Alphabetical (A-Z)")
print("2. Reverse Alphabetical (Z-A)")
print("3. By Length (Longest First)")

choice = input("Enter 1, 2, or 3: ")

if choice == '1':
    sorter = AlphabeticalSort()
elif choice == '2':
    sorter = ReverseSort()
elif choice == '3':
    sorter = LegnthSort()
else:
    print("Invalid choice. Defaulting to alphabetical.")
    sorter = AlphabeticalSort()

sorted_headlines = sorter.sort(headlines)

# Step 3: Ask if user wants to apply decorators
apply_decorators = input("\nWould you like to apply decorators (timestamp, truncate, filter)? (yes/no): ").lower()

decorated_headlines = []
for h in sorted_headlines:
    headline_obj = BaseHeadline(h)

    if apply_decorators == 'yes':
        # Add timestamp, truncate to 80 chars, and filter for a keyword like "AI"
        headline_obj = TimestampDecorator(headline_obj)
        headline_obj = TruncateDecorator(headline_obj, max_length=80)
        headline_obj = KeywordDecorator(headline_obj, keyword="AI")

        final_text = headline_obj.get_text()
        if final_text:
            decorated_headlines.append(final_text)
    else:
        decorated_headlines.append(h)

# Step 4: Display final headlines
print("\nFinal Headlines:\n")
for idx, h in enumerate(decorated_headlines, 1):
    print(f"{idx}. {h}")

# Step 5: Save top 150 headlines to a file
output_path = "Headlines.txt"
with open(output_path, "w", encoding="utf-8") as f:
    for h in decorated_headlines[:150]:
        f.write(h + "\n")

print(f"\nTop 150 headlines saved to {output_path}")
