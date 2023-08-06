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

import skia

from fchart3.graphics_interface import INCH, DPMM, POINT, GraphicsInterface, DrawMode

DPI_IMG = 100.0
DPMM_IMG = DPI_IMG/INCH
PONT_IMG = 1.0/DPMM_IMG

A4_WIDTH_POINTS = 594
A4_HEIGHT_POINTS = 842


class SkiaDrawing(GraphicsInterface):
    """
    A SkiaDrawing - implement Graphics interface using Skia-Python
    """

    def __init__(self, fobj, width, height, format='pdf', pixels=False, landscape=False, tolerance=None):
        """
        width (horizontal) and height (vertical) in mm
        """
        GraphicsInterface.__init__(self, (width / DPMM_IMG if pixels else width) , (height / DPMM_IMG if pixels else height))

        self.fobj = fobj
        self.format = format
        self.landscape = landscape
        self.surface = None
        self.canvas = None
        self.sfc_width = None
        self.sfc_height = None
        self.tolerance = tolerance
        self.set_origin(self.gi_width/2.0, self.gi_height/2.0)

    def new(self):
        if self.format == 'png':
            self.set_point_size(PONT_IMG)
            self.sfc_width = int(self.gi_width * DPMM_IMG)
            self.sfc_height = int(self.gi_height * DPMM_IMG)
            self.surface = skia.Surface(self.sfc_width, self.sfc_height)
            self.canvas = self.surface.getCanvas()
            self.canvas.scale(DPMM_IMG, DPMM_IMG)
            self.canvas.translate(self.gi_origin_x, self.gi_origin_y)
        else:
            if self.landscape:
                self.sfc_width = A4_HEIGHT_POINTS
                self.sfc_height = A4_WIDTH_POINTS
                self.document = skia.PDF.MakeDocument(self.fobj)
                self.canvas = document.page(self.sfc_width, self.sfc_height)
                self.canvas.scale(DPMM, DPMM)
                self.canvas.translate(self.gi_origin_x*DPMM + 15*DPMM, self.gi_origin_y*DPMM + (210-self.gi_height)*DPMM/2)
            else:
                self.sfc_width = A4_WIDTH_POINTS
                self.sfc_height = A4_HEIGHT_POINTS
                self.document = skia.PDF.MakeDocument(self.fobj)
                self.canvas = document.page(self.sfc_width, self.sfc_height)
                self.canvas.scale(DPMM, DPMM)
                self.canvas.translate(self.gi_origin_x*DPMM + (210-self.gi_width)*DPMM/2, self.gi_origin_y*DPMM + 15*DPMM)
        self.paint = skia.Paint(AntiAlias=True)

    def clear(self):
        return
        if self.gi_background_rgb:
            self.canvas.clear(skia.Color4f(self.gi_background_rgb[0], self.gi_background_rgb[1], self.gi_background_rgb[2], 1.0))

    def save(self):
        GraphicsInterface.save(self)

    def restore(self):
        GraphicsInterface.restore(self)

    def set_font(self, font='Arial', fontsize=12*POINT):
        return
        GraphicsInterface.set_font(self, font, fontsize)
        self.canvas.set_font_size(self.gi_fontsize)
        self.canvas.select_font_face(self.gi_font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    def set_linewidth(self, linewidth):
        self.paint.setStrokeWidth(linewidth)

    def set_solid_line(self):
        pass
        # GraphicsInterface.set_solid_line(self)

    def set_dashed_line(self, on, off, start=0.0):
        pass
        # GraphicsInterface.set_dashed_line(self, on, off, start)

    def line(self, x1,y1,x2,y2):
        self.paint.setColor4f(skia.Color4f(self.gi_pen_rgb[0], self.gi_pen_rgb[1], self.gi_pen_rgb[2]))
        self.paint.setStyle(skia.Paint.kStroke_Style)
        self.canvas.drawLine((x1,-y1), (x2,-y2), self.paint)

    def rectangle(self,x,y,width,height, mode=DrawMode.BORDER):
        self.canvas.drawRect(skia.Rec(x, -y, width, height))

    def circle(self, x, y, r, mode=DrawMode.BORDER):
        if mode == DrawMode.BORDER:
            self.paint.setStyle(skia.Paint.kStroke_Style)
            self.paint.setColor4f(skia.Color4f(self.gi_pen_rgb[0], self.gi_pen_rgb[1], self.gi_pen_rgb[2]))
        elif mode == DrawMode.FILL:
            self.paint.setStyle(skia.Paint.kFill_Style)
            self.paint.setColor4f(skia.Color4f(self.gi_fill_rgb[0], self.gi_fill_rgb[1], self.gi_fill_rgb[2]))
        else:
            self.paint.setStyle(skia.Paint.kStrokeAndFill_Style)
            self.paint.setColor4f(skia.Color4f(self.gi_fill_rgb[0], self.gi_fill_rgb[1], self.gi_fill_rgb[2]))
        self.canvas.drawCircle(x, -y, r, self.paint)

    def polygon(self, vertices, mode=DrawMode.BORDER):
        pass

    def ellipse(self,x,y,rlong,rshort, posangle, mode=DrawMode.BORDER):
        pass

    def _draw_element(self, mode):
        if mode == DrawMode.BORDER:
            self.canvas.set_source_rgb(self.gi_pen_rgb[0], self.gi_pen_rgb[1], self.gi_pen_rgb[2])
            self.canvas.set_dash(self.gi_dash_style[0], self.gi_dash_style[1])
            self.canvas.stroke()
        elif mode == DrawMode.FILL:
            self.canvas.set_source_rgb(self.gi_fill_rgb[0], self.gi_fill_rgb[1], self.gi_fill_rgb[2])
            self.canvas.fill()
        else:
            self.canvas.set_source_rgb(self.gi_fill_rgb[0], self.gi_fill_rgb[1], self.gi_fill_rgb[2])
            self.canvas.fill_preserve()
            self.canvas.set_source_rgb(self.gi_pen_rgb[0], self.gi_pen_rgb[1], self.gi_pen_rgb[2])
            self.canvas.stroke()

    def text(self, text):
        pass

    def text_right(self, x, y, text):
        pass

    def text_left(self, x, y, text):
        pass

    def text_centred(self, x, y, text):
        pass

    def text_width(self, text):
        return 10.0

    def translate(self, dx, dy):
        # self.canvas.translate(dx, -dy)
        pass

    def rotate(self, angle):
        # self.canvas.rotate(-angle)
        pass

    def clip_path(self, path):
        pass

    def reset_clip(self):
        pass

    def finish(self):
        if self.format == 'png':
            image = self.surface.makeImageSnapshot()
            image.save(self.fobj, skia.kPNG)
        else:
            pass

    def on_screen(self, x, y):
        return x > -self.gi_width/2.0 and x < self.gi_width/2.0 and y > -self.gi_height/2.0  and y < self.gi_height/2.0

    def to_pixel(self, x, y):
        return (int(x * DPMM_IMG + self.sfc_width/2), int(y * DPMM_IMG + self.sfc_height/2))
