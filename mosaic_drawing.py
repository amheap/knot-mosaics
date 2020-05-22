import math
import cairo
import numpy as np


def init_context(surface, scale, line_width=0.15):
    ctx = cairo.Context(surface)
    ctx.scale(scale, scale)  # Normalizing the canvas
    ctx.set_line_width(line_width)
    ctx.set_source_rgb(0, 0, 0)
    return ctx


def draw_box(surface, scale, x=0, y=0, line_width=.03):
    ctx = init_context(surface, scale, line_width=line_width)
    ctx.translate(x, y)
    ctx.rectangle(0, 0, 1, 1)
    ctx.stroke()


def draw_arc(ctx):
    ctx.move_to(0.5, 0)
    ctx.arc(0, 0, 0.5, 0, math.pi / 2)


def t4(surface, scale, x=0, y=0):
    ctx = init_context(surface=surface, scale=scale)
    ctx.translate(x, y)
    draw_arc(ctx)
    ctx.stroke()
    draw_box(surface, scale,  x, y)


def t0(surface, scale, x=0, y=0):
    draw_box(surface, scale,  x, y)


def t1(surface, scale, x=0, y=0):
    draw_box(surface, scale, x, y)
    ctx = init_context(surface=surface, scale=scale)
    ctx.translate(x, y)
    ctx.translate(0, 1)
    ctx.rotate(-math.pi / 2)
    draw_arc(ctx)
    ctx.stroke()


def t2(surface, scale, x=0, y=0):
    ctx = init_context(surface=surface, scale=scale)
    ctx.translate(x, y)
    ctx.translate(1, 1)
    ctx.rotate(math.pi)
    draw_arc(ctx)
    ctx.stroke()

    draw_box(surface, scale, x, y)


def t3(surface, scale, x=0, y=0):
    ctx = init_context(surface=surface, scale=scale)
    ctx.translate(x, y)
    ctx.translate(1, 0)
    ctx.rotate(math.pi / 2)
    draw_arc(ctx)
    ctx.stroke()

    draw_box(surface, scale, x, y)


def t5(surface, scale, x=0, y=0):
    ctx = init_context(surface=surface, scale=scale)
    ctx.translate(x, y)
    ctx.move_to(0, 0.5)
    ctx.line_to(1, 0.5)
    ctx.stroke()

    draw_box(surface, scale, x, y)


def t6(surface, scale, x=0, y=0):
    ctx = init_context(surface=surface, scale=scale)
    ctx.translate(x, y)
    ctx.rotate(math.pi/2)
    ctx.translate(0, -1)
    ctx.move_to(0, 0.5)
    ctx.line_to(1, 0.5)
    ctx.stroke()

    draw_box(surface, scale, x, y)


def t7(surface, scale, x=0, y=0):
    t1(surface, scale,  x, y)
    t3(surface, scale,  x, y)


def t8(surface, scale, x=0, y=0):
    t2(surface, scale,  x, y)
    t4(surface, scale,  x, y)


def t9(surface, scale, x=0, y=0):
    t5(surface, scale,  x, y)

    ctx = init_context(surface=surface, scale=scale)
    ctx.translate(x, y)
    ctx.rotate(math.pi / 2)
    ctx.translate(0, -1)
    ctx.move_to(0, 0.5)
    ctx.line_to(.35, 0.5)
    ctx.move_to(.65, 0.5)
    ctx.line_to(1, 0.5)
    ctx.stroke()


def t10(surface, scale, x=0, y=0):
    t6(surface, scale,  x, y)

    ctx = init_context(surface=surface, scale=scale)
    ctx.translate(x, y)
    ctx.move_to(0, 0.5)
    ctx.line_to(.35, 0.5)
    ctx.move_to(.65, 0.5)
    ctx.line_to(1, 0.5)
    ctx.stroke()

tile_functions = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]


def draw_knot(m, surface, scale, size=7):
    width = scale * size
    m = np.array(m)
    for i, tile in enumerate(m.flatten()):
        tile_functions[tile](surface, scale, x=divmod(i, size)[1], y=divmod(i, size)[0])
    draw_box(surface, width, line_width=.06 / size)  # draw a thicker outside border on the mosaic
