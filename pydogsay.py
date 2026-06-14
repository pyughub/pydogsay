#!/usr/bin/env python3
"""pydogsay — like cowsay, but with a dog."""

import sys
import textwrap
import argparse

DOG = r"""
      / \__
     (    @\___
     /         O
    /   (_____/
   /_____/   U
"""

DOG_SMALL = r"""
  __  __
 (  \/  )
  \    /
   \/\/
    WW
"""

DOG_BIG = r"""
        __
      /  ) )__
    /  /      \__
   (  (   __    ) )
   (   '-(  )--'  )
    \_   ''--''  _/
      \________/
       )      (
      /        \
     /  _/\_/\  \
    /  /      \  \
   /  /        \  \
  /  /          \  \
 (  (            )  )
  \  \          /  /
   \  \        /  /
    \  \      /  /
     \  \    /  /
      \__\  /__/
       (______)

  /^^\    /^^\
 (|  |)  (|  |)
"""

DOG_THINK = r"""
        __
      /  ) )__
    /  /      \__
   |  |    __    |
   |   '-(  )--' |
    \_   ''--'' _/
      \________/
"""

_B = '       .-\"-.\n'
_B += '     _/.-.-.\\_\n'
_B += '    ( ( o o ) )\n'
_B += '     |/  \"  \\|\n'
_B += '      \\\'---\\\'/\n'
_B += '      /`\"\"\"`\\\n'
_B += '     /   _,   \\\n'
_B += '    /__/   \\___)\n'
DOG_BONE = _B

DOGS = {
    "default": DOG,
    "small": DOG_SMALL,
    "big": DOG_BIG,
    "think": DOG_THINK,
    "bone": DOG_BONE,
}


def make_bubble(text: str, thought: bool = False) -> str:
    """Wrap text in a speech (or thought) bubble."""
    lines = text.splitlines()
    if not lines:
        lines = [""]
    max_width = max(len(line) for line in lines) if lines else 0
    max_width = max(max_width, 1)

    wrapped: list[str] = []
    for line in lines:
        if len(line) <= max_width:
            wrapped.append(line + " " * (max_width - len(line)))
        else:
            wrapped.append(line)

    if len(wrapped) == 1:
        if thought:
            border = "o"
            top = f" {border}{'_' * (max_width + 2)}{border}"
            mid = f"( {wrapped[0]} )"
            bot = f" {border}{'-' * (max_width + 2)}{border}"
        else:
            top = f" {'_' * (max_width + 2)}"
            mid = f"< {wrapped[0]} >"
            bot = f" {'-' * (max_width + 2)}"
        return f"{top}\n{mid}\n{bot}"
    else:
        if thought:
            border = "o"
            top = f" {border}{'_' * (max_width + 2)}{border}"
            bot = f" {border}{'-' * (max_width + 2)}{border}"
            mids = "\n".join(
                f"( {wrapped[i]} )" for i in range(len(wrapped))
            )
        else:
            top = f" {'_' * (max_width + 2)}"
            bot = f" {'-' * (max_width + 2)}"
            first = f"/ {wrapped[0]} \\"
            last = f"\\ {wrapped[-1]} /"
            inner = "\n".join(
                f"| {wrapped[i]} |" for i in range(1, len(wrapped) - 1)
            )
            if inner:
                mids = f"{first}\n{inner}\n{last}"
            else:
                mids = f"{first}\n{last}"
        return f"{top}\n{mids}\n{bot}"


def fit_dog(dog: str, bubble_width: int) -> str:
    """Pad the dog to roughly align with the bubble width."""
    lines = dog.splitlines()
    # Remove empty leading/trailing lines
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="pydogsay — like cowsay, but with a dog.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="dogs: " + ", ".join(DOGS),
    )
    parser.add_argument("message", nargs="*", help="Message to display (reads stdin if omitted)")
    parser.add_argument(
        "-t", "--thought", action="store_true", help="Use a thought bubble instead of speech"
    )
    parser.add_argument(
        "-d",
        "--dog",
        choices=list(DOGS),
        default="default",
        help="Dog style (default: default)",
    )
    parser.add_argument(
        "-w", "--width", type=int, default=40, help="Max width for text wrapping (default: 40)"
    )
    parser.add_argument("-l", "--list", action="store_true", help="List all dog styles and exit")
    parser.add_argument(
        "-T",
        "--tongue",
        action="store_true",
        help="Add a tongue to the default dog",
    )
    parser.add_argument(
        "-W",
        "--wag",
        action="store_true",
        help="Show a wagging animation (3 frames)",
    )

    args = parser.parse_args()

    if args.list:
        print("Available dog styles:")
        for name, art in DOGS.items():
            print(f"\n  [{name}]")
            print(textwrap.indent(art.strip(), "    "))
        sys.exit(0)

    # Get message
    if args.message:
        text = " ".join(args.message)
    else:
        text = sys.stdin.read().rstrip()
    if not text:
        text = "Woof!"

    # Wrap text
    wrapped = "\n".join(
        textwrap.fill(text, width=args.width).splitlines()
    ) if args.width > 0 else text

    # Render bubble
    bubble = make_bubble(wrapped, thought=args.thought)

    # Get dog art
    dog = DOGS[args.dog]

    # Tongue mod for default dog
    if args.tongue and args.dog == "default":
        dog = dog.replace("   U", "  UU")

    dog = fit_dog(dog, 0)

    # Wag animation
    if args.wag:
        import time
        frames = [dog, dog.replace("   U", "  UU"), dog]
        try:
            for _ in range(2):
                for frame in frames:
                    sys.stdout.write("\033[2J\033[H")  # clear screen
                    sys.stdout.write(bubble + "\n" + frame + "\n")
                    sys.stdout.flush()
                    time.sleep(0.3)
        except KeyboardInterrupt:
            pass
    else:
        print(bubble)
        print(dog)


if __name__ == "__main__":
    main()
