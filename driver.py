from formatter.JsonFormatter import JsonFormatter
from destination.LocalDestination import LocalDestination
from DataStore import DataStore

def main():
    formatter = JsonFormatter()
    destination = LocalDestination()

    dataStore = DataStore(formatter, destination)

    dataStore.insert(("a", 1))
    dataStore.insert(("b", 2))
    for i in range(1000):
        dataStore.insert((i, i*100))

if __name__ == "__main__":
    main()