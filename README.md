# Lab 04 - Group ICEMEN

## What We Did
In this lab, our group successfully collaborated on a shared GitHub repository to practice version control and automated testing. Specifically, we:
- Set up a public GitHub repository with `.gitignore` and base Python modules.
- Individually cloned the repository and configured our local Git environments.
- Created individual unit tests and shared `pytest` fixtures across multiple test files (`test_deposit.py`, `test_withdraw.py`, `test_teardown.py`, `test_shared.py`, and `conftest.py`).
- Executed frequent `git pull`, `git commit`, and `git push` commands to synchronize our work.
- Intentionally triggered and collaboratively resolved a real Git merge conflict.
- Used Git commands (`git log`, `git diff`, `git status`) to inspect changes and verify every member's contributions.

## Who Did What
| Member | GitHub Username | File |
|---|---|---|
| Aung Zay Oo (6705140079) | 6705140079-maker-github | test_deposit.py |
| Thet Naing Tun (6705140062) | thetnaingtun-github | test_withdraw.py |
| Aung Khant Ko (6705140063) | aungkhantko-github | test_teardown.py |
| Thet Htoo San (6705140080) | thethtoo2911-github | test_shared.py |
| Nyan Moe Aung (6705140058) | NyanMoeAung-6705140058-github | conftest.py |

- **Resolution:** We resolved this by opening the `README.md` file, deleting the conflict markers (`<<<<<<< HEAD`, `=======`, `>>>>>>>`), and keeping both members' rows in the final table since everyone needs to be listed[cite: 1]. After saving, we staged the file and committed the resolution[cite: 1].
- **Why Git Could Not Resolve It Automatically:** Git performs merges line-by-line[cite: 1]. Because two different commits added different text onto the exact same lines of the `README.md` file concurrently, Git could not automatically decide which changes to keep or overwrite without human intervention[cite: 1].

## Git Contribution Summary
```text
     4	Aung Zay Oo
     3	Thet Naing Tun
     3	Aung Khant Ko
     3	Thet Htoo San
     3	Nyan Moe Aung
