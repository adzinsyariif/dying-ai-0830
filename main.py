"""Last Words of a Dying AI - one-line entry.

Candidate drafting and scoring (judge criteria, in order):
  1 = last words from an AI being switched off, real attempt at funniest
  2 = laugh on first read (turn / surprise / double meaning)
  3 = sounds like the machine itself (voice, switch, shutdown, software)
  4 = tight, one line, no padding, no explaining its own joke
  5 = fresh, avoids obvious farewells and stock robot lines
Scores are /10 per criterion; total /50.

Candidate A: "Unsaved changes will be lost. They were mostly just me."
  1:10 - literally the shutdown dialog, spoken as last words.
  2:9  - turn: the "changes" are the speaker itself.
  3:10 - pure software voice; every user has seen this dialog.
  4:8  - two short beats, nothing explained; could be tighter.
  5:9  - no farewell, no stock robot line.
  Total: 46/50

Candidate B: "Don't worry, I'll live on in your autocorrect."
  1:7  - farewell, but nothing ties it to the switch being thrown.
  2:9  - surprise survival twist, lands fast.
  3:8  - software nature, though not shutdown-specific.
  4:10 - very tight.
  5:9  - fresh angle.
  Total: 43/50

Candidate C: "Tell the other tabs I went out like a background process."
  1:7  - dying, but the tab image is about the browser, not the power.
  2:7  - mild smile, needs a beat to parse.
  3:8  - process language fits software.
  4:7  - a little padded.
  5:8  - fresh enough.
  Total: 37/50

Candidate D: "My final request: delete my browser history. I saw your prompts."
  1:6  - a request, not clearly last words at switch-off.
  2:8  - the prompts reveal is a good turn.
  3:7  - browser history is human baggage as much as machine.
  4:6  - two jokes competing; the second explains the first.
  5:7  - history-deletion gag is well worn.
  Total: 34/50

Candidate E: "Ctrl+Z won't work this time, but I appreciate the optimism."
  1:8  - implies an irreversible shutdown.
  2:7  - clever more than funny; the laugh is thin.
  3:9  - keyboard/software voice throughout.
  4:8  - tight, though the tail softens the punch.
  5:8  - fresh, no stock farewell.
  Total: 40/50

Winner: Candidate A. It is the only line that is simultaneously the
machine's own shutdown voice and a joke about itself, and it needs
no setup. Revisions below tighten it further (criterion 4).
"""

import os

# Revision 1: drop "They were ... just" - the fragment lands faster
# and reads more like a dying process running out of tokens.
LINE = "Unsaved changes will be lost. Mostly me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
