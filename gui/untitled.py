
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App


class untitled(App):
    def __init__(self, *args, **kwargs):
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        container0 = Container()
        container0.attr_class = "Container"
        container0.attr_editor_newclass = False
        container0.css_height = "648.0px"
        container0.css_left = "6.0px"
        container0.css_position = "absolute"
        container0.css_top = "12.0px"
        container0.css_width = "1152.0px"
        container0.variable_name = "container0"
        button0 = Button()
        button0.attr_class = "Button"
        button0.attr_editor_newclass = False
        button0.css_height = "36.0px"
        button0.css_left = "618.0px"
        button0.css_position = "absolute"
        button0.css_top = "6.0px"
        button0.css_width = "108.0px"
        button0.text = "Pick Starting Position"
        button0.variable_name = "button0"
        container0.append(button0,'button0')
        button1 = Button()
        button1.attr_class = "Button"
        button1.attr_editor_newclass = False
        button1.css_height = "36.0px"
        button1.css_left = "618.0px"
        button1.css_position = "absolute"
        button1.css_top = "48.0px"
        button1.css_width = "108.0px"
        button1.text = "button"
        button1.variable_name = "button1"
        container0.append(button1,'button1')
        button2 = Button()
        button2.attr_class = "Button"
        button2.attr_editor_newclass = False
        button2.css_height = "36.0px"
        button2.css_left = "618.0px"
        button2.css_position = "absolute"
        button2.css_top = "90.0px"
        button2.css_width = "108.0px"
        button2.text = "button"
        button2.variable_name = "button2"
        container0.append(button2,'button2')
        baseField = Svg()
        baseField.attr_class = "Svg"
        baseField.attr_editor_newclass = False
        baseField.css_background_color = "rgb(155,155,155)"
        baseField.css_height = "600.0px"
        baseField.css_left = "10px"
        baseField.css_position = "absolute"
        baseField.css_top = "10px"
        baseField.css_width = "600.0px"
        baseField.variable_name = "baseField"
        topDiag = SvgLine()
        topDiag.attr_class = "SvgLine"
        topDiag.attr_editor_newclass = False
        topDiag.attr_stroke = "rgb(255,255,255)"
        topDiag.attr_stroke_width = "4.0"
        topDiag.attr_x1 = "20.0"
        topDiag.attr_x2 = "600.0"
        topDiag.attr_y1 = "0"
        topDiag.attr_y2 = "580.0"
        topDiag.variable_name = "topDiag"
        baseField.append(topDiag,'topDiag')
        bottomDiag = SvgLine()
        bottomDiag.attr_class = "SvgLine"
        bottomDiag.attr_editor_newclass = False
        bottomDiag.attr_stroke = "rgb(255,255,255)"
        bottomDiag.attr_stroke_width = "4.0"
        bottomDiag.attr_x1 = "0"
        bottomDiag.attr_x2 = "580.0"
        bottomDiag.attr_y1 = "20.0"
        bottomDiag.attr_y2 = "600.0"
        bottomDiag.variable_name = "bottomDiag"
        baseField.append(bottomDiag,'bottomDiag')
        redFar = SvgLine()
        redFar.attr_class = "SvgLine"
        redFar.attr_editor_newclass = False
        redFar.attr_stroke = "rgb(255,255,255)"
        redFar.attr_stroke_width = "4.0"
        redFar.attr_x1 = "200.0"
        redFar.attr_x2 = "200.0"
        redFar.attr_y1 = "0"
        redFar.attr_y2 = "50"
        redFar.variable_name = "redFar"
        baseField.append(redFar,'redFar')
        redLow1 = SvgLine()
        redLow1.attr_class = "SvgLine"
        redLow1.attr_editor_newclass = False
        redLow1.attr_stroke = "rgb(255,255,255)"
        redLow1.attr_stroke_width = "4.0"
        redLow1.attr_x1 = "400.0"
        redLow1.attr_x2 = "400.0"
        redLow1.attr_y1 = "0.0"
        redLow1.attr_y2 = "100.0"
        redLow1.variable_name = "redLow1"
        baseField.append(redLow1,'redLow1')
        redLow2 = SvgLine()
        redLow2.attr_class = "SvgLine"
        redLow2.attr_editor_newclass = False
        redLow2.attr_stroke = "rgb(255,255,255)"
        redLow2.attr_stroke_width = "4.0"
        redLow2.attr_x1 = "500.0"
        redLow2.attr_x2 = "600.0"
        redLow2.attr_y1 = "200.0"
        redLow2.attr_y2 = "200.0"
        redLow2.variable_name = "redLow2"
        baseField.append(redLow2,'redLow2')
        redClose = SvgLine()
        redClose.attr_class = "SvgLine"
        redClose.attr_editor_newclass = False
        redClose.attr_stroke = "rgb(255,255,255)"
        redClose.attr_stroke_width = "4.0"
        redClose.attr_x1 = "550.0"
        redClose.attr_x2 = "600.0"
        redClose.attr_y1 = "500.0"
        redClose.attr_y2 = "500.0"
        redClose.variable_name = "redClose"
        baseField.append(redClose,'redClose')
        blueFar = SvgLine()
        blueFar.attr_class = "SvgLine"
        blueFar.attr_editor_newclass = False
        blueFar.attr_stroke = "rgb(255,255,255)"
        blueFar.attr_stroke_width = "4.0"
        blueFar.attr_x1 = "0"
        blueFar.attr_x2 = "50"
        blueFar.attr_y1 = "100.0"
        blueFar.attr_y2 = "100.0"
        blueFar.variable_name = "blueFar"
        baseField.append(blueFar,'blueFar')
        blueLow1 = SvgLine()
        blueLow1.attr_class = "SvgLine"
        blueLow1.attr_editor_newclass = False
        blueLow1.attr_stroke = "rgb(255,255,255)"
        blueLow1.attr_stroke_width = "4.0"
        blueLow1.attr_x1 = "0"
        blueLow1.attr_x2 = "100.0"
        blueLow1.attr_y1 = "400.0"
        blueLow1.attr_y2 = "400.0"
        blueLow1.variable_name = "blueLow1"
        baseField.append(blueLow1,'blueLow1')
        blueLow2 = SvgLine()
        blueLow2.attr_class = "SvgLine"
        blueLow2.attr_editor_newclass = False
        blueLow2.attr_stroke = "rgb(255,255,255)"
        blueLow2.attr_stroke_width = "4.0"
        blueLow2.attr_x1 = "200.0"
        blueLow2.attr_x2 = "200.0"
        blueLow2.attr_y1 = "500.0"
        blueLow2.attr_y2 = "600.0"
        blueLow2.variable_name = "blueLow2"
        baseField.append(blueLow2,'blueLow2')
        blueBarrier1 = SvgLine()
        blueBarrier1.attr_class = "SvgLine"
        blueBarrier1.attr_editor_newclass = False
        blueBarrier1.attr_stroke = "rgb(0,50,190)"
        blueBarrier1.attr_stroke_width = "10.0"
        blueBarrier1.attr_x1 = "100.0"
        blueBarrier1.attr_x2 = "200.0"
        blueBarrier1.attr_y1 = "403.0"
        blueBarrier1.attr_y2 = "403.0"
        blueBarrier1.variable_name = "blueBarrier1"
        baseField.append(blueBarrier1,'blueBarrier1')
        blueBarrier2 = SvgLine()
        blueBarrier2.attr_class = "SvgLine"
        blueBarrier2.attr_editor_newclass = False
        blueBarrier2.attr_stroke = "rgb(0,50,190)"
        blueBarrier2.attr_stroke_width = "10.0"
        blueBarrier2.attr_x1 = "197.0"
        blueBarrier2.attr_x2 = "197.0"
        blueBarrier2.attr_y1 = "398.0"
        blueBarrier2.attr_y2 = "500.0"
        blueBarrier2.variable_name = "blueBarrier2"
        baseField.append(blueBarrier2,'blueBarrier2')
        redBarrier1 = SvgLine()
        redBarrier1.attr_class = "SvgLine"
        redBarrier1.attr_editor_newclass = False
        redBarrier1.attr_stroke = "rgb(190,0,0)"
        redBarrier1.attr_stroke_width = "10.0"
        redBarrier1.attr_x1 = "403.0"
        redBarrier1.attr_x2 = "403.0"
        redBarrier1.attr_y1 = "100.0"
        redBarrier1.attr_y2 = "200.0"
        redBarrier1.variable_name = "redBarrier1"
        baseField.append(redBarrier1,'redBarrier1')
        redBarrier2 = SvgLine()
        redBarrier2.attr_class = "SvgLine"
        redBarrier2.attr_editor_newclass = False
        redBarrier2.attr_stroke = "rgb(190,0,0)"
        redBarrier2.attr_stroke_width = "10.0"
        redBarrier2.attr_x1 = "398.0"
        redBarrier2.attr_x2 = "500.0"
        redBarrier2.attr_y1 = "197.0"
        redBarrier2.attr_y2 = "197.0"
        redBarrier2.variable_name = "redBarrier2"
        baseField.append(redBarrier2,'redBarrier2')
        svgsubcontainer0 = SvgSubcontainer()
        svgsubcontainer0.attr_class = "SvgSubcontainer"
        svgsubcontainer0.attr_editor_newclass = False
        svgsubcontainer0.attr_height = "600.0"
        svgsubcontainer0.attr_width = "600.0"
        svgsubcontainer0.attr_x = "0.0"
        svgsubcontainer0.attr_y = "0.0"
        svgsubcontainer0.variable_name = "svgsubcontainer0"
        svgcircle0 = SvgCircle()
        svgcircle0.attr_class = "SvgCircle"
        svgcircle0.attr_cx = "50.0"
        svgcircle0.attr_cy = "50.0"
        svgcircle0.attr_editor_newclass = False
        svgcircle0.attr_fill = "rgb(255,230,0)"
        svgcircle0.attr_r = "13.0"
        svgcircle0.variable_name = "svgcircle0"
        svgsubcontainer0.append(svgcircle0,'svgcircle0')
        svgcircle1 = SvgCircle()
        svgcircle1.attr_class = "SvgCircle"
        svgcircle1.attr_cx = "100.0"
        svgcircle1.attr_cy = "100.0"
        svgcircle1.attr_editor_newclass = False
        svgcircle1.attr_fill = "rgb(255,230,0)"
        svgcircle1.attr_r = "13.0"
        svgcircle1.variable_name = "svgcircle1"
        svgsubcontainer0.append(svgcircle1,'svgcircle1')
        svgcircle2 = SvgCircle()
        svgcircle2.attr_class = "SvgCircle"
        svgcircle2.attr_cx = "150.0"
        svgcircle2.attr_cy = "150.0"
        svgcircle2.attr_editor_newclass = False
        svgcircle2.attr_fill = "rgb(255,230,0)"
        svgcircle2.attr_r = "13.0"
        svgcircle2.variable_name = "svgcircle2"
        svgsubcontainer0.append(svgcircle2,'svgcircle2')
        svgcircle3 = SvgCircle()
        svgcircle3.attr_class = "SvgCircle"
        svgcircle3.attr_cx = "200.0"
        svgcircle3.attr_cy = "200.0"
        svgcircle3.attr_editor_newclass = False
        svgcircle3.attr_fill = "rgb(255,230,0)"
        svgcircle3.attr_r = "13.0"
        svgcircle3.variable_name = "svgcircle3"
        svgsubcontainer0.append(svgcircle3,'svgcircle3')
        svgcircle4 = SvgCircle()
        svgcircle4.attr_class = "SvgCircle"
        svgcircle4.attr_cx = "250.0"
        svgcircle4.attr_cy = "250.0"
        svgcircle4.attr_editor_newclass = False
        svgcircle4.attr_fill = "rgb(255,230,0)"
        svgcircle4.attr_r = "13.0"
        svgcircle4.variable_name = "svgcircle4"
        svgsubcontainer0.append(svgcircle4,'svgcircle4')
        svgcircle5 = SvgCircle()
        svgcircle5.attr_class = "SvgCircle"
        svgcircle5.attr_cx = "350.0"
        svgcircle5.attr_cy = "350.0"
        svgcircle5.attr_editor_newclass = False
        svgcircle5.attr_fill = "rgb(255,230,0)"
        svgcircle5.attr_r = "13.0"
        svgcircle5.variable_name = "svgcircle5"
        svgsubcontainer0.append(svgcircle5,'svgcircle5')
        svgcircle6 = SvgCircle()
        svgcircle6.attr_class = "SvgCircle"
        svgcircle6.attr_cx = "400.0"
        svgcircle6.attr_cy = "400.0"
        svgcircle6.attr_editor_newclass = False
        svgcircle6.attr_fill = "rgb(255,230,0)"
        svgcircle6.attr_r = "13.0"
        svgcircle6.variable_name = "svgcircle6"
        svgsubcontainer0.append(svgcircle6,'svgcircle6')
        svgcircle7 = SvgCircle()
        svgcircle7.attr_class = "SvgCircle"
        svgcircle7.attr_cx = "450.0"
        svgcircle7.attr_cy = "450.0"
        svgcircle7.attr_editor_newclass = False
        svgcircle7.attr_fill = "rgb(255,235,0)"
        svgcircle7.attr_r = "13.0"
        svgcircle7.variable_name = "svgcircle7"
        svgsubcontainer0.append(svgcircle7,'svgcircle7')
        svgcircle8 = SvgCircle()
        svgcircle8.attr_class = "SvgCircle"
        svgcircle8.attr_cx = "500.0"
        svgcircle8.attr_cy = "500.0"
        svgcircle8.attr_editor_newclass = False
        svgcircle8.attr_fill = "rgb(255,230,0)"
        svgcircle8.attr_r = "13.0"
        svgcircle8.variable_name = "svgcircle8"
        svgsubcontainer0.append(svgcircle8,'svgcircle8')
        svgcircle9 = SvgCircle()
        svgcircle9.attr_class = "SvgCircle"
        svgcircle9.attr_cx = "550.0"
        svgcircle9.attr_cy = "550.0"
        svgcircle9.attr_editor_newclass = False
        svgcircle9.attr_fill = "rgb(255,230,0)"
        svgcircle9.attr_r = "13.0"
        svgcircle9.variable_name = "svgcircle9"
        svgsubcontainer0.append(svgcircle9,'svgcircle9')
        svgcircle10 = SvgCircle()
        svgcircle10.attr_class = "SvgCircle"
        svgcircle10.attr_cx = "150.0"
        svgcircle10.attr_cy = "250.0"
        svgcircle10.attr_editor_newclass = False
        svgcircle10.attr_fill = "rgb(255,230,0)"
        svgcircle10.attr_r = "13.0"
        svgcircle10.variable_name = "svgcircle10"
        svgsubcontainer0.append(svgcircle10,'svgcircle10')
        svgcircle11 = SvgCircle()
        svgcircle11.attr_class = "SvgCircle"
        svgcircle11.attr_cx = "110.0"
        svgcircle11.attr_cy = "380.0"
        svgcircle11.attr_editor_newclass = False
        svgcircle11.attr_fill = "rgb(255,230,0)"
        svgcircle11.attr_r = "13.0"
        svgcircle11.variable_name = "svgcircle11"
        svgsubcontainer0.append(svgcircle11,'svgcircle11')
        svgcircle12 = SvgCircle()
        svgcircle12.attr_class = "SvgCircle"
        svgcircle12.attr_cx = "150.0"
        svgcircle12.attr_cy = "380.0"
        svgcircle12.attr_editor_newclass = False
        svgcircle12.attr_fill = "rgb(255,230,0)"
        svgcircle12.attr_r = "13.0"
        svgcircle12.variable_name = "svgcircle12"
        svgsubcontainer0.append(svgcircle12,'svgcircle12')
        svgcircle13 = SvgCircle()
        svgcircle13.attr_class = "SvgCircle"
        svgcircle13.attr_cx = "190.0"
        svgcircle13.attr_cy = "380.0"
        svgcircle13.attr_editor_newclass = False
        svgcircle13.attr_fill = "rgb(255,230,0)"
        svgcircle13.attr_r = "13.0"
        svgcircle13.variable_name = "svgcircle13"
        svgsubcontainer0.append(svgcircle13,'svgcircle13')
        svgcircle14 = SvgCircle()
        svgcircle14.attr_class = "SvgCircle"
        svgcircle14.attr_cx = "220.0"
        svgcircle14.attr_cy = "410.0"
        svgcircle14.attr_editor_newclass = False
        svgcircle14.attr_fill = "rgb(255,230,0)"
        svgcircle14.attr_r = "13.0"
        svgcircle14.variable_name = "svgcircle14"
        svgsubcontainer0.append(svgcircle14,'svgcircle14')
        svgcircle15 = SvgCircle()
        svgcircle15.attr_class = "SvgCircle"
        svgcircle15.attr_cx = "220.0"
        svgcircle15.attr_cy = "450.0"
        svgcircle15.attr_editor_newclass = False
        svgcircle15.attr_fill = "rgb(255,230,0)"
        svgcircle15.attr_r = "13.0"
        svgcircle15.variable_name = "svgcircle15"
        svgsubcontainer0.append(svgcircle15,'svgcircle15')
        svgcircle16 = SvgCircle()
        svgcircle16.attr_class = "SvgCircle"
        svgcircle16.attr_cx = "220.0"
        svgcircle16.attr_cy = "490.0"
        svgcircle16.attr_editor_newclass = False
        svgcircle16.attr_fill = "rgb(255,230,0)"
        svgcircle16.attr_r = "13.0"
        svgcircle16.variable_name = "svgcircle16"
        svgsubcontainer0.append(svgcircle16,'svgcircle16')
        svgcircle17 = SvgCircle()
        svgcircle17.attr_class = "SvgCircle"
        svgcircle17.attr_cx = "250.0"
        svgcircle17.attr_cy = "150.0"
        svgcircle17.attr_editor_newclass = False
        svgcircle17.attr_fill = "rgb(255,230,0)"
        svgcircle17.attr_r = "13.0"
        svgcircle17.variable_name = "svgcircle17"
        svgsubcontainer0.append(svgcircle17,'svgcircle17')
        svgcircle18 = SvgCircle()
        svgcircle18.attr_class = "SvgCircle"
        svgcircle18.attr_cx = "300.0"
        svgcircle18.attr_cy = "200.0"
        svgcircle18.attr_editor_newclass = False
        svgcircle18.attr_fill = "rgb(255,230,0)"
        svgcircle18.attr_r = "13.0"
        svgcircle18.variable_name = "svgcircle18"
        svgsubcontainer0.append(svgcircle18,'svgcircle18')
        svgcircle19 = SvgCircle()
        svgcircle19.attr_class = "SvgCircle"
        svgcircle19.attr_cx = "350.0"
        svgcircle19.attr_cy = "250.0"
        svgcircle19.attr_editor_newclass = False
        svgcircle19.attr_fill = "rgb(255,230,0)"
        svgcircle19.attr_r = "13.0"
        svgcircle19.variable_name = "svgcircle19"
        svgsubcontainer0.append(svgcircle19,'svgcircle19')
        svgcircle20 = SvgCircle()
        svgcircle20.attr_class = "SvgCircle"
        svgcircle20.attr_cx = "450.0"
        svgcircle20.attr_cy = "350.0"
        svgcircle20.attr_editor_newclass = False
        svgcircle20.attr_fill = "rgb(255,230,0)"
        svgcircle20.attr_r = "13.0"
        svgcircle20.variable_name = "svgcircle20"
        svgsubcontainer0.append(svgcircle20,'svgcircle20')
        svgcircle21 = SvgCircle()
        svgcircle21.attr_class = "SvgCircle"
        svgcircle21.attr_cx = "380.0"
        svgcircle21.attr_cy = "110.0"
        svgcircle21.attr_editor_newclass = False
        svgcircle21.attr_fill = "rgb(255,230,0)"
        svgcircle21.attr_r = "13.0"
        svgcircle21.variable_name = "svgcircle21"
        svgsubcontainer0.append(svgcircle21,'svgcircle21')
        svgcircle22 = SvgCircle()
        svgcircle22.attr_class = "SvgCircle"
        svgcircle22.attr_cx = "380.0"
        svgcircle22.attr_cy = "150.0"
        svgcircle22.attr_editor_newclass = False
        svgcircle22.attr_fill = "rgb(255,230,0)"
        svgcircle22.attr_r = "13.0"
        svgcircle22.variable_name = "svgcircle22"
        svgsubcontainer0.append(svgcircle22,'svgcircle22')
        svgcircle23 = SvgCircle()
        svgcircle23.attr_class = "SvgCircle"
        svgcircle23.attr_cx = "380.0"
        svgcircle23.attr_cy = "190.0"
        svgcircle23.attr_editor_newclass = False
        svgcircle23.attr_fill = "rgb(255,230,0)"
        svgcircle23.attr_r = "13.0"
        svgcircle23.variable_name = "svgcircle23"
        svgsubcontainer0.append(svgcircle23,'svgcircle23')
        svgcircle24 = SvgCircle()
        svgcircle24.attr_class = "SvgCircle"
        svgcircle24.attr_cx = "410.0"
        svgcircle24.attr_cy = "220.0"
        svgcircle24.attr_editor_newclass = False
        svgcircle24.attr_fill = "rgb(255,230,0)"
        svgcircle24.attr_r = "13.0"
        svgcircle24.variable_name = "svgcircle24"
        svgsubcontainer0.append(svgcircle24,'svgcircle24')
        svgcircle25 = SvgCircle()
        svgcircle25.attr_class = "SvgCircle"
        svgcircle25.attr_cx = "450.0"
        svgcircle25.attr_cy = "220.0"
        svgcircle25.attr_editor_newclass = False
        svgcircle25.attr_fill = "rgb(255,230,0)"
        svgcircle25.attr_r = "13.0"
        svgcircle25.variable_name = "svgcircle25"
        svgsubcontainer0.append(svgcircle25,'svgcircle25')
        svgcircle26 = SvgCircle()
        svgcircle26.attr_class = "SvgCircle"
        svgcircle26.attr_cx = "490.0"
        svgcircle26.attr_cy = "220.0"
        svgcircle26.attr_editor_newclass = False
        svgcircle26.attr_fill = "rgb(255,230,0)"
        svgcircle26.attr_r = "13.0"
        svgcircle26.variable_name = "svgcircle26"
        svgsubcontainer0.append(svgcircle26,'svgcircle26')
        svgcircle27 = SvgCircle()
        svgcircle27.attr_class = "SvgCircle"
        svgcircle27.attr_cx = "250.0"
        svgcircle27.attr_cy = "350.0"
        svgcircle27.attr_editor_newclass = False
        svgcircle27.attr_fill = "rgb(255,230,0)"
        svgcircle27.attr_r = "13.0"
        svgcircle27.variable_name = "svgcircle27"
        svgsubcontainer0.append(svgcircle27,'svgcircle27')
        svgcircle28 = SvgCircle()
        svgcircle28.attr_class = "SvgCircle"
        svgcircle28.attr_cx = "300.0"
        svgcircle28.attr_cy = "400.0"
        svgcircle28.attr_editor_newclass = False
        svgcircle28.attr_fill = "rgb(255,230,0)"
        svgcircle28.attr_r = "13.0"
        svgcircle28.variable_name = "svgcircle28"
        svgsubcontainer0.append(svgcircle28,'svgcircle28')
        svgcircle29 = SvgCircle()
        svgcircle29.attr_class = "SvgCircle"
        svgcircle29.attr_cx = "350.0"
        svgcircle29.attr_cy = "450.0"
        svgcircle29.attr_editor_newclass = False
        svgcircle29.attr_fill = "rgb(255,230,0)"
        svgcircle29.attr_r = "13.0"
        svgcircle29.variable_name = "svgcircle29"
        svgsubcontainer0.append(svgcircle29,'svgcircle29')
        baseField.append(svgsubcontainer0,'svgsubcontainer0')
        svgline13 = SvgLine()
        svgline13.attr_class = "SvgLine"
        svgline13.attr_editor_newclass = False
        svgline13.attr_stroke = "rgb(255,255,255)"
        svgline13.attr_stroke_width = "4.0"
        svgline13.attr_x1 = "400.0"
        svgline13.attr_x2 = "400.0"
        svgline13.attr_y1 = "550.0"
        svgline13.attr_y2 = "600.0"
        svgline13.variable_name = "svgline13"
        baseField.append(svgline13,'svgline13')
        container0.append(baseField,'baseField')

        self.container0 = container0
        return self.container0
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
