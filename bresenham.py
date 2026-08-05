import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Get the user's desktop display info to calculate screen size
display_info = pygame.display.Info()
DESKTOP_WIDTH = display_info.current_w
DESKTOP_HEIGHT = display_info.current_h

# Set window size to roughly 50% of your desktop's width and height
WINDOW_WIDTH = int(DESKTOP_WIDTH * 0.5)
WINDOW_HEIGHT = int(DESKTOP_HEIGHT * 0.5)

# Setup screen globally
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Interactive Bresenham's Circle Drawing - 50x50 Grid")

# Grid dimensions
GRID_SIZE = 50

# Colors (RGB)
BG_COLOR = (30, 30, 30)          # Dark background
GRID_COLOR = (60, 60, 60)        # Subtle grid lines
PIXEL_COLOR = (0, 255, 128)      # Color for circle pixels (Mint Green)
CENTER_COLOR = (255, 100, 100)   # Color for the center point (Soft Red)

def bresenham_circle(xc, yc, r):
    """Generates a set of (x, y) coordinates representing a circle using Bresenham's algorithm."""
    pixels = set()
    x = 0
    y = r
    d = 3 - 2 * r
    
    def add_symmetric_points(xc, yc, x, y):
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        for p in points:
            if 0 <= p[0] < GRID_SIZE and 0 <= p[1] < GRID_SIZE:
                pixels.add(p)

    add_symmetric_points(xc, yc, x, y)
    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        add_symmetric_points(xc, yc, x, y)
        
    return pixels
def draw_grid_and_pixels(surface, active_pixels, center_point, current_width, current_height):
    """Draws a centered square grid with perfect square pixels."""
    surface.fill(BG_COLOR)
    
    # Calculate a uniform cell size so pixels are ALWAYS perfect squares
    # We base it on the smaller window dimension to keep the 50x50 grid fully visible
    cell_size = min(current_width, current_height) / GRID_SIZE
    
    # Calculate offsets to center the grid on the screen
    grid_pixel_width = cell_size * GRID_SIZE
    offset_x = (current_width - grid_pixel_width) / 2
    offset_y = (current_height - grid_pixel_width) / 2

    gap = 1 if cell_size > 6 else 0

    # Draw active circle pixels as uniform squares
    for (x, y) in active_pixels:
        rect = pygame.Rect(
            offset_x + (x * cell_size) + gap, 
            offset_y + (y * cell_size) + gap, 
            cell_size - (gap * 2), 
            cell_size - (gap * 2)
        )
        pygame.draw.rect(surface, PIXEL_COLOR, rect)

    # Draw center point as a square
    if center_point:
        cx, cy = center_point
        center_rect = pygame.Rect(
            offset_x + (cx * cell_size) + gap, 
            offset_y + (cy * cell_size) + gap, 
            cell_size - (gap * 2), 
            cell_size - (gap * 2)
        )
        pygame.draw.rect(surface, CENTER_COLOR, center_rect)

    # Draw the grid lines forming the pixel boxes
    for i in range(GRID_SIZE + 1):
        pos = i * cell_size
        # Vertical lines
        pygame.draw.line(surface, GRID_COLOR, (offset_x + pos, offset_y), (offset_x + pos, offset_y + grid_pixel_width))
        # Horizontal lines
        pygame.draw.line(surface, GRID_COLOR, (offset_x, offset_y + pos), (offset_x + grid_pixel_width, offset_y + pos))

def main():
    """Main application loop."""
    global screen  # Tells Python to use the global screen variable defined at the top
    
    center_point = None
    circle_pixels = set()
    
    current_width = WINDOW_WIDTH
    current_height = WINDOW_HEIGHT

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.VIDEORESIZE:
                current_width, current_height = event.w, event.h
                screen = pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                
                cell_width = current_width / GRID_SIZE
                cell_height = current_height / GRID_SIZE
                grid_x = int(mouse_x // cell_width)
                grid_y = int(mouse_y // cell_height)

                if center_point is None:
                    center_point = (grid_x, grid_y)
                    circle_pixels = set() 
                else:
                    cx, cy = center_point
                    radius = round(math.hypot(grid_x - cx, grid_y - cy))
                    
                    if radius > 0:
                        circle_pixels = bresenham_circle(cx, cy, radius)
                    
                    center_point = None

        # Render everything
        draw_grid_and_pixels(screen, circle_pixels, center_point, current_width, current_height)
        pygame.display.flip()

# This is the entry point that calls main() at the very bottom of the file
if __name__ == "__main__":
    main()