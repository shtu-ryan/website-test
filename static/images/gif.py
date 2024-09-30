from pathlib import Path

import imageio.v3 as iio

path = Path(".")

pngs = list(path.glob("*.png"))
pngs.sort(key=lambda x: x.stem)

group = {}

for png in pngs:
    name = png.stem
    splited = name.split("_")
    series, index = "_".join(splited[:-1]), splited[-1]
    if series not in group:
        group[series] = []

    png_img = iio.imread(png)
    group[series].append(png_img)

for name, pngs in group.items():
    print(name)
    iio.imwrite(path / f"{name}.gif", pngs, loop=0, fps=5)
