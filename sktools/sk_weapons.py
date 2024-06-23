import csv
import sys
from itertools import zip_longest
from urllib.request import urlopen

from bs4 import BeautifulSoup


def main(images: bool = False) -> None:
    """
    Generate a CSV file of weapon names from the Soul Knight Fandom Wiki,
    sorted by category.
    :param images: Wether the CSV file should contain links to images of the
    weapon rather than the weapon names, defaults to False
    :type images: bool, optional
    """
    url = "https://soul-knight.fandom.com/wiki/Soul_Knight_Handbook"
    weapons: dict[str, list[str]] = {}

    with urlopen(url) as conn:
        html = conn.read()

    soup = BeautifulSoup(html, features="html.parser")

    tabber = soup.find_all("div", class_="tabber wds-tabber")[1]  # First is achievements  # noqa
    tabs = tabber.find_all("div", class_="wds-tab__content")
    tabs_header = tabber.find("ul", class_="wds-tabs")
    categories = [li.find("a").text for li in tabs_header.find_all("li")]

    for category, tab in zip(categories, tabs):
        weapons[category] = []
        for row in tab.find_all("div", class_="wikia-gallery-row"):
            for weapon in row.find_all("div", class_="wikia-gallery-item"):
                img = weapon.find("img", class_="thumbimage")
                if images:
                    weapons[category].append(  # Only include base path
                        img["src"].split(".png")[0] + ".png"
                    )
                else:
                    weapons[category].append(img["title"].split(" (")[0])

    writer = csv.writer(sys.stdout)
    writer.writerow(weapons.keys())
    writer.writerows(zip_longest(*weapons.values()))


if __name__ == "__main__":
    main("--images" in sys.argv or "-i" in sys.argv)
