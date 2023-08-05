#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""程序入口"""

import argparse
import os
import re
import sys
import traceback
import urllib.request
import _thread

# 我觉得在输入确定的环境下用不着这玩意
# 不过打包到了 PyPI 也不用像以前那些忌惮第三方库了
# 不用白不用
import defusedxml.ElementTree  # type: ignore

from Annotations2Sub import version
from Annotations2Sub.flag import Flags
from Annotations2Sub.Annotation import Parse
from Annotations2Sub.Convert import Convert
from Annotations2Sub.Sub import Sub
from Annotations2Sub.internationalization import _
from Annotations2Sub.tools import (
    AnnotationsForArchive,
    CheckUrl,
    RedText,
    VideoForInvidious,
    YellowText,
    Stderr,
)

# 程序入口
def main():
    parser = argparse.ArgumentParser(
        description=_(
            "一个可以把 Youtube Annotation 转换成 ASS 字幕(Advanced SubStation Alpha)文件的脚本"
        )
    )
    parser.add_argument(
        "queue",
        type=str,
        nargs="+",
        metavar=_("文件 或 videoId"),
        help=_(
            "多个需要转换的文件的文件路径, 或者是多个需要预览, 生成, 从Internet Archive 下载注释文件 Youtube 视频的 videoId"
        ),
    )
    parser.add_argument(
        "-l",
        "--embrace-libass",
        action="store_true",
        help=_("拥抱 libass 的怪癖和特性, 不指定此选项则会适配 xy-vsfilter"),
    )

    # 虽然把分辨率置为 100, 100 字幕滤镜也能正常定位, 但是显然正确的分辨率更惹字幕滤镜喜欢
    parser.add_argument(
        "-x",
        "--transform-resolution-x",
        default=100,
        type=int,
        metavar=100,
        help=_("变换分辨率X"),
    )

    parser.add_argument(
        "-y",
        "--transform-resolution-y",
        default=100,
        type=int,
        metavar=100,
        help=_("变换分辨率Y"),
    )

    # 应该使用非衬线字体, 但是 SSA 不能方便的指定字体家族, 只得出此下策
    parser.add_argument(
        "-f",
        "--font",
        default=_("Microsoft YaHei"),
        type=str,
        metavar=_("Microsoft YaHei"),
        help=_("指定字体"),
    )

    # 其实我觉得这个选项应该没啥用
    parser.add_argument(
        "-o",
        "--output-directory",
        type=str,
        metavar=_("文件夹"),
        help=_("指定转换后文件的输出路径, 不指定此选项转换后的文件会输出至与被转换文件同一目录"),
    )

    parser.add_argument(
        "-d",
        "--download-for-archive",
        action="store_true",
        help=_("尝试从 Internet Archive 下载注释文件"),
    )
    parser.add_argument(
        "-i",
        "--invidious-instances",
        metavar="invidious.domain",
        help=_("指定 invidious 实例(https://redirect.invidious.io/)"),
    )

    # 就是拼接参数执行 mpv
    parser.add_argument(
        "-p",
        "--preview-video",
        action="store_true",
        help=_("预览视频, 需要 mpv(https://mpv.io/) 并指定 invidious 实例"),
    )

    # 与上面同理
    parser.add_argument(
        "-g",
        "--generate-video",
        action="store_true",
        help=_("生成视频, 需要 FFmpeg(https://ffmpeg.org/) 并指定 invidious 实例"),
    )

    parser.add_argument(
        "-s", "--output-to-stdout", action="store_true", help=_("输出至标准输出")
    )

    parser.add_argument(
        "-n", "--no-overwrite-files", action="store_true", help=_("不覆盖文件")
    )

    parser.add_argument(
        "-k", "--no-keep-intermediate-files", action="store_true", help=_("不保留中间文件")
    )

    # 可能是用来甩锅用的
    parser.add_argument(
        "-u",
        "--unstable",
        action="store_true",
        help=_("启用不稳定功能, 会出现一些问题"),
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help=_("显示版本号"),
        version=_("Annotations2Sub v{version}").format(version=version),
    )

    # 这个好像不是用来调试用的
    parser.add_argument(
        "-V",
        "--verbose",
        action="store_true",
        help=_("显示更多些消息"),
    )

    args = parser.parse_args()

    filePaths = []

    if args.unstable:
        Flags.unstable = True

    if args.verbose:
        Flags.verbose = True

    if args.output_to_stdout:
        if args.output_directory:
            Stderr(RedText(_("--output-to-stdout 与 --output-directory 选项相斥")))
            exit(1)
        if args.no_overwrite_files:
            Stderr(RedText(_("--output-to-stdout 与 --no-overwrite-files 选项相斥")))
            exit(1)
        if args.preview_video or args.generate_video:
            Stderr(
                RedText(
                    _("--output-to-stdout 与 --preview-video 或 --generate-video 选项相斥")
                )
            )
            exit(1)

    if args.no_keep_intermediate_files:
        if not (args.preview_video or args.generate_video):
            Stderr(
                RedText(
                    _(
                        "--no-keep-intermediate-files 必须和 --preview-video 或 --generate-video 选项使用"
                    )
                )
            )
            exit(1)

    if args.output_directory:
        if os.path.isdir(args.output_directory) is False:
            Stderr(RedText(_("转换后文件的输出路径应该指定一个文件夹")))
            exit(1)

    if args.preview_video or args.generate_video:
        if args.invidious_instances is None:
            Stderr(RedText(_("请指定一个 invidious 实例")))
            Stderr(_("你可以在这里找一个:"), "https://redirect.invidious.io/")
            exit(1)
        args.download_for_archive = True
        args.embrace_libass = True

    # 先查一遍
    if args.download_for_archive is False:
        for filePath in args.queue:
            # 先看看有没有不是文件的
            if os.path.isfile(filePath) is False:
                Stderr(RedText(_("{} 不是一个文件").format(filePath)))
                exit(1)
            # 再看看有没有文件无效的
            try:
                tree = defusedxml.ElementTree.parse(filePath)
                count = 0
                for each in tree.find("annotations").findall("annotation"):
                    count += 1
                if count == 0:
                    Stderr(RedText(_("{} 没有 Annotation").format(filePath)))
                    exit(1)
            except:
                Stderr(RedText(_("{} 不是一个有效的 XML 文件").format(filePath)))
                Stderr(traceback.format_exc())
                exit(1)
            filePaths.append(filePath)

    if args.download_for_archive:
        # 省的网不好不知道
        def CheckNetwork():
            if CheckUrl() is False:
                Stderr(YellowText(_("您好像无法访问 Google 🤔")))

        _thread.start_new_thread(CheckNetwork, ())

        videoIds = []
        for videoId in args.queue:
            # 还是先查一遍
            if re.match(r"[a-zA-Z0-9_-]{11}", videoId) is None:
                Stderr(RedText(_("{} 不是一个有效的视频 ID").format(videoId)))
                exit(1)
            videoIds.append(videoId)
        for videoId in videoIds:
            filePath = f"{videoId}.xml"
            if args.output_directory != None:
                filePath = os.path.join(args.output_directory, filePath)
            # 为了显示个 "下载 ", 我把下载从 AnnotationsForArchive 里拆出来了
            # 之前就直接下载了, 但是我还是更喜欢输出确定且可控
            url = AnnotationsForArchive(videoId)
            Stderr(_("下载 {}").format(url))
            string = urllib.request.urlopen(url).read().decode("utf-8")
            if string == "":
                Stderr(YellowText(_("{} 可能没有 Annotation").format(videoId)))
                continue
            with open(filePath, "w", encoding="utf-8") as f:
                f.write(string)
            filePaths.append(filePath)

    if args.embrace_libass and (
        args.transform_resolution_x == 100 or args.transform_resolution_y == 100
    ):
        Stderr(
            YellowText(
                _(
                    "--embrace-libass 需要注意, 如果您的视频不是 16:9, 请使用 --transform-resolution-x --transform-resolution-y, 以确保效果."
                )
            )
        )

    outputs = []
    for filePath in filePaths:
        output = filePath + ".ass"
        if args.output_directory != None:
            # 把文件名剥离出来
            fileName = os.path.basename(filePath) + ".ass"
            output = os.path.join(args.output_directory, fileName)

        # 从这里开始就是 __init__.py 开头那个流程图
        # 其实这才是核心功能, 其他的都是有的没的
        with open(filePath, "r", encoding="utf-8") as f:
            string = f.read()
        tree = defusedxml.ElementTree.fromstring(string)
        annotations = Parse(tree)
        events = Convert(
            annotations,
            args.embrace_libass,
            args.transform_resolution_x,
            args.transform_resolution_y,
        )
        if events == []:
            Stderr(YellowText(_("{} 没有注释被转换").format(filePath)))
        # Annotation 是无序的
        # 按时间重新排列字幕(事件), 主要是为了人类可读
        events.sort(key=lambda event: event.Start)
        sub = Sub()
        sub.events.extend(events)
        sub.info["PlayResX"] = args.transform_resolution_x
        sub.info["PlayResY"] = args.transform_resolution_y
        sub.info["Title"] = filePath
        sub.styles["Default"].Fontname = args.font
        subString = sub.Dump()
        if args.output_to_stdout:
            output = None
            print(subString, file=sys.stdout)
        if args.no_overwrite_files:
            if os.path.exists(output):
                output = None
                Stderr(YellowText(_("文件已存在, 您选择不覆盖文件, 跳过输出")))
        if args.no_keep_intermediate_files:
            os.remove(filePath)
            Stderr(_("删除 {}").format(filePath))
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(subString)
            Stderr(_("保存于: {}").format(output))
            # 为了下面而准备
            outputs.append(output)

    if args.preview_video:
        for output in outputs:
            # 从 Invidious 获取视频流和音频流, 并塞给 mpv, FFmpeg
            video, audio = VideoForInvidious(videoId, args.invidious_instances)
            cmd = rf'mpv "{video}" --audio-file="{audio}" --sub-file="{output}"'
            if Flags.verbose:
                Stderr(cmd)
            exit_code = os.system(cmd)
            if Flags.verbose:
                if exit_code != 0:
                    Stderr(YellowText("exit with {}".format(exit_code)))
            if args.no_keep_intermediate_files:
                os.remove(output)
                Stderr(_("删除 {}").format(output))

    if args.generate_video:
        for output in outputs:
            # 同理
            video, audio = VideoForInvidious(videoId, args.invidious_instances)
            cmd = rf'ffmpeg -i "{video}" -i "{audio}" -vf "ass={output}" {output}.mp4'
            if Flags.verbose:
                Stderr(cmd)
            exit_code = os.system(cmd)
            if Flags.verbose:
                if exit_code != 0:
                    Stderr(YellowText("exit with {}".format(exit_code)))
            if args.no_keep_intermediate_files:
                os.remove(output)
                Stderr(_("删除 {}").format(output))
