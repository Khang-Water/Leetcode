import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    lists = list(players.shape)
    return lists