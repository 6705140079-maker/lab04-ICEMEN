# Lab 04 - Group ICEMEN

## What We Did
In this lab, our group successfully collaborated on a shared GitHub repository to practice version control and automated testing. Specifically, we:
- Set up a public GitHub repository with `.gitignore` and base Python modules.
- Individually cloned the repository and configured our local Git environments.
- Created individual unit tests and shared `pytest` fixtures across multiple test files (`test_deposit.py`, `test_withdraw.py`, `test_teardown.py`, `test_shared.py`, and `conftest.py`).
- Executed frequent `git pull`, `git commit`, and `git push` commands to synchronize our work.
- Intentionally triggered and collaboratively resolved a real Git merge conflict.

## Who Did What
| Member | GitHub Username | File |
|---|---|---|
| Aung Zay Oo (6705140079) | 6705140079-maker-github | test_deposit.py |
| Thet Naing Tun (6705140062) | thetnaingtun-github | test_withdraw.py |
| Aung Khant Ko (6705140063) | aungkhantko-github | test_teardown.py |
| Thet Htoo San (6705140080) | thethtoosan-github | test_shared.py |
| Nyan Moe Aung (6705140058) | NyanMoeAung-6705140058-github | conftest.py |

## Git Contribution Summary
     4	Aung Zay Oo
     3	Thet Naing Tun
     3	Aung Khant Ko
     3	Thet Htoo San
     3	Nyan Moe Aung

## Reflection Questions

1. **Why was your push rejected, and how did you fix it?**
   Our push was rejected because another team member had already pushed their commits to GitHub, meaning our local repository was out of date. We fixed it by running `git pull` to download and merge their latest changes before running `git push` again.

2. **Why could Git not resolve the README conflict automatically?**
   Git could not resolve the conflict because multiple group members tried to modify the exact same lines (the "Who Did What" table) in `README.md` independently, requiring us to manually dictate the final combined result.

3. **What is the difference between committing and pushing?**
   Committing (`git commit`) saves a snapshot of your changes locally on your own computer, while pushing (`git push`) uploads those saved commits to the shared remote repository on GitHub so the rest of the team can see and download them.

4. **How do fixtures reduce duplicated setup code in tests?**
   Fixtures allow us to define setup steps (like initializing a `BankAccount` with 100 or 1000 balance) once, and automatically inject that pre-configured object into any test function that needs it, avoiding repetitive code.
