from .discord_api import DiscordAPI
from .canvas_api import CanvasAPI
import argparse
import sys


def printTeams():
    discord = DiscordAPI()
    for team in discord.getTeamCategories():
        print(team.get('name'))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--teams', help="print team names (scrape from discord)")
    args = ap.parse_args()

    if args.teams:
        printTeams()

if __name__ == '__main__':
    sys.exit(main())
