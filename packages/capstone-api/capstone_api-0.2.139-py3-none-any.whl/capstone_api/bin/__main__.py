#!/usr/bin/env python3
from capstone_api.discord_api import DiscordAPI
from capstone_api.canvas_api import CanvasAPI
import argparse
import sys


def printTeams():
    discord = DiscordAPI()
    print('\n'.join([team.get("name") for team in discord.getTeamCategories()]))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--teams', default=False, action='store_true', help="print team names (scrape from discord)")
    args = ap.parse_args()

    if args.teams:
        printTeams()

if __name__ == '__main__':
    sys.exit(main())
