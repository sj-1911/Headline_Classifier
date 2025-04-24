with open("Headlines.txt", "r", encoding="utf-8") as f:
    headlines = [line.strip() for line in f.readlines() if line.strip()]
