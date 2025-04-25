with open("Headlines.txt", "r", encoding="utf-8") as f:
    headlines = [line.strip() for line in f.readlines() if line.strip()]

headlines = [
    "113 million-year-old ‘hell ant’ found in Brazil is the oldest ever found, scientists say",
    "2025 NFL draft",
    "A 3-week-old baby received a heart transplant 14 years ago and gained a ‘donor mom’",
    "A billionaire Trump supporter has harsh words for the president about his trade war",
    "An ancient ‘terror crocodile’ became a dinosaur-eating giant. Scientists say they now know why",
    "Apple’s new MacBook Air M4 just hit a new low price",
    "Canadian voters",
    "Concerned about US vaccine misinformation and access, public health experts start Vaccine Integrity Project",
    "DNC pushes back on David Hogg’s plans to support primary challenges against Democratic incumbents",
    "Fake tan, fancy nails: How marathons became a catwalk for beauty",
    "Gunman in 2022 mass shooting at suburban Chicago July Fourth parade sentenced to life in prison",
    "How to make exterior wood window shutters",
    "Motorola’s iconic flip phone gets an AI reboot",
    "Simone Biles says gymnastics rivalry with friend Rebeca Andrade has ‘pushed the sport forward’",
    "Zoo welcomes baby elephant born through artificial insemination"
]

labels = [
    "Science",      # headline 1
    "Sports",       # headline 2
    "Health",       # headline 3
    "Politics",     # headline 4
    "Science",      # headline 5
    "Technology",   # headline 6
    "Politics",     # headline 7
    "Health",       # headline 8
    "Politics",     # headline 9
    "Lifestyle",    # headline 10
    "Politics",     # headline 11
    "Lifestyle",    # headline 12
    "Technology",   # headline 13
    "Sports",       # headline 14
    "Science"       # headline 15
]
