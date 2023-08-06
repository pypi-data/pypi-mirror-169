import asyncio
import platform

from . import request

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def get_runemetrics(players: list[str]):
    """
    Takes a list of players and accesses the runemetrics API endpoint.  The results are aggregated and return as json.
    :param players:
    :return:
    """
    urls = [
        f"https://apps.runescape.com/runemetrics/profile/profile?user={player}&activities=20"
        for player in players
    ]
    return asyncio.run(request.get(urls=urls, expected_response="json"))


def get_clan_members(clans: list[str]):
    urls = [
        f"https://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName={clan}"
        for clan in clans
    ]
    return asyncio.run(request.get(urls=urls, expected_response="csv"))
