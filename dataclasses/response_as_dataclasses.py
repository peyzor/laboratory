from dataclasses import dataclass

import requests


def get_top_steam_games():
    top_steam_games_url = "https://api.steampowered.com/ISteamChartsService/GetGamesByConcurrentPlayers/v1/"
    response = requests.get(top_steam_games_url)
    # print(json.dumps(response.json(), indent=4))
    return response.json()


@dataclass
class Rank:
    rank: int
    appid: int
    concurrent_in_game: int
    peak_in_game: int


@dataclass
class Response:
    last_update: int
    ranks: list[Rank]

    def __post_init__(self):
        self.ranks = [Rank(**rank) for rank in self.ranks]


@dataclass
class TopSteamGames:
    response: Response

    def __post_init__(self):
        self.response = Response(**self.response)


def main():
    top_games_response = get_top_steam_games()
    top_games = TopSteamGames(**top_games_response)
    # print(top_games)
    for game in top_games.response.ranks[:3]:
        print(game)


if __name__ == '__main__':
    main()
