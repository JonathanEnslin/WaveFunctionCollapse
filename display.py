import pygame

pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wave Function Collapse")

clock = pygame.time.Clock()
desired_fps = 60

grid_cols = 10
grid_rows = 10

tile_height_px = (screen_height - 50) // grid_rows
tile_width_px = tile_height_px

tile_size_px = (tile_width_px, tile_height_px)

im_empty = pygame.image.load("sprites/empty.png")
im_left_turn = pygame.image.load("sprites/left_turn.png")
im_right_turn = pygame.image.load("sprites/right_turn.png")
im_straight = pygame.image.load("sprites/straight.png")
im_t_intersection = pygame.image.load("sprites/t_intersection.png")
im_cross_intersection = pygame.image.load("sprites/cross_intersection.png")
im_dead_end = pygame.image.load("sprites/dead_end.png")

images = {
    "empty": im_empty,
    "left_turn": im_left_turn,
    "right_turn": im_right_turn,
    "straight": im_straight,
    "t_intersection": im_t_intersection,
    "cross_intersection": im_cross_intersection,
    "dead_end": im_dead_end
}

scaled_images = {
    "empty": pygame.transform.scale(im_empty, tile_size_px),
    "left_turn": pygame.transform.scale(im_left_turn, tile_size_px),
    "right_turn": pygame.transform.scale(im_right_turn, tile_size_px),
    "straight": pygame.transform.scale(im_straight, tile_size_px),
    "t_intersection": pygame.transform.scale(im_t_intersection, tile_size_px),
    "cross_intersection": pygame.transform.scale(im_cross_intersection, tile_size_px),
    "dead_end": pygame.transform.scale(im_dead_end, tile_size_px)
}

tiles_surface = pygame.Surface((grid_cols * tile_width_px, grid_rows * tile_height_px))
tiles_surface.fill((255, 255, 255))

tiles_surface_position = (screen_width // 2 - tiles_surface.get_width() // 2,
                          screen_height // 2 - tiles_surface.get_height() // 2)

tiles = [[scaled_images['empty'] for _ in range(grid_cols)] for _ in range(grid_rows)]

def randomize_tiles():
    import random
    all_tiles = list(images.keys())
    for row in range(grid_rows):
        for col in range(grid_cols):
            tiles[row][col] = scaled_images[random.choice(all_tiles)]
            # apply random rotation
            tiles[row][col] = pygame.transform.rotate(tiles[row][col], 90 * random.randint(0, 3))


randomize_tiles()

timer_interval_ms = 750
timer_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event_id, timer_interval_ms)

running = True
while running:
    clock.tick(desired_fps)

    tiles_surface.fill((255, 255, 255))

    for row in range(grid_rows):
        for col in range(grid_cols):
            tiles_surface.blit(tiles[row][col], (col * tile_width_px,
                                          row * tile_height_px))

    screen.blit(tiles_surface, tiles_surface_position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_event_id:
            randomize_tiles()

    pygame.display.flip()

pygame.quit()
