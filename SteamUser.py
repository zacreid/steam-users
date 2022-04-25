from dataclasses import dataclass, asdict

@dataclass
class SteamUser:
    steamID: str

    # Summary Data
    #Public Data
    personaname: str = None
    profileurl: str = None
    avatar: str = None
    avatarmedium: str = None
    avatarfull: str = None
    personstate: int = None
    communityvisibilitystate: int = None
    profilestate: int = None
    lastlogoff: int = None
    commentpermission: bool = None
    #Private Data
    realname: str = None
    primaryclanid: int = None
    timecreated: int = None
    gameid: int = None
    cityid: str = None
    loccountrycode: str = None
    locstatecode: str = None
    loccityid: str = None

    #Friends List
    friends: list = None

    #Owned Games
    games: list = None
    game_count: int = None
    playtime: dict = None
    recent_playtime: dict = None
    total_playtime: int = None
    last_played: dict = None

    #Groups
    groups: list = None

    #Level
    level: int = None
    playerxp: int = None

    #Bans
    communitybanned: bool = None
    vacbanned: bool = None
    numberofvacbans: int = None
    dayssincelastban: int = None
    numberofgamebans: int = None
    economyban: int = None

    #Badges
    badges: list = None
    
    def asdict(self):
        return asdict(self)

    @classmethod
    def fromdict(cls, d):
        return cls(**d)