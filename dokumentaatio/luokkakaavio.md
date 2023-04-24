```mermaid
classDiagram
    Ghost "1" --> Gameloop
    Level "1.." --> Gameloop
    Spoon "1.." --> Level

        class Ghost{
        image
        alive
        timer
        flip
        speed_x
        speed_y
        jumping
        in_air
        rect
        rect.center
        }
        class Level{
        level
        obstacle_group
        spoon_group
        }
        class Spoon{
            image
            rect
            rect.center
        }
        class Gameloop{
        ghost
        level
        right
        left
        running
        screen
        clock
        }