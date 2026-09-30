Why use a virtual environment?
A venv isolates each project's dependencies, so version conflicts don't happen and the global Python stays clean. With a requirements.txt, anyone can recreate the exact same setup

Why is .env in .gitignore?
Secrets never go into version control. .env is ignored, we commit a .env.example with placeholder values instead, and production uses a secret manager.

What did the usage numbers in your output mean? Hint: it's tokens, which you'll study on Day 8.
Tokens are the sub-word units the model reads and writes. Cost, latency and the context limit are all measured in tokens, and reasoning models also use hidden thinking tokens that count toward cost.