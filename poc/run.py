# %%
from src.Game import Game

def main():
    game = Game()
    for _ in range(6):
        ( 
            game
            .read_a_world_from_user()
            .guess()
            .display()
        )

if __name__ == "__main__":
    main()

# %%
