import pygame
import random
import backend

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
BODY_COLOR = (0, 0, 0)
INFO_FONT_SIZE = 20
INFO_COLOR = (0, 0, 0)


def create_random_bodies(num_bodies, mass_range, radius_range, position_range, velocity_range):
    bodies = []
    for _ in range(num_bodies):
        mass = random.uniform(*mass_range)
        radius = random.uniform(*radius_range)
        position = [
            random.uniform(*position_range),
            random.uniform(*position_range)
        ]
        velocity = [
            random.uniform(*velocity_range),
            random.uniform(*velocity_range)
        ]
        bodies.append(backend.Body(mass, radius, position, velocity))
    return bodies


def display_info(screen, font, body):
    mass_info = f"Mass: {body.mass:.2f}"
    mass_info_surface = font.render(mass_info, True, INFO_COLOR)
    screen.blit(mass_info_surface, (10, 10))

    position_info = f"Position: {body.position}"
    position_info_surface = font.render(position_info, True, INFO_COLOR)
    screen.blit(position_info_surface, (10, 30))

    velocity_info = f"Velocity: {body.velocity}"
    velocity_info_surface = font.render(velocity_info, True, INFO_COLOR)
    screen.blit(velocity_info_surface, (10, 50))
    return screen


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, INFO_FONT_SIZE)

    num_bodies = 100
    bodies = create_random_bodies(
        num_bodies, (10, 1000), (5, 9), (-HEIGHT/2, HEIGHT/2), (-10, 10))

    while True:
        dt = clock.get_time() / 1000.0  # Convert to seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:

                for body in bodies:
                    x = int(body.position[0] + WIDTH / 2)
                    y = int(body.position[1] + HEIGHT / 2)
                    if pygame.Rect(x - body.radius, y - body.radius, body.radius * 2, body.radius * 2).collidepoint(event.pos):
                        body.selected = True
                    else:
                        body.selected = False

        backend.update_bodies(bodies, dt)

        screen.fill(BACKGROUND_COLOR)
        for body in bodies:
            x = int(body.position[0] + WIDTH / 2)
            y = int(body.position[1] + HEIGHT / 2)
            pygame.draw.circle(screen, BODY_COLOR, (x, y), body.radius)
            if body.selected:
                display_info(screen, font, body)
        pygame.display.flip()
        clock.tick(120)


if __name__ == '__main__':
    main()
