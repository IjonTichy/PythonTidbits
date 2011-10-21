#!/usr/bin/python

from Tkinter import *
import math
from collections import Iterable


def flatten(x):
    for i in x:
        if isinstance(i, Iterable):
            yield flatten(i)
        else:
            yield i


class PlotError    (Exception):   pass
class NoLastError  (PlotError):   pass
class NoPlotError  (PlotError):   pass
class NoLineError  (NoPlotError): pass
class NoCircleError(NoPlotError): pass



class Vector2(object):
    """A simple vector class for use in the plotter."""
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    @property
    def coord(self):
        return ((self.x1, self.y1), (self.x2, self.y2))

    def setCoord(self, coord1, coord2):
        if (not isinstance(coord1, tuple)) or (not isinstance(coord2, tuple)):
            raise ValueError("not coordinates")

        if (len(coord1) != 2) or (len(coord2) != 2):
            raise ValueError("proper coordinates not specified (invalid length)")

        try:
            for i in (coord1 + coord2):
                    i = int(i)
        except ValueError:
            raise ValueError("proper coordinates not specified (non-integer)")

        self.x1, self.y1, self.x2, self.y2 = coord1 + coord2

    @property
    def velocity(self):
        return (self.x2-self.x1, self.y2-self.y1)

    @property
    def center(self):
        vx, vy = [i/2.0 for i in self.velocity]
        return (self.x1+vx, self.y1+vy)

    @property
    def signs(self):
        return [(1 if i >= 0 else -1) for i in self.center]

    @property
    def magnitude(self):
        vel = self.velocity
        return ((vel[0]**2)+(vel[1]**2))**0.5  # it's pythagorean

    @property
    def norm(self):
        vel = self.velocity
        mag = self.magnitude
        return tuple(i / mag for i in vel)

    def __add__(self, v2):  # with one of the uglier list comprehensions ever
        x1, y1, x2, y2 = [i+j for i, j in zip(flatten(self.coord), flatten(v2.coord))]
        return Vector2(x1, y1, x2, y2)

    def __repr__(self):
        return "Vector2{0}".format(self.coord)

class Plotter(Frame):
    width      = 750
    height     = 750
    MAXLASTLEN = 0

    lineTagStr = "L:{x1}:{y1}x{x2}:{y2}"
    circleTagStr = "C:{x}:{y}r{rad}s{spokes}"
    polygonTagStr = "P:{x}:{y}r{rad}s{sides}"

    #####
    ###
    # BEGIN INTERNAL FUNCTIONS
    ###
    #####


    def __init__(self, parent=None, width=width, height=height):
        Frame.__init__(self, parent)
        self.canvas = Canvas(self, width=width, height=height, bg="white")
        self.plotCenter = (int(width/2), int(height/2))
        self.canvas.pack()
        for x in range(0, self.plotCenter[0], 10):
            x1 = self.plotCenter[0]+x
            x2 = self.plotCenter[0]-x
            self.canvas.create_line(x1, 0, x1, height, fill="#CCCCCC", tag="grid")
            self.canvas.create_line(x2, 0, x2, height, fill="#CCCCCC", tag="grid")

        for y in range(0, self.plotCenter[1], 10):
            y1 = self.plotCenter[1]+y
            y2 = self.plotCenter[1]-y
            self.canvas.create_line(0, y1, width, y1, fill="#CCCCCC", tag="grid")
            self.canvas.create_line(0, y2, width, y2, fill="#CCCCCC", tag="grid")
        self.__lines = []
        self.__polygons = []
        self.__circles = []
        self.__last = {}


    @property
    def plots(self):
        return self.__lines + self.__polygons + self.__circles

    def __plot(self, x1, y1, x2, y2):
        x1, y1, x2, y2 = [int(i) for i in (x1, y1, x2, y2)]

        nx1, ny1, nx2, ny2 = (x1+self.plotCenter[0], -y1+self.plotCenter[1],
                              x2+self.plotCenter[0], -y2+self.plotCenter[1])

        tagStr = Plotter.lineTagStr.format(x1=x1, x2=x2, y1=y1, y2=y2)

        self.__lines.append(((x1, y1), (x2, y2), tagStr))
        self.canvas.create_line(nx1, ny1, nx2, ny2, fill="black", tag=tagStr)

        return nx1, ny1, nx2, ny2


    def __plotCircle(self, x, y, radius, spokes=0):
        x, y, radius = [int(i) for i in (x, y, radius)]

        nx, ny = self.plotCenter[0]+x, self.plotCenter[1]-y
        tagStr = Plotter.circleTagStr.format(x=x, y=y, rad=radius, spokes=spokes)
        self.__circles.append(((x, y), radius, tagStr))
        self.canvas.create_oval(nx-radius, ny-radius, nx+radius, ny+radius,
                                outline="black", tag=tagStr)
        if spokes > 0:
            spokeInterval = 180.0/spokes
            spokeCount = 0
            spokeDegrees = []
            while spokeCount < 180:
                spokeDegrees.append(spokeCount)
                spokeCount += spokeInterval

            for spoke in spokeDegrees:
                x1 = radius * math.sin(math.radians(spoke))
                y1 = radius * math.cos(math.radians(spoke))
                nx1, nx2 = nx+x1, nx-x1
                ny1, ny2 = ny+y1, ny-y1
                self.canvas.create_line(nx1, ny1, nx2, ny2, fill="black",
                                        tag=tagStr)

        return nx, ny, radius, spokes


    def __plotPolygon(self, x, y, radius, sides, rotation=0):
        # TODO: add spokes PROPERLY
        x, y, radius, sides = [int(i) for i in (x, y, radius, sides)]
        nx, ny = self.plotCenter[0]+x, self.plotCenter[1]-y
        tagStr = Plotter.polygonTagStr.format(x=x, y=y, rad=radius, sides=sides,
                                              rot=rotation)
        self.__polygons.append(((x, y), radius, tagStr))

        cornerInterval = 360.0/sides
        cornerCount = 0.0
        cornerDegrees = []
        cornerCoords = []

        while cornerCount < 360.0:
            cornerDegrees.append(cornerCount + rotation)
            cornerCount += cornerInterval

        for corner in cornerDegrees:
            x1 = radius * math.sin(math.radians(corner))
            y1 = radius * math.cos(math.radians(corner))
            cornerCoords += [(nx+x1, ny+y1)]

        corners = list(flatten(cornerCoords))

        self.canvas.create_polygon(*corners, outline="black", fill="",
                                   tag=tagStr)

        return nx, ny, radius, sides


    def __remove(self, x1, y1, x2, y2):
        x1, y1, x2, y2 = [int(i) for i in (x1, y1, x2, y2)]

        nx1, ny1, nx2, ny2 = (x1+self.plotCenter[0], -y1+self.plotCenter[1],
                              x2+self.plotCenter[0], -y2+self.plotCenter[1])

        tagStr = Plotter.lineTagStr.format(x1=x1, x2=x2, y1=y1, y2=y2)

        tagTuple = ((x1, y1), (x2, y2), tagStr)
        if tagTuple in self.__lines:
            self.__lines.remove(tagTuple)
            self.canvas.delete(tagStr)
            return nx1, ny1, nx2, ny2, tagStr
        else:
            reason = "no such line: {0}".format(tagStr)
            raise NoLineError(reason)


    def __removeCircle(self, x, y, radius, spokes):
        x, y, radius = [int(i) for i in (x, y, radius)]

        nx, ny = self.plotCenter[0]+x, self.plotCenter[1]-y

        tagStr = Plotter.circleTagStr.format(x=x, y=y, rad=radius, spokes=spokes)
        tagTuple = ((x, y), radius, tagStr)

        if tagTuple in self.__circles:
            self.__circles.remove(tagTuple)
            self.canvas.delete(tagStr)
            return nx, ny, radius
        else:
            reason = "no such circle: {0}".format(tagStr)
            raise NoCircleError(reason)


    def __removePolygon(self, x, y, radius, sides, rotation):
        x, y, radius, sides = [int(i) for i in (x, y, radius, sides)]

        nx, ny = self.plotCenter[0]+x, self.plotCenter[1]-y

        tagStr = Plotter.polygonTagStr.format(x=x, y=y, rad=radius, sides=sides,
                                              rot=rotation)
        tagTuple = ((x, y), radius, tagStr)

        if tagTuple in self.__polygons:
            self.__polygons.remove(tagTuple)
            self.canvas.delete(tagStr)
            return nx, ny, radius, sides
        else:
            reason = "no such polygon: {0}".format(tagStr)
            raise NoCircleError(reason)


    def __trimLast(self, key):
        if Plotter.MAXLASTLEN < 1:
            return
        l = len(self.__last[key])
        if l > Plotter.MAXLASTLEN:
            self.__last[key] = self.__last[key][l-Plotter.MAXLASTLEN:]

    #####
    ###
    # END INTERNAL FUNCTIONS
    ###
    #####

    def clear(self):
        for line in self.plots:
            self.canvas.delete(line[2])

        self.__lines = []
        self.__last  = {}


    def plotLine(self, x1, y1, x2, y2):
        self.__plot(x1, y1, x2, y2)

        if 'line' not in self.__last:
            self.__last['line'] = [(x1, y1, x2, y2)]
        else:
            self.__last['line'].append((x1, y1, x2, y2))
            self.__trimLast('line')


    def removeLine(self, x1, y1, x2, y2):
        self.__remove(x1, y1, x2, y2)
        if 'line' in self.__last:
            while (x1, y1, x2, y2) in self.__last['line']:
                self.__last['line'].remove((x1, y1, x2, y2))


    def popLine(self):
        if 'line' not in self.__last:
            raise NoLastError('there is no line history')
        if not self.__last['line']:
            raise NoLastError('line history exhausted')
        coord = self.__last['line'].pop()
        self.__remove(*coord)
        return coord


    def calculatePerpend(self, x1, y1, x2, y2):
        vec = Vector2(x1, y1, x2, y2) # vectors simplified this so damned much
        dx, dy, cx, cy = vec.center * 2
        sx, sy = vec.signs
        px, py = [(abs(i) * j) for (i, j) in zip((dy, dx), (-sx, sy))]
        return cx, cy, px, py      # ^ apply sign, but flip px's sign


    def plotPerpend(self, x1, y1, x2, y2):
        self.__plot(x1, y1, x2, y2)
        cx, cy, px, py =  self.calculatePerpend(x1, y1, x2, y2)
        coord = (cx+px, cy+py, cx-px, cy-py)
        self.__plot(*coord)
        if 'perpend' not in self.__last:
            self.__last['perpend'] = [((x1, y1, x2, y2), coord)]
        else:
            self.__last['perpend'].append(((x1, y1, x2, y2), coord))
            self.__trimLast('perpend')


    def removePerpend(self, x1, y1, x2, y2):
        self.__remove(x1, y1, x2, y2)
        cx, cy, px, py =  self.calculatePerpend(x1, y1, x2, y2)
        coord = (cx+px, cy+py, cx-px, cy-py)
        self.__remove(*coord)
        if 'perpend' in self.__last:
            while ((x1, y1, x2, y2), coord) in self.__last['perpend']:
                self.__last['perpend'].remove(((x1, y1, x2, y2), coord))


    def popPerpend(self):
        if 'perpend' not in self.__last:
            raise NoLastError('there is no perpendicular history')
        if not self.__last['perpend']:
            raise NoLastError('perpendicular history exhausted')
        coord, coord2 = self.__last['perpend'].pop()

        self.__remove(*coord)
        self.__remove(*coord2)
        return coord, coord2


    def plotParallels(self, x1, y1, x2, y2, length):
        px, py =  self.calculatePerpend(x1, y1, x2, y2)[2:]
        vec = Vector2(0, 0, px, py)
        npx, npy = [i*length for i in vec.norm]
        self.__plot(x1+npx, y1+npy, x1-npx, y1-npy)
        self.__plot(x2+npx, y2+npy, x2-npx, y2-npy)
        if 'parallel' not in self.__last:
            self.__last['parallel'] = [((x1, y1, x2, y2), length)]
        else:
            self.__last['parallel'].append(((x1, y1, x2, y2), length))
            self.__trimLast('parallel')


    def removeParallels(self, x1, y1, x2, y2, length):
        px, py =  self.calculatePerpend(x1, y1, x2, y2)[2:]
        vec = Vector2(0, 0, px, py)
        npx, npy = [i*length for i in vec.norm]
        self.__remove(x1+npx, y1+npy, x1-npx, y1-npy)
        self.__remove(x2+npx, y2+npy, x2-npx, y2-npy)
        if 'parallel' in self.__last:
            while ((x1, y1, x2, y2), length) in self.__last['parallel']:
                self.__last['parallel'].remove(((x1, y1, x2, y2), length))


    def popParallels(self):
        if 'parallel' not in self.__last:
            raise NoLastError('there is no parallel history')
        if not self.__last['parallel']:
            raise NoLastError('parallel history exhausted')

        coord, length = self.__last['parallel'].pop()
        x1, y1, x2, y2 = coord

        px, py =  self.calculatePerpend(x1, y1, x2, y2)[2:]
        vec = Vector2(0, 0, px, py)
        npx, npy = [i*length for i in vec.norm]
        coord = (x1+npx, y1+npy, x1-npx, y1-npy)
        coord2 = (x2+npx, y2+npy, x2-npx, y2-npy)
        self.__remove(*coord)
        self.__remove(*coord2)
        return coord, coord2


    def plotCircle(self, x, y, radius, spokes):
        self.__plotCircle(x, y, radius, spokes)

        if 'circle' not in self.__last:
            self.__last['circle'] = [(x, y, radius, spokes)]
        else:
            self.__last['circle'].append((x, y, radius, spokes))
            self.__trimLast('circle')


    def removeCircle(self, x, y, radius, spokes=0):
        self.__removeCircle(x, y, radius, spokes)
        if 'circle' in self.__last:
            while (x, y, radius, spokes) in self.__last['circle']:
                self.__last['circle'].remove((x, y, radius, spokes))


    def popCircle(self):
        if 'circle' not in self.__last:
            raise NoLastError('there is no circle history')
        if not self.__last['circle']:
            raise NoLastError('circle history exhausted')
        coord = self.__last['circle'].pop()
        self.__removeCircle(*coord)
        return coord


    def plotPolygon(self, x, y, radius, sides, rotation):
        self.__plotPolygon(x, y, radius, sides, rotation)

        if 'polygon' not in self.__last:
            self.__last['polygon'] = [(x, y, radius, sides, rotation)]
        else:
            self.__last['polygon'].append((x, y, radius, sides, rotation))
            self.__trimLast('polygon')


    def removePolygon(self, x, y, radius, sides, rotation):
        self.__removePolygon(x, y, radius, sides, rotation)
        if 'polygon' in self.__last:
            while (x, y, radius, sides, rotation) in self.__last['polygon']:
                self.__last['polygon'].remove((x, y, radius, sides, rotation))


    def popPolygon(self):
        if 'polygon' not in self.__last:
            raise NoLastError('there is no polygon history')
        if not self.__last['polygon']:
            raise NoLastError('polygon history exhausted')
        coord = self.__last['polygon'].pop()
        self.__removePolygon(*coord)
        return coord


if __name__ == "__main__": # self-test code
    import doctest, random
    doctest.testmod()

    root = Tk()
    root.title("Plotter")
    plot = Plotter(root, random.randrange(400,600), random.randrange(400,600))
    plot.pack()
    root.mainloop()

