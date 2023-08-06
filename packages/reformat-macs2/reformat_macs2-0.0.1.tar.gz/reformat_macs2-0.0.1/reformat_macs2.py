# -*- coding: utf-8 -*-
# must be compatible with python 2 and 3


import argparse
import logging
import os
import re
import sys

logging.basicConfig(format="%(message)s", level=logging.INFO)
log = lambda message: logging.info(message)


VERSION = "2022-09-19"
HELP = f"""
reformat macs2 output files

arguments:
  $1            path to macs2 output directory
  -h --help     print help message and exit
  -v --version  print version and exit (v. {VERSION})
"""

REFORMAT_INFO = """
--- reformat macs2 ---
macs2 output file BASE_NAME_peaks.xls has been modified as follow:
  - header info has been moved to BASE_NAME.info.txt
  - header labels have beem renamed from -log10(pvalue), -log10(qvalue),
    abs_summit, fold_enrichment to pvalue, qvalue, summit, enrichment
  - coordinates have been switched from 1-based to 0-based (-1 for each
    start and summit values) to match the ones used in .bed files
  - original list (that may includes multiple summits per peak)
    has been moved to BASE_NAME.summits.tsv
  - list containing only one summit (the one with the highest pvalue)
    per peak has been created as BASE_NAME.peaks.tsv and therefore
    reproduce the macs2 output without the --call-summits option
"""


def get_path(dir_path, base_name, extension):
    return os.path.join(dir_path, "{}{}".format(base_name, extension))


def read_summits(file_path):
    info = []
    header = None
    summits = []
    with open(file_path, "r") as file:
        for line in file:
            if line[:3].lower() == "chr":
                header = line \
                    .lower() \
                    .replace("-log10(pvalue)", "pvalue") \
                    .replace("-log10(qvalue)", "qvalue") \
                    .replace("abs_summit", "summit") \
                    .replace("fold_enrichment", "enrichment")
                break
            else:
                info.append(line)
        for line in file:
            summits.append(line.rstrip().split("\t"))
    if header is None or "macs" not in info[0].lower():
        raise RuntimeError("not a macs2 output file: {}".format(file_path))
    for summit in summits:
        summit[1] = int(summit[1]) - 1
        summit[4] = int(summit[4]) - 1
    peaks = []
    for summit in summits:
        name = re.match(r"(.+_[0-9]+)([a-z]*)$", summit[-1]).group(1)
        peak = summit[:-1] + [name]
        peak[6] = float(peak[6])
        if not peaks or name != peaks[-1][-1]:
            peaks.append(peak)
        elif peak[6] > peaks[-1][6]:
            peaks[-1] = peak
    return info, header, summits, peaks


def reformat_macs2(dir_path):
    log("--- reformat macs2 (v: {}) ---".format(VERSION))
    log("directory: {}".format(dir_path))
    if not os.path.isdir(dir_path):
        raise RuntimeError("directory {} not found".format(dir_path))
    base_name = [
        name
        for name in os.listdir(dir_path)
        if name.endswith("_peaks.xls")]
    if len(base_name) != 1:
        raise RuntimeError("no or multiple file matching *_peaks.xls")
    base_name = base_name[0][:-10]
    log("inferred base name: {}".format(base_name))
    summits_path = get_path(dir_path, base_name, "_peaks.xls")
    info, header, summits, peaks = read_summits(summits_path)
    with open(get_path(dir_path, base_name, ".info.txt"), "w") as file:
        file.write("".join(info) + "\n")
        file.write("peak count: {:,}\n".format(len(peaks)))
        file.write("summit count: {:,}\n\n".format(len(summits)))
        file.write(REFORMAT_INFO.strip() + "\n")
    with open(get_path(dir_path, base_name, ".summits.tsv"), "w") as file:
        file.write(header)
        for summit in summits:
            file.write("\t".join(str(field) for field in summit) + "\n")
    with open(get_path(dir_path, base_name, ".peaks.tsv"), "w") as file:
        file.write(header)
        for peak in peaks:
            file.write("\t".join(str(field) for field in peak) + "\n")
    os.remove(summits_path)
    rename = {
        "_peaks.narrowPeak": ".peaks.narrowPeak",
        "_summits.bed": ".summits.bed",
        "_peaks.broadPeak": ".peaks.broadPeak",
        "_peaks.gappedPeak": ".peaks.gappedPeak",
        "_model.r": ".model.r", "_model.pdf": ".model.pdf"}
    for old, new in rename.items():
        old_path = get_path(dir_path, base_name, old)
        if os.path.isfile(old_path):
            new_path = get_path(dir_path, base_name, new)
            os.rename(old_path, new_path)
    log("peak count: {:,}".format(len(peaks)))
    log("summit count: {:,}".format(len(summits)))
    log("--- reformat macs2 done ---")


def main(raw_args):

    if "-h" in raw_args or "--help" in raw_args:
        sys.stderr.write(f"{HELP.strip()}\n")
        return
    if "-v" in raw_args or "--version" in raw_args:
        sys.stderr.write(f"{VERSION}\n")
        return

    parser = argparse.ArgumentParser()
    parser.add_argument("dir_path")
    args = vars(parser.parse_args(raw_args)).values()
    
    return reformat_macs2(*args)


if __name__ == "__main__":
    main(sys.argv[1:])
