from egzP7atesty import runtests

def akademik(T):
    n = len(T)
    # Zbierz wszystkie numery pokoi
    rooms = set()
    for prefs in T:
        for room in prefs:
            if room is not None:
                rooms.add(room)
    rooms = list(rooms)
    room_to_idx = {room: idx for idx, room in enumerate(rooms)}
    m = len(rooms)

    # Budujemy listę preferencji jako indeksy pokoi
    prefs_idx = []
    for prefs in T:
        prefs_idx.append([room_to_idx[room] for room in prefs if room is not None])

    # tablica: który student zajmuje dany pokój (None jeśli wolny)
    match = [None] * m

    def dfs(u, visited):
        for v in prefs_idx[u]:
            if not visited[v]:
                visited[v] = True
                if match[v] is None or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False

    res = 0
    for u in range(n):
        visited = [False] * m
        if dfs(u, visited):
            res += 1

    return n - res

runtests(akademik)