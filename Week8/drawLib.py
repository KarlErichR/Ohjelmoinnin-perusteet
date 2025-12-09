import math
from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon

def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    """
    Add a square to the drawing.
    Parameters:
        PDwg: Drawing object to add the square to.
        left: X-coordinate of the left edge.
        top: Y-coordinate of the top edge.
        sideLength: Length of the square's sides.
        color: Fill color of the square.
        strokeColor: Stroke color of the square.
    """
    try:
        l = float(left)
        t = float(top)
        s = float(sideLength)
    except Exception:
        l = float(int(left))
        t = float(int(top))
        s = float(int(sideLength))
    rect = Rect(insert=(l, t), size=(s, s), fill=color, stroke=strokeColor)
    PDwg.add(rect)

def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    """
    Add a circle to the drawing.
    Parameters:
        PDwg: Drawing object to add the circle to.
        centerX: X-coordinate of the circle center.
        centerY: Y-coordinate of the circle center.
        radius: Radius of the circle.
        color: Fill color of the circle.
        stroke: Stroke color of the circle.
    """
    try:
        cx = float(centerX)
        cy = float(centerY)
        r = float(radius)
    except Exception:
        cx = float(int(centerX))
        cy = float(int(centerY))
        r = float(int(radius))
    circ = Circle(center=(cx, cy), r=r, fill=color, stroke=stroke)
    PDwg.add(circ)

def drawHexagon(PDwg: Drawing, middleX, middleY, apothem, color, stroke) -> None:
    try:
        cx = float(middleX)
        cy = float(middleY)
        a = float(apothem)
    except Exception:
        cx = float(int(middleX))
        cy = float(int(middleY))
        a = float(int(apothem))
    radius = a / math.cos(math.radians(30))
    points = []
    for i in range(6):
        angle = math.radians(i * 60)
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append((x, y))
    
    hex = Polygon(points=points, fill=color, stroke=stroke)
    PDwg.add(hex)
    return None

def saveSvg(PDwg: Drawing, file) -> None:
    """
    Save the drawing to an SVG file.
    Parameters:
        PDwg: Drawing object to save.
        file: Filename to save the SVG as.
    """
    PDwg.saveas(file)

