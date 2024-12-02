# maintaing a single copy of our application state


class ApplicationState:
    instance = None

    def __init__(self) -> None:
        self.isLoggedIn = False

    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn)

# but if we get a second state of the app and instaite it
# and the set its login to True even though they are different state
# we still get the first appState1 to be true beacause we cant create more than one
appState2 = ApplicationState.getAppState()
# SET FIRST APP STATE LOGIN TO BE True
# appState1.isLoggedIn = True
appState2.isLoggedIn = True


# IF WE LOG BOTH OUT WE REALISE THAT BOTH STATE HAS TURN TRUE

print(appState1.isLoggedIn)
print(appState2.isLoggedIn)
