
import requests

name = "stcutils"
version = "20220927"

def get(problem, subpart="value"):
    try:
        url = f"https://raw.githubusercontent.com/paulbaumgarten/stc-tester/main/{problem}.json"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            if subpart in data.keys():
                return data[subpart]
            else:
                print("*" * 50)
                print("STC Utils: Invalid subpart requested")
                print("Subparts available: "+str(list(data.keys())))
                print("*" * 50)
                return None
        else:
            print("*" * 50)
            print("STC Utils: Invalid problem requested")
            print("*" * 50)
            return None
    except Exception as e:
        print("*" * 50)
        print("STC Utils: Network error")
        print("*" * 50)
        print()

def test():
    return get("test") == "Hello world"

def input_list_int(prompt=""):
    return [ int(x) for x in input(prompt).split(" ") ] 

def input_list_float(prompt=""):
    return [ float(x) for x in input(prompt).split(" ") ] 

if __name__=="__main__":
    print(test())


