import requests

def fetch_random_user_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response=requests.get(url)
    data=response.json()
    if data["success"] and "data"in data: #"data" is on object in the response given by API. ek column ka naam hai data
        user_data=data["data"]
        # print(user_data)
        user_name=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return user_name, country
    else:
        raise Exception("Failed to fetch user data")
    
def main():

    try:
        user_name, country=fetch_random_user_freeapi()
        print(f"usrname:{user_name}\n Country:{country}") 
    except Exception as e:
        print(str(e))


if __name__=="__main__":
    main()

