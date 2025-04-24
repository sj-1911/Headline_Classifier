# test_decorators.py

from decorators import BaseHeadline, KeywordDecorator, TruncateDecorator

def test_base_headline():
    headline = BaseHeadline("Breaking News: AI Revolutionizes Healthcare")
    assert headline.get_text() == "Breaking News: AI Revolutionizes Healthcare"
    print("✅ BaseHeadline test passed.")

def test_keyword_decorator_match():
    headline = BaseHeadline("Breaking News: AI Revolutionizes Healthcare")
    decorated = KeywordDecorator(headline, "AI")
    assert decorated.get_text() == "Breaking News: AI Revolutionizes Healthcare"
    print("✅ KeywordDecorator (match) test passed.")

def test_keyword_decorator_no_match():
    headline = BaseHeadline("Breaking News: AI Revolutionizes Healthcare")
    decorated = KeywordDecorator(headline, "Sports")
    assert decorated.get_text() == ""  # Should return empty
    print("✅ KeywordDecorator (no match) test passed.")

def test_truncate_decorator_short():
    headline = BaseHeadline("Short Headline")
    decorated = TruncateDecorator(headline, 30)
    assert decorated.get_text() == "Short Headline"
    print("✅ TruncateDecorator (short text) test passed.")

def test_truncate_decorator_long():
    headline = BaseHeadline("This is a very long headline that should be truncated properly at a certain length")
    decorated = TruncateDecorator(headline, 30)
    assert decorated.get_text() == "This is a very long headline t..."
    print("✅ TruncateDecorator (long text) test passed.")


if __name__ == "__main__":
    test_base_headline()
    test_keyword_decorator_match()
    test_keyword_decorator_no_match()
    test_truncate_decorator_short()
    test_truncate_decorator_long()
