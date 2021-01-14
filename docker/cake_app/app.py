import os

def main():
    print("Cakes are the best!")
    with open("/app/favorites_cakes.txt") as f:
        print(f.read())
    print(f"And I like {os.environ['MY_CAKE']} too!")
    print("i'm on a new branch!")
    print("solve example issue")
    

if __name__ == "__main__":
    main()