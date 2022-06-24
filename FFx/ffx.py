#   MANIM-FFx
#   
#   L        DDDDD    DDDDD    MM         MM  IIIII       A       OOOOOOOOO
#   L        D    D   D    D   M M       M M    I        A A      O       O
#   L        D     D  D     D  M  M     M  M    I       A   A     O       O
#   L        D     D  D     D  M   M   M   M    I      AAAAAAA    O       O
#   L        D    D   D    D   M    M M    M    I     A       A   O       O
#   LLLLLLL  DDDDD    DDDDD    M     M     M  IIIII  A         A  OOOOOOOOO 
#   
#   author: LDDMiao
#   date: 2021 - 11 - 7 TO 2022 - _ - _
#   version: V1.1.1
#       > setup.py
#               author: LDDMiao & cigar666
#               date: 2022 - 2 - 3 TO 2022 - ? - ?
#               version: V2.1.7
#
#   QAQ好长好难做
#   你这代码保熟吗？

import cmath as cm
import math as m
import random as ran
import numpy as np
import scipy as sc
import matplotlib as mat
import matplotlib.pyplot as plt

from manimlib.imports import *
from numpy import *
from decimal import *

DFont_WeiRuanYaHei = "微软雅黑"
DFont_MFLangQianNoncommercial_Light = "MFLangQian_Noncommercial-Light"
DFont_MFLangQianNoncommercial_Bold = "MFLangQian_Noncommercial-Bold"
DFont_MFXingHei_Noncommercial_Light = "MFXingHei_Noncommercial-Light"
DFont_MFXingHei_Noncommercial_Bold = "MFXingHei_Noncommercial-Bold"

class DAni_1:
    # 实现一些代码量较大的动画效果

    # sc = Scene()
    def __init__(self, thisScene):
        self.sc = thisScene
    
    def FunctionGraphEx(self, func, x_range = [-8, 8, 0.01], lineColor = WHITE):
        # 用来画一些自带函数不方便渲染的图像
        # 注意，返回一个VGroup

        it = x_range[0]
        endx = x_range[1]
        st = x_range[2]
        obj = VGroup()
        while it <= endx:
            obj.add(
                Line(
                    [it, func(it), 0],
                    [it + st, func(it + st), 0],
                    color = lineColor
                )
            )
            it = it + st
        return obj

    def getPointWithText(self, text, dotLocate = ORIGIN, textNextSight = UP, **dotsKwards):
        # 获得一个带文字的点，默认使用不含r的TexMobject
        g = VGroup(
            Dot(dotLocate, **dotsKwards),
            TexMobject(text).scale(0.7)
        )
        g[1].next_to(g[0], textNextSight)
        return g

    def gpwtList(self, texts, locates, textsNextSight = UP, **dotsKwards):
        # 获得一堆带文字的点，将返回list
        # texts与locates为list，应该对应
        # textsNextSight为标量，默认为UP
        dots = []
        if len(texts) != len(locates):
            print("texts number is not equal to locates!")
            return []
        for i in range(len(texts)):
            dots.append(self.getPointWithText(
                texts[i],
                dotLocate = locates[i],
                textNextSight = textsNextSight,
                **dotsKwards
            ))
        return dots

    def fadeInTitle(self, titleText, subTitleText = "", titleFont = DFont_MFLangQianNoncommercial_Light, showTime = 5, lineRightTo = 6, lineWidth = 0.075, titletc = {}):
        # 对标题进行一个华丽的淡出淡入
        # 实际上有一点歪打正着，不对可以自行改改

        textHeight = 1.8
        title = Text(titleText, font = titleFont).scale(1.5).move_to(UP * 5, aligned_edge = RIGHT)
        dot = Dot(
            LEFT * (lineRightTo + 0.5),
            color = BLACK
        ).shift(UP * 5)
        sq_cover = Rectangle(
            height = textHeight + 0.5, 
            width = 32, 
            color = BLACK,
            fill_opacity = 1.0,
            stroke_color = BLACK
        ).move_to(UP * 5, aligned_edge = RIGHT)
        if subTitleText == "":
            sq_line = Rectangle(
                height = textHeight, 
                width = lineWidth, 
                color = WHITE,
                fill_opacity = 1.0,
                stroke_color = WHITE
            ).move_to(UP * 5)
            subTitleText = Text("")
        else:
            sq_line = Rectangle(
                height = textHeight, 
                width = lineWidth, 
                color = WHITE,
                fill_opacity = 1.0,
                stroke_color = WHITE
            ).move_to(UP * 5 + DOWN * 0.25)
            subTitleText = Text(subTitleText, font = titleFont).scale(0.7).move_to(UP * 5 + DOWN * 0.5 + RIGHT * title.get_left()[0], aligned_edge = LEFT)
            # print(RIGHT * title.get_left()[0])

        if titletc != {}:
            title.set_color_by_t2c(titletc)
            subTitleText.set_color_by_t2c(titletc)

        self.sc.add(title)
        self.sc.add(subTitleText)
        self.sc.add(sq_cover)
        self.sc.add(dot)
        self.sc.add(sq_line)
        self.sc.play(
            sq_cover.shift, DOWN * 5,
            sq_line.shift, DOWN * 5,
            title.shift, DOWN * 5,
            subTitleText.shift, DOWN * 5,
            run_time = 1.5
        )
        self.sc.wait(0.5)
        self.sc.play(
            sq_cover.shift, LEFT * lineRightTo,
            sq_line.shift, RIGHT * lineRightTo,
            subTitleText.shift, LEFT * title.get_left()[0],
            title.move_to, ORIGIN, aligned_edge = ORIGIN,
            run_time = 1.5
        )
        self.sc.wait(0.25)
        dot.shift(DOWN * 5)
        self.sc.play(
            ShowPassingFlashAround(title),
            Flash(dot, color = WHITE),
            title.scale, 1.2,
            subTitleText.shift, DOWN * 0.3,
            sq_line.shift, LEFT * lineRightTo * 2,
            sq_line.set_opacity, 0.5,
            run_time = 1.5
        )

        self.sc.wait(showTime)

        dot.shift(UP * 5)
        self.sc.play(
            sq_line.shift, RIGHT * lineRightTo,
            sq_line.set_opacity, 1.0,
            sq_cover.shift, RIGHT * lineRightTo,
            title.move_to, LEFT * lineRightTo,
            subTitleText.move_to, LEFT * lineRightTo,
            run_time = 1.5
        )
        self.sc.wait(0.5)
        title.move_to(UP * 5)
        subTitleText.move_to(UP * 5)
        self.sc.play(
            FadeOut(sq_cover),
            FadeOut(sq_line),
            FadeOut(title),
            FadeOut(subTitleText),
            run_time = 1.5
        )
        # self.sc.play(
        #     sq_cover.shift, DOWN * 5,
        #     sq_line.shift, DOWN * 5,
        #     titleText.shift, DOWN * 5,
        #     run_time = 1.5
        # )
        self.sc.wait(1)

    def defineTextList(self, type = "Text", textLocation = ORIGIN, textAligned = ORIGIN, textColor = WHITE, textFont = DFont_MFLangQianNoncommercial_Light, autoScale = False, textScale = 0.8, textWidth = -1, t2cDict = {}, textList = []):
        # 自动生成Text列表，并含有自动格式控制
        # 打开autoScale，若不提供textWidth，则第一个text大小将会设为textScale，否则将所有宽度设为textWidth
        # 其余Text将会进行width自适配
        # 提供t2cdict字典，格式：{"count": {"text": color, ...}, ...}
        # type = "Text" "TextMobject" or "TexMobject"，为后两者时textFont无效

        # 另外这里的逻辑能一次写对也是奇迹
        
        def tryLength(textClass, wid):
            # 返回一个合适于宽度wid的scale系数，最大将返回4
            sc = 0.01
            while sc <= 4:
                textClass.scale(sc)
                loc_1 = textClass.get_left()
                loc_2 = textClass.get_right()
                w_ = loc_2[0] - loc_1[0]
                if w_ >= wid:
                    textClass.scale(1 / sc)
                    return sc
                textClass.scale(1 / sc)
                sc = sc + 0.01
            return 4

        t = []
        w = 0
        # print(textList)
        for i in range(len(textList)):
            # 处理文字，字体，总体颜色
            if type == "Text":
                text = Text(textList[i], font = textFont, color = textColor)
            else:
                text = Text(textList[i], color = textColor)

            # 处理缩放
            if autoScale == True:
                if i == 0 and textWidth == -1:
                    text.scale(textScale)
                    loc1 = text.get_left()
                    loc2 = text.get_right()
                    w = loc2[0] - loc1[0]
                if i != 0 and textWidth == -1:
                    text.scale(tryLength(text, w))
                if textWidth != -1:
                    text.scale(tryLength(text, textWidth))
            else:
                text = text.scale(textScale)

            # 处理位移
            text = text.move_to(textLocation, aligned_edge = textAligned)

            # 处理颜色
            if t2cDict != {}:
                text.set_color_by_t2c(t2cDict.get(str(i), {})) 

            t.append(text)
        return t

    def p2p_LR(self, point, sight, scaleUD = False):
        # 将一个屏幕上点的位置转移到分成两半的左或右边的屏幕的点的位置
        # sight = "L"为左端，sight = "R"为右端，错误的填写将返回原来的点位置
        # scaleUD表示是否对上下同时缩放

        if sight != "L" and sight != "R":
            return point
        
        if scaleUD:
            point[1] = point[1] / 2
        if sight == "L":
            point[0] = -point[0] / 2 - FRAME_WIDTH / 4
            pass
        if sight == "R":
            point[0] = -point[0] / 2 + FRAME_WIDTH / 4
        return point

    def getArrowFromp2p(self, p1, p2, arrowBuff = 0.2, **arrowKwards):
        # 获取一个从点射向点的箭头
        return Arrow(p1.get_center(), p2.get_center(), buff = arrowBuff, **arrowKwards)

    def gafpList(self, pMap, arrowsBuff = 0.2, **arrowKwards):
        # 获取一堆从点射向点的箭头
        # pMap是二维Dot型list，包含有序的箭头关系
        arrows = []
        for i in range(len(pMap)):
            arrows.append(self.getArrowFromp2p(
                pMap[i][0],
                pMap[i][1],
                arrowBuff = arrowsBuff,
                **arrowKwards
            ))
        return arrows

    def shiftList(self, mobjects, locate, type = "method", **animateKwards):
        # 对list内对象进行移动
        # type可选animate或method
        # 若是animate则需提供scene
        # 若是method则返回移动后的list
        if type == "animate":
            l_a = []
            for i in mobjects:
                l_a.append(i.shift)
                l_a.append(locate)
            self.sc.play(
                *[j for j in l_a],
                **animateKwards
            )
        if type == "method":
            for i in range(len(mobjects)):
                mobjects[i] = mobjects[i].shift(locate)
            return mobjects

    def getColorGradient(self, numOfFPS, colors):
        # 返回渐变颜色路径
        # colors为Color型List，若colors为空则生成随机颜色路径，否则按colors渐变三种颜色
        # numOfFPS表示一共帧数
        # 返回一个Color型的List
        resColor = []
        if colors == []:
            colors = [rgb_to_color(np.array([ran.random() for _ in range(3)])) for _ in range(3)]
        ef = int(numOfFPS / (len(colors) - 1))
        for i in range(len(colors) - 1):
            c1 = color_to_rgb(colors[i])
            c2 = color_to_rgb(colors[i + 1])
            dc = (c2 - c1) / ef
            for j in range(ef):
                resColor.append(rgb_to_color(c1 + dc * j))
        less = numOfFPS - len(resColor)
        # 对齐
        if less != 0:
            for _ in range(int(less)):
                resColor.append(colors[len(colors) - 1])
        return resColor


class DAni_2(TexMobject):
    # 本类精简于cigar666的MyText类，可以在公式中使用自定义字体
    # 注意：Tex下标分析方法：
    # 使用debugTeX, 先self.add(tex) 然后再debugTeX(self, tex)
    # 导出最后一帧，观察每段字符上的标号，即为下标
    # 或使用自带的函数get_submobject_index_labels获取下标的VGroup
    # 然后添加

    # 默认配置
    CONFIG = {
        'default_font': DFont_MFLangQianNoncommercial_Bold,
        'tex_scale_factor': 1,
    }

    def __init__(self, *tex_strings, **kwargs):
        # 传入欲实现转换的Tex小块以及参数
        # 例子：
        # formula_i = MyText(
        #         'f', '(', 't', ')', '=', 'x', '(', 't', ')', '+', 'y', '(', 't', ')', 'i', '=', '(', 'R', '-', 'r', ')', 'e^{', 'i', 't}', '+', 'd', 'e^{', '-', 'i', '{R', '-', 'r', '\\over', 'r}', 't}',
        #         default_font = someFont, 
        #         tex_scale_factor = 0.75
        #     )
        # 可以传入color_dict对对应的Tex上色
        # formula_i.set_color_by_tex_to_color_map(color_dict)
        self.tex_list = tex_strings
        TexMobject.__init__(self, *tex_strings, **kwargs)
        self.new_font_texs = VGroup()

    def reset_tex_with_font(self):
        self.new_font_texs = VGroup()

    def get_color_by_tex(self, tex, **kwargs):
        parts = self.get_parts_by_tex(tex, **kwargs)
        colors = []
        for part in parts:
            colors.append(part.get_color())
        return colors[0]

    def get_new_font_texs(self, replace_dict):
        # 将载入的Tex片段转换成为一组Text后输出
        # 需要传入replace_dict参数以表明某些无法识别的Tex片段应该以什么形式输出
        # 例如：
        # replace_dict = {'e^{': 'e', 't}': 't', '{R': 'R', 'r}': 'r', '\\over': '-'}
        # new_formula = formula_i.get_new_font_texs(replace_dict)
        # 只需要转换无法识别的即可，无需写入所有
        for i in range(len(self.tex_strings)):
            tex = self.tex_strings[i]
            color = self.get_color_by_tex(tex)
            if tex in replace_dict:
                tex = replace_dict[tex]
            tex_new = Text(tex, font=self.default_font, color=color)
            tex_new.set_height(self[i].get_height())
            if tex == '-' or tex == '=':
                tex_new.set_width(self[i].get_width(), stretch=True)
            tex_new.scale(self.tex_scale_factor)
            tex_new.move_to(self[i])
            self.new_font_texs.add(tex_new)
        return self.new_font_texs

        

    # HELP：
        # DFont:
        #     DFont_WeiRuanYaHei = "微软雅黑"
        #     DFont_MFLangQianNoncommercial_Light = "MFLangQian_Noncommercial-Light"
        #     DFont_MFLangQianNoncommercial_Bold = "MFLangQian_Noncommercial-Bold"
        #     DFont_MFXingHei_Noncommercial_Light = "MFXingHei_Noncommercial-Light"
        #     DFont_MFXingHei_Noncommercial_Bold = "MFXingHei_Noncommercial-Bold"
        # DAni_1:
        # 实现一些代码量较大的动画效果
        #     __init__ 传入欲实现动画的Scene
        #     FunctionGraphEx 用来画一些自带函数不方便渲染的图像
        #     getPointWithText 获得一个带文字的点，默认使用不含r的TexMobject
        #     gpwtList 获得一堆带文字的点
        #     fadeInTitle 对标题进行一个华丽的淡出淡入
        #     defineTextList 自动生成Text列表，并含有自动格式控制
        #     p2p_LR 将一个屏幕上点的位置转移到分成两半的左或右边的屏幕的点的位置
        #     getArrowFromp2p 获取一个从点射向点的箭头
        #     gafpList 获取一堆从点射向点的箭头
        #     shiftList 对列表内对象进行移动
        #     getColorGradient 返回渐变颜色路径
        # DAni_2:
        # 本类精简于cigar666的MyText类，可以在公式中使用自定义字体 
        #     __init__ 传入欲实现转换的Tex小块以及参数
        #     get_new_font_texs 将载入的Tex片段转换成为一组Text后输出
    
# SETUP OVER


###FUNCTIONS###

ad = DAni_1("") #传入伪参数，适用于不使用self的函数

def protect_range(x):
    if x >= 100 or x <= -100:
        return 15
    else:
        return x

def func_itea(func, n):
    return ad.FunctionGraphEx(lambda x: protect_range(func(x, n)), x_range = [-10, 10, 0.005], lineColor = BLUE)

###CONSTANTS###

def func_2(x, n):
    for _ in range(n):
        x = x ** 2 - 1
    return x

# def func_3_complex(a, b, n):
#     for _ in range(n):
#         x = (cm.cos(x) - cm.sin(x)) / (cm.cos(x) - cm.exp(x))
#     return x

#--1--
text1_1 = TexMobject(r"f\left( f\left( x\right) \right) =ax^2+bx+c").scale(1.4)

text1_2 = [
    TexMobject(r"f\left( x\right) =x^2-1").scale(1.4 * 0.7).shift(DOWN * 2),
    TexMobject(r"f\left( f\left( x\right) \right) =\left( x^2-1\right) ^2-1=x^4-2x^2").scale(1.4 * 0.7 * 0.7).shift(DOWN * 2),
    TexMobject(r"f\left( f\left( f\left( x\right) \right) \right) =\left( x^4-2x^2\right) ^2-1=x^8-4x^6+4x^4-1").scale(1.4 * 0.7 * 0.7).shift(DOWN * 2),
    TexMobject(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right) =\text{...}").scale(1.4 * 0.7 * 0.7).shift(DOWN * 2),
    TexMobject(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right) =\text{...}").scale(1.4 * 0.7 * 0.7).shift(DOWN * 2)
]

text1_2[0].set_color_by_tex(r"f\left( x\right)", GREEN)
text1_2[1].set_color_by_tex(r"f\left( f\left( x\right) \right)", GREEN)
text1_2[2].set_color_by_tex(r"f\left( f\left( f\left( x\right) \right) \right)", GREEN)
text1_2[3].set_color_by_tex(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right)", GREEN)
text1_2[4].set_color_by_tex(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right)", GREEN)

text1_3 = TexMobject(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right)").scale(1.4)

text1_4 = Text("迭 代 函 数", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4)

# def func_1(x, n):
#     for i in range(n):
#         x = (m.sqrt(abs(x)) - 1) ** 2
#     return x

dot1_1 = Dot([0.5 * (1 - m.sqrt(5)), 0.5 * (1 - m.sqrt(5)), 0], color = RED)
dot1_2 = Dot([0.5 * (1 + m.sqrt(5)), 0.5 * (1 + m.sqrt(5)), 0], color = RED)

#--2--
text2_1 = TexMobject(r"f\left( x\right)").scale(1.4)
text2_2 = TexMobject(r"f_0\left( x\right) =f\left( x\right)").scale(1.4).shift(DOWN * 0.5)
text2_3 = TexMobject(r"f_{n+1}\left( x\right) =f\left( f_n\left( x\right)\right)").scale(1.4).shift(DOWN * 1)
text2_4 = TexMobject(r"\Longrightarrow").scale(1.5)
text2_5 = Text(r"归 纳 定 义 函 数 的 迭 代", font = DFont_MFXingHei_Noncommercial_Bold).scale(1).shift(RIGHT * 3)

group1 = VGroup(text2_1, text2_2, text2_3)

#--3--
text3_1 = Text(r"不 动 点", font = DFont_MFLangQianNoncommercial_Bold, color = RED).scale(1.2).shift(LEFT * 10 + UP * 0.5)
text3_2 = TexMobject(r"f\left( x\right) =x^2-1").scale(1.4)
text3_3 = [
    TexMobject(r"P_1=\left( \frac{1-\sqrt{5}}{2} ,\frac{1-\sqrt{5}}{2}\right)").scale(0.6).shift(RIGHT * 3.5 + UP * 2.5),
    TexMobject(r"P_2=\left( \frac{1+\sqrt{5}}{2} ,\frac{1+\sqrt{5}}{2}\right)").scale(0.6).shift(RIGHT * 3.5 + UP * 1.5)
]
dashLine3_1 = DashedLine(array([-2, -2, 0]), array([6, 6, 0]), color = GREY).shift(LEFT * 1)
text3_4 = TexMobject(r"f_{n}\left( x \right) =x").scale(1.4).shift(DOWN * 1)
text3_5 = Text(r"不 动 点", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4)
text3_6 = Text(r"一 阶 不 动 点", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4).shift(UP * 0.5)
text3_7 = Text(r"M 阶 不 动 点", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4).shift(UP * 0.5)
text3_8 = TexMobject(r"f_{nM}\left( x \right) =f_M\left( x \right) =x").scale(1.2).shift(DOWN * 1)
text3_9 = TexMobject(r"f\left( x \right) =\frac{\cos \left( x \right) -\sin \left( x \right)}{\cos \left( x \right) -e^x}").scale(1.2)

numplane_1 = NumberPlane()
numAxes_1 = Axes(
    x_min = -5,
    x_max = 5,
    y_min = -1.25,
    y_max = 5,
    number_line_config={
        "stroke_color": GREY,
        "stroke_width": 2,
        "include_tip": False,
    }
).shift(LEFT * 1)

group2 = VGroup(dot1_1, dot1_2)

#--4--
text4_1 = Text(r"轨 道 图", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4)
text4_2 = [
    TexMobject(r"f\left( x\right) =x^2-1").scale(1).shift(UP * 0.5),
    TexMobject(r"f\left( f\left( x\right) \right) =\left( x^2-1\right) ^2-1=x^4-2x^2").scale(1).shift(UP * 0.5),
    TexMobject(r"f\left( f\left( f\left( x\right) \right) \right) =\left( x^4-2x^2\right) ^2-1=x^8-4x^6+4x^4-1").scale(1).shift(UP * 0.5),
    TexMobject(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right)=\text{...}").scale(1).shift(UP * 0.5),
    TexMobject(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right)=\text{...}").scale(1).shift(UP * 0.5)
]
# text4_3 = [
#     Text(r"x = " + str(func_2(4, 1)), font = "微软雅黑").scale(1).shift(DOWN * 0.5),
#     Text(r"x = " + str(func_2(4, 2)), font = "微软雅黑").scale(1).shift(DOWN * 0.5),
#     Text(r"x = " + str(func_2(4, 3)), font = "微软雅黑").scale(1).shift(DOWN * 0.5),
#     Text(r"x = " + str(func_2(4, 4)), font = "微软雅黑").scale(1).shift(DOWN * 0.5),
#     Text(r"x = " + str(func_2(4, 5)), font = "微软雅黑").scale(1).shift(DOWN * 0.5),
# ]
text4_4 = TexMobject(r"f\left( x \right) \rightarrow x").scale(1.4).shift(UP * 0.5)
text4_5 = TexMobject(r"f\left( x_1\right) =x_2").scale(0.7).shift(DOWN * 0.5)
text4_6 = Text(r"举 个 例 子", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4)
text4_7 = TexMobject(r"x_0=x\quad x_1=f_1\left( x \right) \quad x_2=f_2\left( x \right) \quad x_3=f_3\left( x \right) ").scale(0.8).shift(DOWN * 1)

tq4_1 = TexMobject(r"x_0", color = GREY).scale(1.1)
tq4_2 = TexMobject(r"x_1", color = GREY).scale(1.1 * 0.75)
tq4_3 = TexMobject(r"x_2", color = GREY).scale(1.1 * 0.75).move_to(RIGHT * 1)
tq4_4 = TexMobject(r"x_3", color = GREY).scale(1.1 * 0.75).move_to(RIGHT * 3)
square4_1 = Rectangle(height = 1, width = 1, color = ORANGE, fill_opacity = 1.0)
square4_2 = Rectangle(height = 1, width = 1, color = ORANGE, fill_opacity = 1.0).move_to(RIGHT * 1)
square4_3 = Rectangle(height = 1, width = 1, color = ORANGE, fill_opacity = 1.0).move_to(RIGHT * 2)

square4_1.set_sheen(0.5, RIGHT)
square4_2.set_sheen(0.5, RIGHT)
square4_3.set_sheen(0.5, RIGHT)

group7 = VGroup(tq4_4, square4_1, square4_2, square4_3)

dot4_1 = [
    ad.getPointWithText("x_1", dotLocate = DOWN * 0.5 + LEFT * 0.5, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
    ad.getPointWithText("x_2", dotLocate = DOWN * 0.5 + RIGHT * 0.5, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0)
]
# Dot().get_center
line4_1 = [
    ad.getArrowFromp2p(dot4_1[0][0], dot4_1[1][0], arc_path = 0.8)
]

group3 = VGroup(dot4_1[0], dot4_1[1], line4_1[0], text4_5)

#--5--
text5_1 = TexMobject(r"f\left( x \right) =\frac{1}{x}").scale(1.4)
text5_2 = [
    TexMobject(r"f\left( z_1 \right) =z_2").shift(DOWN * 1),
    TexMobject(r"f\left( z_2 \right) =z_3").shift(DOWN * 1),
    TexMobject(r"f\left( z_3 \right) =z_4").shift(DOWN * 1),
    TexMobject(r"f\left( z_4 \right) =z_1").shift(DOWN * 1)
]
text5_3 = Text(r"轨 道 图", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4).shift(RIGHT * 4)
text5_4 = Text(r"4 - 循 环", font = DFont_MFXingHei_Noncommercial_Bold).shift(DOWN * 1.2)
text5_5 = Text(r"m - 循 环", font = DFont_MFXingHei_Noncommercial_Bold).shift(DOWN * 1.2)
text5_6 = Text(r"m - 圈", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4)

dot5_1 = dot4_1
dot5_2 = [
    ad.getPointWithText("x_1", dotLocate = UP * 1 + LEFT * 3 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 0
    ad.getPointWithText("x_2", dotLocate = UP * 1 + LEFT * 2 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 1
    ad.getPointWithText("x_3", dotLocate = UP * 1 + LEFT * 1 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 2
    ad.getPointWithText("z_1", dotLocate = UP * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 3
    ad.getPointWithText("z_2", dotLocate = RIGHT * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 4
    ad.getPointWithText("z_3", dotLocate = DOWN * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 5
    ad.getPointWithText("z_4", dotLocate = LEFT * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 6
    ad.getPointWithText("y_1", dotLocate = DOWN * 1 + RIGHT * 2 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 7
    ad.getPointWithText("y_2", dotLocate = DOWN * 1 + RIGHT * 1 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0) # 8
]

color5_1, color5_2 = rgb_to_color(hex_to_rgb("#00DBDE")), rgb_to_color(hex_to_rgb("#FC00FF"))

dot5_3 = Dot(
    fill_opacity = 1.0, 
    radius = 0.12, 
    stroke_width = 1.0
).shift(UP * 1).shift(UP * 1)
dot5_4 = Dot(
    fill_opacity = 1.0, 
    radius = 0.12, 
    stroke_width = 1.0
).shift(UP * 1).shift(RIGHT * 1)

dot5_3.set_color(color5_1)
dot5_4.set_color(color5_2)

dot5_3.set_sheen(0.5, RIGHT)
dot5_4.set_sheen(0.5, RIGHT)

#Ahh...
#x_123, z_1234, y_12 -> 0 ~ 8

line5_1 = line4_1
line5_2 = [
    ad.getArrowFromp2p(dot5_2[0][0], dot5_2[1][0]),
    ad.getArrowFromp2p(dot5_2[1][0], dot5_2[2][0]),
    ad.getArrowFromp2p(dot5_2[2][0], dot5_2[3][0]),
    ad.getArrowFromp2p(dot5_2[3][0], dot5_2[4][0]),
    ad.getArrowFromp2p(dot5_2[4][0], dot5_2[5][0]),
    ad.getArrowFromp2p(dot5_2[5][0], dot5_2[6][0]),
    ad.getArrowFromp2p(dot5_2[6][0], dot5_2[3][0]),
    ad.getArrowFromp2p(dot5_2[8][0], dot5_2[5][0]),
    ad.getArrowFromp2p(dot5_2[7][0], dot5_2[8][0])
]

group4 = VGroup(dot5_1[0], dot5_1[1], line5_1[0], text5_1)
group5 = VGroup(*[i for i in dot5_2])
group5.add(*[i for i in line5_2])
group8 = VGroup()
for i in range(9):
    group5.add(dot5_2[i])
    group5.add(line5_2[i])
group6 = VGroup(
    dot5_2[3][0], 
    dot5_2[4][0], 
    dot5_2[5][0], 
    dot5_2[6][0]
)

background5_1 = SurroundingRectangle(group6, opacity = 0.1, fill_color = WHITE, color = BLUE)

#--6--

text6_1 = Text(r"循 环 轨 道 图 的 性 质", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.2)
text6_2 = Text(r"多 个 圈", font = DFont_MFXingHei_Noncommercial_Bold).move_to(RIGHT * 2.5)
text6_3 = Text(r"非 循 环 轨 道 图 有 无 穷 多 顶 点", font = DFont_MFXingHei_Noncommercial_Bold)
text6_4 = Text(r"对 于 函 数 f  ， 其 轨 道 图 可 能 不 止 一 个", font = DFont_MFXingHei_Noncommercial_Bold)
text6_5 = TexMobject(r"f\left( x\right) =x!").move_to(UP * 1 + LEFT * 0.5)
text6_6 = TexMobject(r"x_0=0").move_to(LEFT * (2.5 + 3.75) / 2)
text6_7 = TexMobject(r"x_0=3").move_to(RIGHT * 2)

color6_1 = color5_1

text6_1.set_color_by_t2c({"循 环 轨 道 图": color6_1, "性 质": BLUE})
text6_2.set_color_by_t2c({"多 个": GREEN})
text6_3.set_color_by_t2c({"无 穷 多": GREEN})
text6_4.set_color_by_t2c({"不 止 一 个": GREEN})

#                      < k_2
# y_2 <-- y_1 <-- k_3     ^
#                      > k_1
dot6_1 = dot5_2
dot6_1.append(ad.getPointWithText(r"k_3", dotLocate = DOWN * 1 + RIGHT * 3 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0)) # 9
dot6_1.append(ad.getPointWithText(r"k_1", dotLocate = DOWN * 1.5 + RIGHT * 4 * m.sqrt(2), textNextSight = DOWN, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0)) # 10
dot6_1.append(ad.getPointWithText(r"k_2", dotLocate = DOWN * 0.5 + RIGHT * 4 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0)) # 11

#          v  <
# x_0 --> x_1 ^
# 
dot6_2 = [
    ad.getPointWithText(r"x_0=0", dotLocate = LEFT * 2 + LEFT * 1.75 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
    ad.getPointWithText(r"x_1=1", dotLocate = LEFT * 2 + LEFT * 0.5 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0)
]
# x_0 --> x_1 -- > x_2 --> ...
dot6_3 = [
    ad.getPointWithText(r"x_0=3", dotLocate = RIGHT * 2 + LEFT * 2.25 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
    ad.getPointWithText(r"x_1=6", dotLocate = RIGHT * 2 + LEFT * 0.75 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
    ad.getPointWithText(r"x_2=720", dotLocate = RIGHT * 2 + RIGHT * 0.75 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
    ad.getPointWithText(r"...", dotLocate = RIGHT * 2 + RIGHT * 2.25 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
]

line6_1 = line5_2
line6_1.append(ad.getArrowFromp2p(dot5_2[9][0], dot5_2[7][0]))
line6_1.append(ad.getArrowFromp2p(dot5_2[9][0], dot5_2[10][0]))
line6_1.append(ad.getArrowFromp2p(dot5_2[10][0], dot5_2[11][0]))
line6_1.append(ad.getArrowFromp2p(dot5_2[11][0], dot5_2[9][0]))
line6_2_1 = Line(
    array(
        [
            text6_2.get_center()[0] - 0.5,
            text6_2.get_center()[1],
            0
        ]
    ),
    array(
        [
            text6_2.get_center()[0] + 0.5,
            text6_2.get_center()[1],
            0
        ]
    ),
    color = RED
)
line6_2_2 = Line(
    array(
        [
            text6_2.get_center()[0] - 0.5,
            text6_2.get_center()[1],
            0
        ]
    ),
    array(
        [
            text6_2.get_center()[0] + 1,
            text6_2.get_center()[1],
            0
        ]
    ),
    color = RED
).scale(0.75)
line6_2 = [
    ad.getArrowFromp2p(dot6_2[0][0], dot6_2[1][0]),
    Arc(start_angle = PI + 0.4, angle = 2 * PI - 0.8, radius = 0.5).add_tip().scale(0.5).move_to(LEFT * 2.5 + RIGHT * 0.55 + DOWN * 2)
]
line6_3 = [
    ad.getArrowFromp2p(dot6_3[0][0], dot6_3[1][0]),
    ad.getArrowFromp2p(dot6_3[1][0], dot6_3[2][0]),
    ad.getArrowFromp2p(dot6_3[2][0], dot6_3[3][0]),
]

group6_2_1 = VGroup(
    dot6_1[9][0],
    dot6_1[10][0],
    dot6_1[11][0]
)
group6_1 = VGroup(*[i for i in dot6_1], *[i for i in line6_1])
group6_2 = VGroup(*[i for i in dot6_2], *[i for i in line6_2])
group6_3 = VGroup(*[i for i in dot6_3], *[i for i in line6_3])

rectan6_1 = Rectangle(width = 0.05, height = 3, color = WHITE, fill_opacity = 1.0).move_to(LEFT * 7 + UP * 1.5)

background6_1 = SurroundingRectangle(group6_2_1, opacity = 0.1, fill_color = WHITE, color = PURPLE)
# background6_2 = RoundedRectangle(width = 5, height = 3, opacity = 1.0, fill_color = GREY, stroke_color = WHITE).move_to(UP * 2.5 + LEFT * 5, aligned_edge = LEFT)

# --7--
text7_1 = DAni_2(
    "\\text{i: }", "f", "\\text{的一个}", "2m", "\\text{循环轨道图可分裂为两个}", "f_", "{2}", "\\text{的}", "m", "\\text{循环轨道图}",
    default_font = DFont_MFLangQianNoncommercial_Light,
    text_scale_factor = 0.77
).get_new_font_texs({
    "\\text{i: }": "i： ",
    "\\text{的一个}": "的一个",
    "\\text{循环轨道图可分裂为两个}": "循环轨道图可分裂为两个",
    "f_": "f",
    "{2}": "2",
    "\\text{的}": "的",
    "\\text{循环轨道图}": "循环轨道图"
}).scale(0.8).move_to(UP * 1 + LEFT * 6, aligned_edge = LEFT)
text7_2 = DAni_2("\\text{i: }", "f", "\\text{的一个非循环轨道图可分裂为两个}", "f_", "{2}", "\\text{的非循环轨道图}",
    default_font = DFont_MFLangQianNoncommercial_Light,
    text_scale_factor = 0.77
).get_new_font_texs({
    "\\text{ii: }": "ii: ",
    "\\text{的一个非循环轨道图可分裂为两个}": "的一个非循环轨道图可分裂为两个",
    "f_": "f",
    "{2}": "2",
    "\\text{的非循环轨道图}": "的非循环轨道图"
}).scale(0.8).move_to(UP * 1 + LEFT * 6, aligned_edge = LEFT)
text7_3 = DAni_2("\\text{iii: }", "f", "\\text{的一个}", "2m+1", "\\text{循环轨道图可变形为一个}", "f_", "{2}", "\\text{的}", "2m+1", "\\text{循环轨道图}",
    default_font = DFont_MFLangQianNoncommercial_Light,
    text_scale_factor = 0.77
).get_new_font_texs({
    "\\text{iii: }": "iii: ",
    "\\text{的一个}": "的一个",
    "\\text{循环轨道图可变形为一个}": "循环轨道图可变形为一个",
    "f_": "f",
    "{2}": "2",
    "\\text{的}": "的",
    "\\text{循环轨道图}": "循环轨道图"
}).scale(0.8).move_to(UP * 1 + LEFT * 6, aligned_edge = LEFT)

# x_1 --> x_2 --> x_3 --> z_1
#                     z_4    z_2
#                         z_3 <-- y_2 <-- y_1
dot7_1 = ad.gpwtList(
    [
        "x_1",  # 0
        "x_2",  # 1
        "x_3",  # 2
        "z_1",  # 3
        "z_2",  # 4
        "z_3",  # 5
        "z_4",  # 6
        "y_1",  # 7
        "y_2"   # 8
    ],
    [
        UP * 1 + LEFT * 3 * m.sqrt(2),  # 0
        UP * 1 + LEFT * 2 * m.sqrt(2),  # 1
        UP * 1 + LEFT * 1 * m.sqrt(2),  # 2
        UP * 1,  # 3
        RIGHT * 1,  # 4
        DOWN * 1,  # 5
        LEFT * 1,  # 6
        DOWN * 1 + RIGHT * 2 * m.sqrt(2),  # 7
        DOWN * 1 + RIGHT * 1 * m.sqrt(2)    # 8
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
dot7_1a = ad.gpwtList(
    [
        "x_1",  # 0
        "x_2",  # 1
        "x_3",  # 2
        "z_1",  # 3
        "z_2",  # 4
        "z_3",  # 5
        "z_4",  # 6
        "y_1",  # 7
        "y_2"   # 8
    ],
    [
        UP * 1 + LEFT * 3 * m.sqrt(2),  # 0
        UP * 1 + LEFT * 2 * m.sqrt(2),  # 1
        UP * 1 + LEFT * 1 * m.sqrt(2),  # 2
        UP * 1,  # 3
        RIGHT * 1,  # 4
        DOWN * 1,  # 5
        LEFT * 1,  # 6
        DOWN * 1 + RIGHT * 2 * m.sqrt(2),  # 7
        DOWN * 1 + RIGHT * 1 * m.sqrt(2)    # 8
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
# dot7_1 = [
#     ad.getPointWithText("x_1", dotLocate = UP * 1 + LEFT * 3 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 0
#     ad.getPointWithText("x_2", dotLocate = UP * 1 + LEFT * 2 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 1
#     ad.getPointWithText("x_3", dotLocate = UP * 1 + LEFT * 1 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 2
#     ad.getPointWithText("z_1", dotLocate = UP * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 3
#     ad.getPointWithText("z_2", dotLocate = RIGHT * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 4
#     ad.getPointWithText("z_3", dotLocate = DOWN * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 5
#     ad.getPointWithText("z_4", dotLocate = LEFT * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 6
#     ad.getPointWithText("y_1", dotLocate = DOWN * 1 + RIGHT * 2 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 7
#     ad.getPointWithText("y_2", dotLocate = DOWN * 1 + RIGHT * 1 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0) # 8
# ]

#                  v     <
# x_1 --> x_3 --> z_2 > z_4 <-- y_2
# 
dot7_2 = ad.gpwtList(
    [
        "x_1",  # 0
        "x_3",  # 1
        "z_2",  # 2
        "z_4",  # 3
        "y_2"   # 4
    ],
    [
        LEFT * 3.5 + LEFT * 1.5 + UP * 0.5,  # 0
        LEFT * 3.5 + LEFT * 0.5 + UP * 0.5,  # 1
        LEFT * 3.5 + RIGHT * 0.5 + UP * 0.5,  # 2
        LEFT * 3.5 + RIGHT * 0.5 + DOWN * 0.5,  # 3
        LEFT * 3.5 + RIGHT * 1.5 + DOWN * 0.5  # 4
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
dot7_2a = ad.gpwtList(
    [
        "x_1",  # 0
        "x_3",  # 1
        "z_2",  # 2
        "z_4",  # 3
        "y_2"   # 4
    ],
    [
        LEFT * 3.5 + LEFT * 1.5 + UP * 0.5,  # 0
        LEFT * 3.5 + LEFT * 0.5 + UP * 0.5,  # 1
        LEFT * 3.5 + RIGHT * 0.5 + UP * 0.5,  # 2
        LEFT * 3.5 + RIGHT * 0.5 + DOWN * 0.5,  # 3
        LEFT * 3.5 + RIGHT * 1.5 + DOWN * 0.5  # 4
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
# dot7_2 = [
#     dot7_1[0].move_to(LEFT * 3.5 + LEFT * 1.5 + UP * 0.5),  # x_1     0
#     dot7_1[2].move_to(LEFT * 3.5 + LEFT * 0.5 + UP * 0.5),  # x_3     1
#     dot7_1[4].move_to(LEFT * 3.5 + RIGHT * 0.5 + UP * 0.5),  # z_2     2
#     dot7_1[6].move_to(LEFT * 3.5 + RIGHT * 0.5 + DOWN * 0.5),  # z_4     3
#     dot7_1[8].move_to(LEFT * 3.5 + RIGHT * 1.5 + DOWN * 0.5)   # y_2     4
# ]

#          v     <
# x_2 --> z_1 > z_3 <-- y_1
# 
dot7_3 = ad.gpwtList(
    [
        "x_2",  # 0
        "z_1",  # 1
        "z_3",  # 2
        "y_1"  # 3
    ],
    [
        RIGHT * 3.5 + LEFT * 1 + UP * 0.5,  # 0
        RIGHT * 3.5 + UP * 0.5,  # 1
        RIGHT * 3.5 + DOWN * 0.5,  # 2
        RIGHT * 3.5 + RIGHT * 1 + DOWN * 0.5  # 3
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
dot7_3a = ad.gpwtList(
    [
        "x_2",  # 0
        "z_1",  # 1
        "z_3",  # 2
        "y_1"  # 3
    ],
    [
        RIGHT * 3.5 + LEFT * 1 + UP * 0.5,  # 0
        RIGHT * 3.5 + UP * 0.5,  # 1
        RIGHT * 3.5 + DOWN * 0.5,  # 2
        RIGHT * 3.5 + RIGHT * 1 + DOWN * 0.5  # 3
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
# dot7_3 = [
#     dot7_1[1].move_to(RIGHT * 3.5 + LEFT * 1 + UP * 0.5),  # x_2     0
#     dot7_1[3].move_to(RIGHT * 3.5 + UP * 0.5),  # z_1     1
#     dot7_1[5].move_to(RIGHT * 3.5 + DOWN * 0.5),  # z_3     2
#     dot7_1[7].move_to(RIGHT * 3.5 + RIGHT * 1 + DOWN * 0.5)   # y_1     3
# ]

dot7_4 = Dot(
    point = dot7_1[0].get_center(),
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
dot7_4.set_color(RED)

ad.shiftList(dot7_2, DOWN * 2.5)
ad.shiftList(dot7_3, DOWN * 2.5)
ad.shiftList(dot7_2a, DOWN * 2.5)
ad.shiftList(dot7_3a, DOWN * 2.5)

line7_1 = ad.gafpList([
    [dot7_1[0][0], dot7_1[1][0]],
    [dot7_1[1][0], dot7_1[2][0]],
    [dot7_1[2][0], dot7_1[3][0]],
    [dot7_1[3][0], dot7_1[4][0]],
    [dot7_1[4][0], dot7_1[5][0]],
    [dot7_1[5][0], dot7_1[6][0]],
    [dot7_1[6][0], dot7_1[3][0]],
    [dot7_1[8][0], dot7_1[5][0]],
    [dot7_1[7][0], dot7_1[8][0]],
])
# line7_1 = [
#     ad.getArrowFromp2p(dot7_1[0][0], dot7_1[1][0]),
#     ad.getArrowFromp2p(dot7_1[1][0], dot7_1[2][0]),
#     ad.getArrowFromp2p(dot7_1[2][0], dot7_1[3][0]),
#     ad.getArrowFromp2p(dot7_1[3][0], dot7_1[4][0]),
#     ad.getArrowFromp2p(dot7_1[4][0], dot7_1[5][0]),
#     ad.getArrowFromp2p(dot7_1[5][0], dot7_1[6][0]),
#     ad.getArrowFromp2p(dot7_1[6][0], dot7_1[3][0]),
#     ad.getArrowFromp2p(dot7_1[8][0], dot7_1[5][0]),
#     ad.getArrowFromp2p(dot7_1[7][0], dot7_1[8][0])
# ]
line7_2 = [
    ad.getArrowFromp2p(dot7_2[0][0], dot7_2[1][0]),
    ad.getArrowFromp2p(dot7_2[1][0], dot7_2[2][0]),
    ad.getArrowFromp2p(dot7_2[2][0], dot7_2[3][0]).shift(LEFT * 0.2),
    ad.getArrowFromp2p(dot7_2[3][0], dot7_2[2][0]).shift(RIGHT * 0.2),
    ad.getArrowFromp2p(dot7_2[4][0], dot7_2[3][0])
]
line7_3 = [
    ad.getArrowFromp2p(dot7_3[0][0], dot7_3[1][0]),
    ad.getArrowFromp2p(dot7_3[1][0], dot7_3[2][0]).shift(LEFT * 0.2),
    ad.getArrowFromp2p(dot7_3[2][0], dot7_3[1][0]).shift(RIGHT * 0.2),
    ad.getArrowFromp2p(dot7_3[3][0], dot7_3[2][0])
]

group7_1 = VGroup(*[i1 for i1 in dot7_1a], *[i2 for i2 in line7_1])
group7_2 = VGroup(*[i1 for i1 in dot7_2a], *[i2 for i2 in line7_2])
group7_3 = VGroup(*[i1 for i1 in dot7_3a], *[i2 for i2 in line7_3])

color7_1 = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

###PROGRAMME###

class s0(Scene):
    def construct(self):
        pass

class s1(Scene):
    def construct(self):
        ad_ = DAni_1(self)

        #--1--
        self.wait(1)
        ad_.fadeInTitle("一  迭代函数", subTitleText = "交叠，即是回环", titletc = {"迭代": RED, "交叠": PINK}, showTime = 3)
        # self.wait(2)
        # self.play(Write(text1_1))
        # self.wait(2)
        # self.play(FadeOut(text1_1))
        self.wait(1.5)
        self.play(Write(text1_2[0]))
        self.wait(2)
        self.play(
            text1_2[0].scale, 0.7,
            text1_2[0].move_to, DOWN * 2
        )
        self.wait(1.5)
        tmp1 = func_itea(func_2, 1)
        for i in range(5):
            if i != 0:
                tmp2 = func_itea(func_2, i + 2)
                self.play(
                    ReplacementTransform(tmp1, tmp2),
                    ReplacementTransform(text1_2[i - 1], text1_2[i])
                )
                self.wait(2)
                tmp1 = tmp2
            else:
                self.play(FadeIn(tmp1))
                # self.wait(1)
                # self.play(
                #     Write(dot1_1),
                #     Write(dot1_2)
                # )
                self.wait(1)
        self.wait(2)
        self.play(
            Uncreate(tmp2),
            text1_2[4].shift, ORIGIN,
            text1_2[4].scale, 1 / 1.4 / 0.7
        )
        self.wait(0.5)
        self.play(ReplacementTransform(text1_2[4], text1_3))
        self.wait(1.5)
        self.play(ReplacementTransform(text1_3, text1_4))
        self.wait(2.5)
        self.play(FadeOut(text1_4))
        self.wait(3)

        #--2--
        self.play(Write(text2_1))
        self.wait(1.5)
        self.play(
            text2_1.shift, UP * 0.5,
            FadeIn(text2_2)
        )
        self.wait(1.5)
        self.play(
            text2_1.shift, UP * 0.5,
            text2_2.shift, UP * 0.5,
            FadeIn(text2_3)
        )
        self.wait(2)
        self.play(group1.shift, LEFT * 3)
        self.wait(0.25)
        self.play(Write(text2_4))
        self.wait(0.25)
        self.play(Write(text2_5))
        self.wait(2.5)
        self.play(
            FadeOut(group1),
            FadeOut(text2_4),
            FadeOut(text2_5)
        )
        self.wait(2)

        # --3--
        ad_.fadeInTitle("二  不动点", subTitleText = "神静，方可察理", titletc = {"不动": RED, "静": PINK}, showTime = 2)
        self.wait(1)
        self.play(
            FadeIn(text3_1),
            text3_1.move_to, LEFT * 5,
            text3_1.scale, 1 / 1.4 / 1.6
        )
        self.wait(1)
        self.play(Write(text3_2))
        self.wait(1)
        tmp1 = func_itea(func_2, 1)
        self.play(
            FadeOut(text3_2), 
            FadeIn(tmp1),
            Write(numAxes_1)
        )
        self.wait(1)
        for i in range(4):
            if i != 0:
                tmp2 = func_itea(func_2, i + 2)
                tmp2.shift(LEFT * 1)
                text1_2[i].shift(LEFT * 1)
                self.play(
                    ReplacementTransform(tmp1, tmp2),
                    ReplacementTransform(text1_2[i - 1], text1_2[i])
                )
                self.wait(2)
                tmp1 = tmp2
            else:
                # self.play(FadeIn(tmp1))
                # self.wait(1)
                # self.wait(1.5)
                self.play(
                    TransformFromCopy(dot1_1, text3_3[0]),
                    TransformFromCopy(dot1_2, text3_3[1]),
                    tmp1.shift, LEFT * 1,
                    dot1_1.shift, LEFT * 1,
                    dot1_2.shift, LEFT * 1
                )
                self.wait(1.5)
                self.play(
                    Write(dot1_1),
                    Write(dot1_2)
                )
                self.wait(0.5)
                self.play(
                    FadeIn(dashLine3_1)
                )
                self.wait(1)
                text1_2[0].shift(LEFT * 1)
                self.play(Write(text1_2[0]))

        self.play(
            Uncreate(tmp1),
            Uncreate(text3_3[0]),
            Uncreate(text3_3[1]),
            Uncreate(text1_2[3]),
            Uncreate(text3_1),
            Uncreate(dashLine3_1),
            Uncreate(numAxes_1),
            ReplacementTransform(group2, text3_5)
        )
        self.wait(2)
        self.play(
            text3_5.shift, UP * 1,
            FadeIn(text3_4)
        )
        self.wait(2)
        self.play(ReplacementTransform(text3_5, text3_6))
        self.wait(2)
        self.play(ReplacementTransform(text3_6, text3_7))
        self.wait(2)
        self.play(ReplacementTransform(text3_4, text3_8))
        self.wait(3)
        self.play(
            FadeOut(text3_7),
            FadeOut(text3_8)
        )
        self.wait(2)
        # self.play(Write(text3_9))
        # self.wait(2)
        # self.play(
        #     Write(numplane1),
        #     text3_9.scale, 0.7 / 1.4,
        #     text3_9.shift, RIGHT * 4
        # )
        # self.wait(1.5)

        # numplane1.prepare_for_nonlinear_transform()
        # for n in range(5):
        #     self.play(numplane1.apply_function, 
        #         lambda z: array([
        #             float(protect_range(func_3(complex(z[0], z[1]), n + 1).real)),
        #             float(protect_range(func_3(complex(z[0], z[1]), n + 1).imag)),
        #             0.0
        #             ])
        #     )
        #     self.wait(1.5)
        # self.wait(1)
        # self.play(
        #     Uncreate(numplane1), 
        #     Uncreate(text3_9)
        # )

class s2(Scene):
    def construct(self):
        ad_ = DAni_1(self)

        #--4--
        self.wait(0.5)
        # self.play(Write(text4_1))
        # self.wait(3)
        # self.play(FadeOutAndShiftDown(text4_1))
        ad_.fadeInTitle("三  函数轨道图", subTitleText = "破格，不落世俗", titletc = {"轨道": RED, "格": PINK}, showTime = 2)
        self.wait(1.5)
        self.play(FadeIn(tq4_1))
        self.wait(1.5)
        self.play(
            FadeIn(square4_1),
            tq4_1.shift, LEFT * 1.5,
            tq4_1.scale, 0.75
        )
        self.wait(1.5)
        self.play(
            Rotate(square4_1, angle = PI),
            tq4_1.move_to, RIGHT * 1.5
        )
        self.wait(1)
        self.play(
            FadeIn(square4_2),
            ReplacementTransform(tq4_1, tq4_2),
            square4_1.shift, LEFT * 1,
        )
        self.wait(1.5)
        self.play(
            Rotate(square4_2, angle = PI),
            tq4_2.move_to, RIGHT * 2
        )
        self.wait(1)
        self.play(
            FadeIn(square4_3),
            ReplacementTransform(tq4_2, tq4_3),
            square4_1.shift, LEFT * 1,
            square4_2.move_to, ORIGIN,
        )
        self.wait(1)
        self.play(
            Rotate(square4_3, angle = PI),
            tq4_3.move_to, RIGHT * 3
        )
        self.wait(1)
        self.play(ReplacementTransform(tq4_3, tq4_4))
        self.wait(2)
        self.play(
            FadeIn(text4_7),
            group7.shift, UP * 1
        )
        self.wait(3)
        self.play(
            FadeOut(group7),
            text4_7.shift, UP * 1
            # FadeOut(),
        )
        self.wait()
        # self.play(
        #     Write(text4_2[0]),
        #     Write(text4_3[0])
        # )
        # for i in range(4):
        #     self.play(ReplacementTransform(text4_2[i], text4_2[i + 1]))
        #     self.play(ReplacementTransform(text4_3[i], text4_3[i + 1]))
        #     self.wait(1.5)
        # self.play(
        #     Uncreate(text4_2[4]),
        #     Uncreate(text4_3[4])
        # )
        self.wait(2)
        self.play(text4_7.shift, UP * 8)
        self.remove(text4_7)
        self.play(FadeIn(text4_4))
        self.wait(1.5)
        self.play(
            text4_4.shift, UP * 0.5,
            Write(dot4_1[0])
        )
        self.wait(0.25)
        self.play(Write(line4_1[0]))
        self.wait(0.25)
        self.play(Write(dot4_1[1]))
        self.wait(1.5)
        self.play(
            Uncreate(text4_4),
            dot4_1[0].shift, UP * 1,
            dot4_1[1].shift, UP * 1,
            line4_1[0].shift, UP * 1,
            Write(text4_5)
        )
        self.wait(2.5)
        self.play(ReplacementTransform(group3, text4_6))
        self.wait(1.5)
        self.play(FadeOutAndShiftDown(text4_6))

        #--5--
        self.play(Write(text5_1))
        self.wait(1.5)
        self.remove(text4_6)
        self.play(
            text5_1.shift, UP * 1.5,
            Write(dot5_1[0]),
            Write(dot5_1[1]),
            Write(line5_1[0])
            # Write(line5_1[1]),
        )
        self.wait(3)
        self.play(ReplacementTransform(group4, group5))
        self.wait(3)
        self.play(
            group5.shift, LEFT * 1,
            Write(text5_3)
        )
        self.wait(2)
        self.play(
            group5.shift, RIGHT * 1,
            Uncreate(text5_3)
        )
        self.wait(1)
        self.play(Write(background5_1))
        self.wait(2)
        # Arrow().set_color()
        self.play(
            group5.shift, UP * 1,
            background5_1.shift, UP * 1,
            Write(text5_2[0])
        )
        self.wait(0.75)
        self.play(
            Write(dot5_3),
            Write(dot5_4),
            line5_2[3].set_color_by_gradient, color5_1, color5_2
        )
        self.wait(0.75)
        self.play(
            ReplacementTransform(text5_2[0], text5_2[1]),
            line5_2[3].set_color, WHITE,
            line5_2[4].set_color_by_gradient, color5_1, color5_2,
            dot5_3.move_to, RIGHT * 1 + UP * 1,
            dot5_4.move_to, DOWN * 1 + UP * 1
        )
        self.wait(0.75)
        self.play(
            ReplacementTransform(text5_2[1], text5_2[2]),
            line5_2[4].set_color, WHITE,
            line5_2[5].set_color_by_gradient, color5_1, color5_2,
            dot5_3.move_to, DOWN * 1 + UP * 1,
            dot5_4.move_to, LEFT * 1 + UP * 1
        )
        self.wait(0.75)
        self.play(
            ReplacementTransform(text5_2[2], text5_2[3]),
            line5_2[5].set_color, WHITE,
            line5_2[6].set_color_by_gradient, color5_1, color5_2,
            dot5_3.move_to, LEFT * 1 + UP * 1,
            dot5_4.move_to, UP * 1 + UP * 1
        )
        self.wait(0.75)
        self.play(
            ReplacementTransform(text5_2[3], text5_4),
            FadeOut(dot5_3),
            FadeOut(dot5_4),
            line5_2[3].set_color_by_gradient, color5_1, color5_2,
            line5_2[4].set_color_by_gradient, color5_1, color5_2,
            line5_2[5].set_color_by_gradient, color5_1, color5_2,
            line5_2[6].set_color_by_gradient, color5_1, color5_2
        )
        self.wait(2)
        self.play(
            ReplacementTransform(text5_4, text5_5)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(group5, text5_6),
            FadeOutAndShiftDown(text5_5),
            background5_1.shift, ORIGIN
        )
        self.wait(0.25)
        self.play(Uncreate(background5_1))
        self.wait(2)
        self.play(FadeOut(text5_6))
        self.wait(1)

class s3(Scene):
    def construct(self):
        ad_ = DAni_1(self)

        #--6--
        self.wait(1)
        # ad_.fadeInTitle("四  循环", subTitleText = "迷途，寻觅往返", titletc = {"循环": RED, "往返": PINK}, showTime = 2)
        # self.wait(1)
        self.play(Write(text6_1))
        self.wait(0.5)
        self.play(
            # Write(background6_2),
            Write(rectan6_1),
            text6_1.scale, 0.8,
            text6_1.move_to, UP * 2.5 + LEFT * 5, aligned_edge = LEFT
        )
        self.wait(1)
        self.play(Write(group6_1))
        self.wait(0.5)
        self.play(
            Write(background6_1),
            FadeIn(text6_2)
        )
        self.play(Write(line6_2_1))
        self.wait(2)
        self.play(
            Uncreate(group6_1),
            Uncreate(background6_1),
            FadeOut(line6_2_1),
            text6_2.scale, 0.75,
            text6_2.next_to, rectan6_1, direction = RIGHT
        )
        self.play(text6_2.shift, ORIGIN + RIGHT * 0.5)
        line6_2_2.move_to(text6_2.get_center())
        self.play(FadeIn(line6_2_2))
        self.wait(1)
        self.play(Write(text6_3))
        self.wait(3)
        self.play(
            text6_3.scale, 0.75,
            text6_3.next_to, rectan6_1, direction = RIGHT
        )
        self.play(text6_3.shift, DOWN * 0.5 + RIGHT * 0.5)
        self.wait(1)
        self.play(Write(text6_4))
        self.wait(2)
        self.play(text6_4.move_to, DOWN * 3.5)
        self.wait(1.5)
        self.play(Write(text6_5))
        self.wait(1.5)
        self.play(
            Write(text6_6),
            Write(text6_7)
        )
        self.wait(1)
        self.play(
            Write(group6_2),
            Write(group6_3)
        )
        self.wait(4)
        self.play(
            Uncreate(group6_2),
            Uncreate(group6_3),
            Uncreate(text6_6),
            Uncreate(text6_7),
            Uncreate(text6_5),
            text6_4.scale, 0.75,
            text6_4.next_to, rectan6_1, direction = RIGHT
        )
        self.play(text6_4.shift, DOWN * 1 + RIGHT * 0.5)
        self.wait(3)
        self.play(
            FadeOut(text6_1),
            FadeOut(text6_2),
            FadeOut(text6_3),
            FadeOut(text6_4),
            FadeOut(line6_2_2),
            FadeOut(rectan6_1)
            # FadeOut(background6_2)
        )
        self.wait(1)

        # --7--
        ad_.fadeInTitle("四  轨道图的分裂", subTitleText = "天灯，欲裂乾坤", titletc = {"分裂": RED, "裂": PINK}, showTime = 2)
        self.wait(3)
        self.add(
            text7_1.shift(LEFT * 16),
            text7_2.shift(LEFT * 16),
            text7_3.shift(LEFT * 16)
        )
        self.play(text7_1.shift, RIGHT * 16)
        self.wait(2)
        self.play(text7_1.shift, UP * 2)
        self.play(Write(group7_1))
        self.wait(2)

        # 我这里出了好多BUG，所以没法实现颜色的自由转换，我真的麻了

        # 注意：t_all要设置为$TIMER_S到$TIMER_E部分的Animate总时长，dt要设置为帧率
        # self.t_all = 15
        # self.cls = []
        # self.t = 0
        # self.dt = 1 / 15
        # def changeColor(obj):
        #     if self.cls == []:
        #         self.cls = ad_.getColorGradient(int(1 / self.dt) * self.t_all, color7_1)
        #     obj.set_color(self.cls[self.t])
        #     self.t = self.t + 1

        self.play(Write(dot7_4), run_time = 1)
        # dot7_4.add_updater(changeColor)
        # TIMER_S
        self.wait(1.5)
        self.play(
            dot7_4.move_to, dot7_1[2].get_center(),
            run_time = 2
        )
        self.wait(1)
        self.play(
            dot7_4.move_to, dot7_1[4].get_center(),
            run_time = 2
        )
        self.wait(1)
        self.play(
            dot7_4.move_to, dot7_1[6].get_center(),
            run_time = 2
        )
        self.wait(1)
        self.play(
            dot7_4.move_to, dot7_1[8].get_center(),
            run_time = 2
        )
        self.wait(2)
        # TIMER_E
        # dot7_4.remove_updater(changeColor)
        self.play(FadeOut(dot7_4))
        
        # self.play(Uncreate(group7_1))
        self.play(
            ReplacementTransform(dot7_1[0], dot7_2[0]),
            ReplacementTransform(dot7_1[2], dot7_2[1]),
            ReplacementTransform(dot7_1[4], dot7_2[2]),
            ReplacementTransform(dot7_1[6], dot7_2[3]),
            ReplacementTransform(dot7_1[8], dot7_2[4]),
            *[FadeIn(i) for i in line7_2],
            run_time = 4
        )
        # 是否没看清楚？
        self.wait(2)
        self.play(
            ReplacementTransform(dot7_2[0], dot7_1a[0]),
            ReplacementTransform(dot7_2[1], dot7_1a[2]),
            ReplacementTransform(dot7_2[2], dot7_1a[4]),
            ReplacementTransform(dot7_2[3], dot7_1a[6]),
            ReplacementTransform(dot7_2[4], dot7_1a[8]),
            *[FadeOut(i) for i in line7_2],
            run_time = 0.5
        )
        self.wait(1)
        self.play(
            ReplacementTransform(dot7_1a[0], dot7_2a[0]),
            ReplacementTransform(dot7_1a[2], dot7_2a[1]),
            ReplacementTransform(dot7_1a[4], dot7_2a[2]),
            ReplacementTransform(dot7_1a[6], dot7_2a[3]),
            ReplacementTransform(dot7_1a[8], dot7_2a[4]),
            *[FadeIn(i) for i in line7_2],
            run_time = 4
        )
        self.wait(1)
        # self.play(*[FadeIn(i) for i in line7_2])
        self.wait(4)

        self.play(
            ReplacementTransform(dot7_1[1], dot7_3[0]),
            ReplacementTransform(dot7_1[3], dot7_3[1]),
            ReplacementTransform(dot7_1[5], dot7_3[2]),
            ReplacementTransform(dot7_1[7], dot7_3[3]),
            *[FadeIn(i) for i in line7_3],
            run_time = 4
        )
        # 是否没看清楚？
        self.wait(2)
        self.play(
            ReplacementTransform(dot7_3[0], dot7_1a[1]),
            ReplacementTransform(dot7_3[1], dot7_1a[3]),
            ReplacementTransform(dot7_3[2], dot7_1a[5]),
            ReplacementTransform(dot7_3[3], dot7_1a[7]),
            *[FadeOut(i) for i in line7_3],
            run_time = 0.5
        )
        self.wait(1)
        self.play(
            ReplacementTransform(dot7_1a[1], dot7_3a[0]),
            ReplacementTransform(dot7_1a[3], dot7_3a[1]),
            ReplacementTransform(dot7_1a[5], dot7_3a[2]),
            ReplacementTransform(dot7_1a[7], dot7_3a[3]),
            *[FadeIn(i) for i in line7_3],
            run_time = 4
        )
        self.wait(1)
        # self.play(*[FadeIn(i) for i in line7_3])
        self.play(
            group7_2.shift, UP * 2.5,
            group7_3.shift, UP * 2.5,
            *[FadeOut(i) for i in line7_1]
        )
        # self.wait(0.5)
        # self.play(*[FadeOut(i) for i in line7_1])
        self.wait(4)

        # self.wait(1.5)
        # self.play(Uncreate(group7_1))
        # self.play(Write(group7_3))
        # self.wait(1.5)
        self.play(
            Uncreate(group7_2), 
            Uncreate(group7_3)
        )

class test(Scene):
    def construct(self):
        t = TexMobject("\\text{i: }f\\text{的一个}2m\\text{循环轨道图可分裂为两个}f_{2}\\text{的}m\\text{循环轨道图}")
        self.add(t)
        self.wait(2)
        self.add(get_submobject_index_labels(t[0]))
        self.wait(3)
        self.remove(t)
        self.add(text7_1)
        self.wait(3)
        # self.add(text7_1)
        # self.wait(5)




