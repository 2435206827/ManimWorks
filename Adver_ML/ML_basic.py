#   MANIM-Adver_ML
#   
#   L        DDDDD    DDDDD    MM         MM  IIIII       A       OOOOOOOOO
#   L        D    D   D    D   M M       M M    I        A A      O       O
#   L        D     D  D     D  M  M     M  M    I       A   A     O       O
#   L        D     D  D     D  M   M   M   M    I      AAAAAAA    O       O
#   L        D    D   D    D   M    M M    M    I     A       A   O       O
#   LLLLLLL  DDDDD    DDDDD    M     M     M  IIIII  A         A  OOOOOOOOO 
#   
#   author: LDDMiao
#   date: 2022 - 12 - 28 TO 2023 - _ - _
#
#   QAQ
#   你这代码保熟吗？

# -*- coding: UTF-8 -*-

import cmath as cm
import math as m
import random as ran
import numpy as np
import scipy as sc
import matplotlib as mat
import matplotlib.pyplot as plt

from manimlib import *
from numpy import *
from decimal import *

def set_color_by_xyz(ps: list[Dot], mode = "RG", reverse = False, x_range = [-4, 4], y_range = [-4, 4], z_range = [-4, 4]):
    
    x_min, x_max = x_range[0], x_range[1]
    y_min, y_max = y_range[0], y_range[1]
    z_min, z_max = z_range[0], z_range[1]

    for p in ps:
        cx = (p.get_center()[0] - x_min) / (x_max - x_min)
        cy = (p.get_center()[1] - y_min) / (y_max - y_min)
        cz = (p.get_center()[2] - z_min) / (z_max - z_min)

        cx = (1 - cx) if reverse else cx
        cy = (1 - cy) if not reverse else cy

        if mode == "RG":
            p = p.set_fill(rgb_to_color([cx, cy, 0]))
        if mode == "GB":
            p = p.set_fill(rgb_to_color([0, cx, cy]))
        if mode == "RB":
            p = p.set_fill(rgb_to_color([cx, 0, cy]))
        if mode == "RGB":
            p = p.set_fill(rgb_to_color([cx, cy, cz]))
        if mode == "RAND":
            p = p.set_fill(random_bright_color())

    return ps

def rot(theta, x, y, z):
    # q = ((x, y, z)sin(θ/2), cos(θ/2))
    rx, ry, rz = m.sin(theta / 2) * x, m.sin(theta / 2) * y, m.sin(theta / 2) * z
    return [rx, ry, rz, m.cos(theta / 2)]

class test(Scene):
    def construct(self):
        axes = ThreeDAxes([-20, 20], [-20, 20])
        self.play(Write(axes))
        self.wait(2)
        camera = self.camera.frame
        self.play(camera.animate.set_orientation(Rotation(rot(PI / 3, 1, 0, 0))))
        self.wait(2)
        self.play(camera.animate.to_default_state())
        self.wait(2)

class Huigui1(Scene):
    def construct(self):
        def poly(x):
            return 0.095 * x ** 3 + 0.021 * x ** 2 - 0.469 * x - 0.019

        def logi(x):
            return 2.6928 / (1 + 0.6921 * ma.exp(-0.8828 * x))

        dots = [
            [-3.82, -2.63, -3.87],
            [-3.34, -1.6, -3.12],
            [-2.37, -1.66, -2.6],
            [-1.68, -0.67, -1.8],
            [-1.02, 0.65, -0.95],
            [-0.12, 0.58, 0],
            [1.17, 1.23, 0.67],
            [1.63, 2.03, 1.5],
            [2.0, 3.0, 2.14],
            [2.83, 3.23, 2.97]
        ]
        pre_dots = [[x, 0.85 * x + 0.85, 0.997 * x - 0.036] for x in [(ran.random() * 16 - 8) for _ in range(30)]]
        dots2 = [
            [-3.03, -1.11, 0],
            [-2.38, -0.14, 0],
            [-1.58, 0.62, 0],
            [-1.03, 0.58, 0],
            [-0.12, -0.32, 0],
            [0.96, -0.65, 0],
            [1.88, 0.27, 0],
            [3.21, 1.73, 0]
        ]
        dots3 = [
            [-3.99, 0.16, 0],
            [-3.23, 0.25, 0],
            [-2.42, 0.35, 0],
            [-1, 1, 0],
            [-0.32, 1.44, 0],
            [0.68, 1.85, 0],
            [1.64, 2.44, 0],
            [2.55, 2.52, 0],
            [3.63, 2.56, 0]
        ]
        line_point_fit = [
            [-20, 0.85 * (-20) + 0.85, 0.997 * (-20) - 0.036],
            [20, 0.85 * 20 + 0.85, 0.997 * 20 - 0.036]
        ]
        line_point_up = [
            [-20, 0.45 * (-20) + 1.2, 0],
            [20, 0.45 * 20 + 1.2, 0]
        ]
        line_point_down = [
            [-20, 1.3 * (-20) - 1.2, 0],
            [20, 1.3 * 20 - 1.2, 0]
        ]
        dot_cloud = set_color_by_xyz([Dot(d) for d in dots], mode = "RG")
        dot_cloud_pre = [Dot(d, fill_color = BLUE) for d in pre_dots]
        dot_cloud2 = set_color_by_xyz([Dot(d) for d in dots2], mode = "GB")
        dot_cloud3 = set_color_by_xyz([Dot(d) for d in dots3], mode = "RB")
        line_fit = Line(line_point_fit[0], line_point_fit[1]).set_color(WHITE)
        line_up = DashedLine(line_point_up[0], line_point_up[1]).set_color(GREY)
        line_down = DashedLine(line_point_down[0], line_point_down[1]).set_color(GREY)
        axes = ThreeDAxes([-20, 20], [-20, 20])
        poly_graph = FunctionGraph(poly, [-15, 15, 0.01]).set_color(RED)
        logi_graph = FunctionGraph(logi, [-15, 15, 0.01]).set_color(GREEN)

        camera = self.camera.frame

        self.wait(1)
        self.play(Write(axes))
        self.wait(2)
        ran.shuffle(dot_cloud)
        for d in dot_cloud:
            self.play(FadeIn(d), run_time = 0.2)
        self.wait(5)
        self.play(Write(line_up), run_time = 0.5)
        self.wait(0.5)
        self.play(Write(line_down), run_time = 0.2)
        self.wait(1)
        self.play(Write(line_fit))  #render BUG
        self.wait(3)
        self.play(
            *[d.animate.shift(LEFT * 2 + DOWN * 2) for d in dot_cloud], 
            FadeOut(line_up),
            FadeOut(line_down),
            line_fit.animate.shift(LEFT * 2 + DOWN * 2),
            axes.animate.shift(LEFT * 2 + DOWN * 2),
            camera.animate.set_height(14), 
            run_time = 2.5
        )
        self.wait(3)
        for d in dot_cloud_pre:
            self.play(FadeIn(d), run_time = 0.1)
        self.wait(3)
        self.play(
            *[d.animate.shift(RIGHT * 2 + UP * 2) for d in dot_cloud], 
            *[Uncreate(d) for d in dot_cloud_pre],
            camera.animate.set_height(8),
            line_fit.animate.shift(RIGHT * 2 + UP * 2), 
            axes.animate.shift(RIGHT * 2 + UP * 2),
            run_time = 2.5
        )
        self.play(
            camera.animate.set_orientation(Rotation(rot(PI / 3, 1, 0, 0))),
            FadeOut(line_fit)
        )
        self.play(camera.animate.set_orientation(Rotation(rot(PI, 1/6, 2/6, 3/6))), run_time = 5)
        self.wait(3)
        self.play(camera.animate.to_default_state())
        self.wait(1)
        self.play(*[d.animate.set_fill(WHITE) for d in dot_cloud])
        dot_cloud[3], dot_cloud[7] = dot_cloud[3].set_fill(RED), dot_cloud[7].set_fill(RED),
        self.play(
            dot_cloud[3].animate.shift(LEFT * 1 + UP * 2),
            dot_cloud[7].animate.shift(RIGHT * 2 + DOWN * 4)
        )
        self.wait(2)
        dot_cloud[3], dot_cloud[7] = dot_cloud[3].set_fill(WHITE), dot_cloud[7].set_fill(WHITE),
        self.play(
            dot_cloud[3].animate.shift(RIGHT * 1 + DOWN * 2),
            dot_cloud[7].animate.shift(LEFT * 2 + UP * 4)
        )
        self.wait(2)
        g1 = VGroup(*dot_cloud)
        g2 = VGroup(*dot_cloud2)
        g3 = VGroup(*dot_cloud3)
        self.play(ReplacementTransform(g1, g2), run_time = 2)
        self.wait(1)
        self.play(Write(poly_graph))
        self.wait(3)
        self.play(
            ReplacementTransform(g2, g3), 
            ReplacementTransform(poly_graph, logi_graph),
            run_time = 2
        )
        self.wait(2)
        self.play(
            FadeOut(g3), 
            FadeOut(logi_graph), 
            FadeOut(axes)
        )
        self.wait(2)
        
class JuLei1(Scene):
    def construct(self):
        s = """
        编号    糖分    密度    色泽
        01      0.395   2.724   1.939
        02     0.249   2.823   1.755
        03     0.387   2.766   1.925
        04     0.233   2.944   1.698
        05     0.366   2.600   2.114
        06     0.204   3.020   1.594
        """
        s1 = """
        编号    糖分    密度    色泽
        01      0.395   2.724   1.939
        03     0.387   2.766   1.925
        05     0.366   2.600   2.114
        """
        s2 = """
        编号    糖分    密度    色泽
        02     0.249   2.823   1.755
        04     0.233   2.944   1.698
        06     0.204   3.020   1.594
        """
        color_rule = {
            "编号": WHITE,
            "糖分": RED,
            "0.395": RED,
            "0.249": RED,
            "0.387": RED,
            "0.233": RED,
            "0.366": RED,
            "0.204": RED,
            "密度": BLUE,
            "2.724": BLUE,
            "2.823": BLUE,
            "2.766": BLUE,
            "2.944": BLUE,
            "2.600": BLUE,
            "3.020": BLUE,
            "色泽": GREEN,
            "1.939": GREEN,
            "1.755": GREEN,
            "1.925": GREEN,
            "1.698": GREEN,
            "2.114": GREEN,
            "1.594": GREEN,
        }
        t = Text(s, font = "BigruiqiaoGB1.0").set_color_by_text_to_color_map(color_rule)
        t1 = Text(s1, font = "BigruiqiaoGB1.0").shift(UP * 1.7 + RIGHT * 1).scale(0.9).set_color_by_text_to_color_map(color_rule)
        t2 = Text(s2, font = "BigruiqiaoGB1.0").shift(DOWN * 1.7 + RIGHT * 1).scale(0.9).set_color_by_text_to_color_map(color_rule)
        sr1 = SurroundingRectangle(t1, buff = 0.6)
        sr2 = SurroundingRectangle(t2, buff = 0.6)
        br1 = Brace(sr1, LEFT)
        br2 = Brace(sr2, LEFT)

        self.play(Write(t), run_time = 2)
        self.wait(5)
        self.play(
            TransformMatchingStrings(t, t1),
            TransformMatchingStrings(t, t2),
            run_time = 2
        )
        self.play(
            Write(sr1),
            Write(sr2),
            Write(br1),
            Write(br2),
            run_time = 1.5
        )
        self.wait(5)
        self.play(
            Uncreate(sr1),
            Uncreate(sr2),
            Uncreate(br1),
            Uncreate(br2),
            Uncreate(t1),
            Uncreate(t2),
            run_time = 1
        )
        self.wait(1)

class NN1(Scene):
    def construct(self):
        param = [
            [2018, 0.094],
            [2018.8, 0.34],
            [2019.1, 1.5],
            [2019.6, 8.3],
            [2019.7, 11],
            [2020.1, 17.2],
            [2020.35, 175]
        ]
        param = [[p[0] - 2017, m.log10(p[1])] for p in param]

        def calc_line(x1, x2, y1, y2):
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
            return k, b

        def param_graph(x):
            for p in range(len(param) - 1):
                x1, x2, y1, y2 = param[p][0], param[p + 1][0], param[p][1], param[p + 1][1]
                k, b = calc_line(x1, x2, y1, y2)
                if x >= param[p][0] and x <= param[p + 1][0]:
                    return k * x + b
            return 114

        axes = Axes([0, 4, 1], [-2, 3, 1])
        t_x = ["2018", "2019", "2020", "2021"]
        t_y = ["0.01", "0.1", "1", "10", "100", "1000"]
        text_x = [Text(t_x[i], font = "BigruiqiaoGB1.0").scale(0.7).move_to(axes.c2p(i + 1, -0.3)) for i in range(len(t_x))]
        text_y = [Text(t_y[i], font = "BigruiqiaoGB1.0").scale(0.7).move_to(axes.c2p(0.2, i - 2)) for i in range(len(t_y))]
        pg = axes.get_graph(param_graph, [param[0][0], param[6][0], 0.01]).set_color(BLUE)
        ps = [Dot(axes.c2p(p[0], p[1])) for p in param]
        ps = set_color_by_xyz(ps, mode = "RG", x_range = [-6, 6], y_range = [-4, 4])

        self.wait(1)
        self.play(Write(axes))
        self.play(*[Write(t) for t in text_x], run_time = 0.5)
        self.play(*[Write(t) for t in text_y], run_time = 0.5)
        self.wait(1)
        self.play(Write(pg), run_time = 2)
        for p in ps:
            self.play(Write(p), run_time = 0.2)
        self.wait(5)
        self.play(
            *[Uncreate(t) for t in text_x],
            *[Uncreate(t) for t in text_y],
            Uncreate(axes)
        )
        self.play(
            *[Uncreate(p) for p in ps],
            Uncreate(pg)
        )
        self.wait(1)
        