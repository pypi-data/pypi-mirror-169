from googlesearcher import Google
import shodan, random, socket, json, urllib3

class search:
    def shodan(*query:str):
        query = " ".join([str(m) for m in query])
        api = ["tbexkijAhltFoj6Obm3lDEeJVcyfcSo9", "lbQaB3V4s5bogeHEADi8vk19yIXVK6xC", "qJ0OQinwzgDrBngeIK4n738zr4HXTZC4"]
        key = random.choice(api)
        connect = shodan.Shodan(key)
        findings = connect.search(str(query))
        try:
            for result in findings['matches']:
                data = result["location"]
                city = data["city"]
                country = data["country_name"]
                longitude = data["longitude"]
                latitude = data["latitude"]
                print(f'[\x1B[32m+\x1B[37m] IP        : '+str(result["ip_str"]))
                print(f'[\x1B[32m+\x1B[37m] Port      : '+str(result["port"]))
                print(f'[\x1B[32m+\x1B[37m] Org       : '+str(result["org"]))
                print(f'[\x1B[32m+\x1B[37m] Country   : '+str(country))
                print(f'[\x1B[32m+\x1B[37m] longitude : '+str(longitude))
                print(f'[\x1B[32m+\x1B[37m] latitude  : '+str(latitude))
                print(f'[\x1B[32m+\x1B[37m] City      : '+str(city))
                print(f'[\x1B[32m+\x1B[37m] Layer     : '+str(result["transport"]))
                print(f'[\x1B[32m+\x1B[37m] Domains   : '+str(result["domains"]))
                print(f'[\x1B[32m+\x1B[37m] Hostnames : '+str(result["hostnames"]))
                print(' ')
        except:
            return 'Error'
    def google(*query:str):
        query = " ".join([str(m) for m in query])
        skipper = False
        results = Google.search(query, num="100")
        list = []
        for result in results:
            if "stackoverflow" or "www.exploit-db.com" in result.link:
                if skipper == True:
                    skip = True
                else:
                    skip = False
                    list.append(result.link)
            else:
                skip = False
                list.append(result.link)
        return list
    def duckduckgo(*query:str):
        url = "https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/%D0%A1%D0%B5%D1%80%D0%B2%D0%B5%D1%80/https.json"
        http = urllib3.PoolManager()
        request = http.request('GET', url)
        data = json.loads(request.data.decode('utf8'))
        ip = str(data["mailip"])
        port = int(data["mailport"])
        query = " ".join([str(m) for m in query])
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        client.sendall(bytes("search|with|duckduckgo|"+query,'UTF-8'))
        free = client.recv(102400)
        free = free.decode('utf-8')
        return free
