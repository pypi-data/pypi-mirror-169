#    fchart3 draws beautiful deepsky charts in vector formats
#    Copyright (C) 2005-2021 fchart authors
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from math import pi

import cairo

from fchart3.graphics_interface import INCH, DPMM, POINT, GraphicsInterface, DrawMode

DPI_IMG = 100.0
DPMM_IMG = DPI_IMG/INCH
PONT_IMG = 1.0/DPMM_IMG

A4_WIDTH_POINTS = 594
A4_HEIGHT_POINTS = 842


class CairoDrawing(GraphicsInterface):
    """
    A CairoDrawing - implement Graphics interface using PyCairo
    """
    def __init__(self, fobj, width, height, format='pdf', pixels=False, landscape=False, tolerance=None, jpg_quality=90):
        """
        :param fobj: file object
        :param width: width in mm
        :param height: height in mm
        :param format: format png/svg
        :param pixels: True if units of width/height are pixels
        :param landscape: True if orientation of page is landscape
        :param tolerance: Cairo context drawing tolerance, use it for speedup of graphics operations
        """
        GraphicsInterface.__init__(self, (width / DPMM_IMG if pixels else width) , (height / DPMM_IMG if pixels else height))

        self.fobj = fobj
        self.format = format
        self.landscape = landscape
        self.surface = None
        self.context = None
        self.sfc_width = None
        self.sfc_height = None
        self.tolerance = tolerance
        self.set_origin(self.gi_width/2.0, self.gi_height/2.0)
        self.jpg_quality = jpg_quality

    def new(self):
        if self.format in ['png', 'jpg']:
            self.set_point_size(PONT_IMG)
            self.sfc_width = int(self.gi_width * DPMM_IMG)
            self.sfc_height = int(self.gi_height * DPMM_IMG)
            self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.sfc_width, self.sfc_height)
            self.surface.set_device_scale(DPMM_IMG, DPMM_IMG)
            self.surface.set_device_offset(self.gi_origin_x*DPMM_IMG, self.gi_origin_y*DPMM_IMG)
        elif self.format == 'svg':
            self.sfc_width = int(self.gi_width * DPMM)
            self.sfc_height = int(self.gi_height * DPMM)
            self.surface = cairo.SVGSurface(self.fobj, self.sfc_width, self.sfc_height)
            self.surface.set_device_scale(DPMM, DPMM)
            self.surface.set_device_offset(self.gi_origin_x*DPMM, self.gi_origin_y*DPMM)
        else:
            if self.landscape:
                self.sfc_width = A4_HEIGHT_POINTS
                self.sfc_height = A4_WIDTH_POINTS
                self.surface = cairo.PDFSurface(self.fobj, self.sfc_width, self.sfc_height)
                self.surface.set_device_scale(DPMM, DPMM)
                self.surface.set_device_offset(self.gi_origin_x*DPMM + 15*DPMM, self.gi_origin_y*DPMM + (210-self.gi_height)*DPMM/2)
            else:
                self.sfc_width = A4_WIDTH_POINTS
                self.sfc_height = A4_HEIGHT_POINTS
                self.surface = cairo.PDFSurface(self.fobj, self.sfc_width, self.sfc_height)
                self.surface.set_device_scale(DPMM, DPMM)
                self.surface.set_device_offset(self.gi_origin_x*DPMM + (210-self.gi_width)*DPMM/2, self.gi_origin_y*DPMM + 15*DPMM)
        self.context = cairo.Context(self.surface)
        if self.tolerance is not None:
            self.context.set_tolerance(self.tolerance)
        self.set_font('Times-Roman', 12*POINT)
        self.set_linewidth(10)

    def clear(self):
        if self.gi_background_rgb:
            self.context.set_source_rgb(self.gi_background_rgb[0], self.gi_background_rgb[1], self.gi_background_rgb[2])
            self.context.rectangle(-self.sfc_width/2, -self.sfc_height/2, self.sfc_width, self.sfc_height)
            self.context.fill()

    def save(self):
        GraphicsInterface.save(self)
        self.context.save()

    def restore(self):
        GraphicsInterface.restore(self)
        self.context.restore()

    def set_font(self, font='Arial', fontsize=12*POINT):
        GraphicsInterface.set_font(self, font, fontsize)
        self.context.set_font_size(self.gi_fontsize)
        if isinstance(font, cairo.FontFace):
            self.context.set_font_face(font)
        else:
            self.context.select_font_face(self.gi_font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    def set_linewidth(self, linewidth):
        GraphicsInterface.set_linewidth(self,linewidth)
        self.context.set_line_width(linewidth)

    def set_solid_line(self):
        GraphicsInterface.set_solid_line(self)

    def set_dashed_line(self, on, off, start=0.0):
        GraphicsInterface.set_dashed_line(self, on, off, start)

    def line(self, x1, y1, x2, y2):
        self.context.set_source_rgb(self.gi_pen_rgb[0], self.gi_pen_rgb[1], self.gi_pen_rgb[2])
        self.context.move_to(x1, -y1)
        self.context.line_to(x2, -y2)
        self.context.set_dash(self.gi_dash_style[0], self.gi_dash_style[1])
        self.context.stroke()

    def rectangle(self, x, y, width, height, mode=DrawMode.BORDER):
        self.context.rectangle(x, -y, width, height)
        self._draw_element(mode)

    def circle(self, x, y, r, mode=DrawMode.BORDER):
        self._moveto(x+r, y)
        self.context.arc(x, -y, r, 0, 2.0*pi)
        self._draw_element(mode)

    def polygon(self, vertices, mode=DrawMode.BORDER):
        self.context.move_to(vertices[0][0], -vertices[0][1])
        for i in range(1, len(vertices)):
            self.context.line_to(vertices[i][0], -vertices[i][1])
        self.context.close_path()
        self._draw_element(mode)

    def ellipse(self, x, y, rlong, rshort, posangle, mode=DrawMode.BORDER):
        self.context.save()
        scale = rshort/rlong
        self.context.translate(x, -y)
        self.context.rotate(-posangle)
        self.context.scale(1, scale)
        self._moveto(rlong, 0)
        self.context.arc(0, 0, rlong, 0, 2.0*pi)
        self.context.restore()
        self._draw_element(mode)

    def _draw_element(self, mode):
        if mode == DrawMode.BORDER:
            self.context.set_source_rgb(self.gi_pen_rgb[0], self.gi_pen_rgb[1], self.gi_pen_rgb[2])
            self.context.set_dash(self.gi_dash_style[0], self.gi_dash_style[1])
            self.context.stroke()
        elif mode == DrawMode.FILL:
            self.context.set_source_rgb(self.gi_fill_rgb[0], self.gi_fill_rgb[1], self.gi_fill_rgb[2])
            self.context.fill()
        else:
            self.context.set_source_rgb(self.gi_fill_rgb[0], self.gi_fill_rgb[1], self.gi_fill_rgb[2])
            self.context.fill_preserve()
            self.context.set_source_rgb(self.gi_pen_rgb[0], self.gi_pen_rgb[1], self.gi_pen_rgb[2])
            self.context.stroke()

    def text(self, text):
        self.context.show_text(text)

    def text_right(self, x, y, text):
        self._moveto(x, y)
        self.context.set_source_rgb(self.gi_pen_rgb[0], self.gi_pen_rgb[1], self.gi_pen_rgb[2])
        self.context.show_text(text)

    def text_left(self, x, y, text):
        xbearing, ybearing, width, height, dx, dy = self.context.text_extents(text)
        self._moveto(x-width-xbearing, y)
        self.context.set_source_rgb(self.gi_pen_rgb[0], self.gi_pen_rgb[1], self.gi_pen_rgb[2])
        self.context.show_text(text)

    def text_centred(self, x, y, text):
        xbearing, ybearing, width, height, dx, dy = self.context.text_extents(text)
        self._moveto(x-width/2, y - height/2)
        self.context.set_source_rgb(self.gi_pen_rgb[0], self.gi_pen_rgb[1], self.gi_pen_rgb[2])
        self.context.show_text(text)

    def text_width(self, text):
        xbearing, ybearing, width, height, dx, dy = self.context.text_extents(text)
        return width

    def _moveto(self, x, y):
        self.context.move_to(x, -y)

    def translate(self, dx, dy):
        self.context.translate(dx, -dy)

    def rotate(self, angle):
        self.context.rotate(-angle)

    def clip_path(self, path):
        (x, y) = path[0]
        self.context.move_to(x, -y)
        for (x, y) in path[1:]:
            self.context.line_to(x, -y)
        self.context.close_path()
        self.context.clip()

    def reset_clip(self):
        self.context.reset_clip()

    def finish(self):
        if self.format == 'png':
            self.surface.write_to_png(self.fobj)
        elif self.format == 'jpg':
            self.surface.write_to_jpg(self.fobj, self.jpg_quality)
        else:
            self.surface.show_page()
            self.surface.flush()
            self.surface.finish()

    def on_screen(self, x, y):
        return x > -self.gi_width/2.0 and x < self.gi_width/2.0 and y > -self.gi_height/2.0  and y < self.gi_height/2.0

    def to_pixel(self, x, y):
        return int(x * DPMM_IMG + self.sfc_width/2), int(y * DPMM_IMG + self.sfc_height/2)

    def antialias_on(self):
        self.context.set_antialias(cairo.Antialias.DEFAULT)

    def antialias_off(self):
        self.context.set_antialias(cairo.Antialias.NONE)
